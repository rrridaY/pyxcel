import pyxel

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
        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 20 <= pyxel.mouse_x <= 40 and 50 <= pyxel.mouse_y <= 70:
                self.number -= 1
            elif 100 <= pyxel.mouse_x <= 120 and 50 <= pyxel.mouse_y <= 70:
                self.number += 1


    def draw(self):
        pyxel.cls(pyxel.COLOR_DARK_BLUE)
        pyxel.blt(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 0, 8, 0, 8, 8, pyxel.COLOR_BLACK) # 表示したいx座標、y座標、イメージバンク、x座標　y座標、幅、高さ、透過として扱う色
        

App()