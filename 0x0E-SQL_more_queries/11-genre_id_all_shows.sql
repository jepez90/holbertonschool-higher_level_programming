-- lists all shows contained IN the database hbtn_0d_tvshows.
SELECT  s.title
       ,sg.genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS sg
ON s.id = sg.show_id
ORDER BY s.title, sg.genre_id ASC;
