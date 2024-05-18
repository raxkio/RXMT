import requests
import threading
import os
import random
import string
import colorama
import time
import sys
from os import system
from colorama import Fore
os.system("cls")



print('\033[1m' + 'Credits: @LandonMyers on replit')
print('\033[1m' + '         raxkio for recreating in python form and adjusting')
print('\033[1m' + 'Original link: https://replit.com/@LandonMyers/Roblox-Username-Sniper')
print(Fore.RED + """
                       ██╗   ██╗███████╗███████╗██████╗     ███████╗███╗   ██╗██╗██████╗ ███████╗██████╗ 
                       ██║   ██║██╔════╝██╔════╝██╔══██╗    ██╔════╝████╗  ██║██║██╔══██╗██╔════╝██╔══██╗
                       ██║   ██║███████╗█████╗  ██████╔╝    ███████╗██╔██╗ ██║██║██████╔╝█████╗  ██████╔╝
                       ██║   ██║╚════██║██╔══╝  ██╔══██╗    ╚════██║██║╚██╗██║██║██╔═══╝ ██╔══╝  ██╔══██╗
                       ╚██████╔╝███████║███████╗██║  ██║    ███████║██║ ╚████║██║██║     ███████╗██║  ██║
                        ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
""")
print('\033[1m' + '')


import os
def get_username_os():
   return os.getenv("USERNAME")
username = get_username_os()
print(Fore.RED + f"                                                          WHATSUP {username}")
print(f"")
print(Fore.RED + '                       WARNING: SOME VALIDS ARE INVALID DUE TO BANNED ACCOUNTS SO DONT GET UR HOPES UP!' + '\033[0m')

print(f"")
print(f"")
time.sleep(5)
print(Fore.LIGHTCYAN_EX + '\033[1m' + "      INPUT USERNAME LENGTH:", end="")
username = input(Fore.LIGHTRED_EX + " ")
time.sleep(1)
print(Fore.LIGHTCYAN_EX + '      SHOW ONLY VALIDS y/n:', end=" ")
onlyshow = input(Fore.LIGHTRED_EX + ' ')
username2 = int(username)

time.sleep(2)
os.system("cls")

#animation = "|/-\\"

#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]

animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(20):
    time.sleep(0.1)
    sys.stdout.write("\rcool pointless loading screen.... " + animation[i % len(animation)])
    sys.stdout.flush()
    
    

print("\nLoaded!")
print("""                                                                   
                             :::::::                               
                         :::::--::::::::                           
                      ::::-==========-::::                         
                     :::--=%@*=====*=----:::                       
                    :--**+=+=:--::=%%*==-==:                       
                   :--=%=-::=%@@#=------==+-:                      
                   :-=+#-::-=%@@%=-:-:::-*#+:                      
                   ::-+*=-=-=#@%*=-:::::-=**-                      
                    :=**===%%%@@%#*%*-:--=+*=                      
                     :=+===+%#%%*#%=-----:-+-                      
                     ::=====*###*#=-:---:::                        
                     ::-=====*#*=----==-::                         
                   :::::-=====--=====---::                         
                   :::--=======-===-=--::::                        
                   ::-================-:::::                       
                  ::::-============-==:::::::                      
                  :::-:--========------:::::..                     
                  :::-==--=---=====---:::::::::                    
                  :::--=-::--=====------::::::::                   
                  :::----:--=====-====-::::::::::                  
                   :====:::==========---:::::--:::                 
                  ::=++=----=========-==-:::---::::                
                  :-=***=---=====+=======:::---:::::               
                  :==+***=---===+=======-::-=----:::               
                  :-=****=====++*+======-:-======--::              
                  :=++***=++=++**++=====-:=========-::             
                 ::=+++**+++*****+++====--=++***+=-:::             
              :--=-=+***##*#*******+===--=+*++==--::::             
            --=*#==+++**%%%##%%%***+===-=*++====-=-::              
             #%%---=*+*#*=+*#%%#**++==-=+**=+=====---              
                :==+**#===+*#%%****+==-****++===                   
                 +***  ****#%*++**++=--                            
                            +*==*==*-:                             
                              =++==*+                              
                                         """)




time.sleep(5)
os.system("cls")
print(Fore.RED + """
               ██╗   ██╗███████╗███████╗██████╗     ███████╗███╗   ██╗██╗██████╗ ███████╗██████╗ 
               ██║   ██║██╔════╝██╔════╝██╔══██╗    ██╔════╝████╗  ██║██║██╔══██╗██╔════╝██╔══██╗
               ██║   ██║███████╗█████╗  ██████╔╝    ███████╗██╔██╗ ██║██║██████╔╝█████╗  ██████╔╝
               ██║   ██║╚════██║██╔══╝  ██╔══██╗    ╚════██║██║╚██╗██║██║██╔═══╝ ██╔══╝  ██╔══██╗
               ╚██████╔╝███████║███████╗██║  ██║    ███████║██║ ╚████║██║██║     ███████╗██║  ██║
                ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
""")
print("\nStarting! (May take a while to start)")
print(Fore.BLUE + '\033[4m' + 'HINT: PRESS CTRL + C TO STOP' + '\033[0m')
print(Fore.BLUE + '\033[4m' + 'MAY LAG COMPUTER... ALOT' + '\033[0m')

def do_request():
  while True:
    if onlyshow == 'n':
     res = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=username2))
     r = requests.get("https://www.roblox.com/users/profile?username=%s" % res)
     if r.url == "https://www.roblox.com/request-error?code=404":
      print(Fore.WHITE + "[", end="")
      print(Fore.GREEN + "VALID", end="")
      print(Fore.WHITE + "]", end="")
      print(Fore.BLUE + " Found untaken username: %s" % res)
     else:
      print(Fore.WHITE + "[", end="")
      print(Fore.RED + "INVALID", end="")
      print(Fore.WHITE + "]", end="")
      print(Fore.BLUE + " Taken name: %s" % res)
    if onlyshow == 'y':
     res = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=username2))
     r = requests.get("https://www.roblox.com/users/profile?username=%s" % res)
     if r.url == "https://www.roblox.com/request-error?code=404":
      print(Fore.WHITE + "[", end="")
      print(Fore.GREEN + "VALID", end="")
      print(Fore.WHITE + "]", end="")
      print(Fore.BLUE + " Found a username: %s" % res)
     else:
      a = 0
threads = []
for i in range(50):
  t = threading.Thread(target=do_request)
  t.daemon = True
  threads.append(t)
for i in range(50):
  threads[i].start()
for i in range(50):
  threads[i].join()
    
