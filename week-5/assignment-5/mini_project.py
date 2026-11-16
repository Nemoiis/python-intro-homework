numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print('''
=== Number Cruncher ===
1. Find minimum
2. Find maximum
3. Search for a number
4. Sort the list
5. Quit
''')

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        min = numbers[0]
        for num in numbers:
            if num < min:
                min = num
        print(f"{min}")

    elif choice == "2":
        max = numbers[0]
        for num in numbers:
            if num > max:
                max = num
        print(f"{max}")

    elif choice == "3":
        numToLook = int(input("Enter A Number: "))
        found = False
        for num in range(len(numbers)):
            if numbers[num] == numToLook:
                print(f"Number found at index {num}")
                found = True
                break

        if not found:
            print("Number not found")

    elif choice == "4":
        print(numbers)

        for i in range(len(numbers) - 1):
            for j in range (len(numbers) - i - 1):
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

        print(numbers)

    elif choice == "5":
        break
        
        


