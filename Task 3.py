import random

def email_checker(email_address): 
    """validates an email passed when called"""
    domain ="pop.ac.uk"
    if email_address.index('@')>2 and domain in email_address:
        return True
    else:
        return False

def reply(query):
    """This function print the output"""   
    random_replies =["Mmmm.","Oh, my","Oh,yes"," I see.","Tell me more."]  
    if "wifi" in query:
        print("WiFi is excellent across the campus.")
    elif "library" in query:
        print('Sorry!The library is closed today')
    elif "deadline" in query:
        print("Your deadline has been extended by two working days")
    elif "coffee" in query:
        print ( "Cafe opens at 7 AM")
    elif 'feebacks' in query:
        print ("You will get feebacks bu next week")
    elif "lab" in query:
        print("Lab are well maintained and open for everyone.")
    else:
        print(random.choice(random_replies))

print ("Welcome to Pop Chat !\nOne of our operators will be pleased to help you today. ")
names = ["Tony", "Marvel ", "Thor", "Blade", "Hulk"]
email = input ("Please enter your Poppleton email address: ")
if email_checker(email) == True:  #it pass the email to check the email
    mail_name = email[0:email.index("@")]
    print(f"Hello, {mail_name}!  Thank you, and Welcome to PopChat!\n")
    print(f"My name is {random.choice(names)}, and it will be my pleasure to help you. ")
    if random.randint(0,10) == 0:  # it checks the network error
        print("* NETWORK ERROR *")
        print(f"Thanks,{mail_name}, for using PopChat. See you again soon!") 
        exit()
    else:
        while True:  #it loops the code
            query = input("----->")
            if "bye" in query or "exit" in query:
                print(f"Thanks,{mail_name}, for using PopChat. See you again soon!") 
                break
            else:
                reply(query)
else:
    print("invalid")