import requests

url = 'https://zccgriffcraft.zendesk.com/api/v2/tickets'
print("Hello there! Welcome to the Zendesk Ticket Requester\nPlease enter your username:")
user = input()
print('Please enter your password:')
pwd = input()
response = requests.get(url, auth = (user,pwd))
if response.status_code == 401:
    print("Invalid Username or Password")
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()
data = response.json()
dataIndex = {}
data_list = data['tickets']
counter = 1
while True:
    for ticket in data_list:
        if(counter == 26):
            break
        print(str(counter) + ': ' + ticket['subject'] + '\n')
        dataIndex[counter] = ticket
        counter += 1
    userResponse = input()
    #print(dataIndex[25]['subject'])
    if userResponse == 'quit':
        exit()

