-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>.
-- First column must be called genre.
-- Second column must be called number_of_shows.
-- Results must be sorted in descending order by the number of shows linked.
SELECT genre.name,COUNT(*) AS number_of_shows
FROM genre INNER JOIN tv_show_genres ON gender.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.name ORDER BY number_of_shows DESC;
