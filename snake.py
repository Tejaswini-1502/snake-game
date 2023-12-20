from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("green")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segments[-1].position()) # adding new segment at the last position of the snake

    def move(self):
        # moving the 3rd seg to 2nd seg's position ; 2nd seg to 1st seg's position
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        # moving the 1st seg by MOVE_DISTANCE
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:  # when the snake is moving up it can't go down
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:   # when the snake is moving down it can't go up
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:  # when the snake is moving left it can't go right
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:   # when the snake is moving right it can't go left
            self.head.setheading(RIGHT)