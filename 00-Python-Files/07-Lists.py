#Lists - Have brackets [] - everything inside is called an item

movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[1]) #return the second item in the list - index
print(movies[0]) #return the first item in the list
print(movies[1:3]) #returns the first number given until right before the last number given
print(movies[1:4]) #returns 1-3
print(movies[1:]) #return 1-end
print(movies[:1]) #everything before 1
print(movies[:2])
print(movies[-1]) #grabs last item

print(len(movies)) #count the items in the list
movies.append("JAWS") #add an item to the end of our list
print(movies)

movies.insert(2, "Hustle")
print(movies)

movies.pop() #removes the last item
print(movies)

movies.pop(0) #remove the first item
print(movies)

amber_movies = ['Just Go With It', '50 First Dates']
our_favorite_movies = movies + amber_movies #combine lists
print(our_favorite_movies)

grades = [["Bob", 82], ["Alice", 90], ["Jeff", 73]]
bobs_grade = grades[0][1]
print(bobs_grade)
grades[0][1] = 83
print(grades)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1][2])