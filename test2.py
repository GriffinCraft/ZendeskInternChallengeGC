import requests

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
    if(response.status_code != 200):
        print("Error")
        exit()
    data = response.json()
    ticket_arr.extend(data['tickets'])
    url = data['next_page']
counter = 1
for ticket in ticket_arr:
    print(str(counter) + " " + ticket['subject'])
    counter+=1

