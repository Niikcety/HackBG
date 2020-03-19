from polynomial import Derivative
import sys

def main():
	der = Derivative(sys.argv[1])
	print(der)

if __name__ == '__main__':
	main()