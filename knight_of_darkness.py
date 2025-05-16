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

def appliquer_gravite():
    personnage["vy"] += GRAVITE
    personnage["y"] += personnage["vy"]

def gerer_collision_avec_sol():
    global personnage
    if personnage["y"] + personnage["hauteur"] >= SOL_Y:
        personnage["y"] = SOL_Y - personnage["hauteur"]
        personnage["vy"] = 0

def personnage_update():
    # Gauche
    if py.btn(py.KEY_Q):
        personnage["x"] -= personnage["vx"]

    # Droite
    if py.btn(py.KEY_D):
        personnage["x"] += personnage["vx"]

    # Saut si sur le sol
    if py.btnp(py.KEY_SPACE):
        if personnage["y"] + personnage["hauteur"] >= SOL_Y:
            personnage["vy"] = SAUT_VELOCITE

def update():
    personnage_update()
    appliquer_gravite()
    gerer_collision_avec_sol()

def draw():
    py.cls(0)
    py.bltm(0, 0, 0, 0, 0, 128, 128)
    py.blt(personnage["x"], personnage["y"], 0, 0, 16, 16, 16, colkey=COLKEY)

py.run(update, draw)
