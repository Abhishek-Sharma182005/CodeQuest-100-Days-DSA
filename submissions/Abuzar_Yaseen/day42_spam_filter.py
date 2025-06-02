emails_sub = input("Enter email subject : ")
emails = [email.strip().strip('"')
for email in emails_sub.split(',')]

spam_input = input("Enter spam keywords: ")
spam_keywords = [word.strip().lower() for word in spam_input.split(',')]

clean_email = []

for email in emails:
    email_lower = email.lower()

    is_spam = any(spam_word in email_lower for spam_word in spam_keywords)
    
    if not is_spam:
        clean_email.append(email)

print("\n Filtered Emails:  ")
for clean in clean_email:
    print("-"+clean)  