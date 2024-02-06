import math
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
#1
def above_5_5(m,movies):
    for movie in movies:
        if movie["name"]==m:
            return movie["imdb"]>5.5
    return False
m=input()
print(above_5_5(m, movies))
#2
def above_55(movie):
    return movie["imdb"]>5.5
for movie in movies:
    if above_55(movie):
        print(movie["name"])
#3
def in_category(c,movies):
    fm=[]
    for movie in movies:
        if movie["category"]==c:
            fm.append(movie)
    return fm
c=input()
cm=in_category(c,movies)
for movie in cm:
    print(movie["name"])
#4
def average_imdb_score(movies):
    total_score=0
    num_movies=len(movies)
    for movie in movies:
        total_score+=movie["imdb"]
    return total_score/num_movies
avg_score=average_imdb_score(movies)
print(avg_score)
#5
def avgscorecat(cat,movies):
    total_score = 0
    num_movies = 0
    for movie in movies:
        if movie["category"] == cat:
            total_score+=movie["imdb"]
            num_movies+=1
    return total_score/num_movies
cat=input()
avgscore=avgscorecat(cat,movies)
print(avgscore)