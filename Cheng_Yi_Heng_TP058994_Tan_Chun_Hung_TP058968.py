"""
Cheng Yi Heng TP058994
Tan Chung Hung TP048968
"""

import datetime
import os

# region CONSTANTS =================================
CUSTOMERS_FILE = "./customers.txt"
CUSTOMER_RENTS_FILE = "./customer_rents.txt"
CARS_FILE = "./cars.txt"
ADMINS_FILE = "./admins.txt"
# endregion ========================================

# region UTILS =====================================
def join_util(join_list:list, join_str:str) -> str:
  if join_list[0] != "":
    return join_str.join(join_list)
  else: return join_list[1]

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
def get_user_selection(prompt_msg:str, selections:list,
  error_msg:str="Input is not within selection given\n") -> str:
  usr_input = ""
  while usr_input not in selections:
    usr_input = input(prompt_msg)
    if usr_input not in selections:
      print(error_msg)

  return usr_input

# forcefully get integer input within a range from user
def get_user_int_range(prompt_msg:str, range_min:int, range_max:int,
  exceed_range_error_msg:str="Input has exceed the range given!\n") -> int:
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
# endregion  =======================================

# region USERNAMES AND PASSWORDS ===================
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

  with open(filename, "w") as file:
    file.write(final_string)

# add file lines to a text file
def add_file_info(filename:str, new_content1:str, new_content2:str) -> None:
  with open(filename, "a") as file:
    file.write(new_content1)
    file.write(new_content2)

# register new username and password
def register_new_user(filename:str, usernames:list) -> None:
  username = ""
  password = ""

  while username == "" or username in usernames:
    username = get_user_not_empty("Enter username: ")
    if username == "":
      print("Username cannot be empty!\n")
    elif username in usernames:
      print("Username has been taken!\nPlease enter another username.\n")

  while password == "":
    password = get_user_not_empty("Enter password: ")
    if password == "":
      print("Password cannot be empty!\n")

  print(f"Your username and password is: {username}, {password}")

  with open(filename, "a", encoding="utf-8") as customer_file:
    customer_file.write(f"{username}\n{password}\n")
# endregion  =======================================

# region LOGIN =====================================
def login(usernames:list, passwords:list) -> int:
  """
  login a user and return the index of the user
  """
  print("Please log in.\n")
  username = ""
  username_idx = 0
  while username not in usernames:
    # get input from user
    username = get_user_not_empty("Username: ")
    if username not in usernames:
      print("Username not found\nPlease try again\n")
    else:
      username_idx = usernames.index(username)

  password = ""
  # check if password is correct corresponding to the username_idx
  while password != passwords[username_idx]:
    # get input from user
    password = get_user_not_empty("Password: ")
    if password != passwords[username_idx]:
      print("Password incorrect\nPlease try again\n")

  print("Logged in!\n")
  input("Press enter to continue...")
  os.system("cls")
  return username_idx
# endregion ========================================

# region ADMIN MENU ================================
def add_new_car() -> None:
  car_details, _ = get_file_info(CARS_FILE)
  car_details = [c.split("|") for c in car_details]
  # lower down all cases to perform name checking
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

    car_detail = f"{brand}|{model}|{description}|{amount}\n"
    car_name = brand.lower() + model.lower()

    if car_name in used_car_names:
      print("The car name has been taken!\nPlease create a unique one.\n")

  hourly_price = get_user_float("Enter hourly price: ")
  daily_price = get_user_float("Enter daily price: ")
  price_detail = f"{hourly_price}|{daily_price}\n"

  print(f"Your car name is: {brand}, {model}")
  print(f"Your car description is: {description}")
  print(f"The hourly price is: {hourly_price}\nThe daily price is: {daily_price}")

  add_file_info(CARS_FILE, car_detail, price_detail)

# modify car details
def modify_car_details():
  cars, prices = get_file_info(CARS_FILE)
  car_details = []
  price_details = []
  for i in range(len(cars)):
    # split makes strings into list in list
    car_details.append(cars[i].split("|"))
    price_details.append(prices[i].split("|"))

  view_cars(False, False)
  car_idx = get_user_int_range("Choose a car index to edit: ", 1, len(car_details)) - 1

  print("\nWhich car detail you want to modify?")
  print("\n1. Car Detail\n2. Price Detail")
  choose_detail = get_user_int_range("\nEnter (1/2): ", 1, 2)
  
  if choose_detail == 1:
    print("\nChoose car detail to be modified:")
    print("\n1. Brand\n2. Model\n3. Description\n4. Cars Remaining")
    detail_idx = get_user_int_range("\nChoose car detail (1-4): ", 1, 4) - 1
    if detail_idx != 3:
      new_info = get_user_not_empty("\nEnter new car detail: ", "Nothing is entered. Please try again!\n")
    else:
      new_info = get_user_int("\nEnter new car remaining: ")

    car_details[car_idx][detail_idx] = str(new_info)
    modification = car_details[car_idx]
    modification = join_util(modification, "|")

    modify_file_info(CARS_FILE, car_idx, True, modification)
  else:
    print("\nWhich price detail you want to modify?")
    print("\n1. Hourly Price\n2. Daily Price")
    detail_idx = get_user_int_range("\nChoose price detail(1/2): ", 1, 2) - 1
    new_info = get_user_float("\nEnter new car rent price: ")

    price_details[car_idx][detail_idx] = str(new_info)
    modification = price_details[car_idx]
    modification = join_util(modification, "|")

    modify_file_info(CARS_FILE, car_idx, False, modification)

def display_records():
  car_indices, dates = get_file_info(CUSTOMER_RENTS_FILE)
  car_indices = [idx.split("|") for idx in car_indices]
  dates = [date.split("|") for date in dates]

  car_details, price_details = get_file_info(CARS_FILE)
  car_details = [detail.split("|") for detail in car_details]
  price_details = [detail.split("|") for detail in price_details]

  usernames, _ = get_file_info(CUSTOMERS_FILE)

  # show rented cars START
  print("\nRented cars:")
  print(len(car_indices))
  for customer_idx in range(len(car_indices)):
    date_details = dates[customer_idx]
    indices_details = car_indices[customer_idx]
    if len(indices_details) <= 0: continue

    print(f"\nCars rented by: {usernames[customer_idx]}\n")
    rent_idx = 0
    for history_idx in range(len(indices_details)):
      if date_details[history_idx] != "-":
        rent_idx += 1
        rent_idx_str = f"{rent_idx}. "
        rent_details = indices_details[history_idx].split(",")
        rent_car_date = date_details[history_idx].split(",")
        if rent_car_date[0] == "":
          print("No cars rented.")
          break
        # convert all string elements from string to integer
        rent_car_date = [int(d) for d in rent_car_date]
        # create readable datetime format
        rent_car_date = datetime.datetime(
          rent_car_date[0], rent_car_date[1],
          rent_car_date[2], rent_car_date[3],
          rent_car_date[4], rent_car_date[5]
        )
        rent_car_details = car_details[int(rent_details[0])]
        print(f"{rent_idx_str}Car: {rent_car_details[0]}, {rent_car_details[1]}")
        print(" "*len(rent_idx_str) + f"Rented on: {rent_car_date}")
        if rent_details[2] == "D":
          print(" "*len(rent_idx_str) + f"Rented for: {rent_details[1]} day(s)")
        else:
          print(" "*len(rent_idx_str) + f"Rented for: {rent_details[1]} hour(s)")
        print(" "*len(rent_idx_str) + f"Status: {'Returned' if int(rent_details[3]) else 'Not returned'}")
  # show rented cars END

  # show cars that are booked START
  print("\n" + "="*50)
  print("Booked cars:")
  for customer_idx in range(len(car_indices)):
    date_details = dates[customer_idx]
    indices_details = car_indices[customer_idx]

    print(f"\nCars booked by: {usernames[customer_idx]}\n")
    rent_idx = 0
    for history_idx in range(len(indices_details)):
      if date_details[history_idx] == "":
        print("No cars booked.")
        break
      if date_details[history_idx] == "-":
        rent_idx += 1
        rent_idx_str = f"{rent_idx}. "
        rent_details = indices_details[history_idx].split(",")
        rent_car_details = car_details[int(rent_details[0])]
        print(f"{rent_idx_str}Car: {rent_car_details[0]}, {rent_car_details[1]}")
  # show cars that are booked END

  # show cars available for rent START
  print("\n" + "="*50)
  print("Cars available for rent:\n")
  view_cars(True, True)
  # show cars available for rent END

# search specific records
def search_records():
  car_indices, dates = get_file_info(CUSTOMER_RENTS_FILE)
  customer_names, _ = get_file_info(CUSTOMERS_FILE)
  car_details, _ = get_file_info(CARS_FILE)

  car_indices = [c.split("|") for c in car_indices]
  dates = [d.split("|") for d in dates]
  car_details = [c.split("|") for c in car_details]

  print("")
  for i in range(len(customer_names)):
    print(f"{i+1}. {customer_names[i]}")
  customer_idx = get_user_int_range(f"\nChoose a customer to be searched (1-{len(customer_names)}): ", 1, len(customer_names)) - 1

  print("\nChoose your option below:")
  print("1. Customer booking\n2. Customer payment")
  option = get_user_int_range("\nEnter option (1/2): ", 1, 2) 
  
  if option == 1:
    # do customer booking
    print(f"\nCars booked by: {customer_names[customer_idx]}\n")
    # all date history in that line
    date_details = dates[customer_idx]
    # all index history in that line
    indices_details = car_indices[customer_idx]

    book_idx = 0
    for history_idx in range(len(indices_details)):
      if date_details[history_idx] == "-":
        book_idx += 1
        rent_idx_str = f"{book_idx}. "
        rent_details = indices_details[history_idx].split(",")
        rent_car_details = car_details[int(rent_details[0])]
        print(f"{rent_idx_str}Car: {rent_car_details[0]}, {rent_car_details[1]}")

  else:
    # do customer payment
    # name in customer_names[i] == car_info[i]
    print(f"\nCars rent by: {customer_names[customer_idx]}\n")
    date_details = dates[customer_idx]
    indices_details = car_indices[customer_idx]

    book_idx = 0
    for history_idx in range(len(indices_details)):
      if date_details[history_idx] != "-":
        book_idx += 1
        rent_idx_str = f"{book_idx}. "
        rent_details = indices_details[history_idx].split(",")
        rent_car_details = car_details[int(rent_details[0])]
        rent_car_date = date_details[history_idx].split(",")
        # convert all string elements from string to integer
        rent_car_date = [int(d) for d in rent_car_date]
        # create readable datetime format
        rent_car_date = datetime.datetime(
          rent_car_date[0], rent_car_date[1],
          rent_car_date[2], rent_car_date[3],
          rent_car_date[4], rent_car_date[5]
        )
        print(f"{rent_idx_str}Car: {rent_car_details[0]}, {rent_car_details[1]}")
        print(" "*len(rent_idx_str) + f"Rented on: {rent_car_date}")
        if rent_details[2] == "D":
          print(" "*len(rent_idx_str) + f"Rented for: {rent_details[1]} day(s)")
        else:
          print(" "*len(rent_idx_str) + f"Rented for: {rent_details[1]} hour(s)")

  input("Press enter to continue...")

def return_rented_cars():
  car_indices, dates = get_file_info(CUSTOMER_RENTS_FILE)
  car_indices = [idx.split("|") for idx in car_indices]
  dates = [date.split("|") for date in dates]

  car_details, price_details = get_file_info(CARS_FILE)
  car_details = [detail.split("|") for detail in car_details]
  price_details = [detail.split("|") for detail in price_details]

  usernames, _ = get_file_info(CUSTOMERS_FILE)

  print("")
  for i in range(len(usernames)):
    print(f"{i+1}. {usernames[i]}")

  customer_idx = get_user_int_range(f"Select a customer (1-{len(usernames)}): ", 1, len(usernames)) - 1

  # show unreturned cars START
  date_details = dates[customer_idx]
  indices_details = car_indices[customer_idx]
  unreturned_history_indices = []
  unreturned_car_indices = []
  unreturned_car_dates = []
  for history_idx in range(len(indices_details)):
    if date_details[history_idx] != "-":
      rent_details = indices_details[history_idx].split(",")
      rent_car_date = date_details[history_idx].split(",")
      if rent_car_date[0] == "": continue
      # convert all string elements from string to integer
      rent_car_date = [int(d) for d in rent_car_date]
      # create readable datetime format
      rent_car_date = datetime.datetime(
        rent_car_date[0], rent_car_date[1],
        rent_car_date[2], rent_car_date[3],
        rent_car_date[4], rent_car_date[5]
      )
      if rent_details[3] != "1":
        # store history index, car index and rent date
        unreturned_history_indices.append(history_idx)
        unreturned_car_indices.append(int(rent_details[0]))
        unreturned_car_dates.append(str(rent_car_date))

  if len(unreturned_history_indices) > 0:
    print(f"\nCars that are not returned by: {usernames[customer_idx]}")
    for i in range(len(unreturned_car_indices)):
      unreturned_car_detail = car_details[unreturned_car_indices[i]]
      print(f"{i+1}. {unreturned_car_detail[0]}, {unreturned_car_detail[1]}")
      print(" "*len(f"{i+1}. ") + f"Rented on: {unreturned_car_dates[i]}")

    return_car_idx = get_user_int_range(f"\nChoose a car to return (1-{len(unreturned_history_indices)}): ", 1, len(unreturned_history_indices)) - 1
    # return the car by setting the last value in rent_details to "1"
    rent_details = indices_details[unreturned_history_indices[return_car_idx]].split(",")
    rent_details[3] = "1"
    indices_details[unreturned_history_indices[return_car_idx]] = join_util(rent_details, ",")

    modify_file_info(CUSTOMER_RENTS_FILE, customer_idx, True, join_util(indices_details, "|"))

  else:
    print(f"There are no cars to return from {usernames[customer_idx]}.")

  input("Car returned, press enter to continue...")
  # show unreturned cars END

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
  admin_func = [add_new_car, modify_car_details, display_records, search_records, return_rented_cars]

  usernames, passwords = get_file_info(ADMINS_FILE)
  login(usernames, passwords)
  while True:
    os.system("cls")
    for i in range(len(admin_list)):
      print(admin_list[i])
    no = get_user_int_range("Choose option (1-6): ", 1, 6)
    if no == 6: return
    admin_func[no-1]()
# endregion ========================================

# region ALL CUSTOMERS MENU ========================
def create_acc():
  usernames, _ = get_file_info(CUSTOMERS_FILE)
  register_new_user(CUSTOMERS_FILE, usernames)
  add_file_info(CUSTOMER_RENTS_FILE, "\n", "\n")

def view_cars(view_available:bool=True, wait=True) -> list:
  cars, price = get_file_info(CARS_FILE)
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

  if wait: input("Press enter to continue...")
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
# endregion ========================================

# region REGISTERED CUSTOMER MENU ==================
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

  rent_idx = 0
  for i in range(len(date_details)):
    if date_details[i] != "-":
      rent_idx += 1
      rent_idx_str = f"{rent_idx}. "
      rent_details = indices_details[i].split(",")
      rent_car_date = date_details[i].split(",")
      if rent_car_date[0] == "":
        print("No cars rented.")
        break
      # convert all string elements from string to integer
      rent_car_date = [int(d) for d in rent_car_date]
      # create readable datetime format
      rent_car_date = datetime.datetime(
        rent_car_date[0], rent_car_date[1],
        rent_car_date[2], rent_car_date[3],
        rent_car_date[4], rent_car_date[5]
      )
      rent_car_details = car_details[int(rent_details[0])]
      print(f"{rent_idx_str}Car: {rent_car_details[0]}, {rent_car_details[1]}")
      print(" "*len(rent_idx_str) + f"Rented on: {rent_car_date}")
      print(" "*len(rent_idx_str) + f"Status: {'Returned' if int(rent_details[3]) else 'Not returned'}")

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
    if date_details[i] == "":
      print("No cars booked.")
      break
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

  available_car_indices = view_cars(True, False)
  available_car_indices = [str(idx+1) for idx in available_car_indices]
  car_idx = get_user_selection("\nSelect car index: ", available_car_indices, "Car index is not available for rent!\n")
  car_idx = int(car_idx) - 1

  car_details[car_idx][3] = str(int(car_details[car_idx][3]) - 1)
  modify_file_info(CARS_FILE, car_idx, True, join_util(car_details[car_idx], "|"))
  # decrease car remaining by 1 END

  # car_indices: car_idx,duration,D/H|car_idx,duration,D/H|car_idx,duration,D/H
  # dates      : date|date|date

  # ask how long does the customer wants to rent the car START
  print("\nDo you want to rent the car in days or hours? Select '1' for days and '2' for hours")
  selection = get_user_int_range("\nChoose option (1/2): ", 1, 2)
  booking_result = ""
  if selection == 1:
    duration = get_user_int("How many days do you want to rent the car: ")
    booking_result = f"{car_idx},{duration},D,0"
  else:
    duration = get_user_int("How many hours do you want to rent the car: ")
    booking_result = f"{car_idx},{duration},H,0"
  # ask how long does the customer wants to rent the car END

  # append new car index and allocate a new date in customer_rents.txt START
  car_indices, dates = get_file_info(CUSTOMER_RENTS_FILE)
  car_indices = [idx.split("|") for idx in car_indices]
  dates = [date.split("|") for date in dates]

  car_indices[curr_user_idx].append(booking_result)
  dates[curr_user_idx].append("-")

  new_car_indices = join_util(car_indices[curr_user_idx], "|")
  new_dates = join_util(dates[curr_user_idx], "|")

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
      rent_price= float(rent_car_price[0])*int(rent_details[1])
      print(rent_car_details[0], rent_car_details[1], end=" ")
      print(f"* {rent_details[1]} hours (RM {rent_price})")
      total_price += rent_price
    else:
      rent_price = float(rent_car_price[1])*int(rent_details[1])
      print(rent_car_details[0], rent_car_details[1], end=" ")
      print(f"* {rent_details[1]} days (RM {rent_price})")
      total_price += rent_price
      
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
    modify_file_info(CUSTOMER_RENTS_FILE, curr_user_idx, False, join_util(dates[curr_user_idx], "|"))
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
# endregion ========================================

# region MAIN PROGRAM ==============================
def exit_program() -> None:
  print("\nDo you want to continue? To exit to the Main Menu type '1', To Terminate Program type '2': ")
  no = get_user_int_range("Choose option (1/2): ", 1, 2)
  if no == 2: exit()

def main() -> None:
  user_func = [admin, all_customer, registered_customer]

  user_type_list = [
    "MAIN MENU",
    "1. Admin",
    "2. All Customers (Registered / Not-Registered)",
    "3. Registered Customer",
    "4. Exit Program\n"
  ]

  while True:
    os.system("cls")
    print("Welcome to SUPER CAR RENTAL SERVICES!!!\n")
    for i in range(len(user_type_list)):
      print(user_type_list[i])

    no = get_user_int_range("Choose user(1-4): ", 1, 4)
    if no == 4: exit_program()
    else: user_func[no-1]()
# endregion ========================================

main()

