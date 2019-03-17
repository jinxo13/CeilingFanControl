#!/usr/bin/python
import sys
import send_rf
import time

#Rooms
office_id='1000100001000010'
guest_id='0011001011011110'
master_id='0001010011110101'
connor_id='1000111110101010'
fynn_id='1001010010110000'
madi_id='0011000111010101'

#End of command signal
end_cmd = '001'

#Commands
cmd_stop='001000'
cmd_light='011000' #light toggle
cmd_breeze='011100'
cmd_mode='110100' #reverse
cmd_s1='110000'
cmd_s2='100110'
cmd_s3='010000'
cmd_s4='010100'
cmd_s5='100101'
cmd_s6='100000'
cmd_off='111100' #light and fan off
cmd_on=cmd_s3

def main():
    room = sys.argv[1].lower()
    cmd = sys.argv[2].lower()
            
    room_id = eval(room+'_id')
    cmd_id = eval('cmd_'+cmd)
    code = room_id+'.'+cmd_id+'.'+end_cmd
    print(code)
    send_rf.cmd=code
    send_rf.cmdLen=32
    send_rf.pin=22
    #send_rf.durataBitLunga=float(335)/1000000
    #send_rf.durataBitScurta=float(335)/1000000
    send_rf.nAttempts=5
    send_rf.extended_delay=float(8000)/1000000
    send_rf.do(code)
    if (cmd != 'light' and cmd != 'mode'):
        time.sleep(2)
        send_rf.do(code)


if (__name__ == "__main__"):
    main()
