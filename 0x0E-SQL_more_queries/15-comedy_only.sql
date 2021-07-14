-- lists all Comedy shows IN the database hbtn_0d_tvshows.
SELECT s.title
FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg
ON g.id = sg.genre_id
INNER JOIN tv_shows AS s
ON sg.show_id = s.id
WHERE g.name = 'Comedy'
ORDER BY title asc;
