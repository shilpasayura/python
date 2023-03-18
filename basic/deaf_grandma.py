

# Unless you shout (all uppercase letters) grandma can't hear you.
# If you say BYE Grandma pretends not to hear you because she
# doesn't want you to leave.  You must repeat BYE three times
# before you can leave.

import random

bye_count = 0

while bye_count < 3: 
    statement = input( )

    # Grandma doesn't want you to leave.
    if statement == "BYE":
        bye_count = bye_count + 1
        print("(Pretends not to hear you.)")

    # Grandma can only hear you if you shout.
    elif statement == statement.upper( ):
        bye_count = 0
        print(f"NO, NOT SINCE {random.randrange(1930, 1952)}.")

    # Grandma can't hear you if you don't shout.
    else:
        print("HUH? SPEAK UP SONNY!")
        bye_count = 0
