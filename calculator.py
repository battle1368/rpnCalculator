import sys
import rpncalc

expression = ""
for i in range(len(sys.argv) - 1):
	expression = expression + sys.argv[i + 1] + " "
result = rpncalc.calc(expression)
if result == ValueError:
	print("Invalid argument! Expected integer or valid operator.")
elif result == Exception:
	print("Invalid expression!")
else:
	print(rpncalc.calc(expression))