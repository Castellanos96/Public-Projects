import subprocess
# https://docs.python.org/3/library/subprocess.html

# variable of time after user is not found
#signals to lock the computer
lock_timer = 10
#commmand used to access gnome utility
gnome = 'gnome-screensaver-command'
#dictionary, provides states of computer ( LOCK or UNLOCKED)
state = {True: '-l', False: '-d'}
#method allows direct acees to terminal
#locks or unclocks compuuter using gnome and state
def lock_screen(lock):
    subprocess.call((gnome, state[lock]))


