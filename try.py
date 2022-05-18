global bike
global dt
global dte
global user
global a
global k
global total_charges
class showroom:
    def __init__(self, bikesList, name):
        self.bikesList=bikesList
        # self.bikesList = bikesList
        self.name = name
        self.lendDict = {}

    def displayBikes(self):
        print(f"We have following bikes in our showroom: {self.name}")
        
        for bike in self.bikesList:
            print(bike)

    def lendBike(self, user, bike):
        if bike not in self.lendDict.keys():

            self.lendDict.update({bike:user})
            print("Lender-Bike database has been updated. You can take the bike now")
        else:
            print(f"Bike is already being used by {self.lendDict[bike]}")

    def addBike(self, bike):
        self.bikesList.append(bike)
        print("Bike has been added to the bike list")

    def returnBike(self, bike):
        self.lendDict.pop(bike)

    def quantity(self,q):
        a=100
        if a<q:
            print("please enter valid choice")
        else:
            if k<=0:
                print("Enter a positive number.")
            else: 
                print(f"rented bikes; {k}\n")
                ab=int(a-k)
                print(f"Available Bikes: {ab}\n")

class customer(showroom):
    def __init__(self,Name):
        self.Name=Name
        #self.bike=bike
        #self.dte=dte
        #self.dt=dt

     
    

if __name__ == '__main__':
    krishna = showroom(['Suzuki', 'Bullet', 'Yamaha', 'TVS', 'Hero'], "Haribol")
    



    while(True):
        print(f"Welcome to the {krishna.name} showroom. Enter your choice to continue")
        print("\nTotal bikes are 100\n")
        print("1. Display Bikes")
        print("2. Lend a Bike")
        print("3. Add a Bike")
        print("4. Return a Bike")
        print("5. Bike Details")
        user_choice = input()
        if user_choice not in ['1','2','3','4','5']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)


        if user_choice == 1:
            krishna.displayBikes()



        elif user_choice == 2:
            
            bike =input('Enter the name of the bike you want to lend:')
            if bike=="Suzuki":
                print("\t\tRental Charges\t\n\n        Daily\t\tweekly\t\tMonthly\n\n\t₹50\t\t₹300\t\t₹1200\n")

            elif bike=="Bullet":
                 print("\t\tRental Charges (Per Bike)\t\n\n       Daily\t\tweekly\t\tMonthly\n\n\t₹50\t\t₹300\t\t₹1200\n")
            elif bike=="Yamaha":
                 print("\t\tRental Charges (Per Bike)\t\n\n       Daily\t\tweekly\t\tMonthly\n\n\t₹50\t\t₹300\t\t₹1200\n")
            elif bike=="TVS":
                 print("\t\tRental Charges (Per Bike)\t\n\n       Daily\t\tweekly\t\tMonthly\n\n\t₹50\t\t₹300\t\t₹1200\n")
            elif bike=="Hero":
                 print("\t\tRental Charges (Per Bike)\t\n\n       Daily\t\tweekly\t\tMonthly\n\n\t₹50\t\t₹300\t\t₹1200\n")
            k=int(input("Enter the quantity\t\n"))
            krishna.quantity(k)
            print("1. Daily Basis")
            print("2. Weekly Basis")
            print("3. Monthly Basis")
            select=input("On what basis you want to rent?\n")
            if select=='Daily Basis':
                print("Charge=₹50")
                total_charges=int(k*50)
                print("total_charges=₹", total_charges)
            elif select=='Weekly Basis':
                print("Charges=₹300")
                total_charges=int(k*300)
                print("total_charges=₹", total_charges)
            elif select=='Monthly Basis':
                print("Charges= ₹1200")
                total_charges=(k*1200)
                print("total_charges=₹", total_charges)
            else:
                print("Please enter a valid choice.")

            user = input("Enter your name:\t")
            dte=input("Enter date of renting(DD/MM/YYYY)\n\t\tFrom:")
            dt=input("\t\tTo  :")
            # local_time=time.asctime(seconds)
            # time.asctime(time.localtime(time.time()))
            # print("local current time:",localtime)

            krishna.lendBike(user, bike)

        elif user_choice == 3:
            bike = input("Enter the name of the bike you want to add:")
            krishna.addBike(bike)


        elif user_choice == 4:
            bike = input("Enter the name of the bike you want to return:")
            krishna.returnBike(bike)
            
        
        elif user_choice==5:
            bike1=customer(user)
            print('\nUser Name:',end="")
            print(bike1.Name)

            #bike1=customer(bike)
            print('Bike :\t  ',end="")
            print(bike)
            #print(bike1.bike)

            #bike1=customer(dte)
            print('\nDuration:')
            print('\tFrom:\t',end="")
            print(dte)
            
            print('\tTo:\t',end="")
            print(dt)
            #bike1=customer(dt)

            print(f"Number of Bikes lended:{k}\n")
            print(f"Total Charges:{total_charges}")

           
           # print(bike1.dt)
            
           # print("")
            
            #print(f"Rental Details\nName:{user}\nBike Rented: {bike}\nDuration: {dte} to {dt}")
            
        else:
            print("Not a valid option")


        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue