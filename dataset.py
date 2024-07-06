from algorithms import Movie, MoviesCollection

genres_list = ['thriller', 'adventure', 'sci-fi', 'musical', 'history',
          'drama', 'fantasy', 'animation', 'horror', 
          'romance', 'comedy', 'biography']

collection_list = [['Inception', 'adventure', '2010', '8.8'],
           ['Interstellar', 'sci-fi', '2014', '8.7'],
           ['The Lord of the Rings: The Fellowship of the Ring', 'fantasy', '2001', '8.9'],
           ['The Lord of the Rings: The Two Towers', 'fantasy', '2002', '8.8'],
           ['The Lord of the Rings: The Return of the King', 'fantasy', '2003', '9'],
           ['Atonement', 'romance', '2007', '7.8'],
           ['Gladiator', 'adventure', '2000', '8.5'],
           ['Avatar', 'fantasy', '2009', '7.9'],
           ['Der Untergang', 'history', '2004', '8.2'],
           ['Les Miserables', 'musical', '2012', '7.5'],
           ['Ted', 'comedy', '2012', '6.9'],
           ['X-Men', 'sci-fi', '2000', '7.3'],
           ['The Lion King', 'animation', '1994', '8.5'],
           ['The Greatest Showman', 'musical', '2017', '7.5'],
           ['The Notebook', 'romance', '2004', '7.8'],
           ['Titanic', 'drama', '1997', '7.9'],
           ['Cinderella', 'animation', '1950', '7.3'],
           ['A Beautiful Mind', 'biography', '2001', '8.2'],
           ['The Hunger Games', 'adventure', '2012', '7.2'],
           ['The Green Mile', 'drama', '1999', '8.6'],
           ['Iron Man', 'sci-fi', '2008', '7.9'],
           ['Zombieland', 'comedy', '2009', '7.5'],
           ['Dumb and Dumber', 'comedy', '1994', '7.3'],
           ['The Shawshank Redemption', 'drama', '1994', '9.3'],
           ['The Godfather', 'drama', '1972', '9.2'],
           ['Mad  Max: Fury Road', 'adventure', '2015', '8.1'],
           ['The Phantom of the Opera', 'musical', '2004', '7.2'],
           ['La vita e bella', 'drama', '1997', '8.6'],
           ['Stardust', 'fantasy', '2007', '7.6'],
           ['Up', 'animation', '2009', '8.3'],
           ['Sleepy Hollow', 'horror', '1999', '7.3'],
           ['The Prestige', 'thriller', '2006', '8.5'],
           ['The Departed', 'thriller', '2006', '8.5'],
           ['The Conjuring', 'horror', '2013', '7.5'],
           ['The Sound of Music', 'musical', '1965', '8.1'],
           ['The Pianist', 'biography', '2002', '8.5'],
           ['La La Land', 'romance', '2016', '8.0'],
           ['Matrix', 'sci-fi', '1999', '8.7'],
           ['Now You See Me', 'thriller', '2013', '7.2'],
           ['About Time', 'romance', '2013', '7.8'],
           ['Kingdom of Heaven', 'history', '2005', '7.3'],
           ['WALL-E', 'animation', '2008', '8.4'],
           ["Schindler's List", 'history', '1993', '9.0'],
           ['Oblivion', 'sci-fi', '2013', '7.0'],
           ['Finding Nemo', 'animation', '2003', '8.2'],
           ['Lincoln', 'history', '2012', '7.3'],
           ['Alien', 'horror', '1979', '8.5'],
           ["The King's Speach", 'biography', '2010', '8.0'],
           ['The Hangover', 'comedy', '2009', '7.7'],
           ['I Am Legend', 'horror', '2007', '7.2'],
           ['Shutter Island', 'thriller', '2010', '8.2'],
           ['Pride and Prejudice', 'romance', '2005', '7.8']
           ] 



collection_HashMap = MoviesCollection(len(genres_list))
for item in collection_list:
    collection_HashMap.add_movie(Movie(item[0], item[1], item[2], item[3]))



