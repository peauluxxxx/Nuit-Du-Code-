mport pyxel as py

py.init(128, 128, title="Knight of Darkness NDC")
py.load("2.pyxres")

# Variables principales
personnage_position = {"x": 10, "y": 90, "v": 2}
t_chute = 0
en_saut = False
sur_le_sol = True
mouvement = False

def personnage():
    global en_saut, mouvement, personnage_position

    x = personnage_position["x"]
    y = personnage_position["y"]
    v = personnage_position["v"]

    # Déplacement droite
    if py.btn(py.KEY_D) and x + v < py.width:
        x += v
        mouvement = True

    # Déplacement gauche
    if py.btn(py.KEY_Q) and x - v > 0:
        x -= v
        mouvement = True

    # Saut
    if py.btn(py.KEY_SPACE) and sur_le_sol:
        en_saut = True
        y -= 7.5  # saut instantané
        mouvement = True

    personnage_position["x"] = x
    personnage_position["y"] = y

def gravite():
    global t_chute, personnage_position, en_saut, sur_le_sol

    if not sur_le_sol:
        t_chute += 1
        personnage_position["y"] += t_chute / 4
    else:
        t_chute = 0

def verifier_sol():
    global sur_le_sol
    px = personnage_position["x"] - 8
    py_ = personnage_position["y"] - 16
    color = py.pget(px, py_)
    sur_le_sol = (color != 0)

def update():
    verifier_sol()
    personnage()
    gravite()

def draw():
    py.cls(0)
    py.bltm(0, 0, 0, 0, 0, 128, 128)
    py.blt(personnage_position["x"], personnage_position["y"], 0, 0, 16, 16, 16,colkey = 2)

py.run(update, draw)
