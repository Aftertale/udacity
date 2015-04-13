import turtle

def draw_shape():
    
    window = turtle.Screen()
    window.bgcolor("black")

    kiran = turtle.Turtle()
    kiran.shape("turtle")
    kiran.color("yellow")
    kiran.speed(2)
    L=1
    while (L <= 3):
        m=1
        if (L==3):
            kiran.forward(240)
            kiran.left(60)
            kiran.forward(240)
            kiran.right(60)
        while (m <= 2):
            n=1
            while ( n <= m ):
              if (m==2 and n==2):
                  kiran.forward(120)
                  kiran.left(60)
                  kiran.forward(120)
                  kiran.right(60)

              kiran.color("green")
              kiran.begin_fill()
              kiran.right(120)
              kiran.forward(60)
              kiran.left(120)
              kiran.forward(60)
              kiran.left(120)
              kiran.forward(60)
              kiran.end_fill()
              kiran.right(180)
              kiran.forward(60)

              kiran.color("green")
              kiran.begin_fill()      
              kiran.forward(60)
              kiran.right(120)
              kiran.forward(60)
              kiran.right(120)
              kiran.forward(60)
              kiran.end_fill()

              kiran.right(180)
              kiran.forward(60)

              kiran.color("green")
              kiran.begin_fill()
              kiran.right(120)
              kiran.forward(60)
              kiran.left(120)
              kiran.forward(60)
              kiran.left(120)
              kiran.forward(60)
              kiran.end_fill()

              kiran.right(180)
              kiran.forward(60)
              kiran.right(180)

              if (m==2 and n==2):
                  kiran.right(180)
                  kiran.forward(120)
                  kiran.right(180)

              n=n+1
            m=m+1
        L=L+1
    window.exitonclick()

draw_shape()
