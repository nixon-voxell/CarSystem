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
def get_user_not_empty(prompt_msg:str, error_msg:str) -> str:
  usr_input = ""
  while usr_input == "":
    usr_input = input(prompt_msg)
    if usr_input == "":
      print(error_msg + "\n")

  return usr_input
# endregion  ==================================

# region USERNAMES AND PASSWORDS ==============
# get usernames and passwords from a text file
def get_file_info(filename:str) -> tuple:
  file = open(filename, "r", encoding="utf-8")
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
      username_idx = usernames.index(username)

  password = ""
  # check if password is correct corresponding to the username_idx
  while password != passwords[username_idx]:
    # get input from user
    password = input("Password: ")
    if password != passwords[username_idx]:
      print("Password incorrect\nPlease try again")

  print("Logged in!")
# endregion ===================================



# region ADMIN MENU ===========================
def add_cars(filename:str="./cars.txt") -> None:
  car_details, _ = get_file_info(filename)
  car_details = [c.split("|") for c in car_details]
  used_car_names = [c[0].lower()+c[1].lower() for c in car_details]

  # for c in car_details:
  #   used_car_names.append(c[0]+c[1])

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

def admin():
  admin_list = [
  "1. Add Cars to be rented out.",
  "2. Modify Car Details.",
  "3. Display Records of..",
  "4. Search Specific Record of..",
  "5. Return a Rented Car."
  ]
  admin_func = [add_cars, modify_car_details, display_records, search_records]

  usernames, passwords = get_file_info("./admins.txt")
  login(usernames, passwords)
  for i in range(len(admin_list)):
    print(admin_list[i])
  no = get_user_int("Choose option(1-5): ")
  admin_func[no-1]()
# endregion ===================================

# region CUSTOMER MENU ========================
def create_acc():
  usernames, _ = get_file_info("./customers.txt")
  register_new_user("./customers.txt", usernames)

def view_cars():
  cars, price = get_file_info("cars.txt")
  for i in range(len(cars)):
    car_detail = cars[i].split("|")
    price_detail = price[i].split("|")
    print("")
    print("-----Car List-----")
    print(f"Cars: {car_detail[0]}, {car_detail[1]}")
    print(f"Description: {car_detail[2]}")
    print(f"Hourly Price: {price_detail[0]}")
    print(f"Daily Price: {price_detail[1]}")

def all_customer():
  customer_list = [
  "1. View all cars available for rent.",
  "2. Create new Account."
  ]
  customer_func = [view_cars, create_acc]

  for i in range(len(customer_list)):
    print(customer_list[i])
  no = get_user_int("Choose option(1/2): ")
  customer_func[no-1]()
# endregion ===================================

# region REGISTERED CUSTOMER MENU =============
def modify_personal_details():
  pass

def view_history():
  pass

def view_rented_cars():
  pass

def book_cars():
  pass

def payment():
  pass

def registered_customer():
  registered_customer_list = [
    "1. Modify Personal Details.",
    "2. View Personal Rental History.",
    "3. View Detail of Cars to be Rented Out. ",
    "4. Select and Book a car for a specific duration",
    "5. Do payment to confirm Booking."
  ]
  registered_customer_func = [modify_personal_details, view_history, view_rented_cars, book_cars, payment]

  usernames, passwords = get_file_info("./customers.txt")
  login(usernames, passwords)
  for i in range(len(registered_customer_list)):
    print(registered_customer_list[i])
  no = get_user_int("Choose option(1-5): ")
  registered_customer_func[no-1]()
# endregion ===================================

# region MAIN PROGRAM ===================================
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

def main() -> None:
  user_func = [admin, all_customer, registered_customer]
  print("Welcome to SUPER CAR RENTAL SERVICES!!!")

  while True:
    main_menu()
    no = get_user_int("Choose user(1-3): ")
    user_func[no-1]()

    exit_program()

back_func = [main_menu, exit]
def exit_program() -> None:
  print("")
  print("Do you want to continue? To exit to the Main Menu type ‘1’, To Terminate Program type '2': ")
  no = get_user_int("Choose option(1/2): ")
  back_func[no-1]()

# endregion ===================================

if __name__ == "__main__":
  # make sure that this is the sript that we are running
  # this will not run if this script is imported instead of running directly
  main()

