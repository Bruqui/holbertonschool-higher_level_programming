-- Retrieves the titles of TV shows that do not have an associated genre.
-- Uses a LEFT JOIN to include all TV shows, ensuring those without genres are considered.
-- Filters results to show only shows with NULL in genre_id, indicating no genre association.
-- Orders results alphabetically by the show's title.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;