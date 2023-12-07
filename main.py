resquest = 0
code = 1234

while resquest < 3:
    user = int(input("Enter the code: "))
    if user == code:
        print("Welcome")
        break
    else:
        print("Mauvais PIN", 2 - resquest, "tentatives restants")
    resquest = resquest + 1
