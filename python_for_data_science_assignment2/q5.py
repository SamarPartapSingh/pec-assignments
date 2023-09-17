def extract_email_domain(email_string):
    parts = email_string.split('@')
    
    if len(parts) == 2:
        return parts[1]
    else:
        return None

email_string = "user@domain.com python"
domain = extract_email_domain(email_string)
if domain:
    print("Email Domain:", domain)
else:
    print("No email address found in the input string.")
