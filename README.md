First, you'll have to create an account here and follow the instructions to get your API key.

The resulting product consists of two CSV files: "movies_list.csv" and "metadata.csv" with 15000 instances of movies sorted by popularity, the first 10000 being English movies and the last 5000 being Italian ones. I'll show you how to edit these settings, for example, to gather 1000 Spanish movies.

To run correctly, the script needs to be run in the following order:

movie list.py
This script generates 'movie_list.csv', the first part of the dataset which consists of genre_ids, id, original_language, overview, popularity, release_date, title, vote_average, and vote_count.

rows 6-10 is where you define your API and the movies you want to retrieve, following this format: 'language':number of movies
row 58 is where you can change the features selected for the database you are creating
meta data.py
This script requires as input an index of movie IDs, for example, the output of the previous script. Then, for each of those movies, it gathers the director, the top 5 most popular actors, and keywords. I implemented multithreading to speed up the code.
