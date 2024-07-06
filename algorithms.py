
def linear_search(list, target):
    matches = []
    for item in list:
        if target == item[0:len(target)]:
            matches.append(item)
    return matches




class Movie:
    def __init__(self, title, genre, year, score = None):
        self.title = title
        self.genre = genre
        self.year = year
        self.score = score
    
    def __repr__(self):
        ret = " * {0} ({1}), score: {2}".format(self.title, self.year, self.score)
        return ret




class MoviesCollection:
    def __init__(self, size):
        self.array_size = size
        self.array = [None for i in range(self.array_size)]

    def hash(self, genre, count_collisions = 0):
        key_bytes = genre.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions
    def compressor(self, hash_code):
        return hash_code % self.array_size
    
    def add_movie(self, movie):
        genre = movie.genre
        index = self.compressor(self.hash(genre))
        loc = self.array[index]
        if loc is None:
            self.array[index] = [genre, []]
            self.array[index][1].append(movie)
            return
        if loc[0] == genre:
            self.array[index][1].append(movie)
            return
        count_collisions = 1
        while loc[0] != genre:
            new_index = self.compressor(self.hash(genre, count_collisions))
            new_loc = self.array[new_index]
            if new_loc is None:
                self.array[new_index] = [genre, []]
                self.array[new_index][1].append(movie)
                return
            if new_loc[0] == genre:
                self.array[new_index][1].append(movie)
                return
            count_collisions += 1
        
    def return_movies_by_genre(self, genre):
        index = self.compressor(self.hash(genre))
        loc = self.array[index]
        if loc is None:
            return None
        if loc[0] == genre:
            return self.array[index][1]
        count_collisions = 1
        while loc[0] != genre:
            new_index = self.compressor(self.hash(genre, count_collisions))
            new_loc = self.array[new_index]
            if new_loc is None:
                return None
            if new_loc[0] == genre:
                return self.array[new_index][1]
            count_collisions += 1

    def print_movies_by_genre(self, genre):
        print("-------------------------------------------")
        print("We recommend the following {} movies:\n".format(genre))
        genre_set = self.return_movies_by_genre(genre)
        for movie in genre_set:
            print(movie)
        print("-------------------------------------------")








