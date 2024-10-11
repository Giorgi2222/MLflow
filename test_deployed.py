import requests
import json

# Define the MLflow model endpoint
url = "http://127.0.0.1:8000/invocations"

# Example Iris data (sepal length, sepal width, petal length, petal width)
# This is one instance of the Iris dataset (e.g., Iris-setosa)
iris_data = [
    [5.1, 3.5, 1.4, 0.2]  # Example values for one iris flower
]

# Create the payload for the POST request
payload = {
    "instances": iris_data
}

# Set headers
headers = {
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check the response
if response.status_code == 200:
    # If the request was successful, print the prediction
    prediction = response.json()
    print("Prediction:", prediction)
else:
    # If the request failed, print the error message
    print("Error:", response.status_code, response.text)
