code_list = [200,404,500,200]

for code in code_list:
    if code == 500:
        print(f"The server displayed the status code {code} , stopping execution")
        break
    elif code == 200:
        print(f"The server is working wiht hte status code {code}, and still running ")
    elif code == 404:
        print(f"The server is working wiht hte status code {code}, and still running ")
    else:
        pritn(f"The server got an unexpetced srror {code}")

print("----------End of the print Run------------")

