mylist = list()
while True:
    inp = input("Enter the number")
    if inp == "done": break
    values = float(inp)
    mylist.append(values)   
print("Maximum: ",max(mylist),"Minimum: ",min(mylist))
