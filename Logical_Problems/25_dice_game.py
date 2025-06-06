'''
25.John is playing a dice game. The rules are as follows.
Roll two dice.
Add the numbers on the dice together.
Add the total to your overall score.
Repeat this for three rounds.
But if you roll DOUBLES, your score is instantly wiped to 0 and your game ends immediately!
Create a function that takes in a list of tuples as input, and return John's score after his game has ended.
Examples
dice_game([(1, 2), (3, 4), (5, 6)]) ➞ 21

dice_game([(1, 1), (5, 6), (6, 4)]) ➞ 0

dice_game([(4, 5), (4, 5), (4, 5)]) ➞ 27

Notes
Ignore all other tuples in the list if a throw happens to be doubles and go straight to returning 0.
John only has two dice and will always give you outcomes for three rounds.
'''

def dice_game(rolls):
    total = 0
    for die1, die2 in rolls:
        if die1 == die2:
            return 0  
        total += die1 + die2
    return total

print(dice_game([(1, 2), (3, 4), (5, 6)])) 
print(dice_game([(1, 1), (5, 6), (6, 4)])) 

