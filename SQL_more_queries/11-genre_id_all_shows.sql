-- Retrieves each TV show's title and its associated genre ID, if available.
-- Uses a LEFT JOIN to include all TV shows, even those without a genre.
-- Orders results alphabetically by the show's title and by genre ID in ascending order within each title.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;