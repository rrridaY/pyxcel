##########################################
# import
##########################################
import Vector


##########################################
# Textureクラス
##########################################
class Texture:

    def __init__(self, _img, _pos, _width, _height, _colkey):
        self.img    = _img        # イメージバンク番号
        self.Pos    = _pos        # 画像保存座標
        self.width  = _width      # 幅
        self.height = _height     # 高さ
        self.colKey = _colkey     # 透過にする色