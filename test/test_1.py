import time
import numpy as np
import sys
sys.path.append('..')

from Library import TurnTable

def test_the_wrap360(angle):
    return print(TurnTable.wrapTo360(angle))

def rotation_test_1(increment=5., verbose=True):
    angles = np.arange(-180., 180., increment)
    tt = TurnTable.TurnTable(offset = 185., verbose=verbose)
    for a in angles:
        tt.position(a, block=False)
        sys.stdout.writelines('{} \r'.format(a))
        time.sleep(.2)
        if a==175.: time.sleep(1.)

def neck_rotation_test():
    pass

def main():
    return rotation_test_1()
    #return test_the_wrap360(np.asarray([90., 360., -180.]))
    #return collect_sonar_test_1()

if __name__=='__main__':
    main()