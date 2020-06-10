import random
from tkinter import *


class Tiles:
    """
    Tiles object with the cropped picture parts -> tiles in list.
    """

    def __init__(self, grid):
        """
        Constructor of the Tiles.
        """
        self.tiles = []
        self.grid = grid
        self.moves = 0

        # we need two ids for the swap of the two positions of the picked tiles
        self.swap_event_counter = 0  # counter for the swap
        self.part1 = -1  # first tile part for the swap event
        self.part2 = -1  # second tile part for the swap event

    def add(self, tile):
        """
        tile - parameter, part of the picture.
        Add tile - picture element part to the list.
        """
        self.tiles.append(tile)

    def get_tile(self, pos_in_list):
        """
        pos_in_list - picture part position in the list.
        Get the actual tile, with this position (in tiles list) parameter.
        Return this Tile object.
        """
        for tile in self.tiles:
            if tile.position_in_list == pos_in_list:
                return tile

    def change_tiles(self, first_tile, sec_tile):
        """
        first_tile - parameter first int id -> position of the picture part in the list
        sec_tile - parameter second int id -> position of the picture part in the list
        first_tile - sec_tile this two picture part going to swap.
        """
        t1 = self.get_tile(first_tile)  # get the first Tile object.
        t2 = self.get_tile(sec_tile)  # get the second Tile object.
        t1.pos, t2.pos = t2.pos, t1.pos  # position swap
        t1.position_in_list, t2.position_in_list = t2.position_in_list, t1.position_in_list  # position swap, tiles list position.
        self.moves += 1  # moves counter until the win.
        print("-------------------")
        if self.swap_event_counter == 2:
            self.show()
            self.swap_event_counter = 0

    def slide_parameters(self, key):
        """
        Handle the information of the picked picture parts, and call the change_tiles.
        """
        try:
            if 0 <= int(key) <= 8 and self.swap_event_counter == 0:
                self.part1 = int(key)
                self.swap_event_counter += 1
                # print(self.swap_event_counter)
            elif 0 <= int(key) <= 8 and self.swap_event_counter < 2:
                self.part2 = int(key)
                self.swap_event_counter += 1
                # print(self.swap_event_counter)
                if self.swap_event_counter == 2:
                    # print("swap call")
                    self.change_tiles(self.part1, self.part2)
        except:
            pass

    def suffle(self):
        """
        Shuffle the picture parts - tiles. To play the game.
        Set up the list position (tiles list).
        """
        random.shuffle(self.tiles)
        i = 0
        for row in range(self.grid):
            for col in range(self.grid):
                self.tiles[i].pos = (row, col)
                i += 1
        # set up the list position, to the list position swap.
        position_counter = 0
        for tile in range(len(self.tiles)):
            self.tiles[tile].position_in_list = position_counter
            position_counter += 1

    def show(self):
        """
        Game visualization.
        """
        for tile in self.tiles:
            print("pos: " + str(tile.pos) + " good_pos: " + str(tile.good_pos))
            tile.show()

    def is_correct(self):
        """
        Check the win period, the picture part - tile is in the good position or not.
        Return logical values.
        """
        for tile in self.tiles:
            if not tile.is_correct_pos():
                return False
        return True


class Tile(Label):
    """
    Tile object.
    Inherited from label.
    """

    def __init__(self, parent, image, pos):
        """
        Constructor of the Tile.
        """
        Label.__init__(self, parent, image=image)
        self.image = image
        self.pos = pos
        self.good_pos = pos
        self.position_in_list = -1  # list position id (tiles list)

    def show(self):
        """
        Game visualization. Tile visualize.
        """
        self.grid(row=self.pos[0], column=self.pos[1])

    def is_correct_pos(self):
        """
        Tile position check, fot the win check.
        """
        return self.pos == self.good_pos
