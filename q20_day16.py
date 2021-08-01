def string_check():
    number = str(input())
    try:
        print(int(number))
        quit()
    except ValueError:
        print("Bad String")


string_check()
