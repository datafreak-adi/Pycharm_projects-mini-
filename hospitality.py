import json


class Report:
    def __init__(self):  # contructor
        self.d = {}
        try:
            with open("file.json", "r") as f:
                data = json.load(f)
                self.d.update(data)

        except FileNotFoundError:
            self.d = {"anant": "ANAN098"}
            with open("file.json", "w") as f:
                json.dump(self.d, f)

        # Making an user-friendly environment by giving choice
        print("Enter 1 to create a new entry else enter 2 to get a list of existing users")

        # USER enter his choice
        self.choice = int(input())

    # A function created to print mutiple lines in a file
    def hello(self):
        multiline_input = ""
        while True:
            line = input("Enter a line (Press 9 when you are done with typing): ")
            if line == "9":
                break
            multiline_input += line + "\n"

        return multiline_input

    def new_user(self):

        # If user enter 1 then he needs to create a new username and password
        # USer also need to enter patient's data
        if self.choice == 1:
            user = input("Enter new username : ")
            new_password = input("Enter new password : ")

            # Username and password of new patient get stored in the dictonary
            d2 = {user: new_password}

            self.d.update(d2)

            with open("file.json", "w") as f:
                json.dump(self.d, f)

            print(" Enter information about new user including his name, DOB ,sex ,Blood Group, medical history: ")

            with open(f"{user}.txt", "w") as f:
                f.writelines(self.hello())  # writing the data in the file

        else:
            # printing the list of existing users

            with open("file.json", "r") as f:
                data = json.load(f)
                print(data.keys())

            a = input("Enter username of the user you want to get acess of : ")

            b = input("Enter password of the user you want to get acess of : ")

            if a in data and data[a] == b:  # checking for correct username and password
                # To avoid any sort of error in program

                with open(f"{a}.txt", "r") as f:
                    while True:
                        line = f.readline()
                        if not line:
                            break
                        print(line)

            else:  # message to be returned if username or password is incorrect
                print("Wrong username or password, Please retry")
                self.choice = 2
                self.new_user()


# Function calling by creating an object
obj = Report()
obj.new_user()