# 5 Replace all spaces with underscores

import re

text = "Python is fun"
modified = re.sub(r'\s+', '_', text)
print(modified)  # Python_is_fun