import pyxel

# 定数
SCREEN_WIDTH = 160  
SCREEN_HEIGHT = 120
STONE_INTERVAL_FLAME = 30
FLAME_PER_SECOND = 30


# シーン
TITLE_SCENE = "title"
PLAY_SCENE = "play"

START_PLAYER_POSX = SCREEN_WIDTH // 2

def new_stone():
    """ランダムなX座標の石をY=0に生成"""
    return Stone(pyxel.rndi(0, SCREEN_WIDTH - 16), 0)
        
def perflame(flame)->bool:
    """受け取ったフレームごとの処理の実行bool"""
    return pyxel.frame_count % flame == 0


class Stone:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def update(self):
        if self.y < SCREEN_HEIGHT:
            self.y += 1

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, pyxel.COLOR_BLACK)
    
    def is_removable(self):
        return self.y == SCREEN_HEIGHT 
    

class App:
    def __init__(self):
        pyxel.init(160, 120, title="koha game")

        # mouse を許可
        pyxel.mouse(True)

        # イメージバンクの読み込み
        pyxel.load("my_resource.pyxres")

        # プレイヤーの開始X座標
        self.player_x = START_PLAYER_POSX

        # 石の座標
        self.stones = []
        
        #石が衝突しているかどうか
        self.is_hit = False

        # 実行中のシーン
        self.current_scene = TITLE_SCENE

        # gameoverの表示時間
        self.gameover_disp_time = 0 





        pyxel.run(self.update, self.draw)


    ##############################
    # TITLE SCENE
    ##############################

    #### UPDATE ####

    def update_title_scene(self):
        """タイトルシーン
        ・スペースキーを押すとゲーム開始
        """
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.current_scene = PLAY_SCENE
            self.is_hit = False
            self.stones = []
            self.player_x = START_PLAYER_POSX

    #### DRAW ####
    def draw_title_scene(self):
        pyxel.cls(pyxel.COLOR_LIGHT_BLUE)
        pyxel.text(SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2, "PRESS SPACE", pyxel.COLOR_BLACK)
        pyxel.blt( SCREEN_WIDTH // 2 - 8, SCREEN_HEIGHT // 2 - 8, 0, 0, 72, 6, 6)



    ##############################
    # PLAY SCENE
    ##############################

    #### UPDATE ####
    def update_play_scene(self):
        
        # プレイヤーの移動
        if pyxel.btn(pyxel.KEY_RIGHT) and self.player_x < SCREEN_WIDTH - 16:
            self.player_x += 1
        if pyxel.btn(pyxel.KEY_LEFT) and self.player_x > 0:
            self.player_x -= 1


        # 石の生成
        if perflame(STONE_INTERVAL_FLAME):
            self.stones.append(new_stone())

        # 石の移動
        for stone in self.stones.copy():
            stone.update()

            # 衝突判定
            if (self.player_x < stone.x + 16 and stone.x < self.player_x + 16 and 
                SCREEN_HEIGHT // 2 < stone.y + 16 and stone.y <SCREEN_HEIGHT // 2 + 16):
                self.is_hit = True

            # 画面外に出た石は削除
            if stone.is_removable():
                self.stones.remove(stone)

    #### DRAW ####
    def draw_play_scene(self):
        pyxel.cls(pyxel.COLOR_DARK_BLUE)

        #### イメージバンクを用いた描画
        # プレイヤーの描画
        pyxel.blt(self.player_x, SCREEN_HEIGHT // 2, 
                  0, 
                  48, 0, 16, 16, 
                  pyxel.COLOR_BLACK)
        # 石の描画
        for stone in self.stones:
            stone.draw()

        if self.is_hit:
            pyxel.text(SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2, "GAME OVER", pyxel.COLOR_RED)
            self.gameover_disp_time += 1
            if self.gameover_disp_time > FLAME_PER_SECOND * 2:
                #### 初期化（play→title）
                # タイトルシーンに戻る
                self.current_scene = TITLE_SCENE

                # 初期化
                self.gameover_disp_time = 0
                self.is_hit = False
                self.stones = []
                self.player_x = START_PLAYER_POSX


    ##############################
    # COMMON
    ##############################
    #### UPDATE ####
    def update(self):
        # ゲーム終了
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        # シーンごとの処理
        if self.current_scene == TITLE_SCENE:
            self.update_title_scene()
        elif self.current_scene == PLAY_SCENE:
            self.update_play_scene()
    
    #### DRAW ####
    def draw(self):
        # シーンごとの描画
        if self.current_scene == TITLE_SCENE:
            self.draw_title_scene()
        elif self.current_scene == PLAY_SCENE:
            self.draw_play_scene()


    


App()