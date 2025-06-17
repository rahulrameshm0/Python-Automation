import pywhatkit

phone_number = input("Enter your phone number: ")
pywhatkit.sendwhatmsg(phone_number, "Hey! How you doing", 15, 13,15, True, 2)