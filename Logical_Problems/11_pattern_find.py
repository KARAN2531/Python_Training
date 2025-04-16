'''
11.Given a text and a pattern, return the index of the first occurrence of pattern
in text and return -1 if pattern is not part of text.

Input: text = 'ABCABAABCABAC', pattern = 'ABAA'
Output: 3
Explanation: The pattern occurs only once in the text, starting from index 3.
Input: text = 'ABCABAABCABAC', pattern = 'CAB'
Output: 2
Explanation: The pattern occurs twice in the text, starting from index 2 and 8. The solution should return
the index of the first occurrence, i.e., 2.
'''
text = input("Enter your text: ")
pattern = input("Enter your pattern: ")

found = False

for i in range(len(text) - len(pattern) + 1):
    if text[i:i+len(pattern)] == pattern:
        print(f"Pattern found at index {i}")
        found = True
        break  # Stop after the first match

if not found:
    print(-1)
