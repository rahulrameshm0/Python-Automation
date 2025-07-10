import pywhatkit

phone_number = input("Enter your phone number: ")
pywhatkit.sendwhatmsg(phone_number, "Hey! How you doing", 15, 13, wait_time=15, tab_close=True)

