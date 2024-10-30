-- Retrieves each TV show's title and its associated genre ID.
-- Joins 'tv_shows' with 'tv_show_genres' on matching TV show IDs to link each show to its genres.
-- Orders results alphabetically by title and, for each title, by genre ID in ascending order.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
