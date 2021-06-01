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
def modify_file_info(filename, no, line, info:str) -> tuple:
  file = open(filename, "r", encoding="utf-8")
  file_content = file.read()
  lines = file_content.split("\n")
  lines[no-1][line] = info,"\n"

  file = open("cars.txt", "w")
  file.writelines(lines)

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

def modify_car_details():
  no = ""
  lines = ""
  info = ""
  cars, price = modify_file_info("cars.txt", no, lines, info)
  for i in range(len(cars)):
    car_detail = cars[i].split("|")
    price_detail = price[i].split("|")

  print("Which car detail you want to modify?")
  print("1. Car Detail\n","2. Price Detail")
  input = get_user_int("Enter (1/2): ")
  
  if input == 1:
    print("Which car detail you want to modify?")
    print("1. Brand\n","2. Model\n","3.Description\n")
    no = get_user_int("Choose car detail(1-3): ")
    line = get_user_int("Enter line to modify: ")
    info = input("Enter detail: ")
    content = [car_detail[0][line], car_detail[1][line], car_detail[2][line]]
    content[no-1]()
    car_detail, _ = modify_file_info("cars.txt", no, line, info)
  else:
    print("Which price detail you want to modify?")
    print("1. Hourly Price\n","2. Daily Price")
    no = get_user_int("Choose price detail(1/2): ")
    line = get_user_int("Enter line to modify: ")
    info = input("Enter price: ")
    content = [price_detail[0][line], price_detail[1][line]]
    content[no-1]()
    _, price_detail = modify_file_info("cars.txt", no, line, info)

modify_car_details()

# Car: Brand, Model
# Description: Description
# Hourly Price: Hourly Price
# Daily Price: Daily Price

