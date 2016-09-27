from graphics import *

win = GraphWin("JOGO",560,550)

win.setBackground("black")
#p1 = Point(200,250)
#fundo = Image(p1,"fundo.png")
#fundo.draw(win)


p2 = Point(80,250)
carro1 = Image(p2,"carro11.png")
carro1.draw(win)

p3 = Point(210,250)
carro2 = Image(p3,"carro22.png")
carro2.draw(win)

p4 = Point(350,250)
carro3 = Image(p4,"carro33.png")
carro3.draw(win)

p5 = Point(480,250)
carro4 = Image(p5,"carro44.png")
carro4.draw(win)

#------------------------RETANGULO----
p6 = Point(40,150)
p7 = Point(120,350)
ret = Rectangle(p6,p7)
ret.draw(win)
ret.setOutline("red")
ret.setWidth(5)

p8 = Point(170,150)
p9= Point(250,350)
ret2 = Rectangle(p8,p9)
ret2.draw(win)
ret2.setOutline("red")
ret2.setWidth(5)

p10 = Point(310,150)
p11= Point(390,350)
ret3 = Rectangle(p10,p11)
ret3.draw(win)
ret3.setOutline("red")
ret3.setWidth(5)

p12 = Point(440,150)
p13= Point(520,350)
ret4 = Rectangle(p12,p13)
ret4.draw(win)
ret4.setOutline("red")
ret4.setWidth(5)

win.getMouse()
win.close()
