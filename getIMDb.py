import imdb
import pandas as pd

# Create an instance of the IMDb class
ia = imdb.IMDb()

# Read the input CSV file
input_csv = 'BelcourtHistoryDatabase2010-2025.csv'  # Path to your input CSV file
df = pd.read_csv(input_csv, header=None, names=["Year", "Title"])

# Create an empty list to store the movie data
movie_data = []

# Iterate through the movie titles in the DataFrame
for index, row in df.iterrows():
    original_year = row['Year']
    original_title = row['Title']
    
    
    try:
        # Search for the movie on IMDb
        print(f"Searching for: {original_title} ({original_year})")  # Debug print
        search_results = ia.search_movie(original_title)
        
        if not search_results:
            print(f"No results found for {original_title}")
            movie_data.append([original_year, original_title, '', '', '', '', '', '', '', '', '', ''])
            continue

        valid_movie = None
        for movie in search_results:
            if movie.get('year') and movie['year'] <= original_year:
                valid_movie = movie
                break  # Take the first valid match
        
        if valid_movie:
            ia.update(valid_movie)
            
            imdb_title = valid_movie.get('title', '')
            imdb_year = valid_movie.get('year', '')
            imdb_director = ', '.join([director['name'] for director in valid_movie.get('directors', [])])
            imdb_cast = ', '.join([actor['name'] for actor in valid_movie.get('cast', [])[:4]])  # Get top 4 actors
            imdb_country = ', '.join(valid_movie.get('countries', []))
            imdb_certification = ', '.join(valid_movie.get('certificates', []))  # May contain multiple ratings per country
            imdb_genre = ', '.join(valid_movie.get('genres', []))
            imdb_runtime = ', '.join(map(str, valid_movie.get('runtimes', [])))  # Convert runtime to string
            imdb_plot_outline = valid_movie.get('plot outline', '')
            imdb_poster_url = valid_movie.get('cover url', '')
            imdb_url = f"https://www.imdb.com/title/tt{valid_movie.movieID}/"

            movie_data.append([
                original_year, original_title, imdb_title, imdb_year, imdb_director, imdb_cast, 
                imdb_country, imdb_certification, imdb_genre, imdb_runtime, imdb_poster_url, imdb_plot_outline, imdb_url
            ])
        else:
            print(f"No valid release year match for {original_title}")
            movie_data.append([original_year, original_title, '', '', '', '', '', '', '', '', '', '', ''])
    
    except Exception as e:
        print(f"Error processing movie: {original_title}. Error: {str(e)}")
        movie_data.append([original_year, original_title, 'Error', 'Error', 'Error', 'Error', 'Error', 'Error', 'Error', 'Error', 'Error', 'Error', 'Error'])

# Create a DataFrame with the collected movie data
output_df = pd.DataFrame(movie_data, columns=[
    "Year", "Title", "IMDb Title", "IMDb Year", "Director", "Cast", "Country", 
    "Certification", "Genre", "Runtime", "Poster URL", "Plot Outline", "IMDb URL"
])

# Write the results to a new CSV file
output_csv = 'movies_with_imdb_data2010-2025.csv'
output_df.to_csv(output_csv, index=False)

print(f"Data has been saved to {output_csv}")
