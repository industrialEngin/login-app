name = "industrial engineer"
password = "1234"
chance = 3
for i in range(3):
    name1 = input("Enter your name: ")
    password1 = input("Enter your password: ")
    if(name1!=name or password1!=password):
        print("Login Failed!")
        chance-=1
        print(chance, "Chances")  
    else:
        print("Enjoy the movie")
