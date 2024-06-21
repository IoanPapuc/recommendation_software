from dataset import genres, collection



def construct_user_choice(genres_list):
    options = []
    user_input = input("What type of movie would you want to see? Type the beginning of the genre and press enter to check if we have it.\n")
    for genre in genres_list:
        if user_input == genre[0:len(user_input)]:
            options.append(genre)
    if len(options) == 1:
        print("The only option available is: {}.".format(options[0]))
        answer = input("Would you want to see {} movies? Enter y/n: ".format(options[0]))
        if answer == 'y':
            print("You choose " + options[0])
            return options[0]
        else:
            return None
    elif len(options) > 1:
        print("The options available are: " + ', '.join(options))
        return construct_user_choice(options)
    else:
        print("No option available for your input: {}".format(user_input))
        return None
    




def get_genre(genres_list):
    genre = construct_user_choice(genres_list)
    if genre:
        print("Am returnat " + genre)
        return genre
    else:
        print("N-am returnat nimic")
        another_genre = input("Do you want to choose another type of movies? Enter y/n: ")
        if another_genre =='y':
            return get_genre(genres_list)
        else:
            return None
        




def print_movies(genres_list, movies_collection):
    genre = get_genre(genres_list)
    if genre:
        for movie in movies_collection:
            if movie[0] == genre:
                print("* {0} ({1})\n IMDB score: {2}".format(movie[1], movie[2], movie[3]))
    else:
        print("Thank you for using our recommendation software!")


print_movies(genres, collection)