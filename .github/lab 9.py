#def binary_search( a_list, target ):
#    start_index = 0
#    end_index = len( a_list ) - 1
#    while end_index >= start_index: # we have not run out of places to find it
#        middle = ( start_index + end_index ) // 2
#        if a_list[middle] == target: # found target at index middle
#            return middle
#        elif a_list[middle] > target: # search left half of list
#            end_index = middle - 1
#        else: # search right half of list
#            start_index = middle + 1
#    return -1 # not found


movie_list = []
release_date = 0
title = 1
budget = 2
box_office = 3


def load_movie_data(filename):
    lines = 0
    try:
        file = open(filename, "r")
        try:
            for line in file:
                lines += 1
                line_entries = line.split(",")
                line_entries[release_date] = line_entries[release_date]
                line_entries[title] = line_entries[title].strip()
                line_entries[budget] = float(line_entries[budget])
                line_entries[box_office] = float(line_entries[box_office])
                movie_list.append(line_entries)
        except ValueError:
            print("Error in line" + str(lines) + ", line skipped.")
    except FileNotFoundError:
        print("This file does not exist.")
    return movie_list


def add_profit_column(data):
    for line in data:
        profit = line[box_office] - line[budget]
        movie_list.append(profit)


def main():
    print(load_movie_data("movies.csv"))
    add_profit_column(load_movie_data("movies.csv"))
    print(movie_list)


main()
