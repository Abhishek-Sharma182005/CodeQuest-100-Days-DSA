emails=input("Enter email subjects (comma-separated): ")
keywords=input("Enter spam keywords (comma-separated): ")

email_list = emails.lower().split(",")
keyword_list = keywords.lower().split(",")

filteredEmails=[]

for email in email_list:
    is_spam = False
    for keyword in keyword_list:
        if keyword in email:
            is_spam = True
            break
    if not is_spam:
        filteredEmails.append(email)

print("\nFiltered Emails:")
for email in filteredEmails:
    print(f"- {email}")