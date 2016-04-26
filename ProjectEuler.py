#PROJECT EULER
#This is practice to keep my python knowledge updated and refreshed.
import math
import timeit


###############PROBLEM 1###############
#Multiples of 3 and 5

def multsTF(n):
	mults = []
	for num in range(n):
		if num%3 == 0 or num%5 == 0:
			mults.append(num)
	summ = 0
	for x in mults:
		summ += int(x)
	return summ

#######################################


###############PROBLEM 2###############
#Even Fibonacci numbers

def efibs(limit):
	n1 = 0
	n2 = 1
	temp = 0
	summ = 0
	fibs = []
	while n2 <= limit:
		fibs.append(n1)
		temp = n1 + n2
		n1 = n2
		n2 = temp
	fibs.append(n1)
	for x in fibs:
		if x%2 == 0:
			summ += x
	print(fibs)
	return summ

#######################################


###############PROBLEM 3###############
#Largest prime factor
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def list_divisors(n): #this can be improved upon, it's super slow dealing with ints that have 9 digits or more
	dlist = []
	for d in range(1,int(math.sqrt(n))+1):
		if n%d == 0:
			dlist.append(d)
	return dlist

def gen_primes(limit):
	plist = []
	for n in range(limit):
		if list_divisors(n) == [1]:
			plist.append(n)
	return plist

def LPF(n):
	l = len(str(n))
	digits = l//3
	plist = gen_primes(int(math.pow(10,digits)))
	plist.reverse()
	for num in plist:
		if n%num == 0:
			return num

#######################################


###############PROBLEM 4###############
#Largest Palindrome Product
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def FLP():
	pal = 0
	for num1 in range(999,99,-1):
		for num2 in range(999,99,-1):
			prod = num1*num2
			sprod = str(prod)
			l = len(sprod)
			m = l//2
			low = sprod[:m]
			high = sprod[m:]
			revhigh = ''
			for index in range(len(high)):
				revhigh += high[-(index+1)]
			if low == revhigh and prod > pal:
				pal = prod
	return pal

#######################################


###############PROBLEM 5###############
#Smallest Multiple
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def SmlMul(n):
	least = 0
	mul = 1
	for num in range(2,n+1):
		mul *= num
	low = n
	num = 1
	while num != mul:
		for num2 in range(n,0,-1):
			if num%num2 == 0:
				low = num2
				if low == 1:
					return num
			elif num%num2 != 0:
				break
		num += 1

#######################################


###############PROBLEM 6###############
#Sum square difference
#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^2 = 55^2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def SSDif(n):
	l1 = []
	summ = 0
	for num in range(1,n+1):
		l1.append(num*num)
		summ += num
	summ *= summ
	return summ - sum(l1)
	

#######################################


###############PROBLEM 7###############
#10001st prime
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

def primeID(n):
	found = False
	num = 0
	count = 0
	while found == False:
		if list_divisors(num) == [1]:
			count += 1
			if count == n:
				return num
		num += 1
		
# i can probalby make a better isPrime function than using list divisors...
#######################################


###############PROBLEM 8###############
#Largest product in a series
#Find the thirteen adjacent digits in the 1000-digit number that have
#the greatest product. What is the value of this product?
thousanddigit='7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

def LPS(anum):
	num = thousanddigit
	prod = 1
	count = anum
	while count != len(num)+1:
		tprod = 1
		for n in range(count-anum,count):
			tprod *= int(num[n])
		if tprod > prod:
			prod = tprod
		count += 1
	return prod



#######################################


###############PROBLEM 9###############
#Special Pythagorean Triplet
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def SPT(n):
	trips = [1,1,1]
	while trips[0] != n/2:
		if (trips[0]*trips[0])+(trips[1]*trips[1]) == trips[2]*trips[2]:
			if trips[0]+trips[1]+trips[2] == n:
				return trips[0]*trips[1]*trips[2]
#this is kind of ugly... it's a good ticker though, kind of like a clock. Also very slow when n >>> 1 so that is why I use n/2, which assumes the largest triplet number is < n/2
		if trips[2] < n/2:
			trips[2] += 1
		elif trips[2] == n/2:
			trips[2] = 1
			if trips[1] < n/2:
				trips[1] += 1
			elif trips[1] == n/2:
				trips [1] = 1
				if trips[0] < n/2:
					trips[0] += 1



#######################################


###############PROBLEM 10###############
#Summation of primes
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

def SOP(n):
	total = 2
	x = 3
	while x <= n:
		state = True
		for div in range(2,(x//2)+1):
			if x%div == 0:
				state = False 
		if state == True:
			total += x
		x += 2
	return total


#	t = []
#	for num in range(start,n+1):
#		state = True
#		for d in range(2,(num//2)+1):
#			if num%d == 0:
#				state = False
#				break
#		if state == True:
#			t.insert(0,num)
#	return sum(t)

#	stack = [2]
#	while start <= n:
#		divs = [1]
#		for number in range(2,start):
#			if start%number == 0:
#				divs.insert(0,number)
#				break
#		if divs == [1]:
#			stack.insert(0,start)
#		start += 2
#	return sum(stack)


#double for loop editing stack?
		

#NEED TO HANDLE THIS WITH A STACK
def split1(n):
	s = []
	s.insert(0,SOP(3,10000))
	for n in range(1,(n//10000)):
		print(n)
		s.insert(0,SOP((10000*n)-1,10000*(n+1)))
	return sum(s)

#######################################

