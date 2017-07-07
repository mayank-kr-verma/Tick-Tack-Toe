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

def makeMoveSystem(ps,ss):
	#win game
	if playData['topL']==playData['topM'] and playData['topL']==ss and playData['topR']=='.':
		playData['topR'] = ss 
	elif playData['topL']==playData['topR'] and playData['topL']==ss and playData['topM']=='.':
		playData['topM'] = ss
	elif playData['topR']==playData['topM'] and playData['topR']==ss and playData['topL']=='.':
		playData['topL'] = ss

	elif playData['midL']==playData['midM'] and playData['midL']==ss and playData['midR']=='.':
		playData['midR'] = ss 
	elif playData['midL']==playData['midR'] and playData['midL']==ss and playData['midM']=='.':
		playData['midM'] = ss
	elif playData['midR']==playData['midM'] and playData['midR']==ss and playData['midL']=='.':
		playData['midL'] = ss

	elif playData['lowL']==playData['lowM'] and playData['lowL']==ss and playData['lowR']=='.':
		playData['lowR'] = ss 
	elif playData['lowL']==playData['lowR'] and playData['lowL']==ss and playData['lowM']=='.':
		playData['lowM'] = ss
	elif playData['lowR']==playData['lowM'] and playData['lowR']==ss and playData['lowL']=='.':
		playData['lowL'] = ss
	

	elif playData['topL']==playData['midL'] and playData['topL']==ss and playData['lowL']=='.':
		playData['lowL'] = ss
	elif playData['topL']==playData['lowL'] and playData['topL']==ss and playData['midL']=='.':
		playData['midL'] = ss
	elif playData['lowL']==playData['midL'] and playData['lowL']==ss and playData['topL']=='.':
		playData['lowL'] = ss

	elif playData['topM']==playData['midM'] and playData['topM']==ss and playData['lowM']=='.':
		playData['lowM'] = ss
	elif playData['topM']==playData['lowM'] and playData['topM']==ss and playData['midM']=='.':
		playData['midM'] = ss
	elif playData['lowM']==playData['midM'] and playData['lowM']==ss and playData['topM']=='.':
		playData['lowM'] = ss

	elif playData['topR']==playData['midR'] and playData['topR']==ss and playData['lowR']=='.':
		playData['lowR'] = ss
	elif playData['topR']==playData['lowR'] and playData['topR']==ss and playData['midR']=='.':
		playData['midR'] = ss
	elif playData['lowR']==playData['midR'] and playData['lowR']==ss and playData['topR']=='.':
		playData['lowR'] = ss
	

	elif playData['topL']==playData['midM'] and playData['topL']==ss and playData['lowR']=='.':
		playData['lowR'] = ss
	elif playData['topL']==playData['lowR'] and playData['topL']==ss and playData['midM']=='.':
		playData['midM'] = ss
	elif playData['lowR']==playData['midM'] and playData['lowR']==ss and playData['topL']=='.':
		playData['topL'] = ss

	elif playData['topR']==playData['midM'] and playData['topR']==ss and playData['lowL']=='.':
		playData['lowL'] = ss
	elif playData['topR']==playData['lowL'] and playData['topR']==ss and playData['midM']=='.':
		playData['midM'] = ss
	elif playData['lowL']==playData['midM'] and playData['lowL']==ss and playData['topR']=='.':
		playData['topR'] = ss 

	#opp stop

	elif playData['topL']==playData['topM'] and playData['topL']==ps and playData['topR']=='.':
		playData['topR'] = ss 
	elif playData['topL']==playData['topR'] and playData['topL']==ps and playData['topM']=='.':
		playData['topM'] = ss
	elif playData['topR']==playData['topM'] and playData['topR']==ps and playData['topL']=='.':
		playData['topL'] = ss

	elif playData['midL']==playData['midM'] and playData['midL']==ps and playData['midR']=='.':
		playData['midR'] = ss 
	elif playData['midL']==playData['midR'] and playData['midL']==ps and playData['midM']=='.':
		playData['midM'] = ss
	elif playData['midR']==playData['midM'] and playData['midR']==ps and playData['midL']=='.':
		playData['midL'] = ss

	elif playData['lowL']==playData['lowM'] and playData['lowL']==ps and playData['lowR']=='.':
		playData['lowR'] = ss 
	elif playData['lowL']==playData['lowR'] and playData['lowL']==ps and playData['lowM']=='.':
		playData['lowM'] = ss
	elif playData['lowR']==playData['lowM'] and playData['lowR']==ps and playData['lowL']=='.':
		playData['lowL'] = ss
	

	elif playData['topL']==playData['midL'] and playData['topL']==ps and playData['lowL']=='.':
		playData['lowL'] = ss
	elif playData['topL']==playData['lowL'] and playData['topL']==ps and playData['midL']=='.':
		playData['midL'] = ss
	elif playData['lowL']==playData['midL'] and playData['lowL']==ps and playData['topL']=='.':
		playData['lowL'] = ss

	elif playData['topM']==playData['midM'] and playData['topM']==ps and playData['lowM']=='.':
		playData['lowM'] = ss
	elif playData['topM']==playData['lowM'] and playData['topM']==ps and playData['midM']=='.':
		playData['midM'] = ss
	elif playData['lowM']==playData['midM'] and playData['lowM']==ps and playData['topM']=='.':
		playData['lowM'] = ss

	elif playData['topR']==playData['midR'] and playData['topR']==ps and playData['lowR']=='.':
		playData['lowR'] = ss
	elif playData['topR']==playData['lowR'] and playData['topR']==ps and playData['midR']=='.':
		playData['midR'] = ss
	elif playData['lowR']==playData['midR'] and playData['lowR']==ps and playData['topR']=='.':
		playData['lowR'] = ss
	

	elif playData['topL']==playData['midM'] and playData['topL']==ps and playData['lowR']=='.':
		playData['lowR'] = ss
	elif playData['topL']==playData['lowR'] and playData['topL']==ps and playData['midM']=='.':
		playData['midM'] = ss
	elif playData['lowR']==playData['midM'] and playData['lowR']==ps and playData['topL']=='.':
		playData['topL'] = ss

	elif playData['topR']==playData['midM'] and playData['topR']==ps and playData['lowL']=='.':
		playData['lowL'] = ss
	elif playData['topR']==playData['lowL'] and playData['topR']==ps and playData['midM']=='.':
		playData['midM'] = ss
	elif playData['lowL']==playData['midM'] and playData['lowL']==ps and playData['topR']=='.':
		playData['topR'] = ss

		#make normal move

	elif playData['midM']=='.':
		playData['midM'] = ss

	elif playData['topL']=='.':
		playData['topL'] = ss
	elif playData['topR']=='.':
		playData['topR'] = ss
	elif playData['lowL']=='.':
		playData['lowL'] = ss
	elif playData['lowR']=='.':
		playData['lowR'] = ss

	elif playData['topM']=='.':
		playData['topM'] = ss
	elif playData['lowM']=='.':
		playData['lowM'] = ss
	elif playData['midL']=='.':
		playData['midL'] = ss
	elif playData['midR']=='.':
		playData['midR'] = ss

		

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
	ss = 'O'
else:
	p2 = p
	p1 = 'system'
	ss = 'X'
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
			makeMoveSystem(ps,ss)
	else:
		player = 'O'
		print p2+'\'s turn'
		if p2 == p:
			makeMove()
		elif p2 == 'system':
			makeMoveSystem(ps,ss)
	
	winner = checkWinner()
	opt = playerData.get(winner,0)
	if opt == p:
		playField()
		print 'Congrats %s, you won' %p
		exit()
	elif opt == 'system':
		playField()
		print 'Boo yaa! %s' %p
		exit()
playField()
print 'Looks like a tie'