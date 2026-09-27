print("=======================")
print("Welcome To Ride Builder")
print("=======================")

print("Step 1 - Pick your vehicle")
print(" 1 - bike")
print(" 2 - car")
print()
choice = int(input("enter the no. 1 or 2 : "))
print()
if choice==1:
    print("Step 2: Pick your bike type")
    print(" 1 - Scooty ")
    print(" 2 - mountain bike ")
    bike_type = int(input("Enter the no. 1 or 2"))
    print()
    if bike_type==1:
        print("You picked - Scooty")
        print("Top speed - 80km/hr")
        print("Best for - city road")
    else:
        print("You picked - mountain bike")
        print("Top speed - 40km/hr")
        print("Best for - hilly roads")

elif choice==2:
    print("Step 2 - pick your car type")
    print(" 1 - Sedan")
    print(" 2 - SUV")
    car_type = int(input("Enter 1 or 2:"))
    print()
    if car_type==1:
        print("You picked - Sedan")
        print("Seats - 5 passenger")
        print("Best for - Family Trips")
    else:
        print("You picked - SUV")
        print("Seats - 7 seats")
        print("Best for - off-road adventures")
else:
    print("Invalid choice")
    print("Write 1 for bike and 2 for car")
print()
print("==================================")
print("    your custom ride is ready   ")
print("           Enjoy the ride          ")
print("==================================")