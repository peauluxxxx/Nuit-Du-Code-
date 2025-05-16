import pyxel as py

py.init(128, 128, title="Knight of Darkness NDC")
py.load("2.pyxres")

py.play(0, [0,0,0,0,0,0], loop = True)
py.play(1, [1,1,2,1,1,3], loop = True)
animation_frame = 0
sprite_x = 0
sprite_y = 16
compteur = 0
sprite_chevalier = [(0,16), (16,16), (32,16), (48,16)]
coffre = {"x": 0,
          "y": 16
          }
coeur = 2
pos_decor = 128
ennemis = []

# Constantes
GRAVITE = 0.5
SAUT_FORCE = -4
SOL_Y = 112
COLKEY = 2
t = 0
lvl2 = False
# État du personnage
personnage = {
    "x": 10,
    "y": 50,
    "vx": 1,
    "vy": 0,
    "largeur": 16,
    "hauteur": 16,
    "en_saut": False
}

# Fonctions de collision
def collision_verticale(y_offset):
    for i in range(personnage["largeur"]):
        couleur = py.pget(personnage["x"] + i, personnage["y"] + y_offset)
        if couleur == 0:
            return True
    return False

def collision_horizontale(x_offset):
    for i in range(personnage["hauteur"]):
        couleur = py.pget(personnage["x"] + x_offset, personnage["y"] + i)
        if couleur == 0:
            return True
    return False

# Mise à jour du personnage
def personnage_update():
    global pos_decor
    # Déplacement horizontal
    if py.btn(py.KEY_Q) and not collision_horizontale(-1):
        if lvl2 == True:
            pos_decor -= 4
            vx = 0
        personnage["x"] -= personnage["vx"]
        animation()
    if py.btn(py.KEY_D) and not collision_horizontale(personnage["largeur"]):
        if lvl2 == True:
            pos_decor += 4
            vx = 0
        personnage["x"] += personnage["vx"]
        animation()

    # Saut
    si_au_sol = collision_verticale(personnage["hauteur"])
    if si_au_sol:
        personnage["vy"] = 0
        personnage["en_saut"] = False
        if py.btnp(py.KEY_SPACE):
            personnage["vy"] = SAUT_FORCE
            personnage["en_saut"] = True
    else:
        personnage["vy"] += GRAVITE

    # Collision plafond
    if collision_verticale(-1) and personnage["vy"] < 0:
        personnage["vy"] = 0

    # Application de la gravité
    personnage["y"] += personnage["vy"]


def animation():
    global sprite_x, sprite_y, animation_frame, compteur
    if animation_frame % 5 == 0:
        compteur += 1
        if compteur > 3:
            compteur = 0
        sprite_x = sprite_chevalier[compteur][0]
        sprite_y = sprite_chevalier[compteur][1]


def dessin_coeur(coeur):
    x = 80
    for i in range(coeur):
        py.blt(x,0, 0,112, 48, 16, 16)
        x+= 16

def dessin_coffre(coffre):
    global t, lvl2
    py.blt(coffre["x"],coffre["y"], 0,32, 32, 16, 16)
    if coffre['x'] + personnage['largeur'] == personnage['x'] and coffre['y'] == personnage['y']:
        py.blt(coffre["x"],coffre["y"], 0,48, 32, 16, 16)
        while t < 121 :
            t += 1
            print(t)
        if t  >= 120 :
            lvl2 = True
            print(lvl2)


        

def update():
    global animation_frame
    animation_frame += 1
    if animation_frame > 30:
        animation_frame = 0
    personnage_update()

    
def draw():
    global lvl2
    py.cls(0)
    if lvl2 == False :
        py.bltm(0, 0, 0, 0, 0, 128, 128)
        dessin_coffre(coffre)
    else:
        py.bltm(0,0,0, pos_decor, 0, 128, 128)

    py.blt(personnage["x"], personnage["y"], 0, sprite_x, sprite_y, 16, 16, colkey=COLKEY)
    dessin_coeur(coeur)
py.run(update, draw)
