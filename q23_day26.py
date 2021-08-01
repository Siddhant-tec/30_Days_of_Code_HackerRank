return_date = input().split()
return_day = int(return_date[0])
return_month = int(return_date[1])
return_year = int(return_date[2])

due_date = input().split()
due_day = int(due_date[0])
due_month = int(due_date[1])
due_year = int(due_date[2])


def compute_fine():
    fine = 0
    if return_year > due_year:
        fine = 10000
    elif return_year == due_year:
        if return_month == due_month and return_date > due_date:
            fine = 15 * (return_day - due_day)
        elif return_month > due_month:
            fine = 500 * (return_month - due_month)
    else:
        fine = 0
    print(fine)


compute_fine()
