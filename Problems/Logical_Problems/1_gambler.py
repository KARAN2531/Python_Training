'''
1. Gambler
a. Desc -> Simulates a gambler who start with $stake and place fair $1 bets until
he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
times he/she wins and the number of bets he/she makes. Run the experiment N
times, averages the results, and prints them out.
b. I/P -> $Stake, $Goal and Number of times
c. Logic -> Play till the gambler is broke or has won
d. O/P -> Print Number of Wins and Percentage of Win and Loss.'''

from random import randint
class Gambler:
    @staticmethod
    def game():
        stake = int(input("Enter Starting amount: "))
        goal = int(input("Enter the goal amount: "))
        win=0
        loss=0

        while stake>0 and stake<goal:
            x = randint(0,1)
            print(f"X: {x}")
            if x==0:
                stake-=1
                loss+=1
            else:
                stake+=1
                win+=1
                
        print(f"Stake: {stake}")
        print (f"Rounds won: {win}\nRounds lost: {loss}")
        total = win+loss
        if stake==goal:
            winpercent = round((win/total)*100,2)
            print(f"Win Percentage: {winpercent}")
            return winpercent
        elif stake==0:
            losspercent = round((loss/total)*100,2)
            print(f"Loss Percentage: {losspercent}")
            return (100 - losspercent)
        

n = int(input("Enter number of times you want to run this test: "))
if n>0:
    totwin=0
    for _ in range(n):
        totwin+=Gambler.game()
        
    print(f"Average Win Percent across the {n} tries is: {totwin/n}")
    print(f"Average Loss Percent across the {n} tries is: {100-(totwin/n)}")




    