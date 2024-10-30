-- Retrieves the titles of TV shows along with their associated genre names.
-- Uses LEFT JOIN to include all TV shows, ensuring that those without genres are still listed.
-- Joins 'tv_shows' with 'tv_show_genres' to link each show to its genres.
-- Further joins with 'tv_genres' to access genre names based on genre IDs.
-- Orders the results first by TV show title in ascending order, and then by genre name in ascending order.

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;