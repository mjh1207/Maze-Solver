from graphics import Window, Point, Line, Cell

def main():
    win = Window(800, 600)
    
    cell = Cell(win)
    cell.has_right_wall = False
    cell.draw(200, 300, 50, 100)
    win.wait_for_close()

main()