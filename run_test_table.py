import time
import random
import numpy

from Library import TurnTable

tt = TurnTable.TurnTable(verbose=True)
tt.velocity = 100

locations = numpy.arange(-90, 90, 11)

for i in range(20):
    tt.position(0)
    time.sleep(2)
    x = random.randint(-180, 180)
    tt.position(x)
    time.sleep(0.5)
