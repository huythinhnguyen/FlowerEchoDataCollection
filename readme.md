# Requirements

```
conda install pyserial
conda install numpy
conda install matplotlib
pip install easygui
conda install scipy
pip install sshkeyboard
``` 

Add user to dialout group:

```
sudo adduser $USER dialout
```


# Dynamixel

I copied the MX106.json file and renamed it to XL430. 
I checked this file against the control table at

<https://emanual.robotis.com/docs/en/dxl/x/xl430-w250/>

Some entries in the json file do not appear in the control table. I assume this is ok.  

I fixed a typo in the orginal table:

```
    "Values:": {
      "Min_Position": 0,
      "Max_Position": 4095,
      "Max_Angle": 360
    }
```

to (removed an extra `:`)

```
    "Values": {
      "Min_Position": 0,
      "Max_Position": 4095,
      "Max_Angle": 360
    }
```

I added the following function to `dynamixel_controller.py`:

`def new_xl430(self, dxl_id, protocol=2, control_table_protocol=None)`

`set_velocity_mode()` results in an error as this refers to a memory space in ROM