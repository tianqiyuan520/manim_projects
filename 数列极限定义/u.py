from manim import *
from manim.utils import *
import math
'''工具库'''

def darw_line(axes:Axes,x1:2,y1:2,x2:1,y2:1,**kwargs)->VMobject:
    '''线性函数'''
    k= (y2-y1)/(x2-x1)
    b = (y1+y2-k*x1-k*x2)/2
    curve = axes.plot(lambda n: k*n+b, color=WHITE)
    return curve
def darw_line2(dot1:Dot,dot2:Dot,**kwargs)->Line:
    '''连线'''
    c=WHITE
    for key, value in kwargs.items():
        if(key=='c'or key ==  'color'):
            c = value
    return Line(np.array((dot1.get_x(),dot1.get_y(),0)),np.array((dot2.get_x(),dot2.get_y(),0)),color=c)

def darw_t_line(axes:Axes,x1:2,func:ParametricFunction,length:10,**kwargs)->Line:
    '''该点切线\nx1为横坐标值'''
    c=WHITE
    isDashed = False
    
    for key, value in kwargs.items():
        if(key=='c'or key ==  'color'):
            c = value
        elif(key=='isDashed'or key ==  'd'):
            isDashed = True
    if isDashed: return DashedVMobject(Line(axes.i2gp(x1,func),axes.i2gp(x1+0.0001,func),color=c).set_length(length))
    return Line(axes.i2gp(x1,func),axes.i2gp(x1+0.0001,func),color=c).set_length(length)

def new_text(text_list=None,**kwargs)->VGroup:
    if text_list is None:
        text_list = []
    '''中文与公式混搭
    text_list二维数组 [
        [Text(),MathTex()],
        []
    ]
    '''
    font = ""
    font_size=DEFAULT_FONT_SIZE
    for key, value in kwargs.items():
        if(key=='f'or key ==  'font'):
            font = value
        elif(key=='s'or key ==  'size'):
            font_size=value
    result = VGroup()
    for i in text_list:
        item = VGroup()
        for j in i :
            if(isinstance(j,str)):
                if(j[0]!='$'and j[-1]!='$'):
                    j = Text(j,font=font)
                else:
                    j = MathTex(j[1:-1])
            elif(isinstance(j,Text)):
                j = Text(j.text,font=font)
            if(isinstance(j,Text)):
                j.font_size = font_size
            else:
                j.font_size = font_size+10
            item.add(j)
        result.add(item.arrange(RIGHT,buff=0.1))
    return result.arrange(DOWN,buff=0.3, aligned_edge=LEFT)

def _t(time:float):
    var = str(time - int(time))
    var2 = var[var.find('.') + 1 :]
    var3 = (int(var2)/(6*10**(len(var2)-1)))
    return round(int(time)+var3,5)

def buildSequence(axes:Axes,n:[0],func:lambda:1,**kwargs)->"list[Dot]":
    '''定义数列函数图像'''
    return [Dot(axes.c2p(i,func(i))) for i in n]
