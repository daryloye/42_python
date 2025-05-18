import sys

try:
	if len(sys.argv) > 2:
		raise AssertionError("more than one argument is provided")
	elif len(sys.argv) == 1:
		exit()

	try:
		if int(sys.argv[1]) % 2 == 0:
			print("I'm Even.")
		else:
			print("I'm Odd.")
	except:
		raise AssertionError("argument is not an integer")

except AssertionError as e:
	print(f"{type(e).__name__}: {e}")