-- Retrieves the names of genres and the count of TV shows associated with each genre.
-- Uses a LEFT JOIN to include all genres, ensuring that those with no associated shows are considered.
-- Groups results by genre name to aggregate the count of shows.
-- Filters results to show only genres that have at least one associated show.
-- Orders results in descending order based on the number of shows for each genre.

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC, tv_genres.id ASC;