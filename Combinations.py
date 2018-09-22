import datetime
import itertools

# There are 93 items in this list...
pwdChars = '0123456789abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVQHY"\'-></\-_=+{}[]|?~`€@£#$%^&*()§±' + chr(0x20)

#  no of characters/digits in password
noPwdChars = 5
combinations = 0

startTime = datetime.datetime.now()
print("Started: {}".format(startTime))
print("*" * 50)

with open('Combinations.txt','w') as txt_file:

	for i in range(0, noPwdChars):
		for p in itertools.product(pwdChars, repeat=i+1):
			string = ''.join(p)
			txt_file.write(string + "\n")
			print(''.join(p))
			combinations += 1

endTime = endTime = datetime.datetime.now()
print('')
print("*" * 50)
print("Finished: {}".format(endTime))
totalTime = endTime - startTime
print("Time taken: {}".format(totalTime))
print('Combinations: {}'.format(combinations))
print("*" * 50)
































