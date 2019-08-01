import json
import requests

# New ticket info
name = input("What is the name of the user you would like to create?: ")
email = input("What is email of the user?: ")
phone = input("What is phone number of the user?: ")
organization = input("What is the name of the organization that you would like to create?")

# Package the data in a dictionary matching the expected JSON
#data = {'user': {'name': name, 'identities': [{ 'type': 'email', 'value': email }, { 'type': 'phone', 'value': phone }]}}
#data = {'name': name, 'email': email}
#data = { "user": {"name": name, { "email": email }}}
data = {"user": {"name": name, "email": email, "phone": phone, "verified": True}}
data1 = {"organization": {"name": organization }}


# Encode the data to create a JSON payload
payload = json.dumps(data)
payload1 = json.dumps(data1)

print(payload)
print(payload1)

# Set the request parameters
url = 'https://secom1.zendesk.com/api/v2/users.json'
url1 = 'https://secom1.zendesk.com/api/v2/organizations.json'
user = 'user' + '/token'
pwd = 'hahayaright'
headers = {'content-type': 'application/json'}

# Do the HTTP post request
response = requests.post(url, data=payload, auth=(user, pwd), headers=headers)
response1 = requests.post(url1, data=payload1, auth=(user, pwd), headers=headers)

# Let's make those reponses JSON!
# print(response)
# print(response1)
# print(response.text)
# print(response1.text)
#print(type(response))
type_swap = response.json()
type_swap1 = response1.json()


json_response = json.loads(response.text)
json_response1 = json.loads(response1.text)

type(json_response1)

# Take the user id and add it to the new organization
user_id = type_swap['user']['id']
organization_id = type_swap1['organization']['id']
print(organization_id)

# Set up the last request
url2 = 'https://.zendesk.com/api/v2/organization_memberships.json'

# Set up the membership data to be sent
data2 = {"organization_membership": {"user_id": user_id, "organization_id": organization_id }}

# Set up the last payload
payload2 = json.dumps(data2)
print(payload2)

# Make the last request to add the member to the organization
reponse2 = requests.post(url2, data=payload2, auth=(user, pwd), headers=headers)

# Check for HTTP codes other than 201 (Created)
if response.status_code != 201:
   print('Status:', response.status_code, 'Problem with the request. Exiting.')
   exit()

# Report success
print('Good Job!!!')
