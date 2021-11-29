import requests
import time


def print_tix(min, max, ticket_arr):
    for x in range(min, max):
        print(str(x + 1) + " " + ticket_arr[x]['subject'])


def tix_info(ticket):
    print("Subject: " + ticket.get('subject', 'N/A'))
    print("Description: " + ticket.get('description', 'N/A'))
    print("ID: " + str(ticket.get('id', 'N/A')))
    print("Group ID: " + str(ticket.get('group_id', 'N/A')))
    print("Status: " + ticket.get('status', 'N/A'))
    print("Created on: " + ticket.get('created_at', 'N/A'))
    print("Updated at: " + ticket.get('updated_at', 'N/A'))



url = 'https://zccgriffcraft.zendesk.com/api/v2/tickets'
print("Hello there! Welcome to the Zendesk Ticket Requester\nPlease enter your username:")
user = 'PLACEHOLDER'
print('Please enter your password:')
pwd = 'PLACEHOLDER'

session = requests.Session()
session.auth = (user, pwd)

ticket_arr = []

while url:
    response = session.get(url)
    if response.status_code == 429:
        print('Rate limited! Please wait.')
        time.sleep(int(response.headers['retry-after']))
        continue
    if response.status_code != 200:
        print("Error Code: " + str(response.status_code))
        exit()
    data = response.json()
    ticket_arr.extend(data['tickets'])
    url = data['next_page']
minIndex = 0
maxIndex = 25
arrLength = len(ticket_arr)
if maxIndex > arrLength:
    maxIndex = arrLength
print_tix(minIndex, maxIndex, ticket_arr)
while True:
    print("---------")
    print("Viewing tickets " + str(minIndex + 1) + "-" + str(maxIndex) + " out of " + str(arrLength))
    if maxIndex != arrLength:
        print("Type 'next' to view the next page")
    if minIndex != 0:
        print("Type 'back' to view the previous page")
    print("Type a ticket number to see more info")
    print("Or type 'quit' to exit")

    userInput = input()
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
    else:
        print("Please select a valid option")

