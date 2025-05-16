import pyxel as py

py.init(128,128,"knight_of_darkness NDC")
py.load("2.pyxres")

# Variable principale
personnage_position = {"x": 10, "y": 90, 'v': 1 }
t_chute = 0
en_saut = False
sur_sol = True
# fonctions 

def personnage(personnage_position):
  global en_saut
  x = personnage_position["x"]
  y = personnage_position["y"]
  v = personnage_position['v']
    #a droite
  if pyxel.btn(pyxel.KEY_RIGHT) and alien[0] + v <= 15:
        v = 0
        x += v
    # a gauche
  if pyxel.btn(pyxel.KEY_LEFT) and alien[0] - v >= 0:
        v = 2
        x -= v
  if py.btn(pyxel.KEY_SPACE):
    en_saut = True
    y += 4
    

  
def gravité():
    global t_chute
    for i in range(t_chute):
            personnnage_position["y"] += i / 16
            if estSurUnePlateforme():
                return None  # retour anticipé : on s'arrête là
            personnnage_position["y"] -= i / 16
            personnnage_position["y"] += t_chute / 16
    else:
        t_chute = 0

def sur_sol(personnage_position):
  global sur_sol
  if pget(personnage_position["x"],personnage_position['y']) == 1:
    sur_sol = True
  else : 
    sur_sol = False

  
def UPDATE():
global personnage_position, en haut, sur sol   




def DRAW():
  py.cls()
  py.bltm(0,0,0, 1,0,0,16,16)
  personnage = py.blt(personnage_position['x'], personnage_position["y"],0,0,16,16,16)
  
  



py.run(UPDATE,DRAW)





