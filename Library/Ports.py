import serial.tools.list_ports
from Library import Settings

def find_port(field, match, verbose=False):
    ports = serial.tools.list_ports.comports()
    selected_port = None
    for current_port in ports:
        device = current_port.device
        description = current_port.description
        hwid = current_port.hwid
        vid = current_port.vid
        pid = current_port.pid
        serial_number = current_port.serial_number
        location = current_port.location
        if verbose:print(field, match, str(hwid))

        if field == 'hwid' and match in str(hwid): selected_port = device
        if field == 'description' and match in str(description): selected_port = device
        if field == 'vid' and match in str(vid): selected_port = device
        if field == 'pid' and match in str(pid): selected_port = device
        if field == 'serial' and match in str(serial_number): selected_port = device

        if Settings.port_find_verbose:
            print('#' * 10)
            print(device)
            print('#' * 10)
            print('Description:', description)
            print('hwid:', hwid)
            print('vid:', vid)
            print('pid:', pid)
            print('Serial_number:', serial_number)
            print('location:', location)


    if Settings.port_find_verbose:
        print('--' * 10)
        print('Field:', field)
        print('Match:', match)
        print('Selected port:', str(selected_port))
    return selected_port