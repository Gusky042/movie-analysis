
import pandas as pd

print("=" * 50)
print("🎬 MY MOVIE ANALYSIS PROJECT")
print("=" * 50)

# Load our movie data
print("\n📀 Loading movies.csv...")
movies = pd.read_csv('movies.csv')


print("\n✅ Here's our movie data:")
print(movies.to_string())

# Let's add this after the code above:

print("\n" + "=" * 50)
print("📊 UNDERSTANDING OUR DATA")
print("=" * 50)

# How many movies do we have?
print(f"\n📌 Total movies: {len(movies)}")

# What columns do we have?
print(f"\n📌 Columns: {list(movies.columns)}")

# the first movie?
print(f"\n📌 First movie:")
print(movies.iloc[0])

print("\n" + "=" * 50)
print("🎯 ANSWERING QUESTIONS")
print("=" * 50)

# QUESTION 1: What's the highest rated movie?
print("\n1️⃣ What's the highest rated movie?")

# Find the highest rating
highest_rating = movies['rating'].max()
print(f"   Highest rating: {highest_rating}")

# Find which movie has that rating
best_movie = movies[movies['rating'] == highest_rating]
print(f"   Best movie(s):")
print(best_movie[['title', 'rating']])

# QUESTION 2: What's the average rating of all movies?
print("\n2️⃣ What's the average rating?")
avg_rating = movies['rating'].mean()
print(f"   Average rating: {avg_rating:.2f}")

# QUESTION 3: Which year had the most movies?
print("\n3️⃣ Which year had the most movies?")
year_counts = movies['year'].value_counts()
print(year_counts)
print(f"\n   Most movies in: {year_counts.index[0]} ({year_counts.values[0]} movies)")

# QUESTION 4: Who directed the most movies?
print("\n4️⃣ Who directed the most movies?")
director_counts = movies['director'].value_counts()
print(director_counts)
print(f"\n   Most movies by: {director_counts.index[0]} ({director_counts.values[0]} movies)")


# Let's see the first 3 movies
print(f"\n📌 First 3 movies:")
print(movies.head(3))

print("\n" + "=" * 50)
print("🔍 FINDING SPECIFIC MOVIES")
print("=" * 50)

# Find all movies from 1994
print("\n📅 Movies from 1994:")
movies_1994 = movies[movies['year'] == 1994]
print(movies_1994[['title', 'year', 'director', 'rating']])

# Find movies with rating above 8.5
print("\n⭐ Movies rated above 8.5:")
high_rated = movies[movies['rating'] > 8.5]
print(high_rated[['title', 'rating']])

# Find movies directed by Christopher Nolan
print("\n🎬 Movies by Christopher Nolan:")
nolan_movies = movies[movies['director'] == 'Christopher Nolan']
print(nolan_movies[['title', 'year', 'rating']])

# Find movies with budget less than 50 million
print("\n💰 Low budget movies (< 50 million):")
low_budget = movies[movies['budget_millions'] < 50]
print(low_budget[['title', 'budget_millions']])

print("\n" + "=" * 50)
print("➕ ADDING NEW COLUMNS")
print("=" * 50)

# Let's add a column that tells us if the movie is a blockbuster
# Blockbuster = budget > 100 million
movies['is_blockbuster'] = movies['budget_millions'] > 100
print("\n🎬 Added 'is_blockbuster' column:")
print(movies[['title', 'budget_millions', 'is_blockbuster']])

# Let's add a rating category
def rating_category(rating):
    if rating >= 9:
        return "Masterpiece"
    elif rating >= 8:
        return "Excellent"
    elif rating >= 7:
        return "Good"
    else:
        return "Average"

movies['rating_category'] = movies['rating'].apply(rating_category)
print("\n📊 Added 'rating_category' column:")
print(movies[['title', 'rating', 'rating_category']])

print("\n" + "=" * 50)
print("📊 GROUPING AND SUMMARIZING")
print("=" * 50)

# Average rating by director
print("\n🎬 Average rating by director:")
avg_by_director = movies.groupby('director')['rating'].mean().sort_values(ascending=False)
print(avg_by_director)

# How many movies per rating category
print("\n📊 Movies by rating category:")
category_counts = movies['rating_category'].value_counts()
print(category_counts)

# Average budget by rating category
print("\n💰 Average budget by rating category:")
budget_by_category = movies.groupby('rating_category')['budget_millions'].mean()
print(budget_by_category)

print("\n" + "=" * 50)
print("💾 SAVING OUR RESULTS")
print("=" * 50)

# Save our analysis to a new file
movies.to_csv('movies_with_analysis.csv', index=False)
print("\n✅ Saved to 'movies_with_analysis.csv'")

# Save top movies list
top_movies = movies.nlargest(5, 'rating')
top_movies.to_csv('top_movies.csv', index=False)
print("✅ Saved top 5 movies to 'top_movies.csv'")

# Create a summary file
with open('movie_summary.txt', 'w') as f:
    f.write("MOVIE ANALYSIS SUMMARY\n")
    f.write("=" * 50 + "\n\n")
    f.write(f"Total movies: {len(movies)}\n")
    f.write(f"Average rating: {movies['rating'].mean():.2f}\n")
    f.write(f"Best movie: {movies.loc[movies['rating'].idxmax(), 'title']} ({movies['rating'].max()})\n")
    f.write(f"Worst movie: {movies.loc[movies['rating'].idxmin(), 'title']} ({movies['rating'].min()})\n")
    f.write(f"Most productive director: {director_counts.index[0]} ({director_counts.values[0]} movies)\n")

print("✅ Saved summary to 'movie_summary.txt'")