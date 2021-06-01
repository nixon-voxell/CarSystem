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

def modify_car_details():
  cars, prices = get_file_info("car_test.txt")
  car_details = []
  price_details = []
  for i in range(len(cars)):
    car_details.append(cars[i].split("|"))
    price_details.append(prices[i].split("|"))
  print(car_details)

# run the function
modify_car_details()