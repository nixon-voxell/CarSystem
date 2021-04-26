print("Welcome to SUPER CAR RENTAL SERVICES!!!")

# LOGIN ================================

#             0      1      2
usernames = ["ali", "abu", "ahmad"]
#             0          1          2
passwords = ["alipass", "abupass", "ahmadpass"]

def login(usernames, passwords):
  username = ""
  username_idx = 0
  while username not in usernames:
    # get input from user
    username = input("Username: ")
    if username not in usernames:
      print("Username not found\nPlease try again")
    else:
      username_idx = usernames.index(username)

  password = ""
  # check if password is correct corresponding to the username_idx
  while password != passwords[username_idx]:
    # get input from user
    password = input("Password: ")
    if password != passwords[username_idx]:
      print("Password incorrect\nPlease try again")

  print("Logged in!")

role_list = ["Choose your role:","1. Admin","2. All Customers (Registered / Not-Registered)","3. Registered Customer"]

def exit(back):
  if back == 0:
    print("--Main Menu--")
    for i in range(len(role_list)):
      print(role_list[i])
      return role 
  else:
    quit()

def choose_role(role):
  if role == 1:
    #admin function
  elif role == 2:
    try:
        #allcustomers_function
    except:
        print("Invalid input Please try again")
        return back
        exit(back)
  elif role == 3:
    try:
        #registeredcustomer_function
    except:
        print("Invalid input Please try again")
        return back
        exit(back)
  else:
    return back
    exit(back)

login(usernames, passwords)
back = input("Do you want to continue? To exit to the Main Menu type ‘0’, To Terminate Program type '1': ")
exit(back)
role = input("Choose your role: ")
choose_role(role)

