import time
import random
import numpy
from Library import TurnTable
from sshkeyboard import listen_keyboard


class TableController:
    def __init__(self, start=0):
        self.tt = TurnTable.TurnTable(verbose=True)
        self.current_position = start
        self.tt.position(self.current_position, block=True)


    def update_position(self, delta):
        self.current_position += delta
        print('Current position:', self.current_position)
        self.tt.position(self.current_position, block=True)



if __name__ == "__main__":

    controller = TableController()
    def press(key):
        print(key)
        if key == '4': controller.update_position(-5)
        if key == '6': controller.update_position(5)
        if key == '1': controller.update_position(-10)
        if key == '3': controller.update_position(10)

    def release(key):
        time.sleep(0.5)


    listen_keyboard(on_press=press,
                    on_release=release)





