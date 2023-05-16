import requests
import json

# Define the request data
request_data = {
    'data': 'Morteza',
    'age': 35,
    'email': 'mortexa.A@example.com'
}

# Send the request to the server
url = 'http://localhost:8000'

try:
    response = requests.post(url, data=json.dumps(request_data))
    response.raise_for_status()  # Raise an exception if the response has an error status code

    # Print the response from the server
    print(response.text)

except requests.exceptions.RequestException as e:
    # Handle the exception and print an error message
    print('An error occurred during the request:', str(e))
