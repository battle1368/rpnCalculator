import sys

stack = []

def push(arg):
	stack.append(arg)

def pop():
	return stack.pop(-1)

def calc(expression):
	operands = expression.split()
	for i in operands:
		if i == "+":
			operand2 = pop()
			operand1 = pop()
			push(operand1 + operand2)
		elif i == "-":
			operand2 = pop()
			operand1 = pop()
			push(operand1 - operand2)
		elif i == "*":
			operand2 = pop()
			operand1 = pop()
			push(operand1 * operand2)
		elif i == "/":
			operand2 = pop()
			operand1 = pop()
			push(operand1 // operand2)
		elif i == "%":
			operand2 = pop()
			operand1 = pop()
			push(operand1 % operand2)
		else:
			try:
				i = int(i)
			except ValueError:
				print("Invalid argument! Expected integer or valid operator.")
				exit()
			push(i)
	if len(stack) != 1:
		print("Invalid expression!")
		exit()
	else:
		return pop()

expression = ""
for i in range(len(sys.argv) - 1):
	expression = expression + sys.argv[i + 1] + " "
print(calc(expression))