-- Retrieves the titles of TV shows that are classified under the 'Comedy' genre.
-- Joins the 'tv_shows' table with 'tv_show_genres' to link shows to their genres.
-- Further joins with 'tv_genres' to filter based on genre names.
-- Filters results to include only shows that belong to the 'Comedy' genre.
-- Orders the results alphabetically by the show's title in ascending order.

SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;