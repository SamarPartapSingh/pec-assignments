# Input email IDs into a tuple
email_ids = tuple(input("Enter email IDs separated by space: ").split())

usernames = ()
domains = ()

for email in email_ids:
    parts = email.split('@')
    if len(parts) == 2:
        usernames += (parts[0],)
        domains += (parts[1],)

# Display all three tuples
print("Email IDs:", email_ids)
print("Usernames:", usernames)
print("Domains:", domains)
