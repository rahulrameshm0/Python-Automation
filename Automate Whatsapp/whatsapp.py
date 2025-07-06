# import pywhatkit
#
# phone_number = input("Enter your phone number: ")
# pywhatkit.sendwhatmsg(phone_number, "Hey! How you doing", 15, 13,15, True, 2)

a = [1,2,3,4,5,6,7,8,9,10]
user = int(input("Enter a number: "))
b = 5
for i in a:
    if i == user:
        print(a.index(user))
        break
else:
    c = 0
    for j in enumerate(a):
        if j != a:
            print(len(j))
            break