import numpy as np

port_find_verbose = False

sonar_field = 'serial'
sonar_match = 'DN00S38L'

table_field = 'serial'
table_match = 'FT763FH3'

connect_sonar = True
connect_lidar = False
connect_servo = True
connect_rotation_table = True

default_repeats = 5

#ports on windows
# Only used when running on linux
servo_port = 'COM4'
sonar_port = 'COM5'

def generate_servo_position_lookup_table(min_angle=-90, max_angle=90, step=.5):
    angle_range = np.arange(min_angle, max_angle+step, step)
    position_range = np.flip(np.linspace(832, 2528, len(angle_range)))
    return angle_range, position_range

def generate_servo_positions(min_angle, max_angle, step):
    angles = np.arange(min_angle, max_angle+step, step)
    a_range, p_range = generate_servo_position_lookup_table()
    condition = np.where(np.in1d(a_range, angles))
    positions = p_range[condition]
    return positions


#servo_zero = 1220
#servo_range = [400, 2000]
#servo_positions = np.linspace(832, 2528, 73)
#servo_positions = np.linspace(1256, 2104, 91)
servo_positions = generate_servo_positions(-10, 10, 10)

rotation_table_angles = np.arange(-180., 180., 45.)
rotation_table_offset = 185.

start_freq = 40000 +1
end_freq = 40000 - 1
samples = 100
measurement_pause = 0.1
servo_pause = .5
turntable_pause = 1.


if __name__=='__main__':
    position = generate_servo_positions(-90, 90, 5.)
    print(position)