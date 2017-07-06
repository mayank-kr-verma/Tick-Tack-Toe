#################################################
#      Two player tick tack toe game			#				
#      Author - MakX							#
#      Date - 5 july 17							#
#################################################

playData = {'topL' : '.', 'topM' : '.', 'topR' : '.',
			'midL' : '.', 'midM': '.', 'midR': '.',
			'lowL' : '.', 'lowM': '.', 'lowR': '.'}
moveList = ['topL' , 'topM' , 'topR' ,
			'midL' , 'midM', 'midR',
			'lowL' , 'lowM', 'lowR']

def firstTimePlay():
	print 'Hello and welcome to a two player game of tick tack toe'
	print 'Enter the name of first player : '
	player1 = raw_input('> ')
	print 'Enter the name of second player : '
	player2 = raw_input('> ')
	return player1, player2

def playField():
	print playData['topL']+'|'+playData['topM']+'|'+playData['topR']
	print '-+-+-'
	print playData['midL']+'|'+playData['midM']+'|'+playData['midR']
	print '-+-+-'
	print playData['lowL']+'|'+playData['lowM']+'|'+playData['lowR']

def makeMove():
	print 'Choose your move:'
	for i in moveList:
		if playData[i] == '.':
			if i[-1] == 'R':
				print i
			else:
				print i,
		else:
			if i[-1] == 'R':
				print '    '
			else:
				print '    ',
	while True:
		choice= raw_input('> ')
		option = playData.get(choice,0)

		if option == '.':
			playData[choice] = player
			break
		else :
			print 'Invalid choice. Try again.'

def checkWinner():
	if playData['topL']==playData['topM'] and playData['topL']==playData['topR'] and playData['topL']==player:
		return player
	if playData['midL']==playData['midM'] and playData['midL']==playData['midR'] and playData['midL']==player:
		return player
	if playData['lowL']==playData['lowM'] and playData['lowL']==playData['lowR'] and playData['lowL']==player:
		return player
	if playData['topL']==playData['midL'] and playData['topL']==playData['lowL'] and playData['topL']==player:
		return player 
	if playData['topM']==playData['midM'] and playData['topM']==playData['lowM'] and playData['topM']==player:
		return player 
	if playData['topR']==playData['midR'] and playData['topR']==playData['lowR'] and playData['topR']==player:
		return player 
	if playData['topL']==playData['midM'] and playData['topL']==playData['lowR'] and playData['topL']==player:
		return player
	if playData['topR']==playData['midM'] and playData['topR']==playData['lowL'] and playData['topR']==player:
		return player	
	return	None

p1, p2 = firstTimePlay()
playerData = {'X' : p1, 'Y' : p2}
player = 'O'
for j in range(9):
	playField()
	if player == 'O':
		player = 'X'
		print p1+'\'s turn'
	else:
		player = 'O'
		print p2+'\'s turn'
	makeMove()
	winner = checkWinner()
	if winner != None:
		playField()
		print 'Congrats player %s, you won' %playerData[player]
		exit()
playField()
print 'Looks like a tie'