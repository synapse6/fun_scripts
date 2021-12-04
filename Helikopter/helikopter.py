import sys
import threading
from playsound import playsound # pip install playsound==1.2.2 

def delete_line(count):
    #cursor up five line
    sys.stdout.write('\x1b[{}A'.format(count))

    #delete last line
    sys.stdout.write('\x1b[2K')

def helikopter_fly():
    while True:
        print('   SOS:SOS:::SOS:',)
        delete_line(1)
        print('                  SOS:SOS:::SOS:',)
        delete_line(1)
        print('                 A           ')
        print('L           /.........')
        print("HEL:===========     [] \ ")
        print('L           \       []  \ ')
        print('             \___________)')
        print('                |       |    ')
        print('            .............../')
        delete_line(7)


if __name__ == '__main__':
    threading.Thread(target=helikopter_fly).start()	
    threading.Thread(target=playsound('heli.mp3')).start()

