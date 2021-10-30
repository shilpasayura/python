#find program folders

import os
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
print(game_folder)
