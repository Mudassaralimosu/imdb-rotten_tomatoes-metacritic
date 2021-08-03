# imdb-rotten_tomatoes-metacritic

With the help of this module, you can get the imdb,rotten tomatoes and metacritic rating.

Also you can get how many peoples have voted on imdb,rotten tomatoes and metacritic so thay there ratings are calculated 

--

## Installation

Run the following to install:

```python
pip install imdb-rtomatoes-metacritic
```

--

## Usage

```
from imdb_rtomatoes_metacritic import Rating

#In the quotes give the movie name or webseries name for which you want to get the ratings or votes

movie = Rating("Avengers Endgame") 

#To get the imdb score

imdb_score = movie.imdb_score()
or
print(movie.imdb_score())

#To get the number of people who have voted on imdb

imdb_votes = movie.imdb_votes()
or
print(movie.imdb_votes())

#To get the Rotten Tomatoes rating that is tomatometer

tomatometer = movie.tomatometer()
or
print(movie.tomatometer())

#To get the number of reviews on rotten tomatoes

reviews = movie.tomatometer_reviews()
or
print(movie.tomatometer_reviews())

#To get the metacritic rating that is metascore

metascore = movie.metacritic_score()
or
print(movie.metacritic_score())

#To get the critic reviews on metacritic

metacritic_votes = movie.metacritic_votes()
or
print(movie.metacritic_votes())
```








