#############################################
# import
#############################################
from Vector import Vector2
import Texture
import pyxel

#############################################
# Objectクラス
# Pos : 座標
# Tex : テクスチャ情報
#############################################
class Object:

    def __init__(self, _pos, _texture):
        self.Pos = _pos
        self.Tex = _texture
    
    # 更新
    def Update():
        pass

    # 描画
    def Render():
        pass

###############################################
# 固定値
###############################################
PLAYER_MOVE_SPEED = 2
PLAYER_JUMP_POWER = 5


###############################################
# Playerクラス
###############################################
class Player(Object):

    # 入力処理
    def Input(self):
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.Pos.x -= PLAYER_MOVE_SPEED
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.Pos.x += PLAYER_MOVE_SPEED
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.Pos.y += PLAYER_JUMP_POWER

    def Update(self):
        
        # 入力処理
        self.Input()

    def Render(self):
        pyxel.blt(self.Pos.x, self.Pos.y, self.Tex.img, self.Tex.Pos.x, self.Tex.Pos.y, self.Tex.width, self.Tex.height, self.Tex.colKey)
