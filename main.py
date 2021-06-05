import datetime
import os

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
      print(error_msg)

  return usr_input

# forcefully get a string input that is inside the given selection from user
def get_user_selection(prompt_msg:str, selections:list, error_msg:str="Input is not within selection given\n") -> str:
  usr_input = ""
  while usr_input not in selections:
    usr_input = input(prompt_msg)
    if usr_input not in selections:
      print(error_msg)

  return usr_input

# forcefully get integer input within a range from user
def get_user_int_range(prompt_msg:str, range_min:int, range_max:int, exceed_range_error_msg:str="Input has exceed the range given!\n") -> int:
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
  print("Please log in.\n")
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
  input("Press enter to continue...")
  os.system("cls")
  return username_idx
# endregion ===================================

# region ADMIN MENU ===========================
def add_new_car(filename:str="./cars.txt") -> None:
  car_details, _ = get_file_info(filename)
  car_details = [c.split("|") for c in car_details]
  used_car_names = [c[0].lower()+c[1].lower() for c in car_details]

  car_detail = ""
  car_name = ""

  brand = ""
  model = ""
  description = ""

  while car_detail == "" or car_name in used_car_names:
    brand = get_user_not_empty("Enter brand: ", "Brand cannot be empty!\n")
    model = get_user_not_empty("Enter model: ", "Model cannot be empty!\n")
    description = get_user_not_empty("Enter description:  ", "Description cannot be empty!\n")
    amount = get_user_int("Enter amount of cars to add: ")

    car_detail = f"{brand}|{model}|{description}|{amount}"
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

# modify car details
def modify_car_details():
  cars, prices = get_file_info(CARS_FILE)
  car_details = []
  price_details = []
  for i in range(len(cars)):
    # split makes strings into list in list
    car_details.append(cars[i].split("|"))
    price_details.append(prices[i].split("|"))

  view_cars(False)
  car_idx = get_user_int_range("Choose a car index to edit: ", 1, len(car_details)) - 1

  print("\nWhich car detail you want to modify?")
  print("\n1. Car Detail\n2. Price Detail")
  choose_detail = get_user_int_range("\nEnter (1/2): ", 1, 2)
  
  if choose_detail == 1:
    print("\nChoose car detail to be modified:")
    print("\n1. Brand\n2. Model\n3. Description\n4. Cars Remaining")
    detail_idx = get_user_int_range("\nChoose car detail (1-4): ", 1, 4) - 1
    if detail_idx != 3:
      new_info = get_user_not_empty("\nEnter new car detail: ", "Nothing is entered\nPlease try again!\n")
    else:
      new_info = get_user_int("\nEnter new car remaining: ")

    car_details[car_idx][detail_idx] = str(new_info)
    modification = car_details[car_idx]
    modification = "|".join(modification)

    modify_file_info(CARS_FILE, car_idx, True, modification)
  else:
    print("\nWhich price detail you want to modify?")
    print("\n1. Hourly Price\n2. Daily Price")
    detail_idx = get_user_int_range("\nChoose price detail(1/2): ", 1, 2) - 1
    new_info = get_user_float("\nEnter new car rent price: ")

    price_details[car_idx][detail_idx] = str(new_info)
    modification = price_details[car_idx]
    modification = "|".join(modification)

    modify_file_info(CARS_FILE, car_idx, False, modification)

def display_records():
  # cars rented out
  # cars available for rent
  # customer bookings
  # customer payment for a specific time duration
  pass

def search_records():
  # customer booking
  # customer payment

  """
  1. select customer
  2. choose booking or payment
  3. display

  - == not paid, only boooked
  date == paid
  """
  pass

# MAIN FUNCTION
def admin():
  os.system("cls")
  admin_list = [
    "ADMIN",
    "\n1. Add a new car.",
    "2. Modify car details.",
    "3. Display records",
    "4. Search specific records",
    "5. Return a rented car.",
    "6. Return to main menu.\n"
  ]
  admin_func = [add_new_car, modify_car_details, display_records, search_records]

  usernames, passwords = get_file_info(ADMINS_FILE)
  login(usernames, passwords)
  while True:
    os.system("cls")
    for i in range(len(admin_list)):
      print(admin_list[i])
    no = get_user_int_range("Choose option (1-6): ", 1, 6)
    if no == 6: return
    admin_func[no-1]()
# endregion ===================================

# region ALL CUSTOMERS MENU ========================
def create_acc():
  usernames, _ = get_file_info(CUSTOMERS_FILE)
  register_new_user(CUSTOMERS_FILE, usernames)
  add_file_info(CUSTOMER_RENTS_FILE, "\n", "\n")

def view_cars(view_available:bool=True) -> list:
  cars, price = get_file_info(CARS_FILE)
  print("\n========== Car List ==========\n")
  available_car_indices = []
  for i in range(len(cars)):
    car_detail = cars[i].split("|")
    price_detail = price[i].split("|")
    if view_available and int(car_detail[3]) <= 0: continue
    available_car_indices.append(i)
    print(f"Car Index: {i+1}")
    print(f"Car: {car_detail[0]}, {car_detail[1]}")
    print(f"Description: {car_detail[2]}")
    print(f"Cars Remaining: {car_detail[3]}")
    print(f"Hourly Price: {price_detail[0]}")
    print(f"Daily Price: {price_detail[1]}\n")

  input("Press enter to continue...")
  return available_car_indices

# MAIN FUNCTION
def all_customer():
  os.system("cls")
  customer_list = [
    "ALL CUSTOMER",
    "\n1. View all cars available for rent.",
    "2. Create new account.",
    "3. Exit to main menu\n"
  ]
  customer_func = [view_cars, create_acc]

  while True:
    os.system("cls")
    for i in range(len(customer_list)):
      print(customer_list[i])
    no = get_user_int_range("Choose option (1-3): ", 1, 3)
    if no == 3: return
    customer_func[no-1]()
# endregion ===================================

# region REGISTERED CUSTOMER MENU =============
def modify_personal_details(curr_user_idx:int) -> None:
  print("\n1. Username\n2. Password\n3. Cancel")
  selection = get_user_int_range("Choose option (1-3): ", 1, 3, "Select 1 or 2 only!\n")
  if selection == 3: return

  if selection == 1:
    new_username = get_user_not_empty("New username: ")
    modify_file_info(CUSTOMERS_FILE, curr_user_idx, True, new_username)
  else:
    new_password = get_user_not_empty("New password: ")
    modify_file_info(CUSTOMERS_FILE, curr_user_idx, False, new_password)

def view_history(curr_user_idx:int) -> None:
  car_indices, dates = get_file_info(CUSTOMER_RENTS_FILE)
  car_indices = [idx.split("|") for idx in car_indices]
  dates = [date.split("|") for date in dates]

  car_details, price_details = get_file_info(CARS_FILE)
  car_details = [detail.split("|") for detail in car_details]
  price_details = [detail.split("|") for detail in price_details]

  print("\nRented cars:\n")
  rented_cars = []

  date_details = dates[curr_user_idx]
  indices_details = car_indices[curr_user_idx]

  for i in range(len(date_details)):
    if date_details[i] != "-":
      rent_details = indices_details[i].split(",")
      rent_car_details = car_details[int(rent_details[0])]
      rent_car_date = date_details[i].split(",")
      rent_car_date = [int(d) for d in rent_car_date]
      rent_car_date = datetime.datetime(
        rent_car_date[0],
        rent_car_date[1],
        rent_car_date[2],
        rent_car_date[3],
        rent_car_date[4],
        rent_car_date[5]
      )
      print(f"Car: {rent_car_details[0]}, {rent_car_details[1]}")
      print(f"Rented on: {rent_car_date}\n")

  input("Press enter to continue...")

def view_booked_cars(curr_user_idx:int) -> None:
  car_indices, dates = get_file_info(CUSTOMER_RENTS_FILE)
  car_indices = [idx.split("|") for idx in car_indices]
  dates = [date.split("|") for date in dates]

  car_details, price_details = get_file_info(CARS_FILE)
  car_details = [detail.split("|") for detail in car_details]
  price_details = [detail.split("|") for detail in price_details]

  print("\nCars to be rented:\n")
  rented_cars = []

  date_details = dates[curr_user_idx]
  indices_details = car_indices[curr_user_idx]

  for i in range(len(date_details)):
    if date_details[i] == "-":
      rent_details = indices_details[i].split(",")
      rent_car_details = car_details[int(rent_details[0])]
      rent_car_price = price_details[int(rent_details[0])]
      print(f"Car: {rent_car_details[0]}, {rent_car_details[1]}")
      print(f"Description: {rent_car_details[2]}")
      if rent_details[2] == "H":
        print(f"Booked for {rent_details[1]} hours.")
        total_price = float(rent_car_price[0])*int(rent_details[1])
      else:
        print(f"Booked for {rent_details[1]} days.")
        total_price = float(rent_car_price[1])*int(rent_details[1])
      print(f"Total Price: RM {total_price}\n")

  input("Press enter to continue...")

def book_cars(curr_user_idx:int) -> None:
  # decrease cars remaning by 1 START
  car_details, price_details = get_file_info(CARS_FILE)
  car_details = [detail.split("|") for detail in car_details]
  price_details = [detail.split("|") for detail in price_details]

  available_car_indices = view_cars(True)
  available_car_indices = [str(idx+1) for idx in available_car_indices]
  car_idx = get_user_selection("\nSelect car index: ", available_car_indices, "Car index is not available for rent!\n")
  car_idx = int(car_idx) - 1

  car_details[car_idx][3] = str(int(car_details[car_idx][3]) - 1)
  modify_file_info(CARS_FILE, car_idx, True, "|".join(car_details[car_idx]))
  # decrease car remaining by 1 END

  # car_indices: car_idx,duration,D/H|car_idx,duration,D/H|car_idx,duration,D/H
  # dates      : date|date|date

  # ask how long does the customer wants to rent the car START
  print("\nDo you want to rent the car in days or hours? Select '1' for days and '2' for hours")
  selection = get_user_int_range("\nChoose option (1/2): ", 1, 2)
  booking_result = ""
  if selection == 1:
    duration = get_user_int("How many days do you want to rent the car: ")
    booking_result = f"{car_idx},{duration},D"
  else:
    duration = get_user_int("How many hours do you want to rent the car: ")
    booking_result = f"{car_idx},{duration},H"
  # ask how long does the customer wants to rent the car END

  # append new car index and allocate a new date in customer_rents.txt START
  car_indices, dates = get_file_info(CUSTOMER_RENTS_FILE)
  car_indices = [idx.split("|") for idx in car_indices]
  dates = [date.split("|") for date in dates]

  car_indices[curr_user_idx].append(booking_result)
  dates[curr_user_idx].append("-")

  new_car_indices = "|".join(car_indices[curr_user_idx])
  new_dates = "|".join(dates[curr_user_idx])

  modify_file_info(CUSTOMER_RENTS_FILE, curr_user_idx, True, new_car_indices)
  modify_file_info(CUSTOMER_RENTS_FILE, curr_user_idx, False, new_dates)
  # append new car index and allocate a new date in customer_rents.txt END

def payment(curr_user_idx:int) -> None:
  # check which booked cars are not payed yet START
  car_indices, dates = get_file_info(CUSTOMER_RENTS_FILE)
  car_indices = [idx.split("|") for idx in car_indices]
  dates = [date.split("|") for date in dates]

  unpaid_car_indices = []
  for i in range(len(car_indices[curr_user_idx])):
    if dates[curr_user_idx][i] == "-":
      unpaid_car_indices.append(i)
  # check which booked cars are not payed yet END

  car_details, price_details = get_file_info(CARS_FILE)
  car_details = [detail.split("|") for detail in car_details]
  price_details = [detail.split("|") for detail in price_details]

  # print out details and show cars that the customer booked START
  total_price = 0
  print("\nCars booked:\n")
  for idx in unpaid_car_indices:
    rent_details = car_indices[curr_user_idx][idx].split(",")
    rent_car_details = car_details[int(rent_details[0])]
    rent_car_price = price_details[int(rent_details[0])]
    if rent_details[2] == "H":
      print(rent_car_details[0], rent_car_details[1], end=" ")
      print(f"* {rent_details[1]} Hours ({rent_car_price[0]})")
      total_price += float(rent_car_price[0])*int(rent_details[1])
    else:
      print(rent_car_details[0], rent_car_details[1], end=" ")
      print(f"* {rent_details[1]} Days ({rent_car_price[1]})")
      total_price += float(rent_car_price[1])*int(rent_details[1])
      
  print(f"The total price is: RM {total_price}\n")
  # print out details and show cars that the customer booked END

  print("Type '1' to pay, '2' to cancel payment.")
  pay = get_user_int_range("Choose option (1/2): ", 1, 2)
  if pay == 1:
    # replace "-" in dates with actual dates to mark it as paid START
    # get current time
    current_time = datetime.datetime.now().strftime("%Y,%m,%d,%H,%M,%S")
    for idx in unpaid_car_indices:
      dates[curr_user_idx][idx] = current_time
    # replace "-" in dates with actual dates to mark it as paid END

    # write car_indices and dates back into the file START
    modify_file_info(CUSTOMER_RENTS_FILE, curr_user_idx, False, "|".join(dates[curr_user_idx]))
    # write car_indices and dates back into the file END

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
  os.system("cls")
  registered_customer_list = [
    "REGISTERED CUSTOMER",
    "\n1. Modify personal details.",
    "2. View personal rental history.",
    "3. View details of cars to be rented out.",
    "4. Select and book a car for a specific duration.",
    "5. Do payment to confirm Booking.",
    "6. Delete account.",
    "7. Exit to main menu\n"
  ]
  registered_customer_func = [modify_personal_details, view_history, view_booked_cars, book_cars, payment, delete_account]

  usernames, passwords = get_file_info(CUSTOMERS_FILE)
  curr_user_idx = login(usernames, passwords)
  in_loop = True
  while in_loop:
    os.system("cls")
    for i in range(len(registered_customer_list)):
      print(registered_customer_list[i])
    no = get_user_int("Choose option (1-7): ")
    if no == 7: return
    in_loop = not registered_customer_func[no-1](curr_user_idx)
# endregion ===================================

# region MAIN PROGRAM ===================================
def exit_program() -> None:
  print("\nDo you want to continue? To exit to the Main Menu type '1', To Terminate Program type '2': ")
  no = get_user_int_range("Choose option (1/2): ", 1, 2)
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
    os.system("cls")
    print("Welcome to SUPER CAR RENTAL SERVICES!!!")
    print("\n========== Main Menu ==========\n")
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

