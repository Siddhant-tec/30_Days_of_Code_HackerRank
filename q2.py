def computegrade(score):

    if score >= 0.9:
        print("A")
    elif 0.8 <= score:
        print("B")
    elif 0.7 <= score:
        print("C")
    elif 0.6 <= score:
        print("D")
    elif 0.5 <= score:
        print("F")
    else:
        print("Out of Range")


score = float(input("Enter the score: "))
computegrade(score)
