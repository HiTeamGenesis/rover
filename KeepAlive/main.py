#Keep it as simple as possible thank you.
#We don't want the file that watches for crashes.... to crash

import subprocess

if __name__ == "__main__":

    #TO-DO: CHANGE THE COMMAND SO IT LAUNCHES THE BACKEND INSTEAD
	process = subprocess.Popen(['python3.9', 'main.py'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
	stdout, stderr = process.communicate()
	exit_code = process.wait()

	print('\nRover Crashed!\n')
	print(stdout, stderr, exit_code)

    #TODO: 
	# - ADD RESTART 
	# - TELL ICR ROVER CRASHED