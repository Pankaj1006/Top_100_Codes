my_str = input("Enter a string: ")
words = [word.lower() for word in my_str.split()]
words.sort()
# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)

