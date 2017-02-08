def hello_user():
    "Powinien wyświetlać to, co sobie user wpisze jako string"

    name = input("Your name is: ")
    surname = input("Your surname is: ")

    if name == "" and surname == "":
        input ("You didn't tell your name and surname! Want to try again? Y/N ")

        if input == "y" or "Y": #jak zrobić by ten warunek zadziałał?
            print ("OK. TRYING AGAIN")
            hello_user()

        else:
            print ("BYE!")

    elif name == "":
        input ("Tell your name! Want to try again? Y/N ")
        if "y" or "Y":
            print ("OK. TRYING AGAIN")
            hello_user()
        else:
            print ("BYE!")

    elif surname == "":
        input ("Tell your surname! Want to try again? Y/N ")
        if "y" or "Y":
            print ("OK. TRYING AGAIN")
            hello_user()
        else:
            print ("BYE!")

    else:
        print  ("Hello, " + name + " " + surname + "!")



hello_user()
