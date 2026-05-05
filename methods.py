word = "library"
print(word.strip())      #Strips all the white spaces from left and right side of a str
print(word.capitalize()) #Capitalizes only first letter of the first word
print(word.title())      #Capitalizes first letter of every word
print(word.split()) #spits the word at whitespaces and returns an array of substring
print(word.split("r")) #splits the word at every r it will encounter 
print(word.split("r", 1)) #splits the word from the first r it encounters

#The above methods can also be written in the following way
print(word.split().title().split("r", 1))