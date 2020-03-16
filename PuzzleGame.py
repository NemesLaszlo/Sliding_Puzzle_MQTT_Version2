import os
import platform
import random
from tkinter import *
import Board
import xml.dom.minidom


class PuzzleGame:
    """
    Puzzle Game main object, with the game parameters, and methods.
    """

    def __init__(self, parent):
        """
        Constructor of the Puzzle Game, with
        a parent parameter, which is the root Tk() object.
        """
        self.parent = parent
        self.grid = 3  # 3x3 board game, for picture cutting.
        self.send_config_xml_to_broker()  # send the xml config file about this game to the mqtt broker.
        self.board = Frame(self.parent)
        self.start()

    def send_config_xml_to_broker(self):
        """
        Read the config xml, convert to string, and send it to the mqtt broker.
        """
        xmlObject = xml.dom.minidom.parse("config_setup.xml")
        pretty_xml_as_string = xmlObject.toprettyxml()
        print(pretty_xml_as_string)

    def pick_random_picture(self):
        """
        Pick a random picture from the project script path's picture folder.
        Return with the path of the picture.
        """
        path_project = os.path.dirname(os.path.realpath(__file__))
        system = platform.system()
        if system == 'Linux' or system == 'Darwin':
            path_pictures = path_project + "/pictures"
            return str(path_pictures + "/" + self.random_picture(path_pictures))
        elif system == 'Windows':
            path_pictures = path_project + "\\pictures"
            return str(path_pictures + "\\" + self.random_picture(path_pictures))

    def random_picture(self, place):
        """
        Pick a random picture from the directory of "place" parameter.
        Return with the picked file name with extension. For example: Picture.jpg
        """
        random_filename = random.choice([
            x for x in os.listdir(place)
            if os.path.isfile(os.path.join(place, x))
        ])
        return random_filename

    def start(self):
        """
        Start the game, Initialize the board and start.
        """
        image = self.pick_random_picture()
        grid = self.grid
        if os.path.exists(image):
            self.board = Board.Board(parent=self.parent, image=image, grid=grid, win=self.win)
            self.board.pack()

    def win(self, moves):
        """
        moves - parameter number of moves until the win.
        Handle the end of the game, write out the steps and the winning message,
        and start a new game with a new random picture.
        """
        self.board.pack_forget()
        win_text = ("You are win, with {0} moves.".format(moves))
        print(win_text)
        self.play_again()

    def play_again(self):
        """
        Restart the game.
        """
        self.start()
