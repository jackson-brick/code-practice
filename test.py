import time
import os
z=os.get_terminal_size()[0]
os.open()

print(f"{time.clock_gettime()}".center(z))