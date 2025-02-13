import pyxel
import Object
from Texture import Texture
from Vector import Vector2
from Object import Player

############################################################
# 固定値
############################################################
WINDOW_WIDTH  = 160
WINDOW_HEIGHT = 120


############################################################
# Appクラス
############################################################
class App:
    def __init__(self):
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, title="Tomoゲーム")
        pyxel.mouse(True)
        pyxel.load("my_resource.pyxres")

        self.player = Player(Vector2(30, 30), Texture(0, Vector2(24, 0), 15, 15, pyxel.COLOR_BLACK))


        pyxel.run(self.update, self.draw)



    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        self.player.Update()



    def draw(self):
        pyxel.cls(pyxel.COLOR_DARK_BLUE)
        # pyxel.blt(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 0, 8, 0, 8, 8, pyxel.COLOR_BLACK) # 表示したいx座標、y座標、イメージバンク、x座標　y座標、幅、高さ、透過として扱う色

        self.player.Render()

App()