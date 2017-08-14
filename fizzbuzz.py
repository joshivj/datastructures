
# write program to print number from 1 to 100
# multiple of 3 print "fizz" instead of number
# multiple of 5 print "buzz" instead of number
# for number which are mutiple of both 3 and 5 print "fizzbuzz"

start = 1
end = 101
val_3 = 3
val_5 = 5
word1 = 'FizzBuzz'
word2 = 'Fizz'
word3 = 'Buzz'

for i in xrange(start,end):
	if i%val_3==0 and i%val_5==0:
		print word1
	elif i%val_5==0:
		print word3
	elif i%val_3==0:
		print word2
	else:
		print i