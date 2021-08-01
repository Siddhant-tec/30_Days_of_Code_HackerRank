my_list = []
while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    try:
        my_list.append(int(number))
    except:
        print("Invalid Input")

print(my_list)
print("Minimum: ", min(my_list),"Maximum: ", max(my_list))

