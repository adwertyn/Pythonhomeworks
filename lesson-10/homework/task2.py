import random

movies_by_genre = {
    "action": ["Mad Max: Fury Road", "John Wick", "Die Hard", "Gladiator"],
    "comedy": ["The Hangover", "Superbad", "Step Brothers", "Groundhog Day"],
    "drama": ["The Shawshank Redemption", "Forrest Gump", "Fight Club", "The Godfather"],
    "sci-fi": ["Inception", "The Matrix", "Interstellar", "Blade Runner 2049"],
}

genre = input("Enter a movie genre (action, comedy, drama, sci-fi, romance, horror): ").strip().lower()

if genre in movies_by_genre:
    movie = random.choice(movies_by_genre[genre])
    print(f"We recommend you watch: {movie}")
else:
    print("Sorry, we don't have recommendations for that genre.")
