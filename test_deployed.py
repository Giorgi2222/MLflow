import requests

# URL for the deployed model
url = "http://127.0.0.1:8000/invocations"

# Test data converted from your input, including the new data
test_data = {
    "dataframe_split": {
        "columns": [
            "fixed_acidity",
            "volatile_acidity",
            "citric_acid",
            "residual_sugar",
            "chlorides",
            "free_sulfur_dioxide",
            "total_sulfur_dioxide",
            "density",
            "pH",
            "sulphates",
            "alcohol",
            "is_red"
        ],
        "data": [
            [7.5, 0.63, 0.12, 5.1, 0.111, 50, 110, 0.9983, 3.26, 0.77, 9.4, 5],
            [7.8, 0.59, 0.18, 2.3, 0.076, 17, 54, 0.9975, 3.43, 0.59, 10, 5],
            [8.3, 0.625, 0.2, 1.5, 0.08, 27, 119, 0.9972, 3.16, 1.12, 9.1, 4],
            [11.5, 0.41, 0.52, 3, 0.08, 29, 55, 1.0001, 3.26, 0.88, 11, 5],
            [10.5, 0.42, 0.66, 2.95, 0.116, 12, 29, 0.997, 3.24, 0.75, 11.7, 7],
            [11.9, 0.43, 0.66, 3.1, 0.109, 10, 23, 1, 3.15, 0.85, 10.4, 7],
            [12.6, 0.38, 0.66, 2.6, 0.088, 10, 41, 1.001, 3.17, 0.68, 9.8, 6],
            [8.2, 0.7, 0.23, 2, 0.099, 14, 81, 0.9973, 3.19, 0.7, 9.4, 5],
            [8.6, 0.45, 0.31, 2.6, 0.086, 21, 50, 0.9982, 3.37, 0.91, 9.9, 6],
            [11.9, 0.58, 0.66, 2.5, 0.072, 6, 37, 0.9992, 3.05, 0.56, 10, 5],
            [12.5, 0.46, 0.63, 2, 0.071, 6, 15, 0.9988, 2.99, 0.87, 10.2, 5],
            [12.8, 0.615, 0.66, 5.8, 0.083, 7, 42, 1.0022, 3.07, 0.73, 10, 7],
            [10, 0.42, 0.5, 3.4, 0.107, 7, 21, 0.9979, 3.26, 0.93, 11.8, 6],
            [10.4, 0.575, 0.61, 2.6, 0.076, 11, 24, 1, 3.16, 0.69, 9, 5],
            [10.3, 0.34, 0.52, 2.8, 0.159, 15, 75, 0.9998, 3.18, 0.64, 9.4, 5],
            [9.4, 0.27, 0.53, 2.4, 0.074, 6, 18, 0.9962, 3.2, 1.13, 12, 7],
        ]
    }
}

# Sending a POST request to the model's endpoint
response = requests.post(url, json=test_data)

# Check the response
if response.status_code == 200:
    print("Response from the model:", response.json())
else:
    print("Error:", response.status_code, response.text)

