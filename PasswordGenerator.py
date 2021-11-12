import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNUVWXYZ"
number = "0123456789"
symbol = "[]{}#():;_-"

all = lower+upper+number+symbol
len = 5
password = ''.join(random.sample(all,len))
print("Your Password Is ", password)