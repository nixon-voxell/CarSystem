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

def func1():
  print("in func1")

def func2():
  print("in func2")

def func3():
  print("in func3")

func_list = [func1, func2, func3]

print("Input a function number to run (1/2/3)")
no = get_user_int("Number: ")
func_list[no-1]()

# find a pattern between if statement and the function call
# if no == 1:
#   func_list[0]()
# elif no == 2:
#   func_list[1]()
# elif no == 3:
#   func_list[2]()
