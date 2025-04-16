'''
24. convert number to word
'''

ones = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}
tens = {
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
}

def num2word(num):
    if num == 0:
        return "zero"

    word = []

    if num >= 10000000:  
        word.append(num2word(num // 10000000) + " crore")
        num %= 10000000

    if num >= 100000:  
        word.append(num2word(num // 100000) + " lakh")
        num %= 100000

    if num >= 1000:  
        word.append(num2word(num // 1000) + " thousand")
        num %= 1000

    if num >= 100:  
        word.append(num2word(num // 100) + " hundred")
        num %= 100

    if num >= 20:  
        word.append(tens[(num // 10) * 10])
        num %= 10

    if num > 0: 
        word.append(ones[num])

    return " ".join(word)

num = int(input("Enter a number: "))
print(num2word(num))
