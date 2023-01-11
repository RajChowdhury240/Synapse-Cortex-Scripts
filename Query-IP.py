import requests
import json

# Replace with your Synapse Cortex API key
api_key = "YOUR_API_KEY"

# Replace with the IP address you want to investigate
ip_address = "127.0.0.1"

# Send the request to Synapse Cortex
response = requests.get(
    f"https://api.synapsecortex.com/v2/investigate?ip={ip_address}",
    headers={"Authorization": f"Bearer {api_key}"}
)

# Parse the JSON response
result = json.loads(response.text)

# Print the threat intelligence information
print(result)
