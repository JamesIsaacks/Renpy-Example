"""
    Renpy Example for GAME 1303
    James D. Isaacks
    San Jacinto College South
    April 9th, 2020

    script.rpy initializes the Ren'py project. This project will explore several key features of Ren'py. It will also
    cover a number of basic programming concepts such as functions, loops, ect.

"""

# Defining a couple of characters to start with. In this example we will use the student as our MC.
define T = Character("Tears")
define R = Character("Recet")

# Define images here. This may only be an initial set of images. Images can be defined in seperate files as well.


# Initialize python internally to define some functions for future use:
init python:

    # This is just an example math function that does a common problem.
    #def pythagorean (self, a: int, b: int) -> float:
        # c^2 = a^2 + b^2
        #c = a^2 + b^2
        # return the hypotenuse of a triangle.
        #return sqrt(c)

    # This would print 13
    #print pythagorean (5, 12)

    # This is our common buy function
    def buy (self, item, cost):


# The game starts here:
label start:


# Setting up some label functions

# Buy menu label
label buyMenu ():
    # Present a category menu to the user
    # Menu items call a common buy function
    menu:
        "Weapons":
            call buyList ('weapons')
        "Armor":
            call buyList ('armor')
        "Magic":
            call buyList ('magic')
        "Items":
            call buyList ('items')

# Sell menu label
label sellMenu ():
    #

# buyList pulls only items of a given category from a given shop inventory
label buyList (category, shop):
    # Show a menu of the items in the shop's inventory that match the given category
