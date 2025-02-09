degrees = int(input("enter a temperature"))

if degrees  > 30:
    print("your temperature is fire")
elif degrees > 20 and degrees <= 30:
    print("worm")
elif degrees <20:
    print("cold")