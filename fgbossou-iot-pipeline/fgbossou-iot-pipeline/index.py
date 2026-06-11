import json
import boto3
import uuid
import logging
import os
from datetime import datetime
from decimal import Decimal

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')


def handler(event, context):
    logger.info("Incoming event: %s", json.dumps(event))
    try:
        body_raw = event.get('body')
        if not body_raw:
            return _response(400, {'message': 'Missing request body'})

        try:
            payload = json.loads(body_raw)
        except json.JSONDecodeError as exc:
            logger.error("JSON decode error: %s", exc)
            return _response(400, {'message': 'Invalid JSON'})

        measurements = payload.get('measurements')
        if not measurements or not isinstance(measurements, list):
            return _response(400, {
                'message': 'Invalid payload: measurements missing or not a list'
            })

        for idx, m in enumerate(measurements):
            for field in ('sensor_id', 'temperature', 'status'):
                if field not in m:
                    return _response(400, {
                        'message': f'Missing field "{field}" in measurement at index {idx}'
                    })

        request_id = str(uuid.uuid4())
        now = datetime.utcnow()
        timestamp = now.isoformat()

        temperatures = [float(m['temperature']) for m in measurements]
        avg_temp = round(sum(temperatures) / len(temperatures), 2)
        error_count = sum(
            1 for m in measurements
            if str(m.get('status', '')).upper() == 'ERROR'
        )

        bucket = os.environ['S3_BUCKET']
        s3_key = (
            f"raw-zone/year={now.strftime('%Y')}"
            f"/month={now.strftime('%m')}"
            f"/day={now.strftime('%d')}"
            f"/{request_id}.json"
        )

        s3_client.put_object(
            Bucket=bucket,
            Key=s3_key,
            Body=json.dumps(payload),
            ContentType='application/json'
        )
        logger.info("S3 write OK: s3://%s/%s", bucket, s3_key)

        table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
        table.put_item(Item={
            'request_id': request_id,
            'timestamp': timestamp,
            's3_path': f"s3://{bucket}/{s3_key}",
            'average_temperature': Decimal(str(avg_temp)),
            'error_count': error_count,
        })
        logger.info("DynamoDB write OK: request_id=%s", request_id)

        return _response(201, {
            'message': 'Data ingested successfully',
            'request_id': request_id,
            's3_path': f"s3://{bucket}/{s3_key}",
            'average_temperature': avg_temp,
            'error_count': error_count,
        })

    except Exception as exc:
        logger.error("Unexpected error: %s", exc, exc_info=True)
        return _response(500, {'message': f'Internal server error: {str(exc)}'})


def _response(status_code, body):
    return {
        'statusCode': status_code,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(body),
    }
