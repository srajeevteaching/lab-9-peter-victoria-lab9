#Programmers: Peter Hope
#Course: CS151, Dr. Rajeev
#Date: 11/18/21
#Lab Number: 9
#Program Inputs: movies file
#Program Outputs: output file with added profit, info of movies with highest and lowest profits


DATE = 0 #release date
TITLE = 1
BUDGET = 2
GROSS = 3 #box office gross

# this function loads the data from the given file into a list of lists
def load_movie_data ():
    movies = []
    try:
        #open the file for reading
        file = open("movies.csv", "r")
        #run through each movie in the file
        for line in file:
            #split the movie into its different parts, add it to a list
            movie = line.split(",")
            #casts the budget and gross into floats
            movie[BUDGET] = float(movie[BUDGET])
            #print("b",movie[BUDGET])
            movie[GROSS] = float(movie[GROSS])
            #print("g",movie[GROSS])
            #add the list to list of movies
            movies.append(movie)
        file.close()
    #try/except for if the above code runs into an error such as not finding file
    except FileNotFoundError:
        print ("file does not exist")
    return movies

# this function subtracts the budget from the box office gross for each movie to find the profit and adds it to the list
def add_profit_column(movies):
    for movie in movies:
        gross = movie[GROSS]
        budget = movie[BUDGET]
        profit = gross-budget
        #print (profit)
        movie.append(profit)

#this function find the max and min profit out of all the movies and prints all the information about those movies
def print_min_and_max_profit(movies):
    max=0
    min=0
    #runs through each movie list in the list of movies
    for movie in movies:
        #if the movie is the new max profit, make it the max
        if movie[4] >max:
            max = movie[4]
            maxmovie=movie
        #if the movie is the new min profit, make it the min
        elif movie[4] < min:
            min = movie[4]
            minmovie=movie
    #print the max and min profit movies and all their info
    print ("max", maxmovie)
    print ("min", minmovie)

#this function takes the new list of lists and prints it into a new file
def save_movie_data(movies):
    #open the new file to write
    movieFile = open("MovieList.txt", "w")
    #print all of the information for all of the movies to the list
    for movie in movies:
        print (movie, file = movieFile)


# main funtion
def main():
    movieList = load_movie_data()
    withprofit = add_profit_column(movieList)
    print_min_and_max_profit(movieList)
    save_movie_data(movieList)

main()