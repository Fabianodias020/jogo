#coding:UTF-8
from graphics import *
import time
import math
   					     
#-------------------------------------------------MENU 2----------------
win2 = GraphWin("JOGO",1200,800)
#-----------------------------------------------------

pgar = Point(600,400)
garagem = Image(pgar,"menu.png")
garagem.draw(win2)

logo=Point(1000,70)

logo = Image(logo,"logo2.png")
logo.draw(win2)

f = Point(130,70)
flag = Image(f,"flag2.png")
flag.draw(win2)

pc = Point(75,650)
cara11 = Image(pc,"cara11.png")
cara11.draw(win2)

pc = Point(1125,650)
cara11 = Image(pc,"cara22.png")
cara11.draw(win2)

#-----------------------BEM VINDO------------------
ptxtw1 = Point(600,200)
saudacao = "BEM VINDO"
bemvindo = Text(ptxtw1,saudacao)
bemvindo.draw(win2)
bemvindo.setTextColor("white")
bemvindo.setSize(36)

ptxt2w1 = Point(410,500)
ptxt3w1 = Point(790,500)
classicos = "Clássicos"
esportivos ="Esportivos"
bemvindo = Text(ptxt2w1,classicos)
bemvindo2 = Text(ptxt3w1,esportivos)
bemvindo.draw(win2)
bemvindo.setTextColor("red")
bemvindo.setSize(15)
bemvindo.setStyle("bold italic")
bemvindo2.draw(win2)
bemvindo2.setTextColor("red")
bemvindo2.setSize(15)
bemvindo2.setStyle("bold italic")


#------------------------------RETANGULOS SELECAO--------



w2ret1 = Point(270,320)
w2ret2 = Point(550,480)
w2ret1 = Rectangle(w2ret1,w2ret2)
w2ret1.draw(win2)
w2ret1.setFill("red")

imgp1 = Point(410,400)
img_1 = Image(imgp1,"class.png")
img_1.draw(win2)


w2ret3 = Point(650,320)
w2ret4 = Point(930,480)
w2ret2 = Rectangle(w2ret3,w2ret4)
w2ret2.draw(win2)
w2ret2.setFill("red")

imgp2 = Point(790,400)
w2ret2 = Image(imgp2,"esport.png")
w2ret2.draw(win2)


#----------------------------------ESCOLHENDO O TIPO DE CARRO--

carro_escolha1 = ""
carro_escolha2 = ""
carro_escolha3 = ""
carro_escolha4 = ""

foto_esp1 = ""
foto_esp2 = ""
foto_esp3 = ""
foto_esp4 = ""




escolhendo2 = True
while escolhendo2 == True:
	click = win2.getMouse()
	clickx = click.getX()
	clicky = click.getY()
	print clickx, clicky

	if ((clickx >=270 and clickx <=550) and (clicky >=320 and clicky <=480)):
		carros_escolha1 = "carro55.png"
		carros_escolha2 = "carro66.png"
		carros_escolha3 = "carro77.png"
		carros_escolha4 = "carro88.png"
		foto_esp3 = "carro7777.png"
		escolhendo2 = False
		win2.close()
		
	elif ((clickx >= 650 and clickx <=930) and (clicky >=320 and clicky <=480)):
		carros_escolha1 = "carro11.png"
		carros_escolha2 = "carro22.png"
		carros_escolha3 = "carro33.png"
		carros_escolha4 = "carro44.png"
		foto_esp1 = "carro1111.png"
		foto_esp2 = "carro2222.png"
		foto_esp3 = "carro3333.png"
		foto_esp4 = "carro4444.png"
		escolhendo2 = False

win2.close()




























#--------------------------------------------------INICIO MENU
win1 = GraphWin("JOGO",1200,800)
#------------------------TITULO--------
pgar = Point(600,400)
garagem = Image(pgar,"menu.png")
garagem.draw(win1)


logo=Point(1000,70)
logo = Image(logo,"logo2.png")
logo.draw(win1)

f = Point(130,70)
flag = Image(f,"flag2.png")
flag.draw(win1)

pc = Point(1125,650)
cara11 = Image(pc,"cara11.png")
cara11.draw(win1)

pc = Point(875,650)
cara11 = Image(pc,"cara22.png")
cara11.draw(win1)

#------------------------------------------
win1.setBackground("gray")

p2 = Point(80,250)
carro1 = Image(p2,carros_escolha1)
carro1.draw(win1)

p3 = Point(210,250)
carro2 = Image(p3,carros_escolha2)
carro2.draw(win1)

p4 = Point(350,250)
carro3 = Image(p4,carros_escolha3)
carro3.draw(win1)

p5 = Point(480,250)
carro4 = Image(p5,carros_escolha4)
carro4.draw(win1)

#------------------------RETANGULO----
uma_cor = color_rgb(0,255,255)

p6 = Point(40,150)
p7 = Point(120,350)
ret = Rectangle(p6,p7)
ret.draw(win1)
ret.setOutline(uma_cor)
ret.setWidth(3)

p8 = Point(170,150)
p9= Point(250,350)
ret2 = Rectangle(p8,p9)
ret2.draw(win1)
ret2.setOutline(uma_cor)
ret2.setWidth(3)

p10 = Point(310,150)
p11= Point(390,350)
ret3 = Rectangle(p10,p11)
ret3.draw(win1)
ret3.setOutline(uma_cor)
ret3.setWidth(3)

p12 = Point(440,150)
p13= Point(520,350)
ret4 = Rectangle(p12,p13)
ret4.draw(win1)
ret4.setOutline(uma_cor)
ret4.setWidth(3)

#++++++++++++++++++++++++++++++ESPECIFICACOES CARRO++++++++++++++++

Ptextesp = Point(680,250)
espnome = "ESPECIFICACOES"
txtesp = Text(Ptextesp,espnome)
txtesp.draw(win1)
txtesp.setSize(15)


retesp1 = Point (700,300)
retesp2 = Point (1020,330)
esp1 = Rectangle(retesp1,retesp2)
esp1.draw(win1)


pesptxt1 = Point(650,315)
txt1 = "Velocidade"
esptxt1 = Text(pesptxt1,txt1)
esptxt1.draw(win1)
esptxt1.setSize(15)

retesp3 = Point(700,360)
retesp4 = Point(1020,390)
esp2 = Rectangle(retesp3,retesp4)
esp2.draw(win1)


pesptxt2 = Point(650,375)
txt2 = "Potencia"
esptxt2 = Text(pesptxt2,txt2)
esptxt2.draw(win1)
esptxt2.setSize(15)

retesp5 = Point(700,420)
retesp6 = Point(1020,450)
esp3 = Rectangle(retesp5,retesp6)
esp3.draw(win1)


pesptxt3 = Point(650,435)
txt3 = "Dinamica"
esptxt3 = Text(pesptxt3,txt3)
esptxt3.draw(win1)
esptxt3.setSize(15)

#------------CARRO ESPECIFICACAO-------

Pcaresp1 = Point(790,150)
Pcaresp2 = Point(1020,270)
caresp = Rectangle(Pcaresp1,Pcaresp2)
caresp.draw(win1)
caresp.setFill("white")

#--------------Introducao Barrinhas--------


#-----------------Barrinha-----------
retesp11 = Point(710,310)
retesp22 = Point(710,320)
esp11 = Rectangle(retesp11,retesp22)
esp11.draw(win1)
esp11.setFill("red")

#-------------Barrinha2------------
retesp11 = Point(710,370)
retesp22 = Point(710,370)
esp22 = Rectangle(retesp11,retesp22)
esp22.draw(win1)
esp22.setFill("red")

#-------------Barrinha3------------
retesp11 = Point(710,430)
retesp22 = Point(710,430)
esp33 = Rectangle(retesp11,retesp22)
esp33.draw(win1)
esp33.setFill("red")


#--------------Imagem carro lado-------------
Pcar_d = Point (900,220)
car_esp_d = Image(Pcar_d,"cora2.png")
car_esp_d.draw(win1)

def carr_esp(nome_imagem):
	global car_esp_d
	carroesp = ""
	carroesp = nome_imagem
	Pcar_d = Point (900,220)
	car_esp_d = Image(Pcar_d,carroesp)
	car_esp_d.draw(win1)



#-------LINHAS DE ESPECIFICOES-----

def linhas_esp(tam1,tam2,tam3):
		i=0
		global esp11,esp22,esp33
		while (i<tam1):
			retesp11 = Point(710,310)
			retesp22 = Point(710 + i,320)
			esp11.undraw()		
			esp11 = Rectangle(retesp11,retesp22)
			esp11.draw(win1)
			esp11.setFill("red")
			i= i + 1
		i=0
		while (i<tam2):
			retesp11 = Point(710,370)
			retesp22 = Point(710 + i,380)
			esp22.undraw()			
			esp22 = Rectangle(retesp11,retesp22)
			esp22.draw(win1)
			esp22.setFill("red")
			i= i + 1
		i=0
		while (i<tam3):
			retesp11 = Point(710,430)
			retesp22 = Point(710 + i,440)	
			esp33.undraw()
			esp33 = Rectangle(retesp11,retesp22)
			esp33.draw(win1)
			esp33.setFill("red")
			i= i + 1

#+++++++++++++++++++++++++++++++botao start++++++++++++++++++++++++
p=Point(1000,650)

start = Image(p,"start2.png")
start.draw(win1)


reta1 = Point(950,600)
reta2 = Point(1050,700)
start = Rectangle(reta1,reta2)

#==============================AUMENTAR LINHA DE SELECAO============
escolhendo = True
carro = ""
habilitado = False
while escolhendo == True:
	
	click = win1.getMouse()
	clickx = click.getX()
	clicky = click.getY()
	print clickx,clicky
	
	if ((clickx >= 40 and clicky >=150) and (clickx<=120 and clicky <=350)):
		car_esp_d.undraw()
		carro = carros_escolha1
		ret.setWidth(8)
		ret2.setWidth(3)
		ret3.setWidth(3)
		ret4.setWidth(3)
		habilitado = True
		
		carr_esp(foto_esp1)
		esp11.undraw()
		esp22.undraw()
		esp33.undraw()
		linhas_esp(300,250,200)

		
		
	elif ((clickx >= 170 and clicky >=150) and (clickx<=250 and clicky <=350)):
		car_esp_d.undraw()
		carro = carros_escolha2
		ret.setWidth(3)
		ret2.setWidth(8)
		ret3.setWidth(3)
		ret4.setWidth(3)
		habilitado = True
		
		carr_esp(foto_esp2)
		esp11.undraw()
		esp22.undraw()
		esp33.undraw()
		linhas_esp(270,280,250)
		
		
	elif ((clickx >= 310 and clicky >=150) and (clickx<=390 and clicky <=350)):
		car_esp_d.undraw()
		carro = carros_escolha3
		ret.setWidth(3)
		ret2.setWidth(3)
		ret3.setWidth(8)
		ret4.setWidth(3)
		habilitado = True
		
		carr_esp(foto_esp3)
		esp11.undraw()
		esp22.undraw()
		esp33.undraw()
		linhas_esp(250,240,270)
		
	elif ((clickx >= 440 and clicky >=150) and (clickx<=520 and clicky <=350)):
		car_esp_d.undraw()
		carro = carros_escolha4
		ret.setWidth(3)
		ret2.setWidth(3)
		ret3.setWidth(3)
		ret4.setWidth(8)
		habilitado = True
		
		carr_esp(foto_esp4)
		esp11.undraw()
		esp22.undraw()
		esp33.undraw()
		linhas_esp(230,290,300)

	
	
	if (((clickx >= 950 and clicky >= 600) and (clickx <= 1050 and clicky <= 700)) and (habilitado == True)):
		escolhendo = False
		win1.close()


		
		
#================================================FINAL MENU============

























#-----------------------------------------------------------------------------JOGO
win = GraphWin("JOGO",700,550)

#--------------------------------

win.setBackground("black")

def fundo(win):

        castle=[]
        cont_castle = 0
        cont_castlex = 275
        cont_castley = 550
        while cont_castle < 80:
                castle.append(Image(Point(cont_castlex,cont_castley),"cena.png"))
                castle_draw = castle[cont_castle]
                castle_draw.draw(win)
                cont_castle += 1
                cont_castley -= 1050

        return castle





castle = fundo(win)
mov_cenario = -5
mov_cenario_cont = 0
	
#++++++++++++++++++++++++++++++RETANGULO DA TELA++++++++++++
plim1 = Point(61,0)
plim2 = Point(500,550)
limite = Rectangle(plim1,plim2)



#++++++++++++++++++++++++++++OBSTACULOS++++++++++++++++++

pobs1 = Point(100,-100)
obs1 = Image(pobs1,"obs11.png")
obs1.draw(win)


pobs2 = Point(220,-190)
obs2 = Image(pobs2,"obs22.png")
obs2.draw(win)

pobs3 = Point(330,-150)
obs3 = Image(pobs3,"obs11.png")
obs3.draw(win)

pobs4 = Point(450,-170)
obs4 = Image(pobs4,"obs33.png")
obs4.draw(win)

pobs5 = Point(100,-900)
obs5 = Image(pobs5,"obs11.png")
obs5.draw(win)


pobs6 = Point(220,-880)
obs6 = Image(pobs6,"obs22.png")
obs6.draw(win)

pobs7 = Point(330,-840)
obs7 = Image(pobs7,"obs11.png")
obs7.draw(win)

pobs8 = Point(450,-600)
obs8 = Image(pobs8,"obs33.png")
obs8.draw(win)


















#++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#------------------------DESENHO CARRO/BOLINHA-----------------
p3 = Point(280,450)
carro = Image(p3,carro)
carro.draw(win)

bcarrop1 = Point(280,379)
bcarroup = Circle(bcarrop1,10)
bcarroup.draw(win)
bcarroup.setFill("red")

bcarrop2 = Point(248,490)
bcarroleft3 = Circle(bcarrop2,10)
bcarroleft3.draw(win)
bcarroleft3.setFill("blue")

bcarrop3 = Point(310,490)
bcarroright3 = Circle(bcarrop3,10)
bcarroright3.draw(win)
bcarroright3.setFill("green")

bcarrop4 = Point(280,520)
bcarrodown = Circle(bcarrop4,10)
bcarrodown.draw(win)
bcarrodown.setFill("purple")

bcarrop5 = Point(248,400)
bcarroleft2 = Circle(bcarrop5,10)
bcarroleft2.draw(win)
bcarroleft2.setFill("yellow")

bcarrop6 = Point(310,400)
bcarroright2 = Circle(bcarrop6,10)
bcarroright2.draw(win)
bcarroright2.setFill("gray")

bcarrop7 = Point(260,385)
bcarroleft1 = Circle(bcarrop7,10)
bcarroleft1.draw(win)
bcarroleft1.setFill("pink")

bcarrop8 = Point(300,385)
bcarroright1 = Circle(bcarrop8,10)
bcarroright1.draw(win)
bcarroright1.setFill("orange")

bcarrop9 = Point(250,520)
bcarroleft4 = Circle(bcarrop9,10)
bcarroleft4.draw(win)
bcarroleft4.setFill("black")

bcarrop10 = Point(310,520)
bcarroright4 = Circle(bcarrop10,10)
bcarroright4.draw(win)
bcarroright4.setFill("white")
#-------------------------------------------------------
#--------------------------------------------------------GPS--------------------
p1g = Point(620,100)
p2g = Point(630,460)
gps = Rectangle(p1g,p2g)
gps.draw(win)
gps.setFill("gray")
pgps = Point(625,460)				
bolagps = Circle(pgps,5)
bolagps.draw(win)
bolagps.setFill("red")	

#-----------------------------------DISTACIA------------------------------------------
psc1 = Point(575,475)
psc2 = Point(680,520)
score = Rectangle(psc1,psc2)
score.draw(win)
score.setFill("gold")


pst = Point(630,487)
txt = "DISTANCIA"
scotxt = Text(pst,txt)
scotxt.draw(win)

pcont = Point(630,505)
contador = 0
#print contador
conta = str(contador/10) + " Mts"
cont = Text(pcont,conta)
cont.draw(win)


#--------CARRO NAO SAI DOS LIMITES-------------------
def limites():
	carro.move(0,0)
	bcarroup.move(0,0)
	bcarrodown.move(0,0)
	bcarroright2.move(0,0)
	bcarroleft2.move(0,0)

def movimentos(x,y):
	bcarroup.move(x,y)
	bcarrodown.move(x,y)
	bcarroright1.move(x,y)
	bcarroleft1.move(x,y)
	bcarroright2.move(x,y)
	bcarroleft2.move(x,y)
	bcarroright3.move(x,y)
	bcarroleft3.move(x,y)
	bcarroright4.move(x,y)
	bcarroleft4.move(x,y)
#-----------------------------------CONTAGEM REGRESSIVA-----------
pcont_regressiva = Point(280,250)
cont_reg = 3
cont_regressiva = Text(pcont_regressiva, str(cont_reg))
cont_regressiva.setSize(36)
cont_regressiva.draw(win)
cont_regressiva.setTextColor("black")
while(cont_reg > 0):
    time.sleep(1)
    cont_reg = cont_reg - 1
    cont_regressiva.setText(str(cont_reg))

cont_regressiva.undraw()
#--------------------------------------------------
tecla = ""
x=0
obs_movimento1 = 1
obs_movimento2 = 0.5
obs_movimento3 = 0.4
obs_movimento4 = 0.7
while True:
	
	win.update()


	time.sleep(0.009)

	#Aumenta a velocidade do cenario

	mov_cenario_cont += 1
	if mov_cenario_cont == 200: #-------------ACELERADOR
		mov_cenario_cont = 0
		mov_cenario += -0.1 #-------------------ACELERADOR
		
		obs_movimento1 +=1
		obs_movimento2 +=1
		obs_movimento3 +=1
		obs_movimento4 +=1
	obs1.move(0,obs_movimento1)
	obs2.move(0,obs_movimento2)
	obs3.move(0,obs_movimento3)
	obs4.move(0,obs_movimento4)
	obs5.move(0,obs_movimento1)
	obs6.move(0,obs_movimento2)
	obs7.move(0,obs_movimento3)
	obs8.move(0,obs_movimento4)

#Move o background
	for x in castle:
		x.move(0,-mov_cenario)
		castlex = x.getAnchor().getX()
		if castlex < -400:
			x.move(0,1600)


#---------------------------------------CENTRO DAS BOLINHAS--------
#------------------------CENTER RIGHT-----------------
	bolinhaRX1 = bcarroright1.getCenter().getX()
	bolinhaRY1 = bcarroright1.getCenter().getY()
	
	bolinhaRX2 = bcarroright2.getCenter().getX()
	bolinhaRY2 = bcarroright2.getCenter().getY()
	
	bolinhaRX3 = bcarroright3.getCenter().getX()
	bolinhaRY3 = bcarroright3.getCenter().getY()
	
	bolinhaRX4 = bcarroright4.getCenter().getX()
	bolinhaRY4 = bcarroright4.getCenter().getY()
#-----------------------CENTER LEFT---------------------
	bolinhaLX1 = bcarroleft1.getCenter().getX()
	bolinhaLY1 = bcarroleft1.getCenter().getY()
	
	bolinhaLX2 = bcarroleft2.getCenter().getX()
	bolinhaLY2 = bcarroleft2.getCenter().getY()
	
	bolinhaLX3 = bcarroleft3.getCenter().getX()
	bolinhaLY3 = bcarroleft3.getCenter().getY()
	
	bolinhaLX4 = bcarroleft4.getCenter().getX()
	bolinhaLY4 = bcarroleft4.getCenter().getY()
#-----------------------CENTER UP------------------------
	bolinhaUX = bcarroup.getCenter().getX()
	bolinhaUY = bcarroup.getCenter().getY()
#-----------------------CENTER DOWN-------------------
	bolinhaDX = bcarrodown.getCenter().getX()
	bolinhaDY = bcarrodown.getCenter().getY()

#------------------------------------------------------
	
#-----------------------------------------------
	if (tecla != "Escape"):
		tecla = win.checkKey()
		print tecla
		
		
		if (tecla == "Up" or tecla == "w"):
			if ((bolinhaUX>=61 and bolinhaUX<=500) and (bolinhaUY>=0 and bolinhaUY<=550)):
				carro.move(0,-8)
				
				movimentos(0,-8)
			else:
				limites()
				
		elif (tecla == "Down" or tecla == "s"):
			if ((bolinhaDX>=61 and bolinhaDX<=500) and (bolinhaDY>=0 and bolinhaDY<=550)):
				carro.move(0,8)
			
				movimentos(0,8)
			else:
				limites()

		elif (tecla == "Right" or tecla == "d"):
			if ((bolinhaRX1>=63 and bolinhaRX1<=500) and (bolinhaRY1>=0 and bolinhaRY1<=550)):
				carro.move(8,0)
				
				movimentos(8,0)
			else:
				limites()
		
		elif (tecla == "Left" or tecla == "a"):
			if ((bolinhaLX1>=63 and bolinhaLX1<=500) and (bolinhaLY1>=0 and bolinhaLY1<=550)):
				carro.move(-8,0)
				
				movimentos(-8,0)
			else:
				limites()

		elif (tecla == "Escape"):
			break
			win.close()
							

#----------------------------------------GPS-----------------
	bolagps.move(0,-0.03)
		
#----------------------------------------DISTANCIA------------
	contador = contador + 1
	#print contador
	cont.undraw()
	conta = str(contador/10) + " Mts"
	cont = Text(pcont,conta)
	cont.draw(win)
	
	
	if (contador>=44000):
		
		break
#------------------------------------------------------

