numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def find_min(numbers):
    min = numbers[0]
    for num in numbers:
        if num < min:
             min = num
    return min

def find_max(numbers):
    max = numbers[0]
    for num in numbers:
        if num > max:
             max = num
    return max    

def search(numbers, target):
    found = False
    for i in range(len(numbers)):
        if numbers[i] == target:
            return f"Number at {i}"

    if found == False:
        return -1

def bubbleSort(numbers):
    newNumbers = []
    for num in numbers:
        newNumbers.append(num)

    for i in range(len(newNumbers) - 1):
        for j in range (len(newNumbers) - i - 1):
            if newNumbers[j] > newNumbers[j+1]:
                newNumbers[j], newNumbers[j+1] = newNumbers[j+1], newNumbers[j]

    return newNumbers
    
def show_menu():
    print('''
    === Number Cruncher ===
    1. Find minimum
    2. Find maximum
    3. Search for a number
    4. Sort the list
    5. Quit
    ''')

    choice = input("Enter a choice: ")
    return choice
        

def main():
    numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

    while True:
        choice = show_menu()

        if choice == "1":
            print(f"Min is: {find_min(numbers)}")

        elif choice == "2":
            print(f"Max is: {find_max(numbers)}")

        elif choice == "3":
            target = int(input("Enter target number: "))
            print(search(numbers, target))

        elif choice == "4":
            print(bubbleSort(numbers))

        elif choice == "5":
            break


main()