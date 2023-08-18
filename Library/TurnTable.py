from Library import Ports
import dynio
from Library import Settings
import time
import math

class TurnTable:
    def __init__(self, verbose=False):
        self.field = Settings.table_field
        self.match = Settings.table_match
        self.motor_id = 2
        self.port = Ports.find_port(field=self.field, match=self.match, verbose=True)
        self.dxl_io = dynio.dxl.DynamixelIO(self.port, baud_rate=1000000)
        self.motor = self.dxl_io.new_xl430(self.motor_id, 2)
        self.motor.set_position_mode()
        self.velocity = 130

    def position(self, x, block=True):
        x = x + 180

        self.motor.torque_enable()
        self.motor.set_velocity(self.velocity)
        self.motor.set_angle(x)
        if not block: return
        while True:
            load = self.motor.get_current()
            time.sleep(0.01)
            if load == 0: return

