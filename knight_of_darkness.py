import pyxel as py

py.init(128, 128, title="Knight of Darkness NDC")
py.load("2.pyxres")

# Variables principales
personnage = {
    "x": 10,
    "y": 90,
    "vx": 2,     # vitesse horizontale
    "vy": 0,     # vitesse verticale (gravité / saut)
    "largeur": 16,
    "hauteur": 16
}

GRAVITE = 0.5
SAUT_VELOCITE = -5
SOL_Y = 112  
COLKEY = 2
sol_toucher = True

def appliquer_gravite():
    if gerer_collision_avec_sol() == False : 
        personnage["vy"] += GRAVITE
        personnage["y"] += personnage["vy"]

def gerer_collision_avec_sol():
    global personnage
    couleur = []
    for i in range(16):
         couleur.append(py.pget(personnage["x"] + i, personnage["y"] + personnage["hauteur"]))
    return 0 in couleur

def gerer_collision_avec_mur():
    global personnage
    couleur2 = []
    for i in range(16):
         couleur2.append(py.pget(personnage["x"] + personnage['largeur'], personnage["y"] + i))
    return 0 in couleur2

def personnage_update():
    # Gauche
    if py.btn(py.KEY_Q) and gerer_collision_avec_mur():
        personnage["x"] -= personnage["vx"]

    # Droite
    if py.btn(py.KEY_D) and gerer_collision_avec_mur():
        personnage["x"] += personnage["vx"]
        
    
    if py.btnp(py.KEY_SPACE) and personnage["y"] > 0:
        if personnage["y"] + personnage["hauteur"] >= SOL_Y:
            personnage["vy"] = SAUT_VELOCITE

    if sol_toucher == True :
        y = 0 



def update():
    personnage_update()
    appliquer_gravite()
    gerer_collision_avec_sol()
    
def draw():
    py.cls(0)
    py.bltm(0, 0, 0, 0, 0, 128, 128)
    py.blt(personnage["x"], personnage["y"], 0, 0, 16, 16, 16, colkey=COLKEY)

py.run(update, draw)
