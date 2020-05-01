from tkinter import *
from PIL import Image, ImageTk
import Tiles

# maximum board size, it the picture is bigger we resize it to 500 x 500
MAX_BOARD_SIZE = 500


class Board(Frame):
    """
    Puzzle Game board object.
    Inherited from Frame.
    """

    def __init__(self, parent, image, grid, win, *args, **kwargs):
        """
        Constructor of the Board.
        """
        Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.grid = grid  # board grid size
        self.win = win  # win method
        self.image = self.open_image(image)
        self.tile_size = self.image.size[0] / self.grid  # cut picture part size -> tile
        self.tiles = self.create_tiles()
        self.tiles.suffle()
        self.tiles.show()
        self.bind_keys()

    def open_image(self, image):
        """
        image - picture file path.
        Open the image, resize it, and crop it.
        Return with the resized or cropped image.
        """
        image = Image.open(image)
        if min(image.size) > MAX_BOARD_SIZE:
            image = image.resize((MAX_BOARD_SIZE, MAX_BOARD_SIZE), Image.ANTIALIAS)
        if image.size[0] != image.size[1]:
            image = image.crop((0, 0, image.size[0], image.size[0]))
        return image

    def create_tiles(self):
        """
        Create tiles from the good sized of image.
        Return with a Tiles object, which has a list of the image tiles - Tile object.
        """
        tiles = Tiles.Tiles(grid=self.grid)
        for row in range(self.grid):
            for col in range(self.grid):
                x0 = col * self.tile_size
                y0 = row * self.tile_size
                x1 = x0 + self.tile_size
                y1 = y0 + self.tile_size
                tile_image = ImageTk.PhotoImage(self.image.crop((x0, y0, x1, y1)))
                tile = Tiles.Tile(self, tile_image, (row, col))
                tiles.add(tile)
        return tiles

    def bind_keys(self):
        """
        Bind the number buttons for the changes.
        Pick two picture part, which going to swap.
        """
        for i in range(10):
            self.bind_all(str(i), self.slide)

    def slide(self, event):
        """
        Handle the number keys, and check the current situation -> finished, and win or net.
        And handle the counter of the moves to the win.
        """

        # self.client.subscribe("devices/11:22:44:55/inbox/User1/function/0")
        # self.client.subscribe("devices/11:22:44:55/inbox/User1/function/1")
        # self.client.subscribe("devices/11:22:44:55/inbox/User1/function/2")
        # self.client.subscribe("devices/11:22:44:55/inbox/User1/function/3")
        # self.client.subscribe("devices/11:22:44:55/inbox/User1/function/4")
        # self.client.subscribe("devices/11:22:44:55/inbox/User1/function/5")
        # self.client.subscribe("devices/11:22:44:55/inbox/User1/function/6")
        # self.client.subscribe("devices/11:22:44:55/inbox/User1/function/7")
        # self.client.subscribe("devices/11:22:44:55/inbox/User1/function/8")

        self.tiles.slide_parameters(event.keysym)
        if self.tiles.is_correct():
            self.win(self.tiles.moves)
