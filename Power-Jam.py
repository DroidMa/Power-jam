import os
import sys
from menu import *

if __name__=="__main__":
  try:
    main.menu()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
