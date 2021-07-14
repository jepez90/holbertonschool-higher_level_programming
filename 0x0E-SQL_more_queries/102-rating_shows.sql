--  lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT  s.title
       ,SUM(sr.rate) AS rating
FROM tv_shows s
INNER JOIN tv_show_ratings sr
ON s.id = sr.show_id
GROUP BY  s.id
ORDER BY rating DESC;
