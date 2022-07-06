stack = []

def push(arg):
	stack.append(arg)

def pop():
	return stack.pop(-1)

def calc(expression):
	global stack
	stack = []
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
				return(ValueError)
			push(i)
	if len(stack) != 1:
		# print("Invalid expression!")
		return(Exception)
	else:
		return pop()