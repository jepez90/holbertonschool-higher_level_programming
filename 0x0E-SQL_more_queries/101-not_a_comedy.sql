-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT  title
FROM tv_shows s
WHERE s.id NOT IN (
    SELECT s.id
    FROM tv_genres AS g
    INNER JOIN tv_show_genres AS sg
    ON g.id = sg.genre_id
    INNER JOIN tv_shows AS s
    ON sg.show_id = s.id
    WHERE g.name = 'Comedy'
    )
ORDER BY title ASC;
