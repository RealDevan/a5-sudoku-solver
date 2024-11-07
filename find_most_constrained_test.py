import a5

# sets of moves for the different games
first_moves = [
    (0, 1, 7),
    (0, 7, 1),
    (1, 2, 9),
    (1, 3, 7),
    (1, 5, 4),
    (1, 6, 2),
    (2, 2, 8),
    (2, 3, 9),
    (2, 6, 3),
    (3, 1, 4),
    (3, 2, 3),
    (3, 4, 6),
    (4, 1, 9),
    (4, 3, 1),
    (4, 5, 8),
    (4, 7, 7),
    (5, 4, 2),
    (5, 6, 1),
    (5, 7, 5),
    (6, 2, 4),
    (6, 5, 5),
    (6, 6, 7),
    (7, 2, 7),
    (7, 3, 4),
    (7, 5, 1),
    (7, 6, 9),
    (8, 1, 3),
    (8, 7, 8),
]

second_moves = [
    (0, 1, 2),
    (0, 3, 3),
    (0, 5, 5),
    (0, 7, 4),
    (1, 6, 9),
    (2, 1, 7),
    (2, 4, 4),
    (2, 7, 8),
    (3, 0, 1),
    (3, 2, 7),
    (3, 5, 9),
    (3, 8, 2),
    (4, 1, 9),
    (4, 4, 3),
    (4, 7, 6),
    (5, 0, 6),
    (5, 3, 7),
    (5, 6, 5),
    (5, 8, 8),
    (6, 1, 1),
    (6, 4, 9),
    (6, 7, 2),
    (7, 2, 6),
    (8, 1, 4),
    (8, 3, 8),
    (8, 5, 7),
    (8, 7, 5),
]
#Create a sudoku board.
b = a5.Board()
#Place the 28 assignments in first_moves on the board.
for trip in first_moves:
    b.rows[trip[0]][trip[1]] = trip[2]
#NOTE - the above code only *puts* the numbers on the board, but doesn't
#   do the work that update does (remove numbers from other lists, etc).

#I'm going to now alter 3 lists on the board to make them shorter (more
#   constrained. 
a5.remove_if_exists(b.rows[0][0], 8)
a5.remove_if_exists(b.rows[0][0], 7)
a5.remove_if_exists(b.rows[0][0], 3)
a5.remove_if_exists(b.rows[0][0], 2)
a5.remove_if_exists(b.rows[4][8], 8)
a5.remove_if_exists(b.rows[4][8], 1)
a5.remove_if_exists(b.rows[4][8], 2)
a5.remove_if_exists(b.rows[4][8], 3)
a5.remove_if_exists(b.rows[4][8], 4)
a5.remove_if_exists(b.rows[6][7], 2)
a5.remove_if_exists(b.rows[6][7], 3)
a5.remove_if_exists(b.rows[6][7], 5)
a5.remove_if_exists(b.rows[6][7], 6)
#we removed 5 items from positions (4,8) so that should now be the most
#  constrained.
assert b.find_most_constrained_cell() == (4,8), "find most constrained cell test 1"