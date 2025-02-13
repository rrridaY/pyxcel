import pyxel

# 定数
SCREEN_WIDTH = 160  
SCREEN_HEIGHT = 120



class App:
    def __init__(self):
        pyxel.init(160, 120, title="koha game")
        ######### 初期化処理 #########

        # mouse を許可
        pyxel.mouse(True)

        # イメージバンクの読み込み
        pyxel.load("my_resource.pyxres")

        # 数字の初期化
        self.number = 0

        # プレイヤーのX座標
        self.player_x = SCREEN_WIDTH // 2

        # 石の座標
        self.stone_x = SCREEN_WIDTH // 2
        self.stone_y = 0
        #石が衝突しているかどうか
        self.is_hit = False




        ######### 実行部分 #########
        pyxel.run(self.update, self.draw)

    def update(self):
        # escape で quit
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        
        # マウスの左クリックで数字を増やす
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 20 <= pyxel.mouse_x <= 40 and 50 <= pyxel.mouse_y <= 70:
                self.number += 1
            elif 110 <= pyxel.mouse_x <= 130 and 50 <= pyxel.mouse_y <= 70:      
                self.number -= 1
        
        # プレイヤーの移動
        if pyxel.btn(pyxel.KEY_RIGHT) and self.player_x < SCREEN_WIDTH - 16:
            self.player_x += 1
        if pyxel.btn(pyxel.KEY_LEFT) and self.player_x > 0:
            self.player_x -= 1

        # 石の移動
        if self.stone_y < SCREEN_HEIGHT:
            self.stone_y += 1
        if self.stone_y == SCREEN_HEIGHT: # 石が画面外に出たら
            self.stone_y = 0
            # self.stone_x = pyxel.random(0, SCREEN_WIDTH - 16)

        # 衝突判定
        if self.player_x < self.stone_x + 16 and self.stone_x < self.player_x + 16 and self.stone_y == SCREEN_HEIGHT - 16:
            self.is_hit = True
        else:
            self.is_hit = False


    def draw(self):
        """描画処理"""
        pyxel.cls(pyxel.COLOR_DARK_BLUE)
        pyxel.text(70, 60, f"{self.number}",pyxel.COLOR_GREEN)

        # +,- ボタン
        pyxel.text(30,60,"+",pyxel.COLOR_WHITE)
        pyxel.text(120,60,"-",pyxel.COLOR_WHITE)

        # pyxeleditから
        pyxel.blt(self.player_x, SCREEN_HEIGHT // 2, 0, 
                  48, 0, 16, 16, 
                  pyxel.COLOR_BLACK)
        pyxel.blt(self.stone_x, self.stone_y, 0, 
                  0, 0, 16, 16, 
                  pyxel.COLOR_BLACK)
        if self.is_hit:
            pyxel.text(SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2, "GAME OVER", pyxel.COLOR_RED)


App()