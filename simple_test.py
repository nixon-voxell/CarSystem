import datetime

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

  # forcefully get a non-empty string from user
def get_user_not_empty(prompt_msg:str, error_msg:str="Input cannot be empty\n") -> str:
  usr_input = ""
  while usr_input == "":
    usr_input = input(prompt_msg)
    if usr_input == "":
      print(error_msg + "\n")

  return usr_input

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

CUSTOMERS_FILE = "./customers.txt"
CARS_FILE = "./cars.txt"
CUSTOMER_RENTS_FILE = "./customer_rents.txt"

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

search_records()