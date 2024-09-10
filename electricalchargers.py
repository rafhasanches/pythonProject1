hours = int(input("Enter hours used: "))
rate1 = 0.07633
rate2 = 0.09259

if hours <= 1000 :
    value = hours * rate1
    print("Amounted owed is $", value)
elif hours > 1000 :
    value = 1000 * rate1 + (hours - 1000) * rate2
    print("Amounted owed is $", value)