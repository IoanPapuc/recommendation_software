from dataset import genres_list, collection_list, collection_HashMap
from algorithms import linear_search, MoviesCollection




def construct_user_choice(genres_list):
    
    user_input = input("What type of movie would you want to see? Type the beginning of the genre and press enter.\n")
    options = linear_search(genres_list, user_input)

    if len(options) == 1:
        print("The only option available is: {}.".format(options[0]))
        while True:
            answer = input("Would you want to see {} movies? Enter y/n: ".format(options[0]))
            if answer == 'y':
                return options[0]
            elif answer == 'n':
                return None
            else:
                print("Please enter a valid option: 'y' for yes or 'n' for no." )
    elif len(options) > 1:
        print("The options available are: " + ', '.join(options))
        return construct_user_choice(options)
    else:
        print("No option available for your input: {}".format(user_input))
        return None
    


def print_movies(genres_list, movies_collection):
    genre = construct_user_choice(genres_list)
    if genre:
        movies_collection.print_movies_by_genre(genre)

    while True:
        another_genre = input("Do you want to choose another type of movies? Enter y/n: ")
        if another_genre =='y':
            print_movies(genres_list, movies_collection)
            return
        elif another_genre == 'n':
            print("Thank you for using our recommendation software!")
            return
        else:
            print("Please enter a valid option: 'y' for yes or 'n' for no." )
   
        



print_movies(genres_list, collection_HashMap)



























