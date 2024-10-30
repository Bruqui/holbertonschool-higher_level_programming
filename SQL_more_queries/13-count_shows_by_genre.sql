-- Retrieves the names of genres and the count of TV shows associated with each genre.
-- Uses a LEFT JOIN to include all genres, ensuring that those with no associated shows are considered.
-- Groups results by genre name to aggregate the count of shows.
-- Filters results to show only genres that have at least one associated show.
-- Orders results in descending order based on the number of shows for each genre.

SELECT genres_name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genres
LEFT JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.name
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;