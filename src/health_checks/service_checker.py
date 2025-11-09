import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()

# Services Variables

Grafana = os.getenv("Grafana")
Prometheus = os.getenv("Prometheus")
Loki = os.getenv("Loki")

Services = {
    "Grafana": Grafana,
    "Prometheus": Prometheus,
    "Loki": Loki
}

def check_service(name,url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{name} is UP")
            return True
        else:
            print(f"{name} returned {response.status_code}")
            return False
    except requests.RequestException as e:
        print(f"{name} is DOWN: {e}")
        return False

all_up = True
for service_name, service in Services.items():
    if not check_service(service_name, service):
        all_up = False

if not all_up:
    sys.exit(1)