Name: Griffin Craft

This is my submission for the Zendesk Coding Challenge!!!

Required Packages:
requests
time (Standard Library)
getpass (Standard Library)
unittest (Standard Library)

Installing 'requests':

On Linux/MacOS, go to your terminal and type
$ python -m pip install requests
($ signifies the start of the shell; do not include it)

Installation:

Linux/MacOS: Go to your terminal, in the directory with ZCCGriffinCraft.py, and type

$ python3 ZCCGriffinCraft.py

Windows: Import ZCCGriffinCraft.py as a PyCharm project, install the requests package, and run

Usage:

The program requires the use of a Zendesk url, with a valid username and password typed into the terminal, to make the API request.
Then the first 25 tickets (or all the tickets if less than 25) will be displayed on the screen. Due to careful consideration, the user should not be able to input something invalid. If so, they are notified of this and are returned to the ticket menu.

The user can select 'next' when not on the last page to flip to the next page, likewise for 'back' and when they're not on the first page

The user can type the number of any given ticket to see the tickets Subject, Description, ID, Group ID, Status, and when the ticket was created

The user can type 'quit' to exit the program.

Unit Tests:

Due to the construction of the program, user error is extrememly unlikely, and in my thorough tests I did not get an OOB error or invalid input. However, for thoroughness, unit tests for the two functions in the program are used and in the file
'test_ZCCGriffinCraft.py'

Any other errors are caught by if statements, and exit the program as they are fatal (Invalid user/pass, no tickets, API Busy, etc.)

Final Words:

Thank you so much for this opportunity! I learned so much and think I became a better programmer in the process. I welcome any and all critiscm with open arms, so even if you decide to move past me, I would really appreciate feedback so I know where to improve for
the future. 
