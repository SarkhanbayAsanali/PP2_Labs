#Task 1:
def is_above_score(movie):
    return movie["imdb"] > 5.5

#Task 2:
def get_above_score_movies(movies):
    return [movie for movie in movies if is_above_score(movie)]

#Task 3:
def get_movies_by_category(movie_list, category):
    return [movie for movie in movie_list if movie["category"] == category]

#Task 4:
def calculate_average_score(movie_list):
    if not movie_list:
        return 0
    return sum(movie["imdb"] for movie in movie_list) / len(movie_list)

#Task 5:
def calculate_average_score_by_category(movie_list, category):
    category_movies = get_movies_by_category(movie_list, category)
    return calculate_average_score(category_movies)

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

print (is_above_score(movies[0]))

print(get_above_score_movies(movies))

print(get_movies_by_category(movies, "Romance"))

print(calculate_average_score(movies))

print(calculate_average_score_by_category(movies, "Suspense"))