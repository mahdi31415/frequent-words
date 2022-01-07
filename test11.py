
file = open("gfg.txt","r",encoding="utf8")
frequent_word = ""
frequency = 0
words = []

# Traversing file line by line
for line in file:
	
	# splits each line into
	# words and removing spaces
	# and punctuations from the input
	line_word = line.lower()
print(line_word)
# Finding the max occurred word
for i in range(0, len(words)):
	
	# Declaring count
	count = 1;
	
	# Count each word in the file
	for j in range(i+1, len(words)):
		if(words[i] == words[j]):
			count = count + 1;

	# If the count value is more
	# than highest frequency then
	if(count > frequency):
		frequency = count;
		frequent_word = words[i];

print("Most repeated word: " + frequent_word)
print("Frequency: " + str(frequency))
file.close();
