#Advanced Strings

my_name = "Heath"
print(my_name[0]) #first letter
print(my_name[-1]) #last letter

sentence = "192.168.138.1"
print(sentence[:4])

print(sentence.split('.')) #delimeter - default is a space

sentence_split = sentence.split('.')
sentence_join = '.'.join(sentence_split)
print(sentence_join)

quote = "He said, 'give me all your money'"
quote = "He said, \"give me all your money\""
print(quote)

too_much_space = "                   hello       "
print(too_much_space.strip())

print("A" in "Apple") #return True
print("a" in "Apple") #return False - case sensitive

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #improved

#user_input = input("Enter yes or no: ")
#if user_input.lower().strip() == "yes":
#    print("You agree!")
#else:
#    print("You disagree!")

movie = "The Hangover"
print("My favorite movie is {}.".format(movie))
print("My favorite movie is %s." % movie)
print(f"My favorite movie is {movie}.")