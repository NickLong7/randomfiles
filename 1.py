command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car has stopped...")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to exit the proggram
        """)
    elif command == "quit":
        break
    else:
        print("Sorry type Help")
    
