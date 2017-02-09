# zrobić z tego funkcję, która:
# po poprawnym wykoanniu funkcji, osoba zotaje zapisana na liście gości na blogu
# dodatkowo, niech np. dodaje jakiś randomowy przydomek ze słownika (trza utworzyć)
#

def hello_user():
    "Powinien wyświetlać to, co sobie user wpisze jako string"

    name = input("Your name is: ")
    surname = input("Your surname is: ")

    if name == "" and surname == "": # zrobić z tego funkcję dla wszystkich przypadków
        print ("You didn't tell your name and surname! Want to try again? Y/N")
        no_name()
    elif name == "":
        print ("You didn't tell your name! Want to try again? Y/N ")
        no_name()
    elif surname == "":
        no_name_surname = input ("You didn't tell your surname! Want to try again? Y/N ")
        no_name()
    else:
        print ("Hello, " + name + " " + surname + "!")

def no_name(): #jak zaimplementować tę funkcję do hello_user?
    no_name_surname = input()
    no_name_surname = no_name_surname.upper()
    if no_name_surname == "Y":
        print ("OK. TRYING AGAIN")
        hello_user()
    else:
        print ("BYE THEN!")

hello_user()
