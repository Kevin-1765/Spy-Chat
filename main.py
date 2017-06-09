#Import Statements
"""
 First Statement is importing the data from spy_details.py file
 Next three statements are for importing the classes which are used for encoding/decoding the text,
 colored chat text and for alert box respectively
"""

from spy_details import spy, Spy, ChatMessage, friends,Status_Messages
from steganography.steganography import Steganography
from termcolor import colored
from pymsgbox import alert
import os

#To begin with giving user a choice to continue with default user profile or to create a new profile

print "Welcome to Spy Chat"
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
query = raw_input(question)

#Function defination add_status() for adding a status message

def add_status():

    updated_status_message = None
    if spy.current_status_message != None:
        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print 'You don\'t have any status message currently \n'
    default = raw_input("Do you want to select from pre-defined status (y/n)? ")
    if default.upper() == "N":
        new_status_message = raw_input("Enter your status message \n")
        if len(new_status_message) > 0:
            Status_Messages.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':
        item_position = 1
        for message in Status_Messages:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1
        message_selection = int(raw_input("\nChoose any of the messages "))
        if len(Status_Messages) >= message_selection:
            updated_status_message = Status_Messages[message_selection - 1]
    else:
        print 'Invalid! Choice Press either y or n.'
    if updated_status_message:
        print 'Status message updated to : %s' % (updated_status_message)
    else:
        print 'Status can\'t be updated. \n'
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
        new_friend.salutation = raw_input("Is He/She is Mr. or Ms.?: ")
        new_friend.name = new_friend.salutation + " " + new_friend.name
        new_friend.age = int(raw_input("Age :"))
        new_friend.rating =float(raw_input("Spy rating : "))
    #if len(new_friend.name) > 0 and ( 12< new_friend.age < 50) and (spy.rating <=new_friend.rating >= spy.rating and new_friend.rating<=5):
        if len(new_friend.name) > 0 and (12 < new_friend.age < 50) and (spy.rating <= new_friend.rating <= 5):
            friends.append(new_friend)
            print 'Friend Added your friend list \n'
    else:
        print 'Sorry you have entered invalid inputs \n'
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

#Function defination send_message() for sending a hidden message(encoded) inside a image

def send_message():
    friend_choice = select_a_friend()
    #imagepath="C:/Users/Capt Kevin/PycharmProjects/Acadview/"#
    input_image = raw_input("Enter the name of the image: ")
    #imagepath=imagepath+"/"+input_image
    #if os.path.isfile(imagepath)==1:
    if os.path.isfile(input_image)==1:
        output_image = "output.jpg"
        text = raw_input("What do you want to say: ")
        if len(text)== 0:
            print "Text Can't be Empty \n"
            exit()
        else:
            #Encodeing the text into image using stegnograhpy class and appending into chat history
            Steganography.encode(input_image, output_image, text)
            new_chat = ChatMessage(text,True)
            friends[friend_choice].chats.append(new_chat)
            print "Your Message Send Successfully \n"
    else:
        print 'No such file is present\n'
        exit()

#End of function

#Function defination 'read_message()' to read message from friends hidden inside a image (decoding)
def read_message():

    secret_text=""
    sender = select_a_friend()
    output_image = raw_input("Enter the name of file: ")
    #Decoding the hidden text from image
    if os.path.isfile(output_image)==1:
        secret_text = Steganography.decode(output_image)
        new_chat = ChatMessage(secret_text, False)

    #if-else condition for hidden text inside a image
        if len(secret_text) > 0:
          friends[sender].chats.append(new_chat)
          print new_chat
        else :
            print 'Oops Looks like there is no hidden message encoded'
            exit()
    else :
        print 'No such file present'
        exit()

#End of function

#Function defination 'read_chat()' to store chat messages

def read_chat():

    read_for = select_a_friend()
    for chat in friends[read_for].chats:

        ctime = colored(chat.time.strftime("%d:%B:%Y"), 'blue')
        cspy = colored(friends[read_for].name, 'red')
           #based upon the message sender the chat message are printed
        if chat.sent_by_me:
                print '['+ctime+']'+ 'you said:'+" "+chat.message
        else:
                print '['+ctime+']'+ cspy + " said: " + chat.message

            #Check for emergency codes
        if chat.message=="SOS"or "SAVE ME"or "HELP ME":
                alert("I Need Your Help Buddy","Emergency")
#End of function

#Function defination 'start_chat(spy)' with one argument as spy for Starting the chatting app
def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name
    if 12 > spy.age > 50:
        print"You age is not eligible to be a Spy"
        exit();
    else:
        if spy.rating < 2.5:
            print "You are bad spy"
        elif 2.5 <= spy.rating <= 3.5:
            print "You are a average spy"
        elif 3.5 < spy.rating <= 4.5:
            print "You are good spy"
        else:
            print "You are Brilliant Spy"

        print "Authentication completed. Welcome " + spy.name + " age "+ str(spy.age) + " and rating of " + str(spy.rating)
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
                    send_message()
                elif choice == 4:
                    read_message()
                elif choice == 5:
                    read_chat()
                else:
                    print 'Goodbye!!'
                    show_menu = False
                    exit()

#End of function

# To start with default user
if query.upper()== "Y":
    start_chat(spy)

# For entering new user information
else:
    spy = Spy('','',0,0.0)
    spy.name = raw_input("Enter Your name first: ")
    c=0
    for i in spy.name:
        if not i.isalpha():
            c = c + 1
    #Check cases for age name,age restrictions,rating range
    if len(spy.name) > 0 and c==0:
        spy.salutation = raw_input("What Should I call you Mr. or Ms.?: ")
        spy.age =int(raw_input("Enter your age : "))
        spy.rating=float(raw_input("Enter your spy rating: "))

        if spy.age < 12 or spy.age > 50:
            print "You\'re age doesn\'t Qualify to be a Spy"
            exit()
        if spy.rating > 5 or spy.rating < 0:
            print 'The Rating can be in between range of 0-5'
            exit()
        else:
             start_chat(spy)
    else:
        print 'Please enter a valid name'
        exit()


#End of Program