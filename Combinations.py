import datetime
import itertools

# There are 93 items in this list...
pwdChars = '0123456789abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVQHY"\'-></\-_=+{}[]|?~`€@£#$%^&*()§±' + chr(0x20)

#  no of characters/digits in password - Change this to set the max length you would like.
noPwdChars = 5

#  Used to log total number of combinations
combinations = 0

#  Collect the start time
startTime = datetime.datetime.now()
print("Started: {}".format(startTime))
print("*" * 50)


#  Create / Open the text file
with open('Combinations.txt','w') as txt_file:

	#  For loop to set maximum lenth of Combined characters
	for i in range(0, noPwdChars):
		#  For loop iterates through all possible char combinations
		for p in itertools.product(pwdChars, repeat=i+1):
			#  Answer it provided in a tuple - this convers it to a string
			string = ''.join(p)
			#  string gets added to the open text file with a EOL at the end
			txt_file.write(string + "\n")
			#  current combination gets printed in console
			print(''.join(p))
			#  Comination counter gets increased by 1
			combinations += 1

#  collect the stop time
endTime = datetime.datetime.now()
print('')
print("*" * 50)
#  print stop time to console
print("Finished: {}".format(endTime))
#  calculate time taken
totalTime = endTime - startTime
#  print time taken to console
print("Time taken: {}".format(totalTime))
#  print number of combinations to console
print('Combinations: {}'.format(combinations))
print("*" * 50)
































