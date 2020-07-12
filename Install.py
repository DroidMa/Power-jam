# Tool Name :- PowerJam
# Creator :- Lesego Ruele
# Date :- 5/7/2020

import os
import sys
from time import sleep
from logo import *
from system import *

class tool:
  @classmethod
  def install(self):
    while True:
      system=sys()
      os.system("clear")
      logo.ins_tnc()
      inp=input("\033[1;33m Do you want to install Power-jam[Y/n]> \033[00m")
      if inp=="y" or inp=="Y":
        os.system("clear")
        logo.installing()
        if system.sudo is not None:
          #require root permission
          if os.path.exists(system.conf_dir+"/Power-Jam"):
            pass
          else:
            os.system(system.sudo+" mkdir "+system.conf_dir+"/Power-Jam")
          os.system(system.sudo+" cp -r Power-Jam.py "+system.conf_dir+"/Power-Jam")
          os.system(system.sudo+" cp -r Power-Jam "+system.bin)
          os.system(system.sudo+" cp -r Power-Jam "+system.bin)
          os.system(system.sudo+" chmod +x "+system.bin+"/Power-Jam")
          os.system(system.sudo+" chmod +x "+system.bin+"/Power-Jam")
          os.system("cd .. && "+system.sudo+" rm -rf Power-Jam")
          if os.path.exists(system.bin+"/Power-Jam") and os.path.exists(system.conf_dir+"/Power-Jam"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m ##> \033[00m")
            break
        else:
          if os.path.exists(system.conf_dir+"/Tool-X"):
            pass
          else:
            os.system("mkdir "+system.conf_dir+"/Power-Jam")
          os.system("cp -r Power-Jam "+system.conf_dir+"/Power-Jam")
          os.system("cp -r Power-Jam "+system.bin)
          os.system("cp -r Power-Jam "+system.bin)
          os.system("chmod +x "+system.bin+"/Power-Jam")
          os.system("chmod +x "+system.bin+"/Power-Jam")
          os.system("cd .. && rm -rf Power-Jam")
          if os.path.exists(system.bin+"/Power-Jam") and os.path.exists(system.conf_dir+"/Power-Jam"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m ##> \033[00m")
            break
      else:
        break

if __name__=="__main__":
  try:
    tool.install()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
