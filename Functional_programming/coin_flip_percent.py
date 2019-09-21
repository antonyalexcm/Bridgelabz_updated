# Flip Coin and print percentage of Heads and Tails

import random

while True:
 try:
  number = int(input("Enter Number: "))
  assert(number > 0), "Number must be bigger than 0"
  break
 except:
  print("This is a string")

q=0 

for i in range (number):
 d = random.uniform(0,1)
 #print(d)
 if(d<0.5):
  q += 1
tail = (q/number)*100

head = ((number-q)/number)*100

print("\nTails occured: {} %".format(tail))
print("\nHeads occured: {} %".format(head))