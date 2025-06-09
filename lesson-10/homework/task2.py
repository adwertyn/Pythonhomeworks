import random
import requests

main_url = "https://api.themoviedb.org/3"
api_key = 'e3fdfbb5ce95f70b6e5f693e68ac518e'
genre_map = {
    'action': 28,
'comedy': 35,
'drama': 18,
'history': 36,
'horror': 27,
'romance': 10749,
'sci-fi': 878,
}
movie_genre = input("Enter genre(action, comedy, drama, history, horror, romance, sci-fi): ").lower()
if movie_genre in genre_map:
    genre_id = genre_map[movie_genre]
    url = f"{main_url}/discover/movie?api_key={api_key}&with_genres={genre_id}"
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json()['results']
        if movies:
            movie = random.choice(movies)
            print(f"We recommend you watch: {movie['title']} (Rating: {movie['vote_average']})")
        else:
            print("No movies found for this genre.")
    else:
        print('Failed to get data')
    
else:
    print("Sorry, that genre is not supported.")

