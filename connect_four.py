import random

p,c = 'x','o' 

b = [['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_'],
['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_'],
['_','_','_','_','_','_','_'],['_','_','_','_','_','_','_']]

def ismoveleft() :
	for j in range(7) :
		if(b[0][j]=='_') : 
			return 1
	return 0

def evaluate() :
	s=0 
	for i in range(6) :
		for j in range(4) :
			if(b[i][j]!='_' and b[i][j]==b[i][j+1]) :
				if(b[i][j]==b[i][j+2]) :
					if(b[i][j]==b[i][j+3]) :
						if(b[i][j]==p) :
							return -10000
						if(b[i][j]==c) :
							return 10000
					else :
						if(b[i][j]==p) :
							s = s-15
						if(b[i][j]==c) :
							s = s+15
				else :
					if(b[i][j]==p) :
						s = s-5
					if(b[i][j]==c) :
						s = s+5


	for i in range(7) :
		for j in range(3) :
			if(b[j][i]!='_' and b[j][i]==b[j+1][i]) :
				if(b[j][i]==b[j+2][i]) :
					if(b[j][i]==b[j+3][i]) :
						if(b[j][i]==p) :
							return -10000
						if(b[j][i]==c) :
							return 10000
					else :
						if(b[j][i]==p) :
							s = s-15
						if(b[j][i]==c) :
							s = s+15
				else :
					if(b[j][i]==p) :
						s = s-5
					if(b[j][i]==c) :
						s = s+5

	for i in range(3) :
		for j in range(4) :
			if(b[i][j]!='_' and b[i][j]==b[i+1][j+1]) :
				if(b[i][j]==b[i+2][j+2]) :
					if(b[i][j]==b[i+3][j+3]) :
						if(b[i][j]==p) :
							return -10000
						if(b[i][j]==c) :
							return 10000
					else :
						if(b[i][j]==p) :
							s = s-15
						if(b[i][j]==c) :
							s = s+15
				else :
					if(b[i][j]==p) :
						s = s-5
					if(b[i][j]==c) :
						s = s+5

	for j in range(6,2,-1) :
		for i in range(3) :
			if(b[i][j]!='_' and b[i][j]==b[i+1][j-1]) :
				if(b[i][j]==b[i+2][j-2]) :
					if(b[i][j]==b[i+3][j-3]) :
						if(b[i][j]==p) :
							return -10000
						if(b[i][j]==c) :
							return 10000
					else :
						if(b[i][j]==p) :
							s = s-15
						if(b[i][j]==c) :
							s = s+15
				else :
					if(b[i][j]==p) :
						s = s-5
					if(b[i][j]==c) :
						s = s+5
	return s

def result(s) :
	if(s==10000) :
		print("Computer wins")
		return 0
	if(s==-10000) :
		print("You win")
		return 0
	if(ismoveleft()==0) :
		print("Draw")
		return 0
	return 1

def minmax(cp,al,be,d) :
	s = evaluate()

	if(s==10000 or s==-10000) :
		return s
	if(ismoveleft()==0) :
		return 0

	if(cp) :
		if(d==7) :
			return evaluate()
		l = [0,1,2,3,4,5,6]
		random.shuffle(l)
		for k in range(7) :
			j = l[k]	
			i = 5
			while(i>0 and b[i][j]!='_') :
				i=i-1
			if(b[i][j]!='_') :
				continue
			b[i][j]=c
			al = max(al,minmax(1-cp,al,be,d+1))
			b[i][j]='_'
			if(be<=al) :
				break
		return al

	else :
		if(d==7) :
			return evaluate()
		l = [0,1,2,3,4,5,6]
		random.shuffle(l)
		for k in range(7) :
			j = l[k]	
			i = 5
			while(i>0 and b[i][j]!='_') :
				i=i-1
			if(b[i][j]!='_') :
				continue
			b[i][j]=p
			be = min(be,minmax(1-cp,al,be,d+1))
			b[i][j]='_'
			if(be<=al) :
				break
		return be

def move() :
	val = -100000
	move = (-1,-1)
	l = [0,1,2,3,4,5,6]
	random.shuffle(l)
	for k in range(7) :
		j = l[k]
		i = 5
		while(i>0 and b[i][j]!='_') :
			i=i-1
		if(b[i][j]!='_') :
			continue
		b[i][j]=c
		moveval = minmax(0,-10000,10000,0)
		if(moveval>val) :
			val=moveval
			move=(i,j)
		b[i][j]='_'
	return move

while(ismoveleft()) :
	y = int(input())
	if(y>7 or y<1) :
		print("Make valid move")
		continue
	y=y-1
	x = 5
	while(x>0 and b[x][y]!='_') :
		x=x-1
	if(b[x][y]!='_') :
		print("Make valid move")
		continue
	b[x][y]=p
	for i in range(6) :
		for j in range(7) :
			print(b[i][j],end=" ")
		print()
	print()
	s = evaluate()
	if(result(s)==0) :
		break
	
	m = move()

	b[m[0]][m[1]]=c
	for i in range(6) :
		for j in range(7) :
			print(b[i][j],end=" ")
		print()
	print()
	s = evaluate()
	if(result(s)==0) :
		break

else :
	print("Draw")

