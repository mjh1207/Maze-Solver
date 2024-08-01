from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed...")
    
    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Line:
    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB
    
    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.pointA.x, self.pointA.y, self.pointB.x, self.pointB.y, fill=fill_color, width=2
        )

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        # left line
        line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        self._win.draw_line(line, "black" if self.has_left_wall else "white")
        #top line
        line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        self._win.draw_line(line, "black" if self.has_top_wall else "white")
        #right line
        line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        self._win.draw_line(line, "black" if self.has_right_wall else "white")
        #bottom line
        line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        self._win.draw_line(line, "black" if self.has_bottom_wall else "white")

    def draw_move(self, to_cell, undo=False):
        color = "red" if not undo else "gray"
        cur_center = Point((self._x2 + self._x1) / 2, (self._y2 + self._y1) / 2)
        dest_center = Point((to_cell._x2 + to_cell._x1) / 2, (to_cell._y2 + to_cell._y1) / 2)
        self._win.draw_line(Line(cur_center, dest_center), color)