# Simulates a gambler who start with stake and place fair stake and place fair bets until he/she goes broke (i.e. has no money) or reach $ goal
import random
inpt = input("Enter the Stake, Goal and the number of Bets : ")

list_0 = [int(i) for i in inpt.split(',')]

win = 0

tot_bets = 0 

for i in range (list_0[2]):
    d = random.uniform(0,1)
    #print(d)

    if(list_0[0] > 0 and list_0[0] <= list_0[1] and tot_bets < list_0[2]):
        #print("used: {}".format(d))
        tot_bets += 1     

        if(d<0.5):
            list_0[0] -= 1

        else:
            list_0[0] += 1
            win += 1
    
print("\nThe total number of wins are: {}".format(win))

print("\nThe percentage of win is: {} %".format((win/tot_bets)*100))

print("\nThe percentage of loss is: {} %".format(((tot_bets-win)/tot_bets)*100))