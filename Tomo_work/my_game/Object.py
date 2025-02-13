#############################################
# import
#############################################
import Vector
import Texture

#############################################
# Objectクラス
# Pos : 座標
# Tex : テクスチャ情報
#############################################
class Object:

    def __init__(self, _x, _y, texture):
        self.Pos = Vector.Vector2(_x, _y)
        self.Tex = texture