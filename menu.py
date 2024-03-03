menu =[
     ["Chicken Burger","Burger με κοτόπουλο, bacon, τυρί edam, τομάτα, μαρούλι με μαγιονέζα",4.20],
     ["Ham Burger", "Burger με μπιφτέκι, τυρί, κέτσαπ, μουστάρδα",2.85],
     ["Green Burger","Burger με ζουμερό μπιφτέκι, τυρί, φρέσκια τομάτα, μαρούλι,κρεμμύδι, πίκλες, κέτσαπ και dressing sauce" ,4.20],
     ["Club Sandwich","Club sandwich με 3 πλούσιες στρώσεις Philadelphia σεφρυγανισμένο ψωμί του τοστ με ζουμερό κοτόπουλο φιλέρο, bacon, τομάτα,μαρούλι και τηγανητές πατάτες" ,10.90],
     ["Σαλάτα ceasars","Δροσερή πράσινη σαλάτα με ζουμερό κοτόπουλου σε βάση μαρουλιού, με καλαμπόκι, κρουτόν, τριμμένο τυρί και vinaigrette ελαιόλαδου" ,6.90],
     ["Κινόα με Λαχανικά", "Δροσερή σαλάτα με κινόα, κόκκινη πιπεριά, τοματίνια,αγγούρι, δυόσμο, φρέσκο μαϊντανό και sauce λαδολέμονο",6.30]
]


#orizw ena leksiko gia na apothikeusw mesa tis paraggelies kai tis times tous
orders = {}


#mia sunartisi gia na ypologisoume ti sinoliki timi mia paragelias
def calculate_price(order):
    total = 0
    for item in order:
        total += item[2] #i timis tou kathe stixioy einai to 3o stixeio stis listas
    return total


#broxos epanalipsis
while True:
   
    #ektipwnei ta diathesima proionta
    print("Διαθέσιμα Προιόντα:")
    for i, item in enumerate(menu):
        print(f"{i+1}. {item[0]} - {item[1]} (${item[2]:.2f})")
    print()

   
    #zitaei ton arithmo trapezioy kai tin paraggelia
    table_num = int(input("Πληκτρολογίστε το αριθμό τραπεζιού που θα κάτσετε (1-10): "))
    order = []
    while True:
        item_num = int(input("Πληκτρολογίστε το αριθμό φαγητού (1-6) ή 0 για το τερματισμό της παραγγελείας: "))
        if item_num == 0: #an o xristis eisagei 0 teleiwnei i paraggelia
            break
        item = menu[item_num - 1] # pairnei to proion pou antistoixi ston arithmo pou eisagame
        order.append(item)  # prostheti to proion stin paraggelia
        print(f"{item[0]} Προσθέστε παραγγελεία.")
    print()

  
    #ypologizei tin sinoliki timi kai to trapezi pou tha katsei o foititis
    price = calculate_price(order)
    print(f"Αριθμός {table_num} τραπεζιού:")
    for item in order:
        print(f"- {item[0]} (${item[2]:.2f})")
    print(f"Σύνολο: ${price:.2f}")
    print()

    
    #zitaei tropo pliromis(karta/metrita)
    while True:
        payment_method = input("Μέθοδος πληρωμής (καρτα/μετρητα): ")
        if payment_method.lower() == "καρτα": #metatrepei olous tous kefalaious xaraktires se pezous
            print("Η πληρωμή με κάρτα πραγματοποιείται.")
            break
        elif payment_method.lower() == "μετρητα":
            while True:
                cash = float(input("Βάλτε το ποσό: "))
                if cash < price:
                    print("Χρειάζεστε περισσότερα μετρητά.")
                else:
                    break
            if cash > price:
                change = cash - price
                print(f"Επεξεργασία πληρωμής με μετρητά. Ρέστα: ${change:.2f}")
            else:
                print("Επεξεργασία πληρωμής με μετρητά. Το ακριβές ποσό που ελήφθη.")
            break
        else:
            print("Μη έγκυρος τρόπος πληρωμής.")
    print()

    #prostheti ti paraggelia sto dictionary(orders)
    orders[table_num] = {"order": order, "price": price, "payment_method": payment_method}

    #Erwtisi gia parapanw paraggelies
    more_orders = input("Υπάρχουν περισσότερες παραγγελίες; (ν/ο) ")
    if more_orders.lower() == "ο":
        break

#ektipwnei oles tis paraggelies kai tis times tous
print("Όλες οι παραγγελίες:")
for table_num, data in orders.items():
    print(f"Table {table_num}:")
    for item in data["order"]:
        print(f"- {item[0]} (${item[2]:.2f})")
    print(f"Σύνολο: ${data['price']:.2f}")
    print(f"Μέθοδος πληρωμής:{data['payment_method']}")
    print()