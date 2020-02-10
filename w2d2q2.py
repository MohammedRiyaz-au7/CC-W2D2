username=input("enter the username:")
password=input("enter the password:")
if username == "riyaz" and password == "password":
 print("enter the system")
elif username != "riyaz" and password == "password":
 print("Username Doesnot Exist")
elif username == "riyaz" and password != "password":
 print("Passwords donot match")
else:
  print("enter the correct credentials")


