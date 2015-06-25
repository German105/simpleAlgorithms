import pgFibonacci

print("A feq individual elements")
print(pgFibonacci.getFibonacci(3))
print(pgFibonacci.getFibonacci(5))
print(pgFibonacci.getFibonacci(15))
print("First 100 elements of Fibonacci")#This is a better way of geting more than one element
table=pgFibonacci.getFibonacciTable(100)
for i in range(len(table)):
	print(table[i])