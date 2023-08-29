import time
import random
import numpy
from Library import TurnTable
from sshkeyboard import listen_keyboard



tt = TurnTable.TurnTable(verbose=True)
tt.position(0)
current_position = 0



while True:
    if keyboard.is_pressed("a"): current_position = current_position - 5
    if keyboard.is_pressed("s"): current_position = current_position + 5
    print('Current Posisition:', current_position)
    if keyboard.is_pressed("q"): break


# tt = TurnTable.TurnTable(verbose=True)
# locations = numpy.arange(-90, 90, 11)
#
# for i in range(20):
#     tt.position(0)
#     time.sleep(2)
#     x = random.randint(-180, 180)
#     tt.position(x)
#     time.sleep(0.5)
