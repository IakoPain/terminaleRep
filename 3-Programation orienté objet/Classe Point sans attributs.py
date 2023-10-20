class Point:
    def placer(self, abscisse, oredonnee):
        self.x, self.y = abscisse, oredonnee
    def translater(self, dx, dy):
        self.x += dx
        self.y += dy
p=Point()
p.placer(12,7)
print("A(", p.x, ",", p.y, ")")
p.translater(2,-3)
print("A(", p.x, ",", p.y, ")")

