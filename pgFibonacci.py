#Simple algoritm using memorisation

def getFibonacciTable(size):
	return getTable(1,1,size)

def getFibonacci(pos):
	table=getTable(1,1,pos+1)#0 is the first element +1 to make the list long enough
	return table[pos]

def getTable(firstElement, secondElement, size):
	table=[0 for x in range(size)]
	table[0]=firstElement
	table[1]=secondElement
	for i in range(2,size):
		table[i]=table[i-1]+table[i-2]
	return table