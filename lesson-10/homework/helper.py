import requests
import random

API_KEY = "e3fdfbb5ce95f70b6e5f693e68ac518e"
BASE_URL = "https://api.themoviedb.org/3"

genre_map = {
    "action": 28,
    "comedy": 35,
    "drama": 18,
    "sci-fi": 878,
    "romance": 10749,
    "horror": 27
}
genre = input("Enter a movie genre (action, comedy, drama, sci-fi, romance, horror): ").strip().lower()

if genre in genre_map:
    genre_id = genre_map[genre]
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
    
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json()['results']
        if movies:
            movie = random.choice(movies)
            print(f"We recommend you watch: {movie['title']} (Rating: {movie['vote_average']})")
        else:
            print("No movies found for this genre.")
    else:
        print("Failed to fetch data from API.")
else:
    print("Sorry, that genre is not supported.")

