import sys
import rpncalc

expression = input("Please enter an expression:\n")
result = rpncalc.calc(expression)
if result == ValueError:
	print("Invalid argument! Expected an integer or a valid operator.")
elif result == Exception:
	print("Invalid expression!")
else:
	print(rpncalc.calc(expression))