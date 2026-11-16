nameList = ["Nemo", "Dory", "Cadence", "Malaya", "Petey", "Marcus"]
name = input("Enter a name: ")

found = False
for i in range(len(nameList)):
    if nameList[i] == name:
        print(f"Name ({name}) was found at index {i}")
        found = True
        break

if found == False:
    print("Name was not found.")
      
