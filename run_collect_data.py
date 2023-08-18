from Library import TurnTable
from Library import Sonar
import time
import numpy
from Library import Misc
from os import path
from matplotlib import pyplot
import shutil


measurement_name = 'test'
start_frequency = 55000
end_frequency = 30000
length = 1000
repeats = 5
inter_measure_delay = 0.1
after_motor_delay = 0.25
angles = numpy.linspace(-180, 179, 20)

sonar = Sonar.Sonar(verbose=True)
sonar.connect()
sonar.set_signal(start_frequency, end_frequency, length)

table = TurnTable.TurnTable(verbose=True)
table.velocity = 100

output_path = path.join('data', measurement_name)
Misc.create_folder(output_path, remove_first=True, ask=True)
for i in range(10): data = sonar.measure()

counter = 0
for current_angle in angles:
    current_angle = int(current_angle)
    print('+ Current Angle:', current_angle)
    table.position(current_angle)
    time.sleep(after_motor_delay)
    measurement_data = numpy.zeros((7000, 2, repeats))

    angle_string = Misc.integer_string(current_angle, n=3)
    count_string = Misc.integer_string(counter, n = 5)

    data_file_path = count_string + '_measurement_' + angle_string + '.npy'
    data_file_path = path.join(output_path, data_file_path)

    image_file_path = count_string + '_measurement_' + angle_string + '.png'
    image_file_path = path.join(output_path, image_file_path)

    shutil.copyfile(path.abspath(__file__), path.join(output_path, 'script_copy.txt'))

    for i in range(repeats):
        data = sonar.measure()
        data = Sonar.convert_data(data)
        data[:, 0] = data[:, 0] - numpy.mean(data[:, 0])
        data[:, 1] = data[:, 1] - numpy.mean(data[:, 1])
        measurement_data[:, :, i] = data
        time.sleep(inter_measure_delay)

    pyplot.figure()
    pyplot.subplot(2, 2, 1)
    Misc.simple_spectrogam(x=data[:, 0], dynamic_range=60)

    pyplot.subplot(2, 2, 2)
    Misc.simple_spectrogam(x=data[:, 1], dynamic_range=60)

    pyplot.subplot(2, 2, 3)
    Misc.simple_spectrogam(x=data[500:, 0], dynamic_range=60)

    pyplot.subplot(2, 2, 4)
    Misc.simple_spectrogam(x=data[500:, 1], dynamic_range=60)

    pyplot.tight_layout()

    pyplot.savefig(image_file_path)
    numpy.save(data_file_path, measurement_data)

    pyplot.close('all')
    counter = counter + 1






