email_dictionary = {}
n = int(input())
for i in range(0, n):
    username, email_id = input("").split()
    email_dictionary[email_id] = username


#print(email_dictionary)


email_list = sorted(email_dictionary.keys())
sorted_list = []
for mail in email_list:
    if mail[len(mail)-10:] == '@gmail.com':
        sorted_list.append(mail)
#print(sorted_list)

name_list = []
for key in email_list:
    if key in sorted_list:
        name_list.append(email_dictionary[key])

#print(sorted(name_list))
print(*sorted(name_list), sep='\n')
