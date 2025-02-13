import pyxel

# 定数
SCREEN_WIDTH = 160  
SCREEN_HEIGHT = 120
STONE_INTERVAL = 30


class Stone:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def update(self):
        if self.y < SCREEN_HEIGHT:
            self.y += 1

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, pyxel.COLOR_BLACK)
        


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
        # self.stone_x = SCREEN_WIDTH // 2
        # self.stone_y = 0
        self.stones = []
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


        # 石の生成
        if pyxel.frame_count % STONE_INTERVAL == 0:
            self.stones.append(Stone(pyxel.rndi(0, SCREEN_WIDTH - 16), 0))

        # 石の移動
        for stone in self.stones.copy():
            stone.update()

            # 衝突判定
            if (self.player_x < stone.x + 16 and stone.x < self.player_x + 16 and 
                SCREEN_HEIGHT // 2 < stone.y + 16 and stone.y <SCREEN_HEIGHT // 2 + 16):
                self.is_hit = True

            # 画面外に出た石は削除
            if stone.y == SCREEN_HEIGHT:
                self.stones.remove(stone)


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
        # 石の描画
        for stone in self.stones:
            stone.draw()

        if self.is_hit:
            pyxel.text(SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2, "GAME OVER", pyxel.COLOR_RED)


App()