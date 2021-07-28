# 15puzzle
Program to solve the (n*n)-1 puzzle

I used A* search to solve this problem. It's similar to a simple BFS, but with an added "heuristic" mechanism so that 
the distance of the "breadth" is defined by both A) how many moves you've made away from the starting position, and B) how far the result is to the solved state of the board. The hope here is that this will steer the search towards the solved state a little faster. 

This algorithm makes sense for this problem because there's a very intuitive way to measure how far a given board is from the solved state. For each tile, sum up how far that tile is from where it needs to be. It's not a perfect metric, but it's enough to speed up the search. 

As is, the program can solve the 2x2 and 3x3 case of the game quickly, but takes more than a few minutes to solve the 4x4. My bet is that the proximity to solved state function gets stuck in local minimas too easily. That would happen when many pieces are in their proper places, and then "trap" the last few pieces from moving to their spots. 

### Features to improve performance:S
- Make the h_dist heuristic more sophisticated to avoid local minimas. A good patch would be to assign a higher value to solving pieces around the edges first, preventing the "trapped" pieces issue. 
- General python prettiness: there's definitely places where list comprehensions and things could improve code quality. Just me out of practice. 

'''