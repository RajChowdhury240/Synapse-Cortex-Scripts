import requests
import json

# Replace with your Synapse Cortex API key
api_key = "YOUR_API_KEY"

# Replace with the FQDN you want to investigate
fqdn = "example.com"

# Send the request to Synapse Cortex
response = requests.get(
    f"https://api.synapsecortex.com/v2/fqdn/{fqdn}",
    headers={"Authorization": f"Bearer {api_key}"}
)

# Parse the JSON response
result = json.loads(response.text)

# Print the FQDN information
print(result)
