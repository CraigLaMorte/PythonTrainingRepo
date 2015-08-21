
#problem 1 - figures out the combinations of 6, 9 and 20 needed to get 51-56 nuggets.  Loops through all possible combinations and returns the correct amounts of each package.
def nuggets(n):
	sm = 0
	md = 0
	lg = 0
	
	for sm in range(10): # first loop of the small package of 6 nuggets
		if (6*sm) + (9*md) + (20*lg) == n:
			return sm, md, lg

		for md in range(10): # first loop of the med package of 9 nuggets
			if (6*sm) + (9*md) + (20*lg) == n:
				return sm, md, lg

			for lg in range(10): # first loop of the large package of 20 nuggets
				if (6*sm) + (9*md) + (20*lg) == n:
					return sm, md, lg
	return None

# problem 3 - figures out the largest possible number that 6, 9 and 20 and not be combined to create.  loops through calling problem 1 function and appends numbers that return no result. stops after 6 consecutive passes
def larg_numb(): 
	counter = 0
	no_list = []

	for i in range(1, 56):
		if counter == 6:
			return no_list[-1]
		elif nuggets(i) == None:
			no_list.append(i)
			counter = 0
		else:
			counter += 1
	print 'the highest value of nuggets that cant be bought is %i' % (no_list[-1])




nugget_number = 60
sm, md, lg = nuggets(nugget_number)
print 'for %i nuggets you need %i small, %i medium, and %i large nugget packages' % (nugget_number, sm, md, lg)

print 'the highest value of nuggets that can not be bought with the combination of sm, md, and lg is %i (after 6 consective passes)' % (larg_numb())

