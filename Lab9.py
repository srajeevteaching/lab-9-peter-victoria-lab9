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

def load_movie_data ():
    movies = []
    try:
        file = open("movies.csv", "r")
        for line in file:
            movie = line.split(",")
            movie[BUDGET] = float(movie[BUDGET])
            #print("b",movie[BUDGET])
            movie[GROSS] = float(movie[GROSS])
            #print("g",movie[GROSS])
            movies.append(movie)
        file.close()
    except FileNotFoundError:
        print ("file does not exist")
    return movies

def add_profit_column(movies):
    for movie in movies:
        gross = movie[GROSS]
        budget = movie[BUDGET]
        profit = gross-budget
        #print (profit)
        movie.append(profit)

def print_min_and_max_profit(movies):
    max=0
    min=0
    for movie in movies:
        if movie[4] >max:
            max = movie[4]
            maxmovie=movie
        elif movie[4] < min:
            min = movie[4]
            minmovie=movie
    print ("max", maxmovie)
    print ("min", minmovie)

def save_movie_data(movies):
    movieFile = open("MovieList.txt", "w")
    for movie in movies:
        print (movie, file = movieFile)



def main():
    movieList = load_movie_data()
    withprofit = add_profit_column(movieList)
    print_min_and_max_profit(movieList)
    save_movie_data(movieList)

main()