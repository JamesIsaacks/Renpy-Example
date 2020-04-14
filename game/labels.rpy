"""
    Labels Example

    James Isaacks
    April 14th, 2020
"""

define t = Character("Crash", color="#FFCC00")
define tt = Character("Dummy", color="#00FF00")
$ crash = 0
$ dummy = 0

# Series of Test Labels
label Test
    # This is a self contained piece of the game.
    t "I'm a dummy!"
    tt "No you dummy, I'm Dummy!"

    menu:
        "Who's the dummy?"

        "Crash":
            crash++
            jump crashTest(crash)
        "Dummy":
            jump dummyTest

# Test Crash
label crashTest(crash)


# Test Dummy
label dummyTest(dummy)
