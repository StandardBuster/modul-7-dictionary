
import os
os.system("cls")

dictionary = {}

# colours = ["blue", "green", "yellow", "Rust"]


cars = [
    {
    "make": "Dennys",
    "model": "Mingieminge",
    "year": 2000,
    # "colours": ["blue", "green", "yellow", "Rust"]
    },
    
    {
    "make": "Borsche",
    "model": "Clorsche 1119",
    "year": 1999,
    # "colours": ["red", "magenta"]
    }
]


while True:
    for car in cars:
        make = car['make']
        model = car['model']
        year = car['year']
        colours = input("What colour do you want? ")


        car.update(
        {
            "make": make,
            "model": model,
            "year": year,
            "colour": colours
        }
        )
        del car['year']
        
        print(car)

        change = input("Do you want to change?(Y/N) ").upper()
        if change == 'N':
            exit()
        

        # print(car)
            # print(f"Du skapar {make} som en riktig {model} i år {year}")

