# 6. Extract dates in format DD-MM-YYYY

import re

text = "My birthday is 08-04-2025."
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
print(dates)  # ['08-04-2025']