-- lists all genres FROM hbtn_0d_tvshows AND displays the number of shows linked to each.
SELECT  g.name      AS genre
       ,COUNT(g.id) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg
ON g.id = sg.genre_id
INNER JOIN tv_shows AS s
ON sg.show_id = s.id
GROUP BY  g.id
ORDER BY number_of_shows DESC;
