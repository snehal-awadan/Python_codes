# Assign : 15
# Q.2)



def process_movie_data(movie_data):
    movies_released_2018 = []
    movies_in_pune = []

    for movie in movie_data:
        parts = movie.split(",")
        if len(parts) == 6:
            if parts[2].strip() == 2018:
                 movies_released_2018.append(parts[2])
            if parts[5].strip() == "pune":
                movies_in_pune.append(movie)
    return movies_released_2018,movies_in_pune

movie_data = []

print("Enter movie data in the following format only: id,name,year,actor/actress, mobile_no,city")
while True:
    movie = input("Enter movie data: ")
    if movie.lower() =="end":
        break
    movie_data.append(movie)

movies_released_2018, movies_in_pune = process_movie_data(movie_data)

print("Movies released in 2018: ")
for movie in movies_released_2018:
    print(movie)

print("Movies released in Pune: ")
for movie in movies_in_pune:
    print(movie)
