"""
 Import statements
 First Statement is for importing the data from spy_details.py file.
 In second statement Steganography is imported to encode/decode the text into image.
 Third statement is for importing the colored class (used for coloring the text).
 Fourth statement is for importing the python message class
 Last statement is for importing the built-in os class
"""

from spy_details import spy, Spy, ChatMessage, friends,Status_Messages
from steganography.steganography import Steganography
from termcolor import colored
from pymsgbox import alert
import os

#The begining of the app with query

print "Welcome to Spy Chat"
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
query = raw_input(question)


#Function defination add_status() for adding a status message

def add_status():

    updated_status_message = None
    if spy.current_status_message != None:
        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print 'Oops you don\'t have any status message currently \n'
    default = raw_input("Do you want to select from previous status (y/n)? ")
    if default.upper() == "N":
        new_status_message = raw_input("What\'s in your mind?\n")
        if len(new_status_message) > 0:
            Status_Messages.append(new_status_message)
            updated_status_message = new_status_message
        else:
            print 'Status Message can\'t be empty'
            exit()

    elif default.upper() == 'Y':
        item_position = 1
        for message in Status_Messages:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1
        message_selection = int(raw_input("\nChoose any of the message"))
        if len(Status_Messages) >= message_selection:
            updated_status_message = Status_Messages[message_selection - 1]
    else:
        print 'Invalid! Choice Press either y or n.'
        exit()
    if updated_status_message:
        print 'Status message updated to : %s' % (updated_status_message)
    else:
        print 'Status can\'t be updated. \n'
        exit()
    return updated_status_message

#End of function


#Function defination add_friend() for adding new friends

def add_friend():

    c = 0
    new_friend = Spy('','',0,0.0)
    new_friend.name = raw_input("Please add your friend's name: ")
    for i in new_friend.name:
        if not i.isalpha():
            c = c + 1
    if c==0 and len(new_friend.name)>0:
        new_friend.salutation = raw_input("Is He/She is a Mr. or Ms.?: ")
        new_friend.age = int(raw_input("Age :"))
        new_friend.rating =float(raw_input("Spy rating : "))
        if len(new_friend.name) > 0 and (12 < new_friend.age < 50) and (spy.rating <= new_friend.rating <= 5):
            friends.append(new_friend)
            print 'Friend added to your friend list \n'
        else:
            print'The age should be greater then 12 and rating should be greater then or equal to your rating.'
            exit()
    else:
        print 'Name can\'t be left empty or alphanumeric \n'
        exit()
    return len(friends)

#End of function


#Function defination select_a_friend() for selecting a friend to chat with

def select_a_friend():
    items = 0
    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (items +1, friend.salutation, friend.name,friend.age,friend.rating)
        items = items + 1
    friend_choice = raw_input("Choose from your friends")
    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

#End of function


#Function defination send_a_message() for sending a hidden message(encoded) inside a image

def send_a_message():
    friend_choice = select_a_friend()
    input_image = raw_input("Enter the name of the image: ")
    if os.path.isfile(input_image)==1:
        output_image = "output.jpg"
        text = raw_input("What do you want to say: ")
        if len(text)== 0:
            print "Text Can't be Empty \n"
            exit()
        else:
#Encoding the text into image using stenography class and appending into chat history
            Steganography.encode(input_image, output_image, text)
            new_chat = ChatMessage(text,True)
            friends[friend_choice].chats.append(new_chat)
            print "Your Message Send Successfully \n"
    else:
        print 'No such file is present\n'
        exit()

#End of function


#Function defination 'read_a_message()' to read message from friends hidden inside a image (decoding)

def read_a_message():
    sender = select_a_friend()
    output_image = raw_input("Enter the name of file: ")
#Decoding the hidden text from image
    if os.path.isfile(output_image)==1:
        secret_text = Steganography.decode(output_image)
        new_chat = ChatMessage(secret_text, False)

#Check for hidden text inside a image
        if len(secret_text) > 0:
            friends[sender].chats.append(new_chat)
            print new_chat
        else:
            print 'Oops Looks like there is no hidden message encoded'
            exit()
    else:
        print 'No such file present'
        exit()

#End of function


#Function defination 'read_chat()' to store chat messages

def read_chat():
    read_for = select_a_friend()
    for chats in friends[read_for].chats:

        ctime = colored(chats.time.strftime("%d:%B:%Y"), 'blue')
        cspy = colored(friends[read_for].name, 'red')
    #According to the message sender the chat message are printed
        if chats.sent_by_me:
                print 'At ['+ctime+']'+ 'you said:'+" "+chats.message
        else:
                print 'At ['+ctime+']'+ cspy + " said: " + chats.message

    #Check for emergency codes
        if chats.message=="SOS"or "SAVE ME"or "HELP ME":
                alert("I Need Your Help Buddy","Emergency")
#End of function


#Function defination 'start_chat(spy)' with one argument as spy for Starting the chatting app

def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name
    if 12 < spy.age or spy.age > 50:
        print"You age is not eligible to be a Spy"
        exit()
    else:
        print "Authentication completed. Welcome " + spy.name + " age " + str(spy.age) + " and rating of " + str(spy.rating)
        if spy.rating < 2.5:
            print "You are bad spy"
        elif 2.5 <= spy.rating <= 3.5:
            print "You are a average spy"
        elif 3.5 < spy.rating <= 4.5:
            print "You are a good spy"
        else:
            print "You are a Brilliant Spy"

        show_menu = True


#Printing Menu for user to select from
        while show_menu:
            menu_choices = "\nWhat do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            choice = raw_input(menu_choices)

            if len(choice) > 0:
                choice = int(choice)

                if choice == 1:
                    spy.current_status = add_status()
                elif choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif choice == 3:
                    send_a_message()
                elif choice == 4:
                    read_a_message()
                elif choice == 5:
                    read_chat()
                else:
                    print 'Goodbye!! Have a good Day'
                    show_menu = False
                    exit()

#End of function

# To start with default user
if query.upper() == 'Y':
    start_chat(spy)

# For entering new user information
elif query.upper() == 'N':
    spy = Spy('','',0,0.0)
    print  "Please fill out the following information to create a new profile"
    spy.name = raw_input("Enter Your name first: ")
    c=0
    for i in spy.name:
        if not i.isalpha():
            c = c + 1
#Check for age name,age restrictions,rating range
    if len(spy.name) > 0 and c==0:
        spy.salutation = raw_input("Are you a Mr. or Ms.?: ")
        spy.age =int(raw_input("Enter your age : "))
        spy.rating=float(raw_input("Enter your spy rating: "))
        spy.status=raw_input('Are you online ? (y/n):')
        m=''

        if spy.age < 12 or spy.age > 50:
             m=m+'You\'re age doesn\'t qualify to be a Spy\n'

        elif spy.rating > 5 or spy.rating < 0:
             m=m+'Spy rating can be in between the range of 0-5\n'

        if len(m)>1:
            print 'These conditions should be satisfied\n'+m
            exit()
        else:
             if spy.status.upper() == 'N':
                 print 'Your online status should be true\n'
                 o=raw_input(' Press y to change your online status')
                 if o.upper()=='Y':
                    start_chat(spy)
                 else:
                     print 'You should be online to start a conversation'
                     exit()
             elif spy.status.upper() == 'Y':
                  start_chat(spy)
    else:
        print 'Please enter a valid name'
        exit()
else:
    print 'You have made a wrong choice'
    exit()
#End of Program