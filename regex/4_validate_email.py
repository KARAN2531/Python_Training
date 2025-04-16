# 4. Validate an email address

import re 

emails = ["user@example.com", "invalid-email@.com"]
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

for email in emails:
    if re.match(pattern, email):
        print(email, "is valid")
    else:
        print(email, "is invalid")