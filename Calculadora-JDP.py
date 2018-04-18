import turtle

def dibujarBoton(n,x,y):
    """

    Descrripcion: procedimiento que dibuja los botones 
    Entradas: ninguna
    Sañida: los botones de la calculadora

    """
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.penup()
    turtle.goto(x+25,y-40)
    turtle.write(n,align="center",font= ("Arial",20,"normal"))


def dibujarcalculadora():
    """
    Descrripcion: Prcedimiento que dibuja la calculadora
    Entradas: Ninguna
    Sañida: Dibujo en el mundo de la tortuga la calculadora 

    """
    turtle.reset()
    turtle.hideturtle()
    turtle.speed(0)
    
    #Dibujar Parte exterior
    turtle.penup()
    turtle.color("dark blue")
    turtle.pencolor("white")
    turtle.begin_fill()
    turtle.goto(0,-200)
    turtle.pendown()
    turtle.pensize(3)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(150)
    turtle.end_fill()

    #Dibuja el Display
    turtle.penup()
    turtle.goto(0,120)
    turtle.color("mediumaquamarine")
    turtle.pencolor("white")
    turtle.begin_fill()
    turtle.pendown()
    turtle.pensize(2)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(235)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.end_fill()

    #Dibujar Botones
    turtle.color("white")
    dibujarBoton("√",-115,100)
    dibujarBoton("CE",-55,100)
    dibujarBoton("%",70,100)
    dibujarBoton("/",7,100)
    dibujarBoton(7,-115,45)
    dibujarBoton(8,-55,45)
    dibujarBoton("X",70,45)
    dibujarBoton(9,7,45)
    dibujarBoton(4,-115,-10)
    dibujarBoton(5,-55,-10)
    dibujarBoton("-",70,-10)
    dibujarBoton(6,7,-10)
    dibujarBoton(1,-115,-65)
    dibujarBoton(2,-55,-65)
    dibujarBoton("+",70,-65)
    dibujarBoton(3,7,-65)
    dibujarBoton(0,-115,-120)
    dibujarBoton(".",-55,-120)
    dibujarBoton("=",70,-120)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-100,120)
    turtle.setheading(0)

 ### Asignacion de Variables para operar ###
A = ""
B = ""
C = ""
O = ""
Num = ""

def haceClick(x,y):
    """
    """
    global A,B,C,O,Num
    
     ## signo √ ##   
    if(x > -115 and x < -65 and y < 100 and y > 50)and turtle.xcor() < 130: 
        turtle.write("√",move=True, align="center", font=("Arial",20,"bold"))
        turtle.forward(17)
        A = float(Num)
        O = "√"
        Num = ""
    ## Borrar los digitos del display CE ##
    else:
        if(x > -55 and x < -5 and y < 100 and y > 50)and turtle.xcor() < 130:
            turtle.penup()
            turtle.goto(5,170)
            turtle.setheading(180)
            turtle.color("mediumaquamarine")
            turtle.pencolor("white")
            turtle.begin_fill()
            turtle.pendown()
            turtle.pensize(2)
            turtle.forward(120)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(235)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(120)
            turtle.left(180)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(-100,120)
            A=""
            B=""
            C=""
            O=""
            Num=""
           
            
        ## signo % ##   
        else:
            if (x > 70 and x < 120 and y < 100 and y > 50)and turtle.xcor() < 130:
                turtle.write("%",move=True, align="center", font=("Arial",20,"bold"))
                turtle.forward(17)
                A = float(Num)
                O = "%"
                Num = ""
            
            ## signo / ##   
            else:
                if(x > 7 and x < 57 and y < 100 and y > 50)and turtle.xcor() < 130:
                    turtle.write("/",move=True, align="center", font=("Arial",20,"bold"))
                    turtle.forward(17)
                    A = float(Num)
                    O = "/"
                    Num = ""
                    
                else:
                    if (x > -115 and x < -65 and y < 45 and y > -5)and turtle.xcor() < 130:
                        turtle.write(7,move=True, align="center", font=("Arial",20,"bold"))
                        turtle.forward(17)
                        Num = Num + "7"
                        
                    else:
                        if(x > -55 and x < -5 and y < 45 and y > -5)and turtle.xcor() < 130:
                            turtle.write(8,move=True, align="center", font=("Arial",20,"bold"))        
                            turtle.forward(17)
                            Num = Num + "8"
                        ## signo X ##   
                        else:
                            if(x > 70 and x < 120 and y < 45 and y > -5)and turtle.xcor() < 130:
                                turtle.write("*",move=True, align="center", font=("Arial",20,"bold"))        
                                turtle.forward(17)
                                A = float(Num)
                                O = "*"
                                Num = ""
                            else:
                                if(x > 7 and x < 57 and y < 45 and y > -5)and turtle.xcor() < 130:
                                    turtle.write(9,move=True, align="center", font=("Arial",20,"bold"))        
                                    turtle.forward(17)
                                    Num = Num + "9"
                                else:
                                    if(x > -115 and x < -65 and y < -10 and y > -60)and turtle.xcor() < 130:
                                        turtle.write(4,move=True, align="center", font=("Arial",20,"bold"))
                                        turtle.forward(17)
                                        Num = Num + "4"
                                    else:
                                        if(x > -55 and x < -5 and y < -10 and y > -60)and turtle.xcor() < 130:
                                            turtle.write(5,move=True, align="center", font=("Arial",20,"bold"))
                                            turtle.forward(17)
                                            Num = Num + "5"
                                        ## signo - ##   
                                        else:
                                            if(x > 70 and x < 120 and y < -10 and y > -60)and turtle.xcor() < 130:
                                                turtle.write("-",move=True, align="center", font=("Arial",20,"bold"))
                                                turtle.forward(17)
                                                A = float(Num)
                                                O = "-"
                                                Num = ""
                                            else:
                                                if(x > 7 and x < 57 and y < -10 and y > -60)and turtle.xcor() < 130:
                                                    turtle.write(6,move=True, align="center", font=("Arial",20,"bold"))
                                                    turtle.forward(17)
                                                    Num = Num + "6"
                                                else:
                                                    if(x > -115 and x < -65 and y < -65 and y > -115)and turtle.xcor() < 130:
                                                        turtle.write(1,move=True, align="center", font=("Arial",20,"bold"))
                                                        turtle.forward(17)
                                                        Num = Num + "1"
                                                    else:
                                                        if(x > -55 and x < -5 and y < -65 and y > -115)and turtle.xcor() < 130:
                                                            turtle.write(2,move=True, align="center", font=("Arial",20,"bold"))
                                                            turtle.forward(17)
                                                            Num = Num + "2"
                                                        ## signo + ##   
                                                        else:
                                                            if(x > 70 and x < 120 and y < -65 and y > -115)and turtle.xcor() < 130:
                                                                turtle.write("+",move=True, align="center", font=("Arial",20,"bold"))
                                                                turtle.forward(17)
                                                                A = float(Num)
                                                                O = "+"
                                                                Num = ""
                                                            else:
                                                                if(x > 7 and x < 57 and y < -65 and y > -115)and turtle.xcor() < 130:
                                                                    turtle.write(3,move=True, align="center", font=("Arial",20,"bold"))
                                                                    turtle.forward(17)
                                                                    Num = Num + "3"
                                                                else:
                                                                    if(x > -115 and x < -65 and y < -120 and y > -170)and turtle.xcor() < 130:
                                                                        turtle.write(0,move=True, align="center", font=("Arial",20,"bold"))
                                                                        turtle.forward(17)
                                                                        Num = Num + "0"
                                                                    else:
                                                                        if(x > -55 and x < -5 and y < -120 and y > -170)and turtle.xcor() < 130:
                                                                            turtle.write(".",move=True, align="center", font=("Arial",20,"bold"))
                                                                            turtle.forward(17)
                                                                            Num = Num + "."
                                                                        
                                                                        ## Hacer que el igual nos mustre el resultado ##   
                                                                        else:
                                                                            if(x > 70 and x < 120 and y < -120 and y > -170)and turtle.xcor() < 130:
                                                                                turtle.penup()
                                                                                turtle.goto(5,170)
                                                                                turtle.setheading(180)
                                                                                turtle.color("mediumaquamarine")
                                                                                turtle.pencolor("white")
                                                                                turtle.begin_fill()
                                                                                turtle.pendown()
                                                                                turtle.pensize(2)
                                                                                turtle.forward(120)
                                                                                turtle.left(90)
                                                                                turtle.forward(50)
                                                                                turtle.left(90)
                                                                                turtle.forward(235)
                                                                                turtle.left(90)
                                                                                turtle.forward(50)
                                                                                turtle.left(90)
                                                                                turtle.forward(120)
                                                                                turtle.left(180)
                                                                                turtle.end_fill()
                                                                                turtle.penup()
                                                                                turtle.goto(-100,120)
                                                                                B=float(Num)
                                                                                if O == "+":
                                                                                    C= A + B
                                                                                else:
                                                                                    if O == "-":
                                                                                        C = A - B
                                                                                    else:
                                                                                        if O == "*":
                                                                                            C = A * B
                                                                                        else:
                                                                                            if O == "/":
                                                                                                C = A / B
                                                                                            else:
                                                                                                if O == "√":
                                                                                                    C = B**(1/A)
                                                                                                else:
                                                                                                    if O == "%":
                                                                                                        C = A % B
                                                                                                    
                                                                            turtle.write(C, font=("arial",25,"normal"))
                                                                                
                          

def calculadora():
    """
    Descirpicion: Programa que hace una calculadora
    Entradas: se ingresan datos por medio del mouse
    Salida: Por pantalla se apreciara el resultado
    """

    dibujarcalculadora()

    turtle.onscreenclick(haceClick)
calculadora() 



    
