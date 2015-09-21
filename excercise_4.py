salary = 40000
save = 5
growth_rate = 1
growth_rate2 = [4, 1, 10, 3, 7, 5]
years = 5


#problem 1
def nest_egg_fixed(salary, save, growth_rate, years):
	fund = [salary * save * .01]

	for x in range(years):
		fund.append(fund[x] * (1 + .01 * growth_rate) + salary * save * .01)

	return fund

#problem 2
def nestEggVariable(salary, save, growthRates):
	fund = [salary * save * .01]

	for x in range(len(growthRates)):
		fund.append(fund[x] * (1 + .01 * growthRates[x]) + salary * save * .01)

	return fund




#problem 3
def postRetirement(savings, growthRates, expenses):
	fund = [savings * (1 + .01 * growthRates[0]) - expenses]
	
	for x in range(1, len(growthRates)):
		fund.append(fund[x-1] * (1 + .01 * growthRates[x]) - expenses)
	return fund
#problem 3
def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    return savingsRecord

def binary_search(savings, growthRates, expenses):
	fund = savings * (1 + .01 * growthRates[0]) - expenses
	
	for x in range(1, len(growthRates)):
		fund = fund * (1 + .01 * growthRates[x]) - expenses
	return fund



#problem 4
def findMaxExpenses():
	salary = 10000
	save = 10
	preRetireGrowthRates = [3, 4, 5, 0, 3, 3, 6, 1, 2, 3]
	postRetireGrowthRates = [10, 5, 0, 5, 1, 3, 5, 2, 3, 1]
	epsilon = .01
	savings = salary * save * .01

	for x in range(len(preRetireGrowthRates)): # determines how much money you will have when you retire
		savings = savings * (1 + .01 * preRetireGrowthRates[x]) + salary * save * .01
	

	high = savings
	low = 0
	guess = (high + low) / 2.0 #initial guess as to how much you can spend each year
	cntrl = 0

	while abs(binary_search(savings, postRetireGrowthRates, guess)) > epsilon and cntrl <= 100: # loops through until it finds the right expense so that when it runs through the retired calculator you will have 0 dollars when you die
		if binary_search(savings, postRetireGrowthRates, guess) > 0: #if the guess is to high, then set the low value to guess.  so when we make our second guess it will get closer to 0
			low = guess
		else:
			high = guess #if guess is to low, high to guess
		guess = (high + low) / 2.0 #adjusts guess
		cntrl += 1
	return guess




print 'problem 1 - list of money in 401k per year', nest_egg_fixed(salary, save, growth_rate, years)
print 'problem 2 - list of money in 401k per year with changing growth rates', nestEggVariable(salary, save, growth_rate2)
print 'problem 3 - list of money in retirement, and how much money you have each year after expenses and growth rate are taken into account', testPostRetirement()
print 'problem 4 - figured out with binary search how much you can spend per year so that you have 0 dollars by the time you die', findMaxExpenses()

	






