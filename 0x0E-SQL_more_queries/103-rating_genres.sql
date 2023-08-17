-- script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
--   Each record should display: tv_genres.name - rating sum
--   Results must be sorted in descending order by their rating

SELECT tv_genres.name, SUM(tv_show_ratings.rate) rating
FROM tv_show_ratings
INNER JOIN tv_genres
INNER JOIN tv_show_genres 
ON tv_show_genres.show_id=tv_show_ratings.show_id 
AND tv_genres.id=tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
