# Create arrays
my_houses = [18.0, 20.0, 10.75, 9.50]
your_houses = [14.0, 24.0, 14.25, 9.0]

for my_house in my_houses:
    for your_house in your_houses:
        if(my_house >= your_house):
            print(str(my_house) +" มากกว่า "+ str(your_house))
        else:
            print(str(my_house) +" น้อยกว่า "+ str(your_house))

    