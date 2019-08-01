#!/usr/bin/python3
import json
import requests
from AutoZen import *
from zendeskcredentials import user, password, headers
import sys
def create_menu():
    answer = True
    while answer:

        menu_settings = ("""What would you like to do?:\n
        (1) Create a Ticket
        (2) Edit a Ticket
        (3) Create a User
        (4) Create a User and Organization 
        (5) Exit Application\n""")

        print(menu_settings)
        user_answer = input()

        if user_answer == "1":
             AutoZen.create_ticket()
        elif user_answer == "2":
             AutoZen.comment_ticket()
        elif user_answer == "3":
             AutoZen.create_user()
        elif user_answer == "":
             print("That answer is unacceptable please try again!")
        elif user_answer == "4":
            AutoZen.create_orgwithmember()
        elif user_answer == "5":
            return False


create_menu()
