import turtle
def draw_triangle(t,size):
    #تابعی برای ترسیم مثلث 
    t.begin_fill()   
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(120)  
    t.end_fill()  

def draw_ser(t,n,size):
    if n==0:
        draw_triangle(t,size)
    else:
        #ترسیم اولین مثلث
        draw_ser(t,n-1,size/2)
        #جلو رفتن 
        t.forward(size/2)
        # ترسیم مثلث دوم
        draw_ser(t,n-1,size/2)
        #رفتن به بالا برای ترسیم مثلث سوم
        t.left(120)
        t.forward(size/2)
        t.right(120)
        #ترسیم مثلث سوم
        draw_ser(t,n-1,size/2)
        #برگشتن به مبدا حرکت
        t.right(120)
        t.forward(size/2)
        t.left(120)

t = turtle.Turtle()
t.fillcolor("violet")
draw_ser(t,3,300)
# جلوگیری از بسته شدن پنجره
turtle.mainloop()


    