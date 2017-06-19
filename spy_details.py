#Importing the datetime python package
from datetime import datetime

#Spy Class
class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.online = True
        self.chats = []
        self.current_status_message = None

#Chat Class
class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


#Default Spy  details
spy = Spy('James Bond', 'Mr.', 29, 4.6,)

#Declaring default friend list
f1 = Spy('Bill Taner', 'Mr.', 27, 4.1)
f2 = Spy('Judi Dench', 'Ms.', 39, 4.6)
friends = [f1,f2]

#Old Status Messages list
Status_Messages=['The Name\'s Bond,James Bond.','On A Secret Mission.','Coding in Python.','You Know Me!']