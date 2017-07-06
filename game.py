#################################################
#      Single player tick tack toe game			#				
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
	print 'Enter your name : '
	playerName = raw_input('> ')
	while True:
		print 'Choose between X and O (X goes first) : '
		playerSign = raw_input('> ')
		if playerSign!='X'and playerSign!='O':
			print 'Error'
		else:
			break
	return playerName, playerSign

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

def makeMoveSystem():
	pass

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

p, ps = firstTimePlay()
if ps == 'X':
	p1 = p
	p2 = 'system'
else:
	p2 = p
	p1 = 'system'
playerData = {'X' : p1, 'O' : p2}
player = 'O'
for j in range(9):
	playField()
	if player == 'O':
		player = 'X'
		print p1+'\'s turn'
		if p1 == p:
			makeMove()
		elif p1 == 'system':
			makeMoveSystem()
	else:
		player = 'O'
		print p2+'\'s turn'
		if p2 == p:
			makeMove()
		elif p2 == 'system':
			makeMoveSystem()
	
	winner = checkWinner()
	if playerData[winner] == p:
		playField()
		print 'Congrats %s, you won' %p
		exit()
	elif playerData[winner] == 'system'
		playField()
		print 'Boo yaa! %s' %p
		exit()
playField()
print 'Looks like a tie'