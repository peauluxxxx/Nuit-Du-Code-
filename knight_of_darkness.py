import pyxel as py


# Initialisation de la fenêtre et chargement du fichier ressource.
py.init(128, 128, title="Knight of Darkness NDC")
py.load("2.pyxres")

# Ajout de la musique 
py.playm(0, loop = True)

# Variable principale
animation_frame = 0
sprite_x = 0
sprite_y = 16
compteur = 0
sprite_chevalier = [(0,16), (16,16), (32,16), (48,16)]
coffre = {"x": 0,
          "y": 16}
coeur = 3


# Constantes
GRAVITE = 0.5
SAUT_FORCE = -4
SOL_Y = 112
COLKEY = 2

# État du personnage
personnage = {
    "x": 10,
    "y": 50,
    "vx": 2,
    "vy": 0,
    "largeur": 16,
    "hauteur": 16,
    "en_saut": False
}

## FONCTION
# Fonctions de collision

def collision_verticale(y_offset):
    """ fonction permettant la collision verticale du personnage avec le décor
    """
    for i in range(personnage["largeur"]):
        couleur = py.pget(personnage["x"] + i, personnage["y"] + y_offset)
        if couleur == 0:
            return True
    return False

def collision_horizontale(x_offset):
    """ fonction permettant la collision horizontale du personnage avec le décor
    """
    for i in range(personnage["hauteur"]):
        couleur = py.pget(personnage["x"] + x_offset, personnage["y"] + i)
        if couleur == 0:
            return True
    return False

# Mise à jour du personnage

def personnage_update():
    """ fonction permettant de déplacer et de faire sauter en appliquant la gravité et la collision plafond
    """
    # Déplacement horizontal
    if py.btn(py.KEY_Q) and not collision_horizontale(-1):
        personnage["x"] -= personnage["vx"]
        animation_deplacement()
    if py.btn(py.KEY_D) and not collision_horizontale(personnage["largeur"]):
        personnage["x"] += personnage["vx"]
        animation_deplacement()

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


def animation_deplacement():
    """ fonction permettant d'animer le personnage en changeant de sprite quand il se déplace
    """
    global sprite_x, sprite_y, animation_frame, compteur
    if animation_frame % 5 == 0:
        compteur += 1
        if compteur > 3:
            compteur = 0
        sprite_x = sprite_chevalier[compteur][0]
        sprite_y = sprite_chevalier[compteur][1]
        
def animation():
    """Foncton qui gére les animations du sprite à l'arrêt
    """
    global sprite_x, sprite_y, animation_frame
    if animation_frame % 10 == 0:
        sprite_x = sprite_chevalier[2][0]
        sprite_y = sprite_chevalier[2][1]
    elif animation_frame % 5 == 0:
        sprite_x = sprite_chevalier[0][0]
        sprite_y = sprite_chevalier[0][1]
        

def dessin_coeur(coeur):
    """ fonction permettant de dessiner les coeurs en fonction de la valeur de l'integer dans la variable coeur
    """
    x = 80
    for i in range(coeur):
        py.blt(x,0, 0,112, 48, 16, 16)
        x+= 16

def dessin_coffre(coffre):
    """ fonction permettant de dessiner le coffre tout en lançant la fin du niveau et l'apparition du niveau suivant
    """
    py.blt(coffre["x"],coffre["y"], 0,32, 32, 16, 16)
    #if coffre['x'] + personnage['largeur'] == personnage['x'] :
        
        
        
#  fonction UPDATE
def update():
    global animation_frame
    animation_frame += 1
    personnage_update()
    animation()

# fonction DRAW
def draw():
    py.cls(0)
    py.bltm(0, 0, 0, 0, 0, 128, 128)
    py.blt(personnage["x"], personnage["y"], 0, sprite_x, sprite_y, 16, 16, colkey=COLKEY)
    dessin_coffre(coffre)
    dessin_coeur(coeur)

# lancement du jeu 
py.run(update, draw)
