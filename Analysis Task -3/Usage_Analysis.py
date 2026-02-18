emails = [
    "ravi@gmail.com",
    "anita@yahoo.com",
    "kiran@gmail.com",
    "suresh@gmail.com",
    "meena@yahoo.com"
]

domain_count = {}

for email in emails:
    domain = email.split("@")[1]
    
    if domain in domain_count:
        domain_count[domain] += 1
    else:
        domain_count[domain] = 1

total_users = len(emails)

for domain, count in domain_count.items():
    percentage = (count / total_users) * 100
    print(f"{domain}: {percentage:.0f}%")
