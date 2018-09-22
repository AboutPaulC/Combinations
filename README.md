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
- 5...........
