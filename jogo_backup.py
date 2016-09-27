from graphics import *
import time
import pyglet   					     


#--------------------------------------------------INICIO MENU
win1 = GraphWin("JOGO",1200,800)
#------------------------TITULO--------
logo=Point(390,70)

logo = Image(logo,"logo2.png")
logo.draw(win1)

f = Point(130,70)
flag = Image(f,"flag2.png")
flag.draw(win1)

pc = Point(280,500)
cara11 = Image(pc,"cara11.png")
cara11.draw(win1)

pca = Point(450,500)
logo3 = Image(pca,"ford-racing2.png")
logo3.draw(win1)

pl = Point(80,520)
logo2 = Image(pl,"red-hot-logo2.png")
logo2.draw(win1)
#------------------------------------------
win1.setBackground("gray")

p2 = Point(80,250)
carro1 = Image(p2,"carro11.png")
carro1.draw(win1)

p3 = Point(210,250)
carro2 = Image(p3,"carro22.png")
carro2.draw(win1)

p4 = Point(350,250)
carro3 = Image(p4,"carro33.png")
carro3.draw(win1)

p5 = Point(480,250)
carro4 = Image(p5,"carro44.png")
carro4.draw(win1)

#------------------------RETANGULO----
p6 = Point(40,150)
p7 = Point(120,350)
ret = Rectangle(p6,p7)
ret.draw(win1)
ret.setOutline("red")
ret.setWidth(3)

p8 = Point(170,150)
p9= Point(250,350)
ret2 = Rectangle(p8,p9)
ret2.draw(win1)
ret2.setOutline("red")
ret2.setWidth(3)

p10 = Point(310,150)
p11= Point(390,350)
ret3 = Rectangle(p10,p11)
ret3.draw(win1)
ret3.setOutline("red")
ret3.setWidth(3)

p12 = Point(440,150)
p13= Point(520,350)
ret4 = Rectangle(p12,p13)
ret4.draw(win1)
ret4.setOutline("red")
ret4.setWidth(3)


click = win1.getMouse()
clickx = click.getX()
clicky = click.getY()


print clickx 

#==============================AUMENTAR LINHA DE SELECAO============
if ((clickx >= 40 and clicky >=150) and (clickx<=120 and clicky <=350)):
	ret.setWidth(8)
else:
	if ((clickx >= 170 and clicky >=150) and (clickx<=250 and clicky <=350)):
		ret2.setWidth(8)
	else:
		if ((clickx >= 310 and clicky >=150) and (clickx<=390 and clicky <=350)):
			ret3.setWidth(8)
		else:
			if ((clickx >= 440 and clicky >=150) and (clickx<=520 and clicky <=350)):
				ret4.setWidth(8)
#===========================================FIM TESTE==============

#+++++++++++++++++++++++++++++++botao start++++++++++++++++++++++++
p=Point(280,400)

start = Image(p,"start2.png")
start.draw(win1)


ret1 = Point(230,353)
ret2 = Point(327,450)
start = Rectangle(ret1,ret2)
start.draw(win1)
start.setOutline("gray")

click = win1.getMouse()
clickx2 = click.getX()
clicky2 = click.getY()
print clickx, clicky


if ((clickx2 >= 230 and clicky2 >= 353) and (clickx2 <= 327 and clicky2 <= 450)):
	win1.close()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++





#--------------------------------------------------------FINAL MENU

if ((clickx >= 40 and clicky >=150) and (clickx<=120 and clicky <=350)):
	win = GraphWin("JOGO",700,550)
	
	win.setBackground("black")
	p = Point(280,150)
	cena = Image(p,"cena22.png")
	cena.draw(win)
	
	p2 = Point(280,-29000)
	cena2 = Image(p2,"cena22.png")
	cena2.draw(win)
	
	
	
	#------------------------CARRO-----------------
	p3 = Point(280,450)
	carro = Image(p3,"carro11.png")
	carro.draw(win)

	#--------------------PEDRA----------------
	p10 = Point(120,-150)
	pedra = Image(p10,"pedra2.png")
	pedra.draw(win)

	p11 = Point(450,-150)
	pedra2 = Image(p11,"pedra2.png")
	pedra2.draw(win)
#--------------------------------------------------------------------------------LINHA DE CHEGADA (ARRUMAR)
	pbola = Point(30,-14000)
	bola = Image(pbola,"flag3.png")
	bola.draw(win)
	
#--------------------------------------------------------------------------------------------------

	#-----------------------------GPS--------------------
	p1g = Point(620,100)
	p2g = Point(630,460)
	gps = Rectangle(p1g,p2g)
	gps.draw(win)
	gps.setFill("gray")
	pgps = Point(625,460)				
	bolagps = Circle(pgps,5)
	bolagps.draw(win)
	bolagps.setFill("red")	
	
	#-----------------------------------SCORE------------
	psc1 = Point(590,480)
	psc2 = Point(670,520)
	score = Rectangle(psc1,psc2)
	score.draw(win)
	score.setFill("gold")
	
	
	pst = Point(630,487)
	txt = "SCORE"
	scotxt = Text(pst,txt)
	scotxt.draw(win)
	
	
	#----------------------------------------------------
	
	
	contador = 0 #-------------------------------CONTADOR
	conta = str(contador)
	pcont = Point(630,505)
	cont = Text(pcont,conta)
	cont.draw(win)
	cont.undraw()
	
	tecla = ""
	x=0
	while True:
		
		time.sleep(0.00005)
		cena.move(0,1)
		cena2.move(0,1)
		bola.move(0,1)
		pedra.move(0,1)
		pedra2.move(0,1)
		
		
		#-----------------------------------------------
		if (tecla != "Escape"):
			tecla = win.checkKey()
			if (tecla == "Up"):
				carro.move(0,-5)
			else:
				if (tecla == "Down"):
					carro.move(0,5)
				else:
					if (tecla == "Right"):
						carro.move(5,0)
					else:
						if (tecla == "Left"):
							carro.move(-5,0)
						else:
							if (tecla == "Escape"):
								break
								win.close()
								
	
	#----------------------------------------GPS-----------------
		if True:
			
			bolagps.move(0,-0.008)
				
	#----------------------------------------CONTADOR------------
		contador = contador + 0.05
						
	#------------------------------------------------------
	
	
else:
	if ((clickx >= 170 and clicky >=150) and (clickx<=250 and clicky <=350)):
		win = GraphWin("JOGO",700,550)
	
		win.setBackground("black")
		p = Point(280,150)
		cena = Image(p,"cena22.png")
		cena.draw(win)
	
		p2 = Point(280,-29000)
		cena2 = Image(p2,"cena22.png")
		cena2.draw(win)
	
	
	
		#------------------------CARRO-----------------
		p3 = Point(280,450)
		carro = Image(p3,"carro22.png")
		carro.draw(win)

		#--------------------PEDRA----------------
		p10 = Point(120,-150)
		pedra = Image(p10,"pedra2.png")
		pedra.draw(win)

		p11 = Point(450,-150)
		pedra2 = Image(p11,"pedra2.png")
		pedra2.draw(win)
	#--------------------------------------------------------------------------------LINHA DE CHEGADA (ARRUMAR)
		pbola = Point(30,-14000)
		bola = Image(pbola,"flag3.png")
		bola.draw(win)
	
	#--------------------------------------------------------------------------------------------------

		#-----------------------------GPS--------------------
		p1g = Point(620,100)
		p2g = Point(630,460)
		gps = Rectangle(p1g,p2g)
		gps.draw(win)
		gps.setFill("gray")
		pgps = Point(625,460)				
		bolagps = Circle(pgps,5)
		bolagps.draw(win)
		bolagps.setFill("red")	
	
		contador = 0 #-------------------------------CONTADOR
	
		tecla = ""
		x=0
		while True:
		
			time.sleep(0.00005)
			cena.move(0,1)
			cena2.move(0,1)
			bola.move(0,1)
			pedra.move(0,1)
			pedra2.move(0,1)
		
		
			#-----------------------------------------------
			if (tecla != "Escape"):
				tecla = win.checkKey()
				if (tecla == "Up"):
					carro.move(0,-5)
				else:
					if (tecla == "Down"):
						carro.move(0,5)
					else:
						if (tecla == "Right"):
							carro.move(5,0)
						else:
							if (tecla == "Left"):
								carro.move(-5,0)
							else:
								if (tecla == "Escape"):
									break
									win.close()
								
	
		#----------------------------------------GPS-----------------
			if True:
			
				bolagps.move(0,-0.008)
				
		#----------------------------------------CONTADOR------------
			#	contador = contador + 0.05
			#	conta = str(contador)
			#	pcont = Point(600,500)
			#	cont = Text(pcont,conta)
			#	cont.draw(win)
			#	cont.undraw()			
		#------------------------------------------------------
	else:
		if ((clickx >= 310 and clicky >=150) and (clickx<=390 and clicky <=350)):
			win = GraphWin("JOGO",700,550)
	
			win.setBackground("black")
			p = Point(280,150)
			cena = Image(p,"cena22.png")
			cena.draw(win)
	
			p2 = Point(280,-29000)
			cena2 = Image(p2,"cena22.png")
			cena2.draw(win)
	
	
	
			#------------------------CARRO-----------------
			p3 = Point(280,450)
			carro = Image(p3,"carro33.png")
			carro.draw(win)

			#--------------------PEDRA----------------
			p10 = Point(120,-150)
			pedra = Image(p10,"pedra2.png")
			pedra.draw(win)

			p11 = Point(450,-150)
			pedra2 = Image(p11,"pedra2.png")
			pedra2.draw(win)
		#--------------------------------------------------------------------------------LINHA DE CHEGADA (ARRUMAR)
			pbola = Point(30,-14000)
			bola = Image(pbola,"flag3.png")
			bola.draw(win)
	
		#--------------------------------------------------------------------------------------------------

			#-----------------------------GPS--------------------
			p1g = Point(620,100)
			p2g = Point(630,460)
			gps = Rectangle(p1g,p2g)
			gps.draw(win)
			gps.setFill("gray")
			pgps = Point(625,460)				
			bolagps = Circle(pgps,5)
			bolagps.draw(win)
			bolagps.setFill("red")	
	
			contador = 0 #-------------------------------CONTADOR
	
			tecla = ""
			x=0
			while True:
		
				time.sleep(0.00005)
				cena.move(0,1)
				cena2.move(0,1)
				bola.move(0,1)
				pedra.move(0,1)
				pedra2.move(0,1)
		
		
				#-----------------------------------------------
				if (tecla != "Escape"):
					tecla = win.checkKey()
					if (tecla == "Up"):
						carro.move(0,-5)
					else:
						if (tecla == "Down"):
							carro.move(0,5)
						else:
							if (tecla == "Right"):
								carro.move(5,0)
							else:
								if (tecla == "Left"):
									carro.move(-5,0)
								else:
									if (tecla == "Escape"):
										break
										win.close()
								
	
			#----------------------------------------GPS-----------------
				if True:
			
					bolagps.move(0,-0.008)
				
			#----------------------------------------CONTADOR------------
				#	contador = contador + 0.05
				#	conta = str(contador)
				#	pcont = Point(600,500)
				#	cont = Text(pcont,conta)
				#	cont.draw(win)
				#	cont.undraw()			
			#------------------------------------------------------

		
		else:
			if ((clickx >= 440 and clicky >=150) and (clickx<=520 and clicky <=350)):
				win = GraphWin("JOGO",700,550)
	
				win.setBackground("black")
				p = Point(280,150)
				cena = Image(p,"cena22.png")
				cena.draw(win)
	
				p2 = Point(280,-29000)
				cena2 = Image(p2,"cena22.png")
				cena2.draw(win)
	
	
	
				#------------------------CARRO-----------------
				p3 = Point(280,450)
				carro = Image(p3,"carro44.png")
				carro.draw(win)

				#--------------------PEDRA----------------
				p10 = Point(120,-150)
				pedra = Image(p10,"pedra2.png")
				pedra.draw(win)

				p11 = Point(450,-150)
				pedra2 = Image(p11,"pedra2.png")
				pedra2.draw(win)
			#--------------------------------------------------------------------------------LINHA DE CHEGADA (ARRUMAR)
				pbola = Point(30,-14000)
				bola = Image(pbola,"flag3.png")
				bola.draw(win)
	
			#--------------------------------------------------------------------------------------------------

				#-----------------------------GPS--------------------
				p1g = Point(620,100)
				p2g = Point(630,460)
				gps = Rectangle(p1g,p2g)
				gps.draw(win)
				gps.setFill("gray")
				pgps = Point(625,460)				
				bolagps = Circle(pgps,5)
				bolagps.draw(win)
				bolagps.setFill("red")	
	
				contador = 0 #-------------------------------CONTADOR
	
				tecla = ""
				x=0
				while True:
		
					time.sleep(0.00005)
					cena.move(0,1)
					cena2.move(0,1)
					bola.move(0,1)
					pedra.move(0,1)
					pedra2.move(0,1)
		
		
					#-----------------------------------------------
					if (tecla != "Escape"):
						tecla = win.checkKey()
						if (tecla == "Up"):
							carro.move(0,-5)
						else:
							if (tecla == "Down"):
								carro.move(0,5)
							else:
								if (tecla == "Right"):
									carro.move(5,0)
								else:
									if (tecla == "Left"):
										carro.move(-5,0)
									else:
										if (tecla == "Escape"):
											break
											win.close()
								
	
				#----------------------------------------GPS-----------------
					if True:
			
						bolagps.move(0,-0.008)
				
				#----------------------------------------CONTADOR------------
					#	contador = contador + 0.05
					#	conta = str(contador)
					#	pcont = Point(600,500)
					#	cont = Text(pcont,conta)
					#	cont.draw(win)
					#	cont.undraw()			
				#------------------------------------------------------


win1.getMouse()
win1.close()
