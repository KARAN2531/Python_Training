# 3. Extract all words from a sentence

import re
text = "Python is awesome!"
words = re.findall(r'\w+', text)
print(words)  # ['Python', 'is', 'awesome']