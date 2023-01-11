import requests
import json

class SynapseCortexThreatIntel:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.synapsecortex.com/v2"

    def get_ip_reputation(self,ip):
        url = f"{self.base_url}/investigate?ip={ip}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch IP reputation: {response.text}")
        return json.loads(response.text)

    def get_hash_info(self, hash):
        url = f"{self.base_url}/analyze?hash={hash}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch hash info: {response.text}")
        return json.loads(response.text)

    def get_fqdn_info(self, fqdn):
        url = f"{self.base_url}/fqdn/{fqdn}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch FQDN info: {response.text}")
        return json.loads(response.text)

    def ingest_iocs(self, iocs):
        url = f"{self.base_url}/ingest"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        response = requests.post(url, headers=headers, data=json.dumps(iocs))
        if response.status_code != 200:
            raise Exception(f"Failed to ingest IOCs: {response.text}")
        return json.loads(response.text)

    def query_iocs(self, iocs):
        url = f"{self.base_url}/query"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        response = requests.post(url, headers=headers, data=json.dumps(iocs))
        if response.status_code != 200:
            raise Exception(f"Failed to query IOCs: {response.text}")
        return json.loads(response.text)

# Instantiate the Cortex
