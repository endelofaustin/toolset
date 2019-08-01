#!/usr/bin/python3

import json
import requests
from zendeskcredentials import user, password, headers

class AutoZen:

    def create_ticket():
        subject = input("What is the subject of the ticket you would like to put in?: ")
        body = input("What would you like to put in the body of your message?: ")

        # Package the data in a dictionary matching the expected JSON
        data = {'ticket': {'subject': subject, 'comment': {'body': body}}}

        # Encode the data to create a JSON payload
        payload = json.dumps(data)

        # Set the request parameters
        url = 'https://.zendesk.com/api/v2/tickets.jsonasync=true'

        # Do the HTTP post request
        response = requests.post(url, data=payload, auth=(user, password), headers=headers)

        # Check for HTTP codes other than 201 (Created)
        if response.status_code != 201:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit()

        # Report success
        print("Good Job you successfully created the ticket!!! :)")
        create_ticket()


    def comment_ticket():

        # Ticket to update
        id = input("What is the ticket ID of the ticket you want to comment? : ")
        body = input("What would you like to add to the ticket?: ")

        # Package the data in a dictionary matching the expected JSON
        ticket_data = {'ticket':{'comment':{ 'body': body }}}

        # Encode the data to create a JSON payload
        payload = json.dumps(data)

        # Set the request parameters
        url = 'https://.zendesk.com/api/v2/tickets/' + id + '.json'

        # Do the HTTP put request
        response = requests.put(url, data=payload, auth=(user, password), headers=headers)

        # Check for HTTP codes other than 200
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit()

        # Report success
        print('Successfully added comment to ticket #{}'.format(id))

    def create_orgwithmember():
        # New ticket info
        name = input("What is the name of the user you would like to create?: ")
        email = input("What is email of the user?: ")
        phone = input("What is phone number of the user?: ")
        organization = input("What is the name of the organization that you would like to create?")

        # Package the data in a dictionary matching the expected JSON
        data = {"user": {"name": name, "email": email, "phone": phone, "verified": True}}
        data1 = {"organization": {"name": organization }}


        # Encode the data to create a JSON payload
        payload = json.dumps(data)
        payload1 = json.dumps(data1)

        print(payload)
        print(payload1)

        # Set the request parameters
        url = 'https://.zendesk.com/api/v2/users.json'
        url1 = 'https://.zendesk.com/api/v2/organizations.json'
        headers = {'content-type': 'application/json'}

        # Do the HTTP post request
        response = requests.post(url, data=payload, auth=(user, password), headers=headers)
        response1 = requests.post(url1, data=payload1, auth=(user, password), headers=headers)

        # Let's make those reponses JSON! 
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
        reponse2 = requests.post(url2, data=payload2, auth=(user, password), headers=headers)

        # Check for HTTP codes other than 201 (Created)
        if response.status_code != 201:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit()

        # Report success
        print('Good Job!!!')

    def create_user():
        #name, email, phone = input(x ,y, z)
        name = input("What is the name of the user you would like to create?: ")
        email = input("What is email of the user?: ")
        phone = input("What is phone number of the user?: ")

        data = {"user": {"name": name, "email": email, "phone": phone, "verified": True}}
        payload = json.dumps(data)
        url = 'https://.zendesk.com/api/v2/users.json'
        response = requests.post(url, data=payload, auth=(user, password), headers=headers)

        # A Little Error handling
        if response.status_code != 201:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit()

        # Report success
        print('Good Job!!!')
