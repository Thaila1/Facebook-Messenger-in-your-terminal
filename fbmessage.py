import fbchat			
from getpass import getpass	
username = str(raw_input("Username: "))
client = fbchat.Client(username, getpass())
no_of_friends = int(raw_input("Number of friends: "))
for i in xrange(no_of_friends):
    name = str(raw_input("Name: "))
    friends = client.searchForUsers(name) 
    friend = friends[0]
    msg = str(raw_input("Message: "))
    sent = client.sendMessage(msg,friend.uid)
    if sent:
        print("Message sent successfully!")

client.logout
