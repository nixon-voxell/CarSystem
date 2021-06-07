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
  car_details, dates = get_file_info(CUSTOMER_RENTS_FILE)
  names, _ = get_file_info(CUSTOMERS_FILE)
  car_list, _ = get_file_info(CARS_FILE)
  
  car_info = [] 
  date_info = []
  cars = []

  # customer_rents
  for i in range(len(car_details)):
    # split makes strings into lists in list
    car_info.append(car_details[i].split("|"))
    date_info.append(dates[i].split("|"))
  
  # cars.txt
  for i in range(len(car_list)):
    cars.append(car_list[i].split("|"))
  
  name = get_user_not_empty("Enter customer name to be searched: ", "Input cannot be empty\n")
  while name in names:
    print("Choose your option below:")
    print("1. Customer booking\n2. Customer payment")
    option = get_user_int_range("Enter option (1/2): ", 1, 2, "Input has exceed the range given!\n") 
    
    if option == 1:
      # do customer booking
      # name in names[i] == car_info[i]
      customer_idx = names.index(name)
      f"{name}'s index is: {customer_idx}"
      if customer_idx >= 0:
        print(name, "booked car detail below: ")
      date_info[customer_idx].index("-")
      rent_car_list = car_info[i].split("|")
      for car in rent_car_list:
        car_idx = car.split(",")[0]
      for car in cars:
        print(cars[car_idx][:2])
      break

    else:
      # do customer payment
      # name in names[i] == car_info[i]
      customer_idx = names.index(name)
      f"{name}'s index is: {customer_idx}"
      if customer_idx >= 0:
        print(name, "paid car detail below: ")
      date_info[customer_idx].index(not "-")
      rent_car_list = car_info[i].split("|")
      for car in rent_car_list:
        car_idx = car.split(",")[0]
      for car in cars:
        print(cars[car_idx][:2])
      break

  return print(name,"is not inside customers.txt\n")

search_records()