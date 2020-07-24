import turtle as t


t.speed("fast")#控制勾勒速度
t.hideturtle()#隐藏箭头
t.bgcolor("black")#背景色

i=0
while i < 135:
               t.pencolor("green")#线的颜色
               t.penup()
               t.goto(0,0)
               t.forward(200)
               t.pendown()
               t.circle(100)
               t.left(2)
               i +=1