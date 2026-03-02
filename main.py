("""
Recursive Fibonacci implementation.

Usage:
  python main.py [n]

If `n` is omitted the script prints `fibonacci(10)`.
""")

def fibonacci(n: int) -> int:
	if n < 0:
		raise ValueError("n must be non-negative")
	if n < 2:
		return n
	return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
	import sys
	try:
		n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
	except ValueError:
		print("Please provide a non-negative integer")
		sys.exit(1)
	print(fibonacci(n))

