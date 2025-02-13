import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, title="koha game")
        ######### 初期化処理 #########

        # mouse を許可
        pyxel.mouse(True)

        # 数字の初期化
        self.number = 0



        ######### 実行部分 #########
        pyxel.run(self.update, self.draw)

    def update(self):
        # escape で quit
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        
        # マウスの左クリックで数字を増やす
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.number += 1


    def draw(self):
        """描画処理"""
        pyxel.cls(pyxel.COLOR_DARK_BLUE)
        pyxel.text(70, 60, f"{self.number}",pyxel.COLOR_GREEN)

        # +,- ボタン
        pyxel.text(30,60,"+",pyxel.COLOR_WHITE)
        pyxel.text(40,60,"-",pyxel.COLOR_WHITE)


App()