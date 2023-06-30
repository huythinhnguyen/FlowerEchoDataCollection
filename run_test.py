from Library import TurnTable
from Library import Sonar
import time
import random
from Library import Settings

# tt = TurnTable.TurnTable(verbose=True)
# tt.velocity = 100
#
# for x in range(200):
#     angle = random.randint(0, 359)
#     print(angle)
#     tt.position(angle)
#     time.sleep(3)

sonar = Sonar.Sonar(verbose=True)
sonar.connect()
sonar.set_signal(Settings.start_frequency, Settings.end_frequency, Settings.length)
while True:
    m = sonar.measure()
    m = Sonar.convert_data(m)
    time.sleep(0.1)