
############################################
# Vectorクラス
############################################
class Vector2:

    def __init__(self):
        self.x = 0
        self.y = 0


    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    # ベクトル加算
    def Add(self, vec1, vec2):
        ans = Vector2()
        ans.x = vec1.x + vec2.x
        ans.y = vec1.y + vec2.x
        return ans

    # ベクトル減算
    def Sub(self, vec1, vec2):
        ans = Vector2()
        ans.x = vec1.x - vec2.x
        ans.y = vec1.y - vec2.y
        return ans