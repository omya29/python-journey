#====================================================
#Day1 -Python Basics
# Written by : Om Borude
# Date : 28th March 2026
#====================================================

# program 1 Variables 
name = " Om Borude "
age =21
City = "Lonimavala"
is_student= True 

print ("my name is ",name)
print ("My age is ",age)
print (" i am live in ",City)
print ("Am i student ? ",is_student)


# Program 2 :Numbers 

failed_attempts = 7
max_allowed =3
threshold =5

print ("Failed Attempts : ",failed_attempts)
print ("Max Allowed : ",max_allowed)

total=failed_attempts + max_allowed
print ("Total ttempts :",total)
 
remaining =failed_attempts - max_allowed
print ("Remaining attempts : ",remaining)

print ("over Limit ? ",failed_attempts > max_allowed)


#program 3 : String

ip_address = "192 .168.1.1"
event="failed login "
username = "admin"

log_entry = ip_address +"|"+ event +"|"+ username 
print (log_entry)

print ("Ip length :",len(ip_address))

print(event.lower())
print(username.upper())

print("FAILED" in event)
print("SUCCESS" in event)


#program 4 ;if elsee

failed_attempts = 5
if failed_attempts >= 3 :
    print("ALERT : Too many FAILED Attempts ")
    print( " Ip os blocked")
else :
    print("login Attempts are normal")


failed_attempts = 2
if failed_attempts >= 3 :
    print("ALERT : Too many FAILED Attempts ")
    print( " Ip os blocked")
else :
    print("login Attempts are normal")
    

#program 5 :mini Security Program


#====================================
#"      Cloudsentinel v.01           "
#====================================


username=input("Enter username :")
password=input("Enter Password:")

correct_user= "Admin"
correct_password="Secure123"

if username == correct_user and password==correct_password:
    print("Login Success Welcome",username)
else:
    print("wrong Credentials for ",username)
    print("this attempt will be logged")