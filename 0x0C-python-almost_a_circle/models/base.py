#!/usr/bin/python3
"""
This is a class
"""
import turtle


class Base:
    """
    This is a class
    """
    __nb_objects = 0

    def __init__(self, id=None):

        Base.__nb_objects = Base.__nb_objects + 1

        if id is None:
            self.id = Base.__nb_objects
        else:
            self.id = id

    def load_from_file(cls):(cls, list_objs):  
        '''Just filling up some space'''
        pass

    def save_to_file_csv(cls, list_objs):  
        '''Just filling up some space'''
        pass

    def load_from_file_csv(cls): 
        '''Just filling up some space'''
        pass

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''Just filling up some space'''
        turtle.setup(width=800, height=600)
        for rect in list_rectangles:
            turtle.penup()
            turtle.setpos(rect.x, rect.y)
            turtle.pendown()
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.left(90)
                turtle.forward(rect.height)
                turtle.left(90)
            turtle.end_fill()
        for square in list_squares:
            turtle.penup()
            turtle.setpos(square.x, square.y)
            turtle.pendown()
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(square.side)
                turtle.left(90)
            turtle.end_fill()
        turtle.exitonclick()
