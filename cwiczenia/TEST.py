hello = "Wpisz swoje imię!"
print (hello)
name = input()
a = "Cześć, " + name + "!"

papaj = ["Karol", "Jan", "Jan Paweł"] #lista elementów papajowych

if name in papaj: #jeżeli element jest w papaju
    print ("HABEMUS!")
else:
    print (a)


# JESTEM TERAZ NA https://www.tutorialspoint.com/python3/python_functions.htm
    # ZADANKO: Gra tekstowa P.O.P.E Stories (Papieska Opowieść P)
    # Funkcja defChoice(): będzie łapała wartości 1,2,3,4 zależne od wyboru,
    # jak brak wyboru 1,2,3,4 to komunikat "wprowadź poprawną wartość"
    # dodać też widok zakładki do strony, gdzie będzie można sobie zagrać
    # dodać dźwięki odpalane przy odpaleniu jakiejś akcji
    # dodać podkład ambientowy
