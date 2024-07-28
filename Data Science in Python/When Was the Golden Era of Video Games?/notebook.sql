-- best_selling_games
SELECT * 
FROM game_sales
ORDER BY games_sold DESC
LIMIT 10;

-- critics_top_ten_years
SELECT g.year, COUNT(g.name) AS num_games, ROUND(AVG(r.critic_score), 2) AS avg_critic_score
FROM game_sales AS g
INNER JOIN reviews AS r
ON g.name = r.name
GROUP BY g.year
HAVING COUNT(g.name) >=4
ORDER BY avg_critic_score DESC

-- golden_years
SELECT u.year, u.num_games, c.avg_critic_score, u.avg_user_score, c.avg_critic_score - u.avg_user_score AS diff
FROM users_avg_year_rating AS u
INNER JOIN critics_avg_year_rating AS c
ON c.year = u.year
WHERE avg_critic_score> 9 OR avg_user_score > 9
ORDER BY year
