# Combinations

I was reading an article on Wi-Fi password generation and wondered just how long it would actually take to generate a list of all possible password combinations...

### BE WARNED - CPU AND TIME INTENSIVE - START WITH A LOW NUMBER

So I wrote a little script to run and see what times it could complete in depending on how many characters in length I requested it to be. The script uses itertools to create the combinations and then writes each to the console with a print command and then to a txt file.

The characters used are: 0123456789abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVQHY-></\-_=+{}[]|?~`€@£#$%^&*()§±'" and SPACE

The computer it is being tested on is an Apple 2015 MBP 15" Retina, 2.8 Intel i7, with 16Gb Ram and a 1TB SSD - Let me know what yours manages to do?!

- Length......Time Taken........No Of Combinations
- 1...........0:00:00.001031........93
- 2...........0:00:00.045862........8,742
- 3...........0:00:04.300669........813,099
- 4...........0:08:01.211785........75,618,300
- 5........... HOURS........ 12.5 to be exact... Keep reading for the figures...

I need my MBP more than using it to find out how long this script will take to run, so i had an idea, grabbed a spare Raspberry Pi B Ver 2 512Mb and set it to work... Yes it is significantly slower than an i7 MBP, but equally it can sit there running the script for as long as it takes without affecting anything else...

- Length......Time Taken........No Of Combinations
- 1...........0:00:00.682163.........93
- 2...........0:01:01.375333.........8,742
- 3...........1:35:31.672425.........813,099
- 4...........     Running Now... And thats as far as you can get on a Pi before it runs out of memory, oh well...

I ran the 5 digit combination on my MBP, it took 12:34:23.184416 to generate 7,032,501,993 combinations... If anyone has a spare super computer lying about to keep testing thatd be great, maybe at some point i'll setup a cloud based instance and run it from there so i can still use my MBP...


