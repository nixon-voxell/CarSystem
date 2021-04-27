print("Welcome to SUPER CAR RENTAL SERVICES!!!")

# region UTILS ================================
# get integer value from user
def get_index(lst:list, item) -> int:
  idx = -1
  for i in range(len(lst)):
    if item == lst[i]:
      idx = i

  return idx

def get_user_int(prompt_msg:str) -> int:
  text = ""
  # check if text is digit or not
  while not text.isdigit():
    # get input from user
    text = input(prompt_msg)

    # check if text is digit or not
    if not text.isdigit():
      # print error message
      print("Input is not an integer\nPlease try again\n")

  return int(text)
# endregion  ==================================



# region LOGIN ================================
#             0      1      2
usernames = ["ali", "abu", "ahmad"]
#             0          1          2
passwords = ["alipass", "abupass", "ahmadpass"]

def login(usernames:list, passwords:list) -> None:
  username = ""
  username_idx = 0
  while username not in usernames:
    # get input from user
    username = input("Username: ")
    if username not in usernames:
      print("Username not found\nPlease try again")
    else:
      username_idx = get_index(usernames, username)

  password = ""
  # check if password is correct corresponding to the username_idx
  while password != passwords[username_idx]:
    # get input from user
    password = input("Password: ")
    if password != passwords[username_idx]:
      print("Password incorrect\nPlease try again")

  print("Logged in!")
# endregion ===================================

# region MAIN MENU ============================
def main_menu() -> None:
  user_type_list = [
    "Choose a user type:\n",
    "1. Admin",
    "2. All Customers (Registered / Not-Registered)",
    "3. Registered Customer\n"
  ]
  print("\n"*10 + "--Main Menu--")
  for i in range(len(user_type_list)):
    print(user_type_list[i])
# endregion ===================================


def choose_user_type(user_type):
  if user_type == 1:
    print("1")
    # admin function
  elif user_type == 2:
    try:
      print("2")
      # all customers function
      pass
    except:
      print("Invalid input Please try again")
  elif user_type == 3:
    try:
      print("3")
      pass
      # registered customer function
    except:
      print("Invalid input Please try again")
  else:
    pass

def main() -> None:
  while True:
    main_menu()
    user_type = int(input("> "))
    choose_user_type(user_type)

    back = input("Do you want to continue? To exit to the Main Menu type ‘0’, To Terminate Program type '1': ")

if __name__ == "__main__":
  # make sure that this is the sript that we are running
  # this will not run if this script is imported instead of ran directly
  main()
