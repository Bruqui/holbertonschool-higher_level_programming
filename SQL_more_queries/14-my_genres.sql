-- Retrieves the names of genres associated with the TV show titled 'Dexter'.
-- Joins the 'tv_shows' table with 'tv_show_genres' to link shows with their genres.
-- Further joins with 'tv_genres' to access genre names based on genre IDs.
-- Filters results to include only the genres for the specified TV show title 'Dexter'.
-- Orders the results alphabetically by genre name in ascending order.

SELECT tv_genres.name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name