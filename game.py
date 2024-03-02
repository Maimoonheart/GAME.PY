# myset = {'apple','orange','cherry','pineapple'}

# print(myset)
# balance = 500
# stake = float(input('stake: '))

# while balance > 0 and balance > stake:

#     guess = input ('Guess the chosen fruit:  ').strip().lower()
#     chosen_fruit = myset.pop()
#     myset.add(chosen_fruit)

#     if guess == chosen_fruit:
#      balance += 30 * stake
#      print('You guessed right.\n Your current balance is', balance)
#     else:
#        balance -= stake
#        print('Wrong\n Your current balance is ',balance) 


user = input('''        GUESS GAME
   NB: This game is only for user more than 18 years of age
     Kindly input your age:  ''')

if user <= '18':
   print ('You are not eligible to play this game.')
   exit()
else:
    myset = {'apple','orange','cherry','pineapple','mango'}
    print(  myset,''' 
      You are to guess the chosen fruit in this game.If you are wrong,twice the amount you staked will be deducted from your balance and vice versa.Now,let us proceed.You have an initial balance of #1000.''')

balance = 1000
stake = float(input('stake: '))
while balance > 0 and balance > stake:
     guess = input ('Guess the chosen fruit:  ').strip().lower()
     chosen_fruit = myset.pop()
     myset.add(chosen_fruit)
     if guess not in myset:
         print('Your guess is not among the available fruits')
         balance = balance
     elif guess == chosen_fruit:
        balance += 2 * stake
        print('You guessed right.\n Your current balance is', balance)
     else:
         balance -= 2 * stake
         print('Wrong\n Your current balance is ',balance)


