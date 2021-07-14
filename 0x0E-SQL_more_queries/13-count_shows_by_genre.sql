-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>.
-- First column must be called genre.
-- Second column must be called number_of_shows.
-- Results must be sorted in descending order by the number of shows linked.
SELECT tv_genres.name AS 'genre' , COUNT(*) AS 'number_of_shows'
FROM tv_genders INNER JOIN tv_show_genres
ON tv_genders.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
