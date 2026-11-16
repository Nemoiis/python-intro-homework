while True:
    try:
        num = int(input("Enter a positive number: "))
        if num <= 0:
            print("Please input a positive number.")

        else:
            print(f"Got it: {num}")
            break

    except ValueError:
        print("Thats not even a number. Type a Positive number")




