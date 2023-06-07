import requests

# GraphQL query
query = '''
query {
  allUsers {
    id
    name
    age
  }
}
'''

# GraphQL endpoint URL (Address and port where Code 1 is running)
url = 'http://localhost:5000/graphql'

# Send the POST request
response = requests.post(url, json={'query': query})

# Check the response
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Request failed:', response.status_code)
