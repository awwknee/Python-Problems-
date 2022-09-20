"""
CISC 131 Problem 1 - Ani Lamichhane (lami5034) and Logan Schorn (scho6370)
"""

import math

def main():
    print("Calculate the area of a triangle, rectangle, or circle?", end="")
    shape = input()
    if shape == "triangle":
        print("What is the base:", end="")
        base = float(input())
        print("What is the height:", end="")
        height1 = float(input())
        print("The area of the trinagle is {:.3f}".format(areaOfTriangle(base, height1)))
    elif shape == "circle":
        print("What is the radius:", end="")
        radius = float(input())
        print("The area of the circle is {:.3f}".format(areaOfCircle(radius)))
    elif shape == "rectangle":
        print("What is the width:", end="")
        width = float(input())
        print("What is the height height:", end="")
        height2 = float(input())
        print("The area of the circle is {:.3f}".format(areaOfRectangle(width, height2)))
    else:
        print("Not a shape.")

def areaOfTriangle(base, height1):
    areatriangle = (base * height1)/2
    return areatriangle
def areaOfCircle(radius):
    areacircle = (math.pi * (radius)**2)
    return areacircle
def areaOfRectangle(width, height2):
    arearectangle = width * height2
    return arearectangle
main()
