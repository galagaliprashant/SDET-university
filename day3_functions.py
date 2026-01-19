# code_list = [200,404,404,402,24242,2342,500]
#
# print("---------------The start of Automation run--------------")
#
# def code_list1(code):
#      if code == 500:
#         print(f"The server displayed the status code {code} , stopping execution")
#      elif code == 200:
#         print(f"The server is working wiht hte status code {code}, and still running ")
#      elif code == 404:
#         print(f"The server is working wiht hte status code {code}, and still running ")
#      else:
#         print(f"The server got an unexpetced srror {code}")
#
# for code in code_list:
#     code_list1(code)
#
# print("----------End of the print Run------------")


def make_coffee(type):
    if type == "coffee":
        return "Coffee"
    elif type == "milk":
        return "Milk"
    else:
        return "Srry not ur day"

print(make_coffee("coffee"))
print(make_coffee("milk"))
print(make_coffee("ksjfb"))