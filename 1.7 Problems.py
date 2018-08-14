# Problem 1.7.1: my filter(L, num)
#                input: list of numbers and a positive integer.
#                output: list of numbers not containing a multiple of num.
#                example: given list = [1,2,4,5,7] and num = 2, return [1,5,7].

def my_filter(L,num): return {L[x] for x in range(len(L)) if L[x]%num != 0}



# Problem 1.7.2: my lists(L)
#                input: list L of non-negative integers.
#                output: a list of lists: for every element x in L create a list containing 1, 2, . . . ,x.
#                example: given [1,2,4] return [[1],[1,2],[1,2,3,4]]. example: given [0] return [[]].

def my_lists(L): return [list(range(1,i+1)) for i in L]

# example/test
l = [0, 1, 10, 5, 1, 5, 2]
my_lists(l)


# Problem 1.7.3: my function composition(f,g)
#                input: two functions f and g, represented as dictionaries, such that g ◦ f exists.
#                output: dictionary that represents the function g ◦ f.
#                example: given f = {0:’a’, 1:’b’} and g = {’a’:’apple’, ’b’:’banana’}, return {0:’apple’, 1:’banana’}.

def my_function_composition(f,g): return {list(f.keys())[i]: list(g.values())[i] for i in f if list(f.values()) == list(g.keys())}

# example/test
w = {0:'a', 1:'b', 2: 'c'}
v = {'a': 'apple', 'b':'banana', 'c': 'carrot'}

my_function_composition(w,v)
