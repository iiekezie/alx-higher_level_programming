-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
-- lists all rows in a database linked to a row in another table
SELECT tv_genres.name, SUM(tv_shows.rating) AS rating_sum
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
