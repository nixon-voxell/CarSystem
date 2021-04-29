# get username and password
# def get_usernames_and_passwords(filename):
#   customer_file = open(filename, "r", encoding="utf-8")
#   customer_file_content = customer_file.read()
#   lines = customer_file_content.split("\n")
#
#   usernames = []
#   passwords = []
#
#   # loop through the entire list lines in the text file and exclude the last line
#   for line_idx in range(len(lines) - 1):
#     # check if line_idx is an even or odd number
#     if line_idx % 2 == 0:
#       usernames.append(lines[line_idx])
#     else:
#       passwords.append(lines[line_idx])
#
#   return usernames, passwords
#
# usernames, passwords = get_usernames_and_passwords("./customers.txt")
#
# print(usernames)
# print(passwords)

# register new username and password
def register_new_user(filename:str) -> None:
  username = ""
  password = ""

  while username == "":
    username = input("Enter username: ")
    if username == "":
      print("Username cannot be empty!\n")

  while password == "":
    password = input("Enter password: ")
    if password == "":
      print("Password cannot be empty!\n")

  print(f"Your user and pass is: {username}, {password}")

  customer_file = open(filename, "a", encoding="utf-8")
  customer_file.write(f"{username}\n{password}\n")
