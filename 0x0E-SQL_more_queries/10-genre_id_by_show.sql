-- lists all shows contained IN hbtn_0d_tvshows that have at least one genre linked.
SELECT  s.title
       ,sg.genre_id
FROM tv_shows AS s
RIGHT JOIN tv_show_genres AS sg
ON s.id = sg.show_id
ORDER BY s.title, sg.genre_id ASC;
