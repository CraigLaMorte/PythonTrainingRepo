# http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00-introduction-to-computer-science-and-programming-fall-2008/assignments/pset1a.pdf

from math import *

#Tests the number to see if it is prime.
def is_prime(test_num):
	
	#divides numbers 2 through half of the number we are testing to see if it returns a remainder of 0. 
	for number in range(2, test_num / 2):
		if test_num % number == 0:
			#a number was divisble into our test number so it is not prime
			return None
	else:
		#no numbers were divisble so this number is a prime number
		return True


#prints out all prime numbers to 1000
def prime_1000():
	
	prime_test = 3
	prime_count = 2
	#since 2 can't be tested with % and we know its prime it is the first to be printed
	print 'prime #1 is 2'
	#loops through and prints all of our primes until we hit our 1000th prime number
	while prime_count <= 1000:
		#comptues to see if our test number is prime or not.  It will return true if it is prime, otherwise it returns None.
		if is_prime(prime_test) == True:
			print "Prime #%i is %i" % (prime_count, prime_test)
			prime_count += 1
				#skips all evens since none are prime (except 2)			
		prime_test += 2
					

#will give the sum of the logarithims of each prime number less then given number
def product_primes(number):
	#test to see if the user put in a number too low
	if number <= 2:
		print 'There are no prime numbers below this numberr'
		return None
	else:
		#start with prime 2 since it can't be tested in is_divisble function and we know the users number is higher then 2.  starts testing on 3
		sum_prime = log(2.0)
		prime_number = 3
		# loops through all numbers until it reaches users number
		while prime_number < number:
			#if give number in loop is tested in function to be prime then it returns true and adds its logarithim to sum_prime
			if is_prime(prime_number) == True:
				sum_prime +=  log(prime_number)
			#skips even since they are not prime
			prime_number += 2
		return sum_prime


#Problem 1 - calls function to print out 1000 prime numbers for 
prime_1000()

# problem 2 - assigns test variable and assigns variable to the function that gives us product of primes
test_number = 100
sum_primes = product_primes(test_number)
print 'The sum of the primes less then %i is %f and the ratio is %f' % (test_number, sum_primes, (test_number / sum_primes))




