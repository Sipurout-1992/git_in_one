# Iterating over dictionary
print("Dictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
	print("% s % d" % (i, d[i]))




# Iterating over a String
print("String Iteration")
s = "Geeks"
for i in s:
    print(i)


# Prints all letters except 'e' and 's'
for letter in 'geeksforgeeks':
	if letter == 'e' or letter == 's':
		continue
	print('Current Letter :', letter)
