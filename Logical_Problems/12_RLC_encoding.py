'''
12. Run–length encoding (RLE) is a simple form of lossless data compression that
runs on sequences with the same value occurring many consecutive times. It
encodes the sequence to store only a single value and its count.
Input:
'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWW
WWWBWWWWWWWWWWWWWW'
Output: '12W1B12W3B24W1B14W'
Explanation: String can be interpreted as a sequence of twelve W’s, one B, twelve W’s, three B’s, and so on..
'''

def run_length_encoding(s):
    if not s:
        return ""

    encoded_string = ""
    count = 1  

    for i in range(1, len(s)):  
        if s[i] == s[i - 1]:  
            count += 1  
        else:  
            encoded_string += str(count) + s[i - 1]  
            count = 1  

    encoded_string += str(count) + s[-1]  
    return encoded_string

rlc_code = input("Enter your string: ")
encoded_output = run_length_encoding(rlc_code)
print("Encoded Output:", encoded_output)
