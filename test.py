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

def get_user_not_empty(prompt_msg:str, error_msg:str) -> str:
  usr_input = ""
  while usr_input == "":
    usr_input = input(prompt_msg)
    if usr_input == "":
      print(error_msg + "\n")

  return usr_input

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

def view_cars():
  cars, price = get_file_info("car_test.txt")
  print("-----Car List-----")
  for i in range(len(cars)):
    car_detail = cars[i].split("|")
    price_detail = price[i].split("|")
    print(f"Car Index: {i+1}")
    print(f"Cars: {car_detail[0]}, {car_detail[1]}")
    print(f"Description: {car_detail[2]}")
    print(f"Hourly Price: {price_detail[0]}")
    print(f"Daily Price: {price_detail[1]}\n")

view_cars()

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
  
# modify file lines from a text file
def modify_file_info(filename:str, location:int, is_content1:bool, info:str) -> None:
  # location is the car idx position in the lists of strings
  # content1 is even lines, content2 is odd lines in a file
  content1, content2 = get_file_info(filename)
  # edit content1[location]/content2[location] based on is_content1
  if is_content1: content1[location] = info
  # cars[(cardetails+pricedetails)idx]
  else: content2[location] = info
  # prices[(cardetails+pricedetails)idx]

  final_string = ""
  for content_idx in range(len(content1)):
    # idx is an integer which will increase until the range ends
    # len must use with list to get int (number of items)
    final_string += content1[content_idx] + "\n"
    final_string += content2[content_idx] + "\n"
    # final_string += "a"
    # equivalent to
    # final_string = final_string + "a"
    # if final_string is "John"
    # final_string += a will be "Johna"

  # use with to auto close, followed by as file
  with open(filename, "w") as file:
    file.write(final_string)

# modify car details
def modify_car_details():
  cars, prices = get_file_info("car_test.txt")
  car_details = []
  price_details = []
  for i in range(len(cars)):
    car_details.append(cars[i].split("|"))
    price_details.append(prices[i].split("|"))
  # split makes strings into list in list
  view_cars()
  car_idx = -1
  while car_idx >= len(car_details) or car_idx < 0:
    car_idx = get_user_int("Choose a car index to edit: ") - 1

    print("Which car detail you want to modify?")
    print("1. Car Detail\n","2. Price Detail")
    choose_detail = get_user_int("Enter (1/2): ")
    
    if choose_detail == 1:
      print("Choose car detail to be modified:")
      print("1. Brand\n","2. Model\n","3. Description\n")
      detail_idx = get_user_int("Choose car detail(1-3): ") - 1
      info = get_user_not_empty("Enter New Car Detail: ", "Nothing is entered\nPlease try again!")
      modification = car_details[car_idx][detail_idx] = info
      # contatenate strings with "|"
      for car_idx in range(len(car_details)):
        car_details[car_idx][:3] += "|"
      modify_file_info("./car_test.txt", car_idx, True, modification)
    else:
      print("Which price detail you want to modify?")
      print("1. Hourly Price\n","2. Daily Price")
      detail_idx = get_user_int("Choose price detail(1/2): ") - 1
      info = get_user_float("Enter New Car Rent Price: ")
      modification = price_details[car_idx][detail_idx] = info
      # contatenate strings with loop and "|"
      for car_idx in range(len(price_details)):
        price_details[car_idx][:2] += "|"
      modify_file_info("./car_test.txt", car_idx, False, str(modification))

modify_car_details()

# Car: Brand, Model
# Description: Description
# Hourly Price: Hourly Price
# Daily Price: Daily Price

