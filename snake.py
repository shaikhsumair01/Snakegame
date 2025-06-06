from turtle import Turtle
STARTING_POSITIONS =[(0,0), (-20,0),(-40,0)]
Move_distance = 20
Up = 90
down= 270
left = 180
right= 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def snake_reset(self):
        for seg in self.segments:
            seg.goto(10000, 100000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(Move_distance)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(Up)
    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(down)
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)