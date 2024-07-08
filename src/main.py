from graphics import Window, Point, Line, Cell
from maze import Maze

def main():
    win = Window(800, 600)
    
    # cellA = Cell(win)
    # cellA.has_top_wall = False
    # cellA.draw(405, 303, 505, 403)

    # cellB = Cell(win)
    # cellB.has_bottom_wall = False
    # cellB.draw(405, 203, 505, 303)

    # cellA.draw_move(cellB)

    maze = Maze(50, 50, 3, 5, 10, 10, win)

    win.wait_for_close()

main()