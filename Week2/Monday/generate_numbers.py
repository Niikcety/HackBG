import sys
from random import randint


def generate_numbers(filename, numbers):
    file = open(filename,"w")
    number = int(numbers)
    for i in range(0,number):
    	random = str(randint(-sys.maxsize-1,sys.maxsize))
    	random = random + " "
    	file.write(random)
    file.close()	


def main():
    generate_numbers(sys.argv[1],sys.argv[2])

if __name__ == '__main__':
    main()