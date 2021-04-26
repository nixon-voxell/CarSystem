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
      print("Username not found")
    else:
      username_idx = usernames.index(username)

  password = ""
  # check if password is correct corresponding to the username_idx
  while password != passwords[username_idx]:
    # get input from user
    password = input("Password: ")
    if password != passwords[username_idx]:
      print("Password incorrect")

  print("Logged in!")


# 