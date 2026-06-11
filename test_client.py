import requests
import json

# Remplacer par la valeur CloudFrontIngestionURL dans les Outputs CloudFormation
CLOUDFRONT_INGESTION_URL = "https://VOTRE_CLOUDFRONT_URL.cloudfront.net"

HEADERS = {"Content-Type": "application/json"}


def send_payload(label, payload):
    print(f"\n{'='*60}")
    print(f"TEST : {label}")
    print(f"{'='*60}")
    print("Payload envoyé :")
    print(json.dumps(payload, indent=2))

    response = requests.post(CLOUDFRONT_INGESTION_URL, headers=HEADERS, json=payload)

    print(f"\nStatut HTTP : {response.status_code}")
    print("Réponse :")
    print(json.dumps(response.json(), indent=2))


# ──────────────────────────────────────────────────────────────
# TEST 1 — Payload valide (4 mesures, mix OK et ERROR)
# ──────────────────────────────────────────────────────────────
valid_payload = {
    "measurements": [
        {"sensor_id": "sensor-1", "temperature": 22.5, "status": "OK"},
        {"sensor_id": "sensor-2", "temperature": 37.8, "status": "ERROR"},
        {"sensor_id": "sensor-3", "temperature": 19.1, "status": "OK"},
        {"sensor_id": "sensor-4", "temperature": 45.0, "status": "ERROR"},
    ]
}

send_payload("Payload valide — HTTP 201 attendu", valid_payload)

# ──────────────────────────────────────────────────────────────
# TEST 2 — Payload invalide (champ temperature manquant)
# ──────────────────────────────────────────────────────────────
invalid_payload = {
    "measurements": [
        {"sensor_id": "sensor-5", "status": "OK"},
        {"sensor_id": "sensor-6", "temperature": 28.0, "status": "OK"},
    ]
}

send_payload("Payload invalide (temperature manquant) — HTTP 400 attendu", invalid_payload)

# ──────────────────────────────────────────────────────────────
# TEST 3 — JSON malformé (body corrompu)
# ──────────────────────────────────────────────────────────────
print(f"\n{'='*60}")
print("TEST : JSON malformé — HTTP 400 attendu")
print(f"{'='*60}")
raw_body = "{ this is not valid json }"
print(f"Body envoyé : {raw_body}")

response = requests.post(CLOUDFRONT_INGESTION_URL, headers=HEADERS, data=raw_body)

print(f"\nStatut HTTP : {response.status_code}")
print("Réponse :")
print(json.dumps(response.json(), indent=2))
