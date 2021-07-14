-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT  g.name
       ,SUM(sr.rate) AS rating
FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg
ON g.id = sg.genre_id
INNER JOIN tv_show_ratings sr
ON sg.show_id = sr.show_id
GROUP BY  g.id
ORDER BY rating DESC;
