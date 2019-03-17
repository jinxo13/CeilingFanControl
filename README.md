# CeilingFanControl
Python scripts to send RF signals to Mercator Caprice ceiling fans

Usage:
'''
python rf_control.py <room> <cmd>

python rf_control.py office light #Toggles the light on or off in the office
python rf_control.py office off #Turns the light AND fan off
python rf_control.py office stop #Stops the fan
python rf_control.py office s[1-6] #Changes the fan speed (turns fan on if off)
python rf_control.py office breeze #Turns on breeze mode
python rf_control.py office mode #Toggles fan rotation between normal and reverse
'''
