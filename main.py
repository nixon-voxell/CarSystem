print("Welcome to SUPER CAR RENTAL SERVICES!!!")

# region UTILS ================================
# get integer value from user
def get_index(lst:list, item) -> int:
  idx = -1
  for i in range(len(lst)):
    if item == lst[i]:
      idx = i

  return idx

# forcefully get integer input from user
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

# region USERNAMES AND PASSWORDS ==============
# get usernames and passwords from a text file
def get_usernames_and_passwords(filename:str) -> tuple:
  customer_file = open(filename, "r", encoding="utf-8")
  customer_file_content = customer_file.read()
  lines = customer_file_content.split("\n")

  usernames = []
  passwords = []

  # loop through the entire list lines in the text file and exclude the last line
  for line_idx in range(len(lines) - 1):
    # check if line_idx is an even or odd number
    if line_idx % 2 == 0:
      usernames.append(lines[line_idx])
    else:
      passwords.append(lines[line_idx])

  return usernames, passwords

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
# endregion  ==================================



# region LOGIN ================================
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
  print("\n"*10 + "-- Main Menu --")
  for i in range(len(user_type_list)):
    print(user_type_list[i])
# endregion ===================================

admin_list = ["1. Add Cars to be rented out.","2. Modify Car Details.","3. Display Records of..","4. Search Specific Record of..","5. Return a Rented Car."]
admin_func = [add_cars, modify_carDetails, display_records, search_records]
def admin():
  usernames, passwords = get_usernames_and_passwords("admins.txt")
  login(usernames, passwords)
  for i in range(len(admin_list)):
    print(admin_list[i])
    no = get_user_int("Choose option(1-5): ")
    admin_func[no-1]()

customer_list = ["1. View all cars available for rent.","2. Create new Account."]
customer_func = [view_cars, create_acc]
def all_customer():
  for i in range(len(customer_list)):
    print(customer_list[i])
    no = get_user_int("Choose option(1/2): ")
    customer_func[no-1]()

registeredCustomer_list = ["1. Modify Personal Details.","2. View Personal Rental History.", "3. View Detail of Cars to be Rented Out. ", "4. Select and Book a car for a specific duration", "5. Do payment to confirm Booking."]
registeredCustomer_func = [modify_personalDetails, view_history, view_rentedCars, book_cars, payment]
def registered_customer():
  usernames, passwords = get_usernames_and_passwords("customers.txt")
  login(usernames, passwords)
  for i in range(len(registeredCustomer_list)):
    print(registeredCustomer_list[i])
    no = get_user_int("Choose option(1-5): ")
    registeredCustomer_func[no-1]()

user_func = [admin, all_customer, registered_customer]

def main() -> None:
  while True:
    main_menu()
    no = get_user_int("Choose user(1-3): ")
    user_func[no-1]()

    exit_program()

def terminate():
  quit()

back_func = [main_menu, terminate]
def exit_program() -> None:
  print("Do you want to continue? To exit to the Main Menu type ‘1’, To Terminate Program type '2': ")
  no = get_user_int("Choose option(1/2): ")
  back_func[no-1]()

if __name__ == "__main__":
  # make sure that this is the sript that we are running
  # this will not run if this script is imported instead of ran directly
  main()
