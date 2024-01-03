


def obliczanie_skanow():
    width = float(input("""3.POWRÓT
Podaj SZEROKOŚĆ skanu: """))
    height = float(input("Podaj DŁUGOŚĆ skanu: "))
    skan_choice = int(input("""1.KOLOR czy 2.CZARNO-BIAŁE?: 
"""))

    cena_skanu_kolorwego = width * height * 30 /1000000
    cena_skanu_czarnego = width * height * 15 /1000000
    
    # skan_choice = 0
    # while skan_choice != 1 or skan_choice != 2 or skan_choice != 3:

    if skan_choice == 1:
        print("Rysunek kosztuje: " + str(cena_skanu_kolorwego) + " zł")

    elif skan_choice == 2:
        print("Rysunek kosztuje: " + str(cena_skanu_czarnego) + " zł")
    
    elif skan_choice == 3:
        start()
    
    else:
        print("To nie jest właściwa wartość")

    start()


 

# def oblaczenie_druku():
    


def start():
    
    print("""Witaj co chcesz obliczyć? 
    """)
    
    choice = 0
    while choice != 1 or choice != 2 or choice !=3:
        
        choice = int(input("""Wybierz 1.SKAN lub 2.WYDRUK 3.Wyjście: 
"""))
    
        if choice == 1:
            obliczanie_skanow()
        
        # elif choice == 2:
            
        elif choice == 3:
            break
        
        else: 
            print("To nie jest właściwa wartość")

start()