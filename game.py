print ("***********************************")
print ("WELCOME TO ROCK, PAPER, SCISSORS")
print ("***********************************")

ans = 'yes'
x = input('whats your name?:')
b = input('and your name?:')
print('\nHello, ' + x)
print('Hello, ' + b)

while (ans != 'no'):
	player = x
	
	stuff_in_string = "\n{}, do you want to choose rock, paper or scissors?".format(player)
	print(stuff_in_string)
	answer1 = input()
		
	if (answer1 != 'rock') and (answer1 != 'paper') and (answer1 != 'scissors'):
		print ("You have not entered rock, paper or scissors\n Try again!")
		answer1 = input()	
		
	player = b
	
	stuff_in_string = "{}, do you want to choose rock, paper or scissors?".format(player)
	print(stuff_in_string)
	answer2 = input()

	if (answer2 != 'rock') and (answer2 != 'paper') and (answer2 != 'scissors'):
		print ("You have not entered rock, paper or scissors\n Try again!")
		answer2 = input()
		
	if(answer1 == answer2):
		print ("It's a tie!")
		
	if (answer1 == 'rock') and (answer2 == 'paper') or (answer2 == 'rock') and (answer1 == 'paper'):
		print ("paper wins!")

	if (answer1 == 'scissors') and (answer2 == 'paper') or (answer2 == 'scissors') and (answer1 == 'paper'):
		print ("Scissors win!")
		
	if (answer1 == 'scissors') and (answer2 == 'rock') or (answer2 == 'scissors') and (answer1 == 'rock'):
		print ("Rock win!")
		
	print('Do you want to play again?') 
	ans = input()
	if(ans == 'no'):
			print('Bye bye')
			exit()