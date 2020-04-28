"""Functions!

"""

$ day = 1
$ price = 100
$ time = 1
$ someVar = 0
$ money = 100

# this is a dictionary that is holding some common items a blacksmith would sell and their prices.
items = {
        'hammer': 500,
        'axe': 350,
        'plow': 1000
         }


def Sell(price, discount):
    price = price - discount*price
    return money + price

money += Sell(items('hammer'), .6)

$ one = 5 + 2 # no, 1 does not equal 5+2. 1=5+2 does not work.
$ chair = 2  # 2 does not equal chair, 2 is the value being stored in chair

label daily
    time++
    menu:
        if time == 2 :"What do you want to do this morning"
        else: "What do you want to do tonight?"

        "Eat":
            jump eat
        "Work":
            jump work
        "Explore":
            jump explore


# label Night
#     time = 1
#     menu:
#         "What do you want to do tonight Brain?"
#
#         "Eat":
#             jump eat
#         "Work":
#             jump work
#         "Explore":
#             jump explore


label TM
    if day => 30:
        jump end
    else:
        if time => 3:
            time = 1
            day++
            jump daily
        else:
            jump daily

label end
    "You lose."
    "Sorry."
    "But there was no way to win."
    "Kinda a waste huh?"
    "But that's life ain't it?"
    "It's not?"
    "Good for you."
