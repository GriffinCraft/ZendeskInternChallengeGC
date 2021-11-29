import requests
import time
import getpass
#Zendesk Intern Coding Challenge by Griffin Craft, started Nov 23 2021, finished Nov 28 2021
#This program returns tickets from the Zendesk API, and displays them in a simple commmand line interface

#print_tix takes a min integer, a max integer, and an array of tickets. print_tix then prints all the tickets in that range, inclusive
def print_tix(min, max, ticket_arr):
    print('---------')
    if min < 0:
        raise ValueError('Invalid min value, must be >= 0')
    if max > len(ticket_arr):
        raise ValueError('Invalid max value, must be <= len(ticket_arr)')
    if ticket_arr is None:
        raise ValueError('Ticket Arr cannot be null')
    if len(ticket_arr) < 1:
        raise ValueError('Ticket Arr must have at least 1 value')
    for x in range(min, max):
        print(str(x + 1) + " " + ticket_arr[x]['subject'])
    

#tix_info takes a ticket and prints the relevant information (subject, description, id, etc)
#The get function is used in case the value is null, as none are essential in the JSON
def tix_info(ticket):
    print('---------')
    if ticket is None:
        raise ValueError('Ticket cannot be null')
    print("Subject: " + ticket.get('subject', 'N/A'))
    print("Description: " + ticket.get('description', 'N/A'))
    print("ID: " + str(ticket.get('id', 'N/A')))
    print("Group ID: " + str(ticket.get('group_id', 'N/A')))
    print("Status: " + ticket.get('status', 'N/A'))
    print("Created on: " + ticket.get('created_at', 'N/A'))
    print("Updated at: " + ticket.get('updated_at', 'N/A'))
    print()
    



url = 'https://zccgriffcraft.zendesk.com/api/v2/tickets'
#Requests username/password
print("Hello there! Welcome to the Zendesk Ticket Requester\nPlease enter your username:")
user = input()
pwd = getpass.getpass("Please enter your password:")
session = requests.Session()
session.auth = (user, pwd)

ticket_arr = []
#Pagnates through the response if theres > 100 tickets
while url:
    response = session.get(url)
    #Called the API too many times; needs to sleep
    if response.status_code == 429:
        print('Rate limited! Please wait.')
        time.sleep(int(response.headers['retry-after']))
        continue
    #Invalid password
    if response.status_code == 401:
        print("Sorry, you have typed an invalid username/password, please restart and enter different credentials")
    #Other error, or the API cannot be accessed. exits the program
    if response.status_code != 200:
        print("Sorry, you've come across an error. Error Code: " + str(response.status_code))
        exit()
    print("Waiting for API Response")
    data = response.json()
    #Puts the data from the tickets in an array for safe keeping
    ticket_arr.extend(data['tickets'])
    url = data['next_page']
#Set indices for the print function
minIndex = 0
maxIndex = 25
arrLength = len(ticket_arr)
if arrLength == 0:
    print("No valid tickets, exiting")
    exit()
#Avoids array OOB error
if maxIndex > arrLength:
    maxIndex = arrLength
print_tix(minIndex, maxIndex, ticket_arr)
#User input section
while True:
    print("---------")
    print("Viewing tickets " + str(minIndex + 1) + "-" + str(maxIndex) + " out of " + str(arrLength))
    #Displays next page option if applicable
    if maxIndex != arrLength:
        print("Type 'next' to view the next page")
    #Displays previous page option if applicable
    if minIndex != 0:
        print("Type 'back' to view the previous page")
    print("Type a ticket number to see more info")
    print("Or type 'quit' to exit")

    userInput = input().lower()
    #These should be self explanatory, errors should not be possible in this section due to the limiting of input
    if userInput == 'quit':
        exit()
    elif userInput == 'next' and maxIndex != arrLength:
        minIndex += 25
        maxIndex += 25
        if maxIndex > arrLength:
            maxIndex = arrLength
        print_tix(minIndex, maxIndex, ticket_arr)
    elif userInput == 'back' and minIndex != 0:
        minIndex -= 25
        maxIndex -= 25
        print_tix(minIndex, maxIndex, ticket_arr)
    elif userInput.isdigit() and minIndex < int(userInput) <= maxIndex:
        tix_info(ticket_arr[int(userInput) - 1])
        #Continues to display the ticket until there's user input
        while True:
            print("Type 'back' to go back to the ticket list, or 'quit' to quit")
            userInput = input().lower()
            if userInput == 'quit':
                exit()
            elif userInput == 'back':
                print_tix(minIndex, maxIndex, ticket_arr)
                break
            else:
                print("Please select a valid option")
    else:
        print("---------")
        print("Please select a valid option")

