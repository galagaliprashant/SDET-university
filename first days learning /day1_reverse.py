#write a script to reverse the string
# Do not use the loops and instead use the slicing

#input the string in a variable
#put the new slicing string to the new variable
#and print the new variable

#define the function def logic
def reverse(text):
    return text[::-1]

def strip(text):
    return text[7::1]

#Testcase1

original= "Prashnth"
reversed = reverse(original)

#test case 2

original = "Order #12345"
striped_ID = strip(original)

#verification part
if original == reversed:
    print("Sorry ,mchaa")
else:
    print("Hurray success")

if original == striped_ID:
    print("Hurray success")
else:
    print("Sorry ,mchaa")

print(f"The orignincal was :{original}")
print(f"The striped id was {striped_ID}")

