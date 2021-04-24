p,c = 'x','o' 

def ismoveleft(b) :
	for i in range(3) :
		for j in range(3) :
			if(b[i][j]=='_') : 
				return 1
	return 0

def evaluate(b) :
	for i in range(3) :
		if(b[i][0]==b[i][1] and b[i][1]==b[i][2]) :
			if(b[i][0]==p) :
				return -10
			elif(b[i][0]==c) :
				return 10

	for i in range(3) :
		if(b[0][i]==b[1][i] and b[1][i]==b[2][i]) :
			if(b[0][i]==p) :
				return -10 
			elif(b[0][i]==c) :
				return 10

	if(b[0][0]==b[1][1] and b[1][1]==b[2][2]) :
		if(b[0][0]==p) :
			return -10 
		elif(b[0][0]==c) :
			return 10

	if(b[0][2]==b[1][1] and b[1][1]==b[2][0]) :
		if(b[1][1]==p) :
			return -10 
		elif(b[1][1]==c) :
			return 10

	return 0

def result(s) :
	if(s==10) :
		print("Computer wins")
		return 0
	if(s==-10) :
		print("You win")
		return 0
	if(ismoveleft(b)==0) :
		print("Draw")
		return 0
	return 1


def minmax(b,d,cp) :
	s = evaluate(b)

	if(s==10 or s==-10) :
		return s
	if(ismoveleft(b)==0) :
		return 0

	if(cp) :
		best = -50 
		for i in range(3) :
			for j in range(3) :
				if(b[i][j]=='_') :
					b[i][j]=c
					best = max(best , minmax(b,d+1,1-cp))
					b[i][j]='_'
		return best-d

	else :
		best = 50
		for i in range(3) :
			for j in range(3) :
				if(b[i][j]=='_') :
					b[i][j]=p 
					best = min(best,minmax(b,d+1,1-cp))
					b[i][j]='_'
		return best+d

def move(b) :
	val = -100
	move=(-1,-1)

	for i in range(3) :
		for j in range(3) :
			if(b[i][j]=='_') :
				b[i][j]=c 
				moveval = minmax(b,0,0)
				if(moveval>val) :
					val=moveval
					move=(i,j)
				b[i][j]='_'
	return move


b = [ ['_','_','_'],['_','_','_'],['_','_','_'] ]


while(ismoveleft(b)) :
	x, y = [int(x) for x in input().split()]
	if(x<1 or y<1 or x>3 or y>3 or b[x-1][y-1]!='_') :
		print("Make valid move")
		continue
	b[x-1][y-1]=p
	for i in b :
		for j in i :
			print(j,end=' ')
		print()
	print()
	s = evaluate(b)
	if(result(s)==0) :
		break
	m = move(b)
	b[m[0]][m[1]]=c
	for i in b :
		for j in i :
			print(j,end=' ')
		print()
	print()
	s = evaluate(b)
	if(result(s)==0) :
		break
else :
	print("Draw")



