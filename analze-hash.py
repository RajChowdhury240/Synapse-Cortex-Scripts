import requests
import json

# Replace with your Synapse Cortex API key
api_key = "YOUR_API_KEY"

# Replace with the hash you want to analyze
hash = "malicious_hash"

# Send the request to Synapse Cortex
response = requests.get(
    f"https://api.synapsecortex.com/v2/analyze?hash={hash}",
    headers={"Authorization": f"Bearer {api_key}"}
)

# Parse the JSON response
result = json.loads(response.text)

# Print the analysis results
print(result)
