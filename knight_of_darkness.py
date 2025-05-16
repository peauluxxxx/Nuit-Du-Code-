import pyxel as py

py.init(128,128,"knight_of_darkness NDC")
py.load("2.pyxres")

# Variable principale
personnage_position = {"x": 10, "y": 90 }




# fonctions 

def personnage(personnage_position):
  
  
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


def UPDATE():




def DRAW():



py.show(UPDATE,DRAW)





