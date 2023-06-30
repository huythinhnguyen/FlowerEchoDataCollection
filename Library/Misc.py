import glob
import os
import sys
import re

import shutil
import easygui
from scipy.signal import spectrogram
from matplotlib import pyplot
import numpy


def create_folder(folder, remove_first=False, ask=False):
    contents = []
    proceed = True
    full_path = os.path.abspath(folder)
    if os.path.isdir(folder): contents = os.listdir(folder)
    message = 'The folder is not empty. Do you want to delete it?\n' + full_path
    if len(contents) > 0 and remove_first:
        if ask: proceed = easygui.ynbox(message, 'Warning', ('Yes', 'No'))
        if not proceed: return False
        shutil.rmtree(folder)
    if not os.path.isdir(folder): os.makedirs(folder)
    return True


def check_file_exists(file, quit_on_no=False):
    exists = os.path.isfile(file)
    full_path = os.path.abspath(file)
    proceed = True
    message = 'The file exists. Do you want to continue?\n' + full_path
    if exists: proceed = easygui.ynbox(message, 'Warning', ('Yes', 'No'))
    if not proceed and quit_on_no: sys.exit()
    return exists


def get_folders(directory='', pattern='*'):
    # folders = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    folders = glob.glob("./%s/%s/" % (directory, pattern))
    return folders


def get_files(directory='.', pattern='*'):
    files = [f for f in os.listdir(directory) if re.match(pattern, f)]
    return files


def integer_string(x, n=4):
    format = f'%0{n}.i'
    result = format % x
    return result

def simple_spectrogam(x, sample_rate=300, n=128, db=True, dynamic_range=50):
    f, t, sxx = spectrogram(x, sample_rate, nperseg=n, noverlap=n - 1)
    if db:
        sxx = sxx / numpy.max(sxx)
        sxx = 10 * numpy.log10(sxx)
        sxx[sxx < - dynamic_range] = - dynamic_range
    pyplot.pcolormesh(t, f, sxx)
    pyplot.ylabel('Frequency [kHz]')
    pyplot.xlabel('Time [msec]')
    return f, t, sxx

