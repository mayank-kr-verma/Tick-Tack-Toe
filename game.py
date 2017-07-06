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
		if playData[choice] == '.':
			playData[choice] = player
			break
		else :
			print 'Invalid choice. Try again.'

p1, p2 = firstTimePlay()
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
playfield()