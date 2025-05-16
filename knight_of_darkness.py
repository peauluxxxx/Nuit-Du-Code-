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
py.play(0, [0,0,0,0,0,0], loop = True)
py.play(1, [1,1,2,1,1,3], loop = True)
GRAVITE = 0.5
SAUT_VELOCITE = -5
SOL_Y = 112  
COLKEY = 2
sol_toucher = True
animation_frame = 0
sprite_x = 0
sprite_y = 16
compteur = 0
sprite_chevalier = [(0,16), (16,16), (32,16), (48,16)]
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
        animation()

    # Droite
    if py.btn(py.KEY_D) and gerer_collision_avec_mur():
        personnage["x"] += personnage["vx"]
        animation()
        
    
    if py.btnp(py.KEY_SPACE) and personnage["y"] > 0:
        if personnage["y"] + personnage["hauteur"] >= SOL_Y:
            personnage["vy"] = SAUT_VELOCITE

    if sol_toucher == True :
        y = 0 

def animation():
    global sprite_x, sprite_y, animation_frame, compteur
    if animation_frame % 5 == 0:
        compteur += 1
        if compteur > 3:
            compteur = 0
        sprite_x = sprite_chevalier[compteur][0]
        sprite_y = sprite_chevalier[compteur][1]
        

def update():
    global animation_frame
    animation_frame += 1
    if animation_frame > 30:
        animation_frame = 0
    personnage_update()
    appliquer_gravite()
    gerer_collision_avec_sol()
    
def draw():
    py.cls(0)
    py.bltm(0, 0, 0, 0, 0, 128, 128)
    py.blt(personnage["x"], personnage["y"], 0, sprite_x, sprite_y, 16, 16, colkey=COLKEY)

py.run(update, draw)
