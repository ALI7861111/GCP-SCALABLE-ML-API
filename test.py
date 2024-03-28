import requests
import numpy as np

# Define the URL of the Flask API endpoint
# after delpoying the model, the url will be the public ip address of the load balancer
url = 'http://35.203.88.188:80/predict'

# Generate a random input array of shape (1, 132) with 0s and 1s
input_array = np.random.randint(2, size=(1, 132))

# Convert the input array to a list
input_list = input_array.tolist()

# Create JSON data to send in the request
data = {'input_array': input_list}

# Send POST request to the Flask API
response = requests.post(url, json=data)

# Print the response
print("Response:", response.json())