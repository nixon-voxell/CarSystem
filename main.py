import datetime

# region CONSTANTS ============================
CUSTOMERS_FILE = "./customers.txt"
CUSTOMER_RENTS_FILE = "./customer_rents.txt"
CARS_FILE = "./cars.txt"
ADMINS_FILE = "./admins.txt"
# endregion ===================================

# region UTILS ================================
# forcefully get integer input from user
def get_user_int(prompt_msg:str) -> int:
  usr_input = ""
  # check if usr_input is digit or not
  while not usr_input.isdigit():
    # get usr_input from user
    usr_input = input(prompt_msg)

    # check if usr_input is digit or not
    if not usr_input.isdigit():
      # print error message
      print("Input is not an integer\nPlease try again\n")

  return int(usr_input)

# forcefully get float input from user
def get_user_float(prompt_msg:str) -> float:
  usr_input = ""
  # check if usr_input is a float or not
  while not usr_input.replace(".", "", 1).isdigit():
    # get usr_input from user
    usr_input = input(prompt_msg)
    # if usr_input is not a float, print error msg
    if not usr_input.replace(".", "", 1).isdigit():
      print("Input is not a number\nPlease try again\n")

  return float(usr_input)

# forcefully get a non-empty string from user
def get_user_not_empty(prompt_msg:str, error_msg:str="Input cannot be empty\n") -> str:
  usr_input = ""
  while usr_input == "":
    usr_input = input(prompt_msg)
    if usr_input == "":
      print(error_msg + "\n")

  return usr_input

# forcefully get a string input that is inside the given selection from user
def get_user_selection(prompt_msg:str, selections:list, error_msg:str="Input is not within selection given\n") -> str:
  usr_input = ""
  while usr_input not in selections:
    usr_input = input(prompt_msg)
    if usr_input not in selections:
      print(error_msg + "\n")

  return usr_input

# forcefully get integer input within a range from user
def get_user_int_range(prompt_msg:str, range_min:int, range_max:int, exceed_range_error_msg:str="Input has exceed the range given\n") -> int:
  """
  get user int and only accept a range of int, anything outside the range will be rejected

  ex: range_min: 0, range_max: 5 only accepts (0, 1, 2, 3, 4, 5)
  """
  usr_int = range_min - 1
  while usr_int < range_min or usr_int > range_max:
    usr_int = get_user_int(prompt_msg)
    if usr_int < range_min or usr_int > range_max:
      print(exceed_range_error_msg)

  return usr_int
# endregion  ==================================

# region USERNAMES AND PASSWORDS ==============
# get usernames and passwords from a text file
def get_file_info(filename:str) -> tuple:
  with open(filename, "r", encoding="utf-8") as file:
    file_content = file.read()
  lines = file_content.split("\n")

  content1 = []
  content2 = []

  # loop through the entire list lines in the text file and exclude the last line
  for line_idx in range(len(lines) - 1):
    # check if line_idx is an even or odd number
    if line_idx % 2 == 0:
      content1.append(lines[line_idx])
    else:
      content2.append(lines[line_idx])

  return content1, content2

# modify file lines from a text file
def modify_file_info(filename:str, location:int, is_content1:bool, info:str) -> None:
  content1, content2 = get_file_info(filename)
  # edit content1[location]/content2[location] based on is_content1
  if is_content1: content1[location] = info
  else: content2[location] = info

  final_string = ""
  for content_idx in range(len(content1)):
    # content_idx is an integer which will increase until the range ends
    final_string += content1[content_idx] + "\n"
    final_string += content2[content_idx] + "\n"

  with open(filename, "w") as file:
    file.write(final_string)

# delete file lines from a text file
def delete_file_info(filename:str, location:int) -> None:
  content1, content2 = get_file_info(filename)

  final_string = ""
  for content_idx in range(len(content1)):
    if (content_idx != location):
      final_string += content1[content_idx] + "\n"
      final_string += content2[content_idx] + "\n"

  # use with to auto close, followed by as file
  with open(filename, "w") as file:
    file.write(final_string)

# add file lines to a text file
def add_file_info(filename:str, new_content1:str, new_content2:str) -> None:
  # use with to auto close, followed by as file
  with open(filename, "a") as file:
    file.write(new_content1)
    file.write(new_content2)

# register new username and password
def register_new_user(filename:str, usernames:list) -> None:
  username = ""
  password = ""

  while username == "" or username in usernames:
    username = input("Enter username: ")
    if username == "":
      print("Username cannot be empty!\n")
    elif username in usernames:
      print("Username has been taken!\nPlease enter another username.\n")

  while password == "":
    password = input("Enter password: ")
    if password == "":
      print("Password cannot be empty!\n")

  print(f"Your username and password is: {username}, {password}")

  with open(filename, "a", encoding="utf-8") as customer_file:
    customer_file.write(f"{username}\n{password}\n")
# endregion  ==================================

# region LOGIN ================================
def login(usernames:list, passwords:list) -> int:
  """
  login a user and return the index of the user
  """
  username = ""
  username_idx = 0
  while username not in usernames:
    # get input from user
    username = input("Username: ")
    if username not in usernames:
      print("Username not found\nPlease try again\n")
    else:
      username_idx = usernames.index(username)

  password = ""
  # check if password is correct corresponding to the username_idx
  while password != passwords[username_idx]:
    # get input from user
    password = input("Password: ")
    if password != passwords[username_idx]:
      print("Password incorrect\nPlease try again\n")

  print("Logged in!\n")
  return username_idx
# endregion ===================================

# region ADMIN MENU ===========================
def add_cars(filename:str="./cars.txt") -> None:
  car_details, _ = get_file_info(filename)
  car_details = [c.split("|") for c in car_details]
  used_car_names = [c[0].lower()+c[1].lower() for c in car_details]

  car_detail = ""
  car_name = ""

  brand = ""
  model = ""
  description = ""

  while car_detail == "" or car_name in used_car_names:
    brand = get_user_not_empty("Enter brand: ", "Brand cannot be empty!")
    model = get_user_not_empty("Enter model: ", "Model cannot be empty!")
    description = get_user_not_empty("This car good for: ", "Description cannot be empty!")

    car_detail = f"{brand}|{model}|{description}"
    car_name = brand.lower() + model.lower()

    if car_name in used_car_names:
      print("The car name has been taken!\nPlease create a unique one.\n")

  hourly_price = get_user_float("Enter hourly price: ")
  daily_price = get_user_float("Enter daily price: ")

  print(f"Your car name is: {brand}, {model}")
  print(f"Your car description is: {description}")
  print(f"The hourly price is: {hourly_price}\nThe daily price is: {daily_price}")

  file = open(filename, "a", encoding="utf-8")
  file.write(f"{car_detail}\n{hourly_price}|{daily_price}\n")

def modify_car_details():
  pass

def display_records():
  pass

def search_records():
  pass

# MAIN FUNCTION
def admin():
  admin_list = [
  "\n1. Add Cars to be rented out.",
  "2. Modify car details.",
  "3. Display records",
  "4. Search specific records",
  "5. Return a rented car.",
  "6. Return to main menu.\n"
  ]
  admin_func = [add_cars, modify_car_details, display_records, search_records]

  usernames, passwords = get_file_info(ADMINS_FILE)
  login(usernames, passwords)
  for i in range(len(admin_list)):
    print(admin_list[i])
  no = get_user_int_range("Choose option(1-5): ", 1, 5)
  admin_func[no-1]()
# endregion ===================================

# region ALL CUSTOMERS MENU ========================
def create_acc():
  usernames, _ = get_file_info(CUSTOMERS_FILE)
  register_new_user(CUSTOMERS_FILE, usernames)
  add_file_info(CUSTOMER_RENTS_FILE, "\n", "\n")

def view_cars():
  cars, price = get_file_info(CARS_FILE)
  print("\n========== Car List ==========\n")
  for i in range(len(cars)):
    car_detail = cars[i].split("|")
    price_detail = price[i].split("|")
    print(f"Car Index: {i+1}")
    print(f"Cars: {car_detail[0]}, {car_detail[1]}")
    print(f"Description: {car_detail[2]}")
    print(f"Hourly Price: {price_detail[0]}")
    print(f"Daily Price: {price_detail[1]}\n")

  input("Press enter to continue...")

# MAIN FUNCTION
def all_customer():
  customer_list = [
  "\n1. View all cars available for rent.",
  "2. Create new account.",
  "3. Exit to main menu\n"
  ]
  customer_func = [view_cars, create_acc]

  while True:
    for i in range(len(customer_list)):
      print(customer_list[i])
    no = get_user_int_range("Choose option(1-3): ", 1, 3)
    if no == 3: return
    customer_func[no-1]()
# endregion ===================================

# region REGISTERED CUSTOMER MENU =============
def modify_personal_details(curr_user_idx:int) -> None:
  print("\n1. Username\n2. Password\n")
  selection = get_user_int_range("Choose which detail do you want to modify: ", 1, 2, "Select 1 or 2 only!\n")

  if selection == 1:
    new_username = get_user_not_empty("New Username: ")
    modify_file_info(CUSTOMERS_FILE, curr_user_idx, True, new_username)
  else:
    new_password = get_user_not_empty("New Password: ")
    modify_file_info(CUSTOMERS_FILE, curr_user_idx, False, new_password)

def view_history(curr_user_idx:int) -> None:
  pass

def view_rented_cars(curr_user_idx:int) -> None:
  pass

def book_cars(curr_user_idx:int) -> None:
  # format: car_idx,date|car_idx,date|car_idx,date
  pass

def payment(curr_user_idx:int) -> None:
  pass

def delete_account(curr_user_idx:int) -> bool:
  decision = ""
  decision = get_user_selection("Are you sure? y/n: ", ["y", "n"])

  if decision == "y":
    delete_file_info(CUSTOMERS_FILE, curr_user_idx)
    delete_file_info(CUSTOMER_RENTS_FILE, curr_user_idx)
    return True

  return False

# MAIN FUNCTION
def registered_customer() -> None:
  registered_customer_list = [
    "\n1. Modify personal details.",
    "2. View personal rental history.",
    "3. View detail of cars to be rented out. ",
    "4. Select and Book a car for a specific duration",
    "5. Do payment to confirm Booking.",
    "6. Delete account",
    "7. Exit to main menu\n"
  ]
  registered_customer_func = [modify_personal_details, view_history, view_rented_cars, book_cars, payment]

  usernames, passwords = get_file_info(CUSTOMERS_FILE)
  curr_user_idx = login(usernames, passwords)
  in_loop = True
  while in_loop:
    for i in range(len(registered_customer_list)):
      print(registered_customer_list[i])
    no = get_user_int("Choose option(1-7): ")
    if no == 7: return
    in_loop = not registered_customer_func[no-1](curr_user_idx)
# endregion ===================================

# region MAIN PROGRAM ===================================
def exit_program() -> None:
  print("\nDo you want to continue? To exit to the Main Menu type '1', To Terminate Program type '2': ")
  no = get_user_int_range("Choose option(1/2): ", 1, 2)
  if no == 2: exit()

def main() -> None:
  user_func = [admin, all_customer, registered_customer]

  user_type_list = [
    "Choose a user type:\n",
    "1. Admin",
    "2. All Customers (Registered / Not-Registered)",
    "3. Registered Customer",
    "4. Exit Program\n"
  ]

  while True:
    print("\n"*10 + "Welcome to SUPER CAR RENTAL SERVICES!!!")
    print("========== Main Menu ==========")
    for i in range(len(user_type_list)):
      print(user_type_list[i])

    no = get_user_int_range("Choose user(1-4): ", 1, 4)
    if no == 4: exit_program()
    else: user_func[no-1]()
# endregion ===================================

if __name__ == "__main__":
  # make sure that this is the sript that we are running
  # this will not run if this script is imported instead of running directly
  main()

