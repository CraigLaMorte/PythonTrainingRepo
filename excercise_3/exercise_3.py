from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings
target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings
key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'


def countSubStringMatch(key, target):
    count = 0
    string_check = True
    string_modify = 0
    generalize_search = []
    
    while string_check == True:
        string_index = find(target, key, string_modify)
       
        if string_index >= 0:
            count += 1
            string_modify = string_index +1
            generalize_search.append(string_index)
        else:
            string_check = False
            return count, generalize_search




def countSubStringMatchRecursive(key, target, count):
    string_index = find(target, key)

    if string_index >= 0:
        count += 1
        return countSubStringMatchRecursive(key, target[string_index+1:], count)
    else:
        return count







count_match, gen_search = countSubStringMatch(key11, target1)

print 'Iteration - there are %i instances of that key located in that string' % (count_match)
print 'recursive - there are %i instances of that key located in that string' % (countSubStringMatchRecursive(key12, target1, 0))

print 'search has found the following starting locations for that keyword in target string - ', gen_search








    
