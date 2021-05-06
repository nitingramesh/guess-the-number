import random
print('hello,wats your name')
name=input()
secretnumber = random.randint(1,20)
print('well'+name+'i am thinking of a number btw')
for guesstaken in range(1,7):
    print('take a guess')
    guess=int(input())
    if guess<secretnumber:
        print('your guess is too low')
    elif guess>secretnumber:
        print('your guess is too high')
    else:
        break
if guess==secretnumber:
    print('goodjob'+str(guesstaken))
else:
    print('nope the number i was thinking was' +str(guesstaken)+'guesse')
