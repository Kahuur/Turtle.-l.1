#T.Lehtsalu
#10.10.22
#Kilpkonna liikumise harjutamine
import turtle


#tekitan akna ja lisan muutujasse
aken = turtle.Screen()
aken.setup(300,300)
aken.title("Kilpkonna harjutus 03")
nurk=0
#konna loomine
konn1 = turtle.Turtle()
for x in range(4):
    konn1.left(nurk)
    konn1.forward(50)
    konn1.left(90)
    konn1.forward(100)
    konn1.left(90)
    konn1.forward(10)
    konn1.left(90)
    konn1.forward(90)
    konn1.right(90)
    konn1.forward(80) 
    konn1.right(90)
    konn1.forward(90)
    konn1.left(90)
    konn1.forward(10)
    konn1.left(90)
    konn1.forward(100)
    konn1.left(90)
    konn1.forward(50)
    nurk+=90


turtle.exitonclick()