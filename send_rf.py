import RPi.GPIO as GPIO
from time import sleep
import sys
import getopt

# Sends RF signal for fans
# Binary is encoded as:
# 0 = 101
# 1 = 100

pin = -1
cmd = ''
initSeq = True
initHigh = 0
initLow = 0
boardType = GPIO.BCM
durataBitShort = float(320)/1000000
durataBitShort0 = float(220)/1000000
durataBitLong = float(600)/1000000

nAttempts = 3
extended_delay = float(9200)/1000000
cmdLen = 40

def transmit_code(command):
	print 'transmit'
	for i in range(1, len(command)+1):
		if (command[i-1] == '1'):
			GPIO.output(pin, 1)
			sleep(durataBitShort)
			GPIO.output(pin, 0)
			sleep(durataBitShort0)
			GPIO.output(pin, 0)
			sleep(durataBitShort0)
		elif (command[i-1] == '0'):
			GPIO.output(pin, 1)
			sleep(durataBitShort)
			GPIO.output(pin, 0)
			sleep(durataBitShort0)
			GPIO.output(pin, 1)
			sleep(durataBitShort)

def setupPin():
	print 'setupPin'
	GPIO.setwarnings(False)
	GPIO.setmode(boardType)
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, 0)
	sleep(0.05)

def splitCommand(command):
	ret = []
	for i in range(0, len(command),cmdLen):
		ret = ret + [command[i:i+cmdLen]];
	return ret

def do(command):
	print 'do'
	setupPin()
	cmds = splitCommand(command)
	for i in range(len(cmds)):
		print 'cmd: ' +  cmds[i]
		for t in range(nAttempts):
			print 'attempt: ' + str(t + 1) + ' for command: ' + cmds[i]
			#init_code()
			transmit_code(cmds[i])
			sleep(extended_delay)

def end():
	GPIO.cleanup()

def usage():
	print '-h : Help'
	#print '-c : Binary command'
	print '-b : Command length (number of bits)'
	print '--------------------------------------'
	print '-p : Pin number default 7'
	print '-t : Pin type (BCM|BOARD) default BCM'
	print '--------------------------------------'
	print '-o : Send init sequence (true|false) default true'
	print '-u : Init up time (microseconds) default 4664us'
	print '-d : Init down time (microseconds) default 1540us'
	print '--------------------------------------'
	print '-l : Low time for bit (microseconds) default 356us'
	print '-m : High time for bit (microseconds) default 712us'
	print '--------------------------------------'
	print '-n : Number of attempts default 3'
	print '-e : Delay time between commands (microseconds) default 8064us'

def main(argsv):
	try:
		opts, args = getopt.getopt(argsv, "b:p:t:o:u:d:l:m:n:e:h")
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			usage()
			sys.exit()
		elif opt == '-p':
			global pin
			pin = int(arg)
		elif opt == '-t':
			print arg
			if arg.upper() == 'BOARD':
				boardType = GPIO.BOARD
			else:
				boardType = GPIO.BCM
		elif opt == '-o':
			global initSeq
			initSeq = arg.upper() == 'TRUE'
		elif opt == '-d':
			global initLow
			initLow = float(arg) / 1000000
		elif opt == '-u':
			global initHigh
			initHigh = float(arg) / 1000000
		elif opt == '-l':
			global durataBitScurta
			durataBitScurta = float(arg) / 1000000
		elif opt == '-m':
			global durataBitLunga
			durataBitLunga = float(arg) / 1000000
		elif opt == '-n':
			global nAttempts
			nAttempts = int(arg)
		elif opt == '-e':
			global extended_delay
			extended_delay = float(arg) / 1000000
		elif opt == '-b':
			global cmdLen
			cmdLen = int(arg)
	do(cmd)

if (__name__ == "__main__"):
	print sys.argv[2:]
	cmd = sys.argv[1]
	main(sys.argv[2:])
