from manim import *
from manim.utils import *
import math
from u import *
#求导

class test(ZoomedScene):
    '''测试'''
    def construct(self):
        ##先渲染个函数
        axes = Axes(
            x_range=(-10, 11),
            x_length=10,
            y_length=10,
            y_range=(-10, 11),
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            }
        )
        axes.add_coordinates()
        axes.move_to(LEFT*5)
        axes.move_to(DOWN)
        def darw_derivative_line(x1:2,y1:2,x2:1,y2:1,**kwargs)->VMobject:
            '''切线'''
            k= (y2-y1)/(x2-x1)
            b = (y1+y2-k*x1-k*x2)/2
            curve = axes.plot(lambda n: k*n+b, color=WHITE,x_range=[-10, 10])
            return curve
        func = lambda x: 2.5*math.sin(0.8*x)
        sin_graph = axes.plot(
            func,
            color=BLUE,
            x_range=[-10, 10], use_smoothing=True
        )
        self.play(Write(axes, lag_ratio=0.01, run_time=1))
        sin_label = axes.get_graph_label(sin_graph, "2.5*\\sin(0.8*x)")
        self.play(
            Create(sin_graph),
            FadeIn(sin_label)
        )
        dot = Dot(color=WHITE)
        
        dot.move_to(axes.i2gp(2, sin_graph))
        self.play(FadeIn(dot, scale=0.5))
        self.add(dot)
        x_tracker = ValueTracker(2)

        
        ##点移动
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), sin_graph)
        )
        ##线移动
        line = darw_derivative_line(x_tracker.get_value(),func(x_tracker.get_value()),x_tracker.get_value()+0.01,func(x_tracker.get_value()+0.01))

        def update_line(mob):
            line.become(darw_derivative_line(x_tracker.get_value(),func(x_tracker.get_value()),x_tracker.get_value()+0.01,func(x_tracker.get_value()+0.01)))
        
        ##导数值
        label = VGroup(Tex('f\'(x)= '),DecimalNumber(number=((func(x_tracker.get_value()+0.01)-func(x_tracker.get_value()))/0.01))).arrange(RIGHT).move_to(dot,UP*1.5)
        
        f_always(
            label[1].set_value,
            lambda: ((func(x_tracker.get_value()+0.01)-func(x_tracker.get_value()))/0.01)
        )
        def update_label(mob):
            label.move_to(dot,UP*2)
        label.add_updater(update_label)

        self.add(line)
        self.add(label)
        line.add_updater(update_line)
        ##相机
        def update_cammer(mob):
            mob.move_to(dot.get_center())
        self.camera.frame.save_state()
        self.camera.frame.add_updater(update_cammer)
        self.play(self.camera.frame.animate.scale(0.5).move_to(dot))
        self.play(x_tracker.animate.set_value(8), run_time=8)
        self.camera.frame.remove_updater(update_cammer)

        line.remove_updater(update_line)
        label.remove_updater(update_label)

        self.play(Restore(self.camera.frame))
        self.wait()
        
        text2 = MathTex("f'(x)=\lim_","{\Delta x \\to 0}\\frac{f(2+\Delta x) - f(2)}{\Delta x}\\\\&=\\frac{4+4\Delta x + {\Delta x}**2-4}{\Delta x}\\\\&=4").shift(RIGHT*3.2+UP*2)
        text2.set_color_by_tex("\lim_",BLUE)
        self.play(Write(text2),run_time=1.8)
        self.wait(3)
        self.wait()


class chapter1(ZoomedScene):
    '''1章'''
    ##开头
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.08,
            zoomed_display_height=10,
            zoomed_display_width=10,
            image_frame_stroke_width=10,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
                },
            **kwargs
        )
    def construct(self):
        ##标题
        axes = Axes(
            x_range=(-20, 21),
            x_length=20,
            y_length=20,
            y_range=(-20, 21),
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            }
        )
        title = Text('''
                导数

            derivative
            '''
        ,font='Microsoft YaHei',t2s={'derivative':ITALIC},t2f={'derivative':'Minecraft AE'},font_size=72,t2c={'导数':'#FFBB44','derivative':PURPLE_B}
        )
        # 临时函数
        func = lambda x: -0.00000541623631977826*x**(7)+0.0000465580780872123*x**(6)+0.000848248294303661*x**(5)-0.00809272376962430*x**(4)-0.0427788017817066*x**(3)+0.376318577897206*x**(2)+0.906174089903259*x-1.56808604655229
        graph = axes.plot(
            func,
            color=BLUE,use_smoothing=True
        )
        self.play(Create(graph))
        ##点
        tracker = ValueTracker(-10)
        dot1 = Dot(axes.i2gp(tracker.get_value(), graph)).add_updater(lambda mob: dot1.move_to(axes.i2gp(tracker.get_value(), graph)))
        self.play(Create(dot1))
        self.play(Flash(dot1, color=RED, flash_radius=0.5))

        line = darw_t_line(axes,tracker.get_value(),graph,5,c=WHITE).add_updater(
            lambda mob: line.become(
                darw_t_line(axes,tracker.get_value(),graph,5,c=WHITE)
            ))
        self.play(Create(line))
        ##播放动画
        self.play(tracker.animate.set_value(10), run_time=6,rate_func=smooth)
        self.wait(0.5)
        self.play(DrawBorderThenFill(title), run_time=2)
        self.wait(1.4)
        self.play(Transform(title,Text('导数',font_size=32,t2c={'导数':'#FFBB44'}).shift(UP*3.5+LEFT*6.5)),*[Uncreate(mob) for mob in [line,graph,dot1]])
        self.wait()





class chapter2(ZoomedScene):
    '''2章'''
    ###正片
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.08,
            zoomed_display_height=10,
            zoomed_display_width=10,
            image_frame_stroke_width=10,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
                },
            **kwargs
        )
    def construct(self):
        ##标题
        axes = Axes(
            x_range=(-5, 6),
            y_range=(-5, 13),
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            }
        ).shift(DOWN+LEFT*4)
        title=Text('导数',font_size=32,t2c={'导数':'#FFBB44'}).shift(UP*3.5+LEFT*6.5)
        self.add(title)
        func = lambda x: -4.9*x**2 + 4.8*x + 11
        graph = axes.plot(
            func,
            color=WHITE,use_smoothing=True,x_range=[0, 3]
        )
        subtitle = Text('本期视频中，我们将初步认识导数',font='Microsoft YaHei',t2c={'导数':'#DB861E'},font_size=32).shift(DOWN*3.5)
        self.add(subtitle)
        self.wait(4)
        subtitle.become(Text('不过在此之前，我们先来了解下“瞬间”概念',font='Microsoft YaHei',t2c={'瞬间':'#DB861E'},font_size=32).shift(DOWN*3.5))
        self.wait(4)
        subtitle.become(Text('在物理中，导数往往是研究物体的瞬时速度（瞬时速率）,\n加速度等的方法',font='Microsoft YaHei',t2c={'瞬时':'#DB861E'},font_size=32).shift(DOWN*3.5))
        self.wait(6)
        self.remove(subtitle)
        text = Text('如题：在一次跳水运动中，某运动员在运动过程中的\n重心相对于水面的高度h与起跳后的时间t存在函数关系:',font='Microsoft YaHei',font_size=32)
        text2 = MathTex("h(t) = -4.9t^2 + 4.8t + 11",tex_to_color_map={"h":BLUE,"t":YELLOW})
        vg = VGroup(text,text2).arrange(DOWN, buff=0.4).shift(UP*3)
        self.play(Write(vg))
        self.play(Create(axes),run_time=1)
        self.play(Create(graph),run_time=2)
        self.wait(12)
        self.play(Transform(text2,axes.get_graph_label(graph, "h(t) = -4.9t^2 + 4.8t + 11",x_val=0).shift(RIGHT*0.5).scale(0.6)))

        subtitle = Text('那么该如何描述运动员从起跳到入水的\n过程中运动的快慢程度呢',font='Microsoft YaHei',t2c={'导数':'#DB861E'},font_size=32).shift(DOWN*3.5)
        text3 = MathTex('v= ','{ {\Delta h} ','\over',' {\Delta t} }').set_color_by_tex_to_color_map({"{\Delta h}" : BLUE, "{\Delta t}" : YELLOW}).shift(RIGHT*3)
        color_dict = {"\Delta h" : BLUE, "\Delta t" : YELLOW}
        text3.set_color_by_tex_to_color_map(color_dict)
        self.add(subtitle)
        self.play(Write(text3))
        self.wait(4)
        subtitle.become(Text('已知速度v等于位移除于时间\n当t在0到0.5之间时,v=(h(0.5)-h(0))/0.5',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5))
        self.wait(5)
        self.play(text3.animate.become(MathTex('v &= ','{ {\Delta h} ','\over',' {\Delta t} }','\\\\&=','\\frac{h(0.5)-h(0)}{0.5}','\\\\&=',f'\\frac{{{func(0.5)}-{func(0)}}}{{0.5}}','\\\\&=',f'{(func(0.5)-func(0))/0.5}').set_color_by_tex_to_color_map({"{\Delta h}" : BLUE, "{\Delta t}" : YELLOW}).shift(RIGHT*3.1+UP)))
        self.wait(1)
        self.play(text3.animate.become(MathTex('v &= ','{ {\Delta h} ','\over',' {\Delta t} }','\\\\&=','\\frac{h(0.5)-h(0)}{0.5}','\\\\&=',f'\\frac{{{func(48/49)}-{func(0)}}}{{48/49}}','\\\\&=',f'{(func(48/49)-func(0))/(48/49)}').set_color_by_tex_to_color_map({"{\Delta h}" : BLUE, "{\Delta t}" : YELLOW}).shift(RIGHT*3.1+UP)))
        subtitle.become(Text('然而当t在0到49分之48之间时,平均速度v为0,\n但运动员这段时间时间内并非处于静止状态',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5))
        self.wait(8)
        self.play(FadeOut(graph,text3))
        self.play(FadeOut(text,shift=UP),FadeOut(text2,shift=UP),axes.animate.shift(UP+RIGHT*4))
        graph = axes.plot(func,color=WHITE,use_smoothing=True,x_range=[0, 3])
        self.play(FadeIn(graph))
        self.wait(2)
        subtitle.become(Text('所以，当时间间隔较长时的平均速度并不好描述运动状态',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5))
        self.wait(6)
        subtitle.become(Text('那当时间间隔短时，平均速度是否可以更好描述运动状态呢',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5))
        self.wait(6.2)
        subtitle.become(Text('事实上时间间隔趋近于0时，平均速度便会近似于该时刻的瞬时速度\n请看图',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5))

        ##点
        tracker = ValueTracker(3)
        dot1 = Dot(axes.i2gp(0.61, graph))
        dot2 = Dot(axes.i2gp(tracker.get_value(), graph),color=PURE_BLUE).add_updater(lambda mob: dot2.move_to(axes.i2gp(tracker.get_value(), graph)))
        self.play(Create(dot1),Create(dot2))
        self.play(Flash(dot1, color=RED, flash_radius=0.5),Flash(dot2, color=BLUE, flash_radius=0.5))
        line = darw_line2(dot1,dot2).set_length(15).add_updater(lambda mob: line.become(darw_line2(dot1,dot2).set_length(15)))
        self.play(Create(line))
        text3.become(MathTex('v&= ','{ {\Delta h} ','\over',' {\Delta t} }').set_color_by_tex_to_color_map({"{\Delta h}" : BLUE, "{\Delta t}" : YELLOW}).shift(RIGHT*3.5))
        ##播放动画
        self.play(tracker.animate.set_value(0.62), run_time=4)
        self.remove(subtitle,text3)
        text3 = MathTex('v &= { {\Delta h} \over {\Delta t} }\\\\&=\\frac{h({0.6 + \Delta t})-h({0.6})}{\Delta t}\\\\&=\\frac{-4.9*(0.6+ \Delta t)^2 + 4.8*(0.6+ \Delta t) + 11}{\Delta t}\\\\&=-1.08').shift(LEFT*3.2+UP).scale(0.65)
        self.wait(2)

        subtitle = Text('我们将用一个式子来概括刚才点逼近的过程',font='Microsoft YaHei',t2c={'导数':'#DB861E'},font_size=32).shift(DOWN*3.5)
        self.add(subtitle)
        self.play(Write(text3))
        self.wait(4)
        subtitle.become(Text('当时间间隔无限趋于0时，平均速度v便无限趋近于t为0.6时的瞬时速度',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5))
        self.wait(8)
        subtitle.become(Text('这便是导数在物理中最直观的体现',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5))
        self.wait(3.2)
        self.play(FadeOut(subtitle,shift=UP))
        subtitle.become(Text('现在我们需将该瞬间变化率概念抽象出来，\n对于一般函数我们是否也可以研究其瞬间变化率呢',font='Microsoft YaHei',t2c={'瞬间变化率':'#DA63A2'},font_size=32).shift(DOWN*3.5))
        self.play(Write(subtitle))
        self.wait(8)
        
        subtitle.become(
            VGroup(
                Text('不过在研究之前，还需具备',font='Microsoft YaHei',font_size=32),
                Text('极限',font='Microsoft YaHei',font_size=32,t2c={'极限':RED}),
                Text('思想',font='Microsoft YaHei',font_size=32,t2c={'思想':RED})
                ).arrange(RIGHT,buff=0).shift(DOWN*3.5))
        self.wait(4)
        self.play(FadeOut(subtitle),*[FadeOut(mob) for mob in [graph,dot1,dot2,axes,line,text3]],run_time=1.4)
        self.play(Transform(subtitle[2],Text('极限',font='Microsoft YaHei',font_size=72,t2c={'极限':GOLD})))
        self.wait()

if __name__ == "__main__":
    from os import system
    system("manim main_.py chapter1 -pql")

class chapter3(ZoomedScene):
    '''3章'''
    ###极限思想
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.08,
            zoomed_display_height=10,
            zoomed_display_width=10,
            image_frame_stroke_width=10,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
                },
            **kwargs
        )
    def construct(self):
        ##标题
        axes = Axes(
            x_range=(-10, 11),
            y_range=(-10, 11),
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2
            },
            tips=True
        ).shift(LEFT*3)
        title=Text('导数',font_size=32,t2c={'导数':'#FFBB44'}).shift(UP*3.5+LEFT*6.5)
        text = Text('极限',font='Microsoft YaHei',font_size=72,t2c={'极限':GOLD})
        self.add(title,text)
        graph = axes.plot(lambda x : 1/x,x_range=[0.05,11],color=WHITE)
        graph2 = axes.plot(lambda x : 1/x,x_range=[-10,-0.05],color=WHITE)
        graph_label = axes.get_graph_label(graph2,'f(x) = 1/x',x_val=-4).scale(0.6).shift(UP*1.8)

        self.wait(3)
        self.play(FadeOut(text,shift=DOWN))
        self.play(Create(axes),Write(graph_label))
        self.play(Create(graph2),Create(graph),run_time=2)
        text = MathTex('\lim _{','{x}',' \\rightarrow','2}','{f(x)}').scale(1.2).shift(RIGHT+UP*2).set_color_by_tex_to_color_map({"\lim" : '#9D80A5', "{x}" : '#4E94CE','2':'#C69256', "f(x)" : '#31B6FF'})
        self.play(Write(text))
        self.play(Flash(text, color=RED, flash_radius=0.5),run_time=1)
        subtitle = Text('该式子表示的是 \n当x无限趋近于2时，f(x)的近似值',font='Microsoft YaHei',t2c={'导数':'#DB861E'},font_size=32).shift(DOWN*3.5)
        self.add(subtitle)
        self.wait(6.5)
        subtitle.become(Text('其中 lim 为 limit缩写.底下表示x趋近于2.\n这个式子表示x趋近于2时右边的近似值',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5))
        self.play(Indicate(text[0]),run_time=2)
        self.play(Indicate(text[1:4]),run_time=2)
        self.play(Indicate(text[4:]),run_time=2)
        self.wait(3)
        subtitle.become(Text('显然，在本图中，可知f(2)为二分之一',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5))
        self.wait(3.2)
        self.play(Transform(text,
        MathTex('\lim _{','{x}',' \\to','\infty^+ }','{f(x)}').scale(1.2).shift(RIGHT+UP*2).set_color_by_tex_to_color_map({"\lim" : '#9D80A5', "{x}" : '#4E94CE','\infty^+':'#C69256', "f(x)" : '#31B6FF'})
        ),run_time=1.8)

        subtitle.become(Text('那么当x无限趋于无穷大时，f(x)的近似值会是什么呢',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5))
        tracker = ValueTracker(0.3)
        dot = Dot(axes.i2gp(tracker.get_value(), graph),color=PURE_BLUE).add_updater(lambda mob: dot.move_to(axes.i2gp(tracker.get_value(), graph)))
        text2 = Text(f'({round(tracker.get_value(),3)},{round(1/tracker.get_value(),3)})',font='Microsoft YaHei').next_to(dot,DOWN*2).scale(0.4).add_updater(lambda mob: 
        text2.become( Text(f'({round(tracker.get_value(),3)},{round(1/tracker.get_value(),3)})',font='Microsoft YaHei').next_to(dot,DOWN*2).scale(0.4) )
        )
        self.play(Create(dot),Write(text2))

        ##播放动画
        self.play(tracker.animate.set_value(10), run_time=4)
        self.wait(2)
        subtitle.become(Text('点向无穷大趋近时，函数值越来越小并且靠近0',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5))
        self.wait(4)
        subtitle.become(Text('当x无限趋近于无穷大时，函数值近似为0',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5))
        self.wait(5)
        subtitle.become(Text('当然极限中还有左极限与右极限等，不过目前只需极限基本思想',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5))
        self.wait(6)
        subtitle.become(Text('现在回到正题，研究函数的瞬时变化率问题',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5))
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in [subtitle,dot,text2,graph2,graph,graph_label,axes,text]])
        self.wait()



class chapter4(ZoomedScene):
    '''4章'''
    ###普通函数
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.08,
            zoomed_display_height=10,
            zoomed_display_width=10,
            image_frame_stroke_width=10,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
                },
            **kwargs
        )
    def construct(self):
        ##标题
        axes = Axes(
            x_range=(-10, 11),
            y_range=(-10, 26),
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2
            },
            tips=True
        ).shift(LEFT*2+DOWN)
        f = lambda x : x**2
        graph = axes.plot(lambda x : x**2,color=WHITE)
        graph_label = axes.get_graph_label(graph,'f(x) = x^2',x_val=0).scale(0.6).shift(DOWN*0.5+RIGHT*0.5)

        title=Text('导数',font_size=32,t2c={'导数':'#FFBB44'}).shift(UP*3.5+LEFT*6.5)
        text = Text('导数几何意义',font='Microsoft YaHei',font_size=72,t2c={'导数':GOLD})
        self.add(title)
        self.play(Write(text),run_time=1)
        self.wait(2)
        self.play(FadeOut(text,shift=DOWN))
        text = MathTex('k&= ','{ {\Delta y} ','\over',' {\Delta x} }','\\\\&= ','{ {f(','{x}','+','\Delta x',')-','f(','{x}',')} ','\over',' {\Delta x} }').scale(2).set_color_by_tex_to_color_map({"\Delta x" : '#AC80D7', "{x}" : '#4EC990','\Delta y':'#9CDCFE'})
        subtitle = Text('设y等于f(x)',font='Microsoft YaHei',t2c={'导数':'#DB861E'},font_size=32).shift(DOWN*3.5)
        self.add(subtitle)
        self.wait(2)
        self.play(Write(text))
        subtitle.become(Text('一条直线斜率k为y变化量与x变化量之比',font='Microsoft YaHei',t2c={'导数':'#DB861E'},font_size=32).shift(DOWN*3.5))
        self.wait(3)
        self.play(text.animate.scale(0.4))
        self.play(text.animate.shift(UP*3+RIGHT*4.5))
        self.play(Create(axes))
        self.play(Create(graph),Write(graph_label))
        subtitle.become(Text('如果想求x=2时的切线斜率，该怎么做呢',font='Microsoft YaHei',t2c={'导数':'#DB861E'},font_size=32).shift(DOWN*3.5))
        self.wait(3)
        ##点
        tracker = ValueTracker(3)
        dot1 = Dot(axes.i2gp(2, graph))
        dot2 = Dot(axes.i2gp(tracker.get_value(), graph)).add_updater(lambda mob: dot2.move_to(axes.i2gp(tracker.get_value(), graph)))
        self.play(Create(dot1),Create(dot2))
        line = darw_line2(dot1,dot2).set_color(GOLD).set_length(15).add_updater(lambda mob: line.become(
            darw_line2(dot1,dot2).set_color(GOLD).set_length(15)
            ))


        subtitle.become(Text('在图中取两点，连线做割线\n取定点P0为(2,4)与动点P为(3,9)',font='Microsoft YaHei',t2c={'导数':'#DB861E'},font_size=32).shift(DOWN*3.5))
        self.play(Flash(dot1, color=RED, flash_radius=0.5),Flash(dot2, color=BLUE, flash_radius=0.5))
        self.wait(2)
        self.play(Create(line))
        self.wait(2)
        line4 = DashedVMobject(darw_t_line(axes,2,graph,15,c=GRAY))
        line2 = darw_line2(
            dot1,
            Dot(axes.c2p(tracker.get_value(),f(2)))
            ).add_updater(
            lambda mob: line2.become(
            darw_line2(
            dot1,
            Dot(axes.c2p(tracker.get_value(),f(2)))
            )
            ))
        line3 = darw_line2(
            dot2,
            Dot(axes.c2p(tracker.get_value(),f(2)))
        ).add_updater(
            lambda mob: line3.become(
            darw_line2(
                dot2,
                Dot(axes.c2p(tracker.get_value(),f(2)))
            )
            ))
        ##dx dy
        Delta_x  = Brace(line2, direction=DOWN*2).add_updater(
            lambda mob: Delta_x.become(
            Brace(line2, direction=DOWN*2)
            ))
        Delta_y  = Brace(line3, direction=RIGHT*2).add_updater(
            lambda mob: Delta_y.become(
            Brace(line3, direction=RIGHT*2)
            ))
        Delta_x_text = Delta_x.get_tex("\Delta x").next_to(Delta_x,DOWN).set_color('#43BF85')
        Delta_y_text  = Delta_y.get_tex("\Delta y").next_to(Delta_y,RIGHT).set_color('#C57992')
        self.play(*[Write(mob) for mob in [line2,line3,Delta_x,Delta_y,Delta_x_text,Delta_y_text]])
        self.play(Create(line4))
        ##播放动画
        self.wait(3)
        self.play(FadeOut(subtitle,shift=LEFT))
        Delta_x_text.add_updater(lambda mob: Delta_x_text.next_to(Delta_x,DOWN))
        Delta_y_text.add_updater(lambda mob: Delta_y_text.next_to(Delta_y,RIGHT))

        self.camera.frame.save_state()

        self.camera.frame.add_updater(
            lambda mob: mob.move_to(dot2.get_center())
        )
        self.play(self.camera.frame.animate.scale(0.5).move_to(dot1.get_center()))
        self.play(tracker.animate.set_value(2.01), run_time=4)
        self.camera.frame.clear_updaters()
        self.play(Restore(self.camera.frame))
        self.wait(1.6)
        subtitle = Text('当两点横坐标间隔越来越小时，两点的割线近似于定点P的切线',font='Microsoft YaHei',t2c={'导数':'#DB861E'},font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(subtitle,shift=RIGHT))
        self.wait(6)
        subtitle.become(Text('所以当横坐标间隔极小时，切线斜率k便由割线斜率k2近似得到',font='Microsoft YaHei',t2c={'导数':'#DB861E'},font_size=32).shift(DOWN*3.5))
        self.wait(6)
        subtitle.become(Text('现在将斜率k由极限表示出来',font='Microsoft YaHei',t2c={'导数':'#DB861E'},font_size=32).shift(DOWN*3.5))
        self.play(*[FadeOut(mob) for mob in [graph,dot1,dot2,line,line2,line3,line4,Delta_x,Delta_y,Delta_x_text,Delta_y_text,axes,graph_label]],Transform(text,
            MathTex('k&= ','{ {\Delta y} ','\over',' {\Delta x} }','\\\\&= ','{ {f(','{x}','+','\Delta x',')-','f(','{x}',')} ','\over',' {\Delta x} }').scale(1.3).set_color_by_tex_to_color_map({"\Delta x" : '#AC80D7', "{x}" : '#4EC990','\Delta y':'#9CDCFE'})
        ))
        self.wait(3)
        self.play(FadeOut(text))
        text =  MathTex('k &= \lim_{ \Delta x \\to 0 }{ {\Delta y } \over { \Delta x } }',
'\\\\ &= \lim_{ \Delta x \\to 0 }{ { f(2 + \Delta x) -f(2) } \over { \Delta x } }'
'\\\\ &= \lim_{ \Delta x \\to 0 }{ { 2^2 + \Delta x^2 + 4 { \Delta x } - 2^2 } \over { \Delta x } }',
'\\\\ &= \lim_{ \Delta x \\to 0 }{ 4 + \Delta x }',
'\\\\ &= 4')
        self.play(Write(text))
        subtitle.become(Text('所以定点P切线的斜率为4',font='Microsoft YaHei',t2c={'新函数':'#DB861E'},font_size=32).shift(DOWN*3.5))
        self.wait(3)
        subtitle.become(Text('现在我们将各点斜率情况给推导出来',font='Microsoft YaHei',t2c={'新函数':'#DB861E'},font_size=32).shift(DOWN*3.5))

        self.play(Transform(text,
            MathTex('k &= \lim_{ \Delta x \\to 0 }{ {\Delta y } \over { \Delta x } }',
'\\\\ &= \lim_{ \Delta x \\to 0 }{ { f(x + \Delta x) -f(x) } \over { \Delta x } }'
'\\\\ &= \lim_{ \Delta x \\to 0 }{ { x^2 + \Delta x^2 + 2x { \Delta x } - x^2 } \over { \Delta x } }',
'\\\\ &= \lim_{ \Delta x \\to 0 }{ 2x + \Delta x }')
))
        self.wait(3)
        subtitle.become(Text('此时各点斜率组成新函数\n也代表该函数瞬时变化率',font='Microsoft YaHei',t2c={'新函数':'#DB861E'},font_size=32).shift(DOWN*3.5))
        self.wait(4)
        self.play(Transform(text,
            MathTex('f^{ \prime }({ x }) &= \lim_{ \Delta x \\to 0 }{ {\Delta y } \over { \Delta x } }',
'\\\\ &= \lim_{ \Delta x \\to 0 }{ { f(x + \Delta x) -f(x) } \over { \Delta x } }'
'\\\\ &= \lim_{ \Delta x \\to 0 }{ { x^2 + \Delta x^2 + 2x { \Delta x } - x^2 } \over { \Delta x } }',
'\\\\ &= \lim_{ \Delta x \\to 0 }{ 2x + \Delta x }')
        ))
        self.wait(2)
        subtitle.become(Text('而这便称为导函数',font='Microsoft YaHei',t2c={'导函数':'#DB861E'},font_size=32).shift(DOWN*3.5))
        self.wait(2.2)
        subtitle.become(Text('将点的横坐标代入所得的值便为该点切线斜率值的近似值',font='Microsoft YaHei',t2c={'近似值':'#DB861E','切线斜率':'#9280B5','横坐标':'#519ABA'},font_size=32).shift(DOWN*3.5))
        self.wait(4.8)
        self.play(FadeOut(subtitle,shift=DOWN))
        self.play(Transform(
            text,
            MathTex('f^{ \prime }(','{x}',') = \lim_{','\Delta x',' \\to 0 }','{ {\Delta y }',' \over ','{ \Delta x } }').scale(1.3).set_color_by_tex_to_color_map({"{x}" : '#AC80D7', "\Delta x" : '#E18E26','\Delta y':'#A86687'})
        ))
        self.play(text.animate.set_submobject_colors_by_gradient(RED, YELLOW,GREEN,BLUE),run_time=1)
        self.play(text.animate.set_submobject_colors_by_gradient(WHITE,RED,YELLOW,GREEN,BLUE),run_time=0.21,rate_func=smooth)
        self.play(text.animate.set_submobject_colors_by_gradient(RED,RED, WHITE,YELLOW,YELLOW,GREEN,BLUE),run_time=0.07,rate_func=smooth)
        self.play(text.animate.set_submobject_colors_by_gradient(RED, YELLOW,YELLOW,WHITE,GREEN,GREEN,BLUE),run_time=0.2,rate_func=smooth)
        self.play(text.animate.set_submobject_colors_by_gradient(RED, YELLOW,GREEN,GREEN,WHITE,BLUE,BLUE),run_time=0.07,rate_func=smooth)
        self.play(text.animate.set_submobject_colors_by_gradient(RED, YELLOW,GREEN,BLUE,BLUE,WHITE),run_time=0.05,rate_func=smooth)
        self.play(text.animate.set_submobject_colors_by_gradient(RED, YELLOW,GREEN,BLUE),run_time=0.12,rate_func=smooth)
        self.wait(2)
        self.play(Transform(
            text,
            Text('导数').scale(2)
            )
        )
        self.wait(1.5)
        self.play(FadeOut(text,shift=DOWN))
        self.wait()

class chapter5(ZoomedScene):
    '''5章'''
    ###终章
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.08,
            zoomed_display_height=10,
            zoomed_display_width=10,
            image_frame_stroke_width=10,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
                },
            **kwargs
        )
    def construct(self):
        ##标题
        axes = Axes(
            x_range=(-10, 11),
            y_range=(-10, 26),
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2
            },
            tips=True
        )
        f = lambda x : x**3/32
        graph = axes.plot(lambda x : x**3/32,color=GRAY_C)
        subtitle = Text('导数可以粗略地理解为函数切线斜率和瞬时变化率',font='Microsoft YaHei',t2c={'导数':'#DB861E'},font_size=32).shift(DOWN*3.5)
        self.play(Write(subtitle))
        self.wait(6)
        subtitle.become(Text('现在，我们再来看导数定义',font='Microsoft YaHei',t2c={'导数':'#DB861E'},font_size=32).shift(DOWN*3.5))
        self.wait(3)
        self.play(FadeOut(subtitle))
        color_map = {"{x}" : '#519ABA', "\Delta x" : '#E18E26','\Delta y':'#AC80D7','x_0':'#68D0FE','\lim':'#4EBE7D'}
        text = new_text([
            ['如果当',
            MathTex('\Delta x \\to 0').set_color_by_tex_to_color_map(color_map),
            '时，平均变化率',
            MathTex('{\Delta y}',' \over',' {\Delta x}').set_color_by_tex_to_color_map(color_map),
            '无限趋近于一个确定的值，即',
            MathTex('{\Delta y}',' \over',' {\Delta x}').set_color_by_tex_to_color_map(color_map)
            ],
            ['有极限，则称',
            MathTex('y = f(','{x}',')').set_color_by_tex_to_color_map(color_map),
            '在',
            MathTex('{x}','=','x_0').set_color_by_tex_to_color_map(color_map),
            '处可导'
            ],
            ['并把这个确定的值叫做',
            MathTex('y = f(','{x}',')').set_color_by_tex_to_color_map(color_map),
            '在',
            MathTex('{x}','=','x_0').set_color_by_tex_to_color_map(color_map),
            '处的'
            ],
            ['导数(也称瞬时变化率),记作'],
            [MathTex('f^{ \prime }(','{x_0}',')').set_color_by_tex_to_color_map(color_map),
            '或',
            MathTex("y' \mid _","{x","=","x_0}").set_color_by_tex_to_color_map(color_map)
            ,"，即"
            ],
            [MathTex('f^{ \prime }(','{x_0}',') = ','\lim_{','\Delta x',' \\to 0 }','{ {\Delta y }',' \over ','{ \Delta x } }','= ','\lim_{','\Delta x',' \\to 0 }','{ { f(','x_0',' + ','\Delta x',') -f(','x_0',') } ','\over',' { \Delta x } }').set_color_by_tex_to_color_map(color_map)
            ]
            ],
            font='Microsoft YaHei',s=32)
        for mob in text:
            self.play(Write(mob),run_time=2)
        self.wait(23)
        subtitle.become(Text('总的概括为以下式子',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5))
        self.play(Write(subtitle))
        self.play(
            Transform(text,
            MathTex('f^{ \prime }(','{x}',') &= ','\lim_{','\Delta x',' \\to 0 }','{ {\Delta y }',' \over ','{ \Delta x } }','\\\\&= ','\lim_{','\Delta x',' \\to 0 }','{ { f(','{x}',' + ','\Delta x',') -f(','{x}',') } ','\over',' { \Delta x } }','\\\\&=','{ { \mathrm{ d } f(','{x}',')}',' \over ','{ \mathrm{ d } ','{x}','} }'
        '\\\\&=','{ { \partial f(','{x}',')}',' \over ','{ \partial ','{x}','} }'
        ).set_color_by_tex_to_color_map(color_map)
            )
        )
        self.wait(3)
        subtitle.become(Text('其中dx与df表示微小增量，所以不用极限符号',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5))
        self.play(Indicate(text[23:29]),run_time=1.8)
        self.wait(3.2)
        subtitle.become(Text('最后一个式子用于多元函数中的偏导',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5))
        self.play(Indicate(text[30:-1]),run_time=1.8)
        self.wait(2.2)
        self.play(FadeOut(text,shift=LEFT))
        subtitle.become(Text('现在，我们再结合图像，加深理解',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5))
        self.play(FadeIn(axes,shift=LEFT),run_time=1.5)
        self.play(Create(graph))
        ##
        tracker = ValueTracker(-4)
        dot1 = Dot(axes.i2gp(tracker.get_value(), graph)).add_updater(lambda mob: dot1.move_to(axes.i2gp(tracker.get_value(), graph)))
        self.play(Create(dot1))
        self.play(Flash(dot1, color=RED, flash_radius=0.5))
        self.wait(1.5)
        self.play(FadeOut(subtitle,shift=DOWN))
        text2 = Text(f'({round(tracker.get_value(),3)},{round(f(tracker.get_value()),3)}),切线斜率k={round((f(tracker.get_value()+0.0001)-f(tracker.get_value()))/0.0001,4)}',font='Microsoft YaHei').next_to(dot1,DOWN*2).scale(0.4).add_updater(lambda mob: 
        text2.become(
            Text(f'({round(tracker.get_value(),3)},{round(f(tracker.get_value()),3)}),切线斜率k={round((f(tracker.get_value()+0.0001)-f(tracker.get_value()))/0.0001,4)}',font='Microsoft YaHei').next_to(dot1,DOWN*2).scale(0.4)
        )
        )
        line = darw_t_line(axes,tracker.get_value(),graph,5,c=WHITE).add_updater(
            lambda mob: line.become(
                darw_t_line(axes,tracker.get_value(),graph,5,c=WHITE)
            ))
        self.play(Create(line),Write(text2))
        ##播放动画
        self.play(tracker.animate.set_value(6), run_time=6,rate_func=smooth)
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in [line,text2,axes,graph,dot1]])
        self.wait(3)
        subtitle.become(Text('谢谢大家观看，我们下期视频再会',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5))
        self.play(Write(subtitle))
        self.wait(5)
        self.play(FadeOut(subtitle))
        self.wait()
class chapter6(ZoomedScene):
    '''6章'''
    ###终章2
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.08,
            zoomed_display_height=10,
            zoomed_display_width=10,
            image_frame_stroke_width=10,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
                },
            **kwargs
        )
    def construct(self):
        ##标题
        text = Text('参考：\n【官方双语】微积分的本质 - 01 -\n (https://www.bilibili.com/video/BV1cx411m78R)\n【官方双语】微积分的本质 - 02 - 导数的悖论\n (https://www.bilibili.com/video/BV1Lx411m7Vj)\n【官方双语】微积分的本质 - 07 - 极限\n (https://www.bilibili.com/video/BV1Rx411v7gV)\n\n\n《直来直去的微积分》-张景中\n《微积分学教程(卷1)》-[俄]菲赫金哥尔茨\n《高中数学选择性必修二》',font='Microsoft YaHei',font_size=32).shift(DOWN*5)
        self.add(text)
        self.play(text.animate.shift(UP*12),run_time=12,rate_func=lambda x:x)
        self.wait()
class test2(ZoomedScene):
    def construct(self):
        axes = Axes(
            x_range=(-10, 11),
            y_range=(-10, 26),
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2
            },
            tips=True
        ).shift(LEFT*2+DOWN)
        f = lambda x : x**2
        graph = axes.plot(lambda x : x**2,color=WHITE)
        # text = MathTex('v= ','{ {\Delta h} ','\over',' {\Delta t} }').set_color_by_tex_to_color_map({"{\Delta h}" : BLUE, "{\Delta t}" : YELLOW})
        line4 = DashedVMobject(darw_t_line(axes,2,graph,15,c=GRAY))
        # self.play(Transform(text3[1],Text('极限',font='Microsoft YaHei',font_size=72,t2c={'极限':GOLD})),FadeOut(text3[0]),FadeOut(text3[2]),run_time=2)
        self.add(line4,graph)

        # c = darw_line2(Dot([1,2,1]),Dot([3,-2,1]))
        # self.add(c)
        self.wait()