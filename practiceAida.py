#Partner 1: Aida Krzalic
#Partner 2: Kim Promthaw
#########################
#Assignment Name: GitHub Practice - 20 points 02/25/20
import random as rand

def getNRandom(n):
	'''takes in an integer and returns a list of n random integers between 1 and 10, inclusive'''
	return [rand.randint(1,10) for i in range(n)]

def multiplyRandom(numbers):
	'''takes in a list of n numbers and returns the product of the numbers'''
	ans = 1;
	for number in numbers:
		ans = ans * number
	return ans

def main():
	print(multiplyRandom(getNRandom(10)))

if __name__ == "__main__":
	main()
