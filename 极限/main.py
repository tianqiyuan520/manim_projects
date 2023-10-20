from manim import *
from manim.utils import *
import math
from u import *
from u import _t

#极限基本思想

class chapter0(ZoomedScene):
    '''序章'''
    def construct(self):
        ##标题
        title = Text('极限\n\n                     '
        ,font='Minecraft AE',font_size=82
        )
        self.play(Write(title))
        self.play(title.animate._set_color_by_t2g({'极限':['#31B6FF']}))

        self.wait(1)
        self.play(FadeOut(title,shift=LEFT))

        word = Text('本期视频中，我们将了解函数极限概念与定义',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(4.5)
        self.play(FadeOut(word))
        word = Text('不过在此之前，需先认识下函数极限的表达',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(4.1)
        self.play(FadeOut(word))

class chapter1(ZoomedScene):
    '''1章'''
    def construct(self):
        text = MathTex('\lim _{','{x}',' \\rightarrow','x_0}','{f','(','{x}',')}','=','L').scale(2.2).shift(UP*2).set_color_by_tex_to_color_map({"\lim" : '#9D80A5', "{x}" : '#FFCB13','x_0':'#CE9178', "{f" : '#24ADF3','L':'#3AC9B0'})
        self.play(Write(text))
        word = Text('其中lim为limit的缩写，底下表示变量x趋近于点x0',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word),Indicate(text[0]))
        self.wait(1)
        self.play(Indicate(text[1]),Indicate(text[2]),Indicate(text[3]))
        self.wait(5)
        self.play(FadeOut(word))
        word = Text('整个式子表示：当x趋近于点x0时f(x)极限值为L',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(Indicate(text))
        self.wait(6.1)
        self.play(FadeOut(word),FadeOut(text))
        word = Text('现在，结合函数图像，来对极限基本思想有直观认识',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(5.17)
        self.play(FadeOut(word))

class chapter2(ZoomedScene):
    '''2章'''
    def __init__(self,**kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            zoomed_display_height=5,
            zoomed_display_width=5,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
                },
            **kwargs
        )

    def construct(self):
        text_t2c = {"x" : '#FFCB13','极限值':'#3AC9B0','趋近':'#3AC9A2','函数值':'#52993E'} # 通用

        axes = Axes(
            x_range=(-5, 6),
            y_range=(-5, 6),
            axis_config={
                "stroke_color": GREY_A
            }
        ).scale(1.2).shift(LEFT*2)
        func = lambda x: x**3-3*x**2+3
        graph = axes.plot(
            func,
            color=BLUE,use_smoothing=False,x_range=[-2,1.96]
        )
        graph2 = axes.plot(
            func,
            color=BLUE,use_smoothing=False,x_range=[2.072,6]
        )
        dot1 = Dot(axes.c2p(2,1),color=BLUE)
        dot1_ = Annulus(0.07,0.08,color=BLUE).next_to(axes.c2p(2,-1),ORIGIN)
        label = MathTex(r'f({x}) =\begin{cases}{x}^3-3{x}^2+3 \quad\quad\quad &{x}\ne 2\\1&{x} = 2\end{cases}',font_size=25).next_to(axes.c2p(4,4),RIGHT*0.4+UP)
        self.play(Create(axes))
        self.play(Create(graph),run_time=0.3)
        self.play(Create(graph2),run_time=0.3)
        self.play(Write(dot1),Write(dot1_),Write(label))

        text = MathTex('\lim _{','{x}',' \\rightarrow','1}','{f','(','{x}',')}','=','?').scale(1.2).shift(UP*1.8).set_color_by_tex_to_color_map({"\lim" : '#24ADF3', "{x}" : '#FFCB13','1}':'#CE9178','?':'#3AC9B0'})
        self.play(Write(text))

        word = Text('在x轴上取一动点P，让动点P不断趋近于1，并记录点P对应的函数值',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        # 动态
        tracker = ValueTracker(-1)
        dot = always_redraw(lambda: Dot(axes.c2p(tracker.get_value(), 0),color=RED).scale(0.5))
        dot2 = always_redraw(lambda: Dot(axes.c2p(tracker.get_value(), func(tracker.get_value())),color=RED).scale(0.5))

        dot_label = always_redraw(
            lambda: Text(f'P点({round(tracker.get_value(),4)},0)',font='Microsoft YaHei',font_size=15).next_to(dot,UP)
        )
        dot_label2 = always_redraw(
            lambda: Text(f'函数值={round(func(tracker.get_value()),4)}',font='Microsoft YaHei',font_size=15).next_to(dot2,UP)
        )
        
        line = always_redraw(lambda: darw_line2(
                dot,
                dot2
                ))
        h_line = always_redraw(lambda: axes.get_horizontal_line(dot2.get_left()))
        
        self.play(FadeIn(word),text.animate.shift(UP+LEFT*5),FadeIn(dot),Indicate(dot),FadeIn(dot2),Write(dot_label),Write(dot_label2),Write(line),FadeIn(h_line))
        self.play(tracker.animate.set_value(0.8), run_time=4)
        self.wait(_t(2.5))
        self.play(FadeOut(word))
        word = Text('在动点p趋近于1时，函数值也不断趋近于1',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))

        ## 局部相机
        ##相机
        zoomed_camera = self.zoomed_camera
        ##聚焦框
        zoomed_display = self.zoomed_display
        ##选择框
        frame = zoomed_camera.frame
        ##渲染
        zoomed_display_frame = zoomed_display.display_frame

        frame.next_to(dot,UP*0.1).add_updater(lambda mob:frame.next_to(dot,UP*0.1))
        frame.set_color(WHITE)
        zoomed_display_frame.set_color(GOLD)
        zoomed_display.shift(DOWN)

        self.play(Create(frame))
        self.activate_zooming()
        self.play(FadeOut(dot_label),FadeOut(dot_label2))
        self.remove(line,h_line)
        dot_label = always_redraw(lambda: Text(f'({round(tracker.get_value(),8)},\n{round(func(tracker.get_value()),8)})',font='Microsoft YaHei',font_size=15).next_to(Dot(axes.c2p(tracker.get_value(), func(tracker.get_value())),color=RED),DOWN))
        line = always_redraw(lambda: darw_line2(dot,Dot(axes.c2p(tracker.get_value(), func(tracker.get_value())),color=RED)))
        h_line = always_redraw(lambda: axes.get_horizontal_line(Dot(axes.c2p(tracker.get_value(), func(tracker.get_value())),color=RED).get_left()))
        h_line2 = always_redraw(lambda: axes.get_horizontal_line(Dot(axes.c2p(1,1)).get_left(),color=GREEN))
        self.add(line,h_line)
        self.play(FadeIn(dot_label),FadeOut(dot2),dot.animate.scale(0.1),Create(h_line2))
        self.remove(dot)
        dot = always_redraw(lambda: Dot(axes.c2p(tracker.get_value(), 0),color=RED).scale(0.1))
        self.add(dot)
        self.play(tracker.animate.set_value(0.99999), run_time=3)

        text2 = MathTex('\lim _{','{x}',' \\rightarrow','1}','{f','(','{x}',')}','=','{1','}').scale(1.2).shift(UP*1.8+UP+LEFT*5).set_color_by_tex_to_color_map({"\lim" : '#24ADF3', "{x}" : '#FFCB13','1}':'#CE9178','{1':'#3AC9B0'})
        self.wait(_t(1.17))
        self.play(FadeOut(word),FadeOut(dot_label),Uncreate(zoomed_display_frame),FadeOut(frame),FadeOut(dot),FadeOut(line),FadeOut(h_line),FadeOut(h_line2),Transform(text,text2))

        word = Text('那么此时便可认为当x趋近于1时，f(x)极限值为1.',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(_t(5.45))
        self.play(FadeOut(word))
        word = Text('恰好f(1)=1，所以当x趋近于1时，极限值与函数值相等',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(_t(6.38))
        self.play(FadeOut(word))
        word = Text('可是，每个点极限值都会与该点的函数值相等吗',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(_t(4.45))
        self.play(FadeOut(word))
        word = Text('例如，f(2)=1.但x趋近于2时，函数值趋近于-1',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)

        dot = always_redraw(lambda: Dot(axes.c2p(tracker.get_value(), 0),color=RED).scale(0.1))
        h_line = always_redraw(lambda: axes.get_horizontal_line(Dot(axes.c2p(tracker.get_value(), func(tracker.get_value())),color=RED).get_left()))
        dot_label = always_redraw(lambda: Text(f'({round(tracker.get_value(),8)},\n{round(func(tracker.get_value()),8)})',font='Microsoft YaHei',font_size=15).next_to(dot,UP))

        line = always_redraw(lambda: darw_line2(dot,Dot(axes.c2p(tracker.get_value(), func(tracker.get_value())),color=RED)))
        tracker.set_value(1)
        self.play(FadeIn(word),*[Create(i) for i in [dot,line,h_line,dot_label]])
        self.play(tracker.animate.set_value(2), run_time=4)
        text2 = MathTex('\lim _{','{x}',' \\rightarrow','2}','{f','(','{x}',')}','=','{-1','}').scale(1.2).shift(UP*1.8+UP+LEFT*5).set_color_by_tex_to_color_map({"\lim" : '#24ADF3', "{x}" : '#FFCB13','2}':'#CE9178','{-1':'#3AC9B0'})
        self.wait(_t(2.48))
        self.play(FadeOut(word),Transform(text,text2))

        word = Text('所以从中可以发现，有时候极限值并非与函数值相等',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(_t(4.53))
        self.play(FadeOut(word),*[FadeOut(i) for i in [dot,line,h_line,dot_label,graph,dot1,dot1_,graph2,label,text]])


class chapter3(ZoomedScene):
    '''3章'''
    def construct(self):
        text_t2c = {"x" : '#FFCB13','极限值':'#3AC9B0','趋近':'#3AC9A2','函数值':'#52993E'} # 通用

        axes = Axes(
            x_range=(-5, 6),
            y_range=(-5, 6),
            axis_config={
                "stroke_color": GREY_A
            }
        ).scale(1.2).shift(LEFT*2)
        func = lambda x: 2*x**3-3*x
        func2 = lambda x: -x**3+x**2+x+1
        graph = axes.plot(
            func,
            color=BLUE,use_smoothing=False,x_range=[-5,0.96]
        )
        graph2 = axes.plot(
            func2,
            color=BLUE,use_smoothing=False,x_range=[1.05,6]
        )
        dot_k = Annulus(0.07,0.08,color=BLUE).next_to(axes.c2p(1,-1),ORIGIN)
        dot_k2 = Annulus(0.07,0.08,color=BLUE).next_to(axes.c2p(1,2),ORIGIN)
        label = MathTex(r'f({x}) =\begin{cases}2x^3-3x \quad\quad\quad &{x}< 2\\-x^3+x^2+x+1&{x} >  2\end{cases}',font_size=25).next_to(axes.c2p(4,4),RIGHT*0.4+UP)
        self.add(axes)
        self.play(Create(graph),Create(graph2),run_time=0.3)
        self.play(Create(dot_k),Create(dot_k2),Write(label))

        text = MathTex('\lim _{','{x}',' \\rightarrow','1}','{f','(','{x}',')}','=','?').scale(1.2).shift(UP*1.8).set_color_by_tex_to_color_map({"\lim" : '#24ADF3', "{x}" : '#FFCB13','1}':'#CE9178','?':'#3AC9B0'})
        word = Text('有时，函数极限值并不好判断',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(3.2)
        self.play(FadeOut(word))

        word = Text('例如：在该函数f(x)中，变量x从左侧趋近于1时，函数值趋近于-1',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word),Write(text))
        self.play(text.animate.shift(UP+LEFT*5))

        tracker = ValueTracker(0)
        dot = always_redraw(lambda: Dot(axes.c2p(tracker.get_value(), 0),color=RED).scale(0.2))
        h_line = always_redraw(lambda: axes.get_horizontal_line(Dot(axes.c2p(tracker.get_value(), func(tracker.get_value())),color=RED).get_left()))
        dot_label = always_redraw(lambda: Text(f'({round(tracker.get_value(),8)},\n{round(func(tracker.get_value()),8)})',font='Microsoft YaHei',font_size=15).next_to(dot,UP))
        line = always_redraw(lambda: darw_line2(dot,Dot(axes.c2p(tracker.get_value(), func(tracker.get_value())),color=RED)))

        self.play(*[Create(i) for i in [dot,line,h_line,dot_label]])
        
        self.play(tracker.animate.set_value(1), run_time=6)
        self.play(Indicate(dot_label))
        self.wait(_t(1.38))
        self.play(FadeOut(word))
        
        word = Text('而变量x从右侧趋近于1时，函数值趋近于2',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(*[FadeOut(i) for i in [dot,line,h_line,dot_label]])

        tracker.set_value(2)
        self.play(FadeIn(word))

        dot = always_redraw(lambda: Dot(axes.c2p(tracker.get_value(), 0),color=RED).scale(0.2))
        h_line = always_redraw(lambda: axes.get_horizontal_line(Dot(axes.c2p(tracker.get_value(), func2(tracker.get_value())),color=RED).get_left()))
        dot_label = always_redraw(lambda: Text(f'({round(tracker.get_value(),8)},\n{round(func2(tracker.get_value()),8)})',font='Microsoft YaHei',font_size=15).next_to(dot,UP+RIGHT))
        line = always_redraw(lambda: darw_line2(dot,Dot(axes.c2p(tracker.get_value(), func2(tracker.get_value())),color=RED)))

        self.play(*[Create(i) for i in [dot,line,h_line,dot_label]])

        self.play(tracker.animate.set_value(1), run_time=3)

        self.play(Indicate(dot_label))
        self.wait(_t(1.37))
        self.play(FadeOut(word))

        word = Text('从中发现，变量x从不同方向趋近时，极限值不同',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(_t(5.14))
        self.play(FadeOut(word))
        word = Text('那么当x趋近于1时，极限值是-1还是2呢',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(_t(5.34))
        self.play(FadeOut(word))
        word = Text('对此，就需要扩充下极限的概念来处理此现象',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(_t(4.18))
        self.play(FadeOut(word))
        word = Text('现在，让我们引入“左右极限”概念',font='Microsoft YaHei',font_size=32,t2c={'左右极限':YELLOW}).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(3)
        self.play(FadeOut(word))
        word = Text('该式子代表当x从左侧开始趋近x0，f(x)极限值为L1',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        text2 = MathTex('\lim _{','{x}',' \\rightarrow','x_0^-}','{f','(','{x}',')}','=','L_1').scale(1.2).shift(UP*1.8).set_color_by_tex_to_color_map({"\lim" : '#24ADF3', "{x}" : '#FFCB13','x_0^-}':'#CE9178','L_1':'#3AC9B0'})
        self.play(FadeIn(word),Transform(text,text2))
        self.wait(_t(6.26))
        self.play(FadeOut(word))
        word = Text('其中x0右上角加上-号，代表x从左侧开始趋近x0',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2)
        self.play(Indicate(text[3]))
        self.wait(_t(4.3))
        self.play(text.animate.shift(UP+LEFT*5))
        self.play(FadeOut(word))

        text2 = MathTex('\lim _{','{x}',' \\rightarrow','x_0^+}','{f','(','{x}',')}','=','L_2').scale(1.2).shift(UP*1.8).set_color_by_tex_to_color_map({"\lim" : '#24ADF3', "{x}" : '#FFCB13','x_0^-}':'#CE9178','L_2':'#3AC9B0'})
        
        word = Text('而x0右上角加上+号，代表x从右侧开始趋近x0',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word),Write(text2))
        self.wait(2)
        self.play(Indicate(text2[3]))
        self.wait(_t(4.1))
        self.play(FadeOut(word))
        self.play(text2.animate.shift(UP+LEFT*5+DOWN))

        word = Text('借左右极限概念，重新表达极限值',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word),
            text.animate.become(
                MathTex('\lim _{','{x}',' \\rightarrow','1^-}','{f','(','{x}',')}','=','-1').scale(1.2).shift(UP*1.8+UP+LEFT*5).set_color_by_tex_to_color_map({"\lim" : '#24ADF3', "{x}" : '#FFCB13','1^-}':'#CE9178','-1':'#3AC9B0'})
            ),
            text2.animate.become(
                MathTex('\lim _{','{x}',' \\rightarrow','1^+}','{f','(','{x}',')}','=','2').scale(1.2).shift(UP*1.8+LEFT*5).set_color_by_tex_to_color_map({"\lim" : '#24ADF3', "{x}" : '#FFCB13','1^+}':'#CE9178','2':'#3AC9B0'})
            )
        )
        self.wait(3.3)
        self.play(FadeOut(word))

        word = Text('从图像可知，我们并不能确定x趋近于1时的极限值\n并且左右极限并不相等',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3)
        self.play(FadeIn(word))
        self.wait(7.2)
        self.play(FadeOut(word))

        word = Text('当如果x趋近于0,时可以确定极限值，并且此时左右极限相等',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(*[FadeOut(i) for i in [dot,line,h_line,dot_label]])

        tracker.set_value(-1)

        dot2 = always_redraw(lambda: Dot(axes.c2p(-tracker.get_value(), 0),color=RED).scale(0.2))
        h_line2 = always_redraw(lambda: axes.get_horizontal_line(Dot(axes.c2p(-tracker.get_value(), func(-tracker.get_value())),color=RED).get_left()))
        dot_label2 = always_redraw(lambda: Text(f'({round(-tracker.get_value(),8)},\n{round(func(-tracker.get_value()),8)})',font='Microsoft YaHei',font_size=15).next_to(dot2,UP*2+RIGHT))
        line2 = always_redraw(lambda: darw_line2(dot2,Dot(axes.c2p(-tracker.get_value(), func(-tracker.get_value())),color=RED)))

        dot = always_redraw(lambda: Dot(axes.c2p(tracker.get_value(), 0),color=RED).scale(0.2))
        h_line = always_redraw(lambda: axes.get_horizontal_line(Dot(axes.c2p(tracker.get_value(), func(tracker.get_value())),color=RED).get_left()))
        dot_label = always_redraw(lambda: Text(f'({round(tracker.get_value(),8)},\n{round(func(tracker.get_value()),8)})',font='Microsoft YaHei',font_size=15).next_to(dot,UP+LEFT))
        line = always_redraw(lambda: darw_line2(dot,Dot(axes.c2p(tracker.get_value(), func(tracker.get_value())),color=RED)))

        self.play(*[Create(i) for i in [dot,line,h_line,dot_label,dot2,h_line2,line2,dot_label2]])

        self.play(tracker.animate.set_value(0), run_time=4)
        self.play(Indicate(dot_label),Indicate(dot_label2))
        self.play(
            text.animate.become(
                MathTex('\lim _{','{x}',' \\rightarrow','0^-}','{f','(','{x}',')}','=','0').scale(1.2).shift(UP*1.8+UP+LEFT*5).set_color_by_tex_to_color_map({"\lim" : '#24ADF3', "{x}" : '#FFCB13','0^-}':'#CE9178','0':'#3AC9B0'})
            ),
            text2.animate.become(
                MathTex('\lim _{','{x}',' \\rightarrow','0^+}','{f','(','{x}',')}','=','0').scale(1.2).shift(UP*1.8+UP+LEFT*5).set_color_by_tex_to_color_map({"\lim" : '#24ADF3', "{x}" : '#FFCB13','0^+}':'#CE9178','0':'#3AC9B0'})
            )
        )
        self.wait(2.1)
        self.play(FadeOut(word))


        word = Text('那么可以知道，当左右极限存在且相等时，x趋于x0的极限值便存在',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(_t(6.53))
        self.play(*[FadeOut(i,shift=UP) for i in [word,dot,line,h_line,dot_label,dot2,h_line2,line2,dot_label2,text,text2,dot_k,dot_k2,graph,graph2,axes,label]])
        text = MathTex(r'\lim_{',r'{x}',r' \to ',r'x_0}',r' {f(',r'{x}',r')=',r'{L}',r'}',r'\Leftrightarrow',r'\lim_{',r'{x}',r' \to ',r'x_0^-}',r' {f(',r'{x}',r')=',r'{L}',r'}',r'\lim_{',r'{x}',r' \to ',r'x_0^+}',r' {f(',r'{x}',r')=',r'{L}',r'}').scale(1.2).set_color_by_tex_to_color_map({"\lim" : '#24ADF3', "{x}" : '#FFCB13','x_0':'#CE9178','{L}':'#3AC9B0'})
        self.play(FadeIn(text,shift=UP))
        self.wait(3)
        self.play(FadeOut(text,shift=UP))
        word = Text('不过现在仍存在一个问题',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2.2)
        self.play(FadeOut(word))
        word = Text('该如何将语言上的“趋近”翻译为数学公式呢',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(_t(3.43))
        self.play(FadeOut(word))
        word = Text('即如何用数学语言严格定义“极限”概念',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(_t(3.38))
        self.play(FadeOut(word))


class chapter4(ZoomedScene):
    '''4章'''
    def construct(self):
        text_t2c = {"x" : '#FFCB13','极限值':'#3AC9B0','趋近':'#3AC9A2','函数值':'#52993E',"ε" : ORANGE, "δ" : PURPLE_C} # 通用
        title = MathTex(r'\varepsilon',' - ',r'\delta',r'\quad definition').scale(2).set_color_by_tex_to_color_map({"epsilon" : ORANGE, "delta" : PURPLE_C})
    
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.5).shift(UP*3.2+LEFT*5))
        #定义
        color_map = {"{x}" : '#FFCB13',"\lim" : '#24ADF3','x_0':'#CE9178','{L}':'#3AC9B0',"epsilon" : ORANGE, "delta" : PURPLE_C}

        definition = new_text([
            [
                '设函数',
                MathTex('f(','{x}',')').set_color_by_tex_to_color_map(color_map),
                '在点',
                MathTex('x_0').set_color_by_tex_to_color_map(color_map),
                '的某一',
                '去心邻域',
                '内有定义，'
            ],
            [
                '如果存在常数L，对于',
                MathTex(r'\forall ',r'\varepsilon',' > 0').set_color_by_tex_to_color_map(color_map)
            ],
            [
                '都',
                MathTex(r'\exists ',r'\delta','>0').set_color_by_tex_to_color_map(color_map),
                '，使不等式',
                MathTex(r'|f(','{x}',')-','L','|<',r'\varepsilon').set_color_by_tex_to_color_map(color_map)
            ],
            [
                '在',
                MathTex(r'|','{x}','-','x_0','|<',r'\delta').set_color_by_tex_to_color_map(color_map),
                '时恒成立，'
            ],
            [
                '那么常数',
                MathTex("L").set_color_by_tex_to_color_map(color_map),
                "就叫做",
                MathTex("f(","{x}",")").set_color_by_tex_to_color_map(color_map),
                "当",
                MathTex('{x}',r'\to','x_0').set_color_by_tex_to_color_map(color_map),
                "时的极限"
            ],
                "记作",
            [
                MathTex(r'\lim_{',r'{x}',r' \to ',r'x_0}',r' {f(',r'{x}',r')=',r'{L}',r'}').set_color_by_tex_to_color_map(color_map)
            ]
            ],
            font='Microsoft YaHei',s=32)
        for mob in definition:
            self.play(Write(mob),run_time=1.5)
        self.play(definition.animate.shift(LEFT*2.5))
        word = Text('其中邻域，可理解为以x0为中心的开区间',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(Indicate(definition[0][5]))
        self.wait(_t(4.18))
        self.play(FadeOut(word))
        explanation = VGroup(
            MathTex(
                r'U(x_0,\delta) = ',r'(x_0-\delta ,x_0+\delta)'
            ),
            MathTex(
                r'\overset{\circ }{U}(x_0,\delta) = \left \{x|x_0-\delta < x < x_0+\delta \right \} \\\quad\quad =',r'\{x|0 < |x-x_0| < \delta \} '
            )
        ).arrange(DOWN,buff=0.1).scale(0.7).shift(RIGHT*3.2+UP)
        word = Text('例如点x0的δ邻域为开区间(x0-δ,x0+δ)',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word),FadeIn(explanation))
        self.play(Indicate(explanation[0][1]))
        self.wait(6.1)
        self.play(FadeOut(word))
        word = Text('而空心邻域则为不包含该点的开区间',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(Indicate(explanation[1][1]))
        self.wait(_t(3.27))
        self.play(FadeOut(word))
        self.play(FadeOut(explanation))
        word = Text('其中ε表示函数值与极限值误差',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(Indicate(definition[1][1]))

        self.wait(_t(3.5))
        self.play(FadeOut(word))

        word = Text('而δ是在ε值确定下来的变量x范围大小',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(_t(4.5))
        self.play(FadeOut(word))

        self.play(FadeOut(definition,shift=LEFT))

        word = Text('或许这样不太好理解。不过没关系，让我们倒着理解试试看',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(_t(5.3))
        self.play(FadeOut(word))


class chapter5(ZoomedScene):
    '''5章'''
    def construct(self):
        text_t2c = {"x" : '#FFCB13','极限值':'#3AC9B0','趋近':'#3AC9A2','函数值':'#52993E',"ε" : ORANGE, "δ" : PURPLE_C} # 通用
        color_map = {"{x}" : '#FFCB13',"\lim" : '#24ADF3','x_0':'#CE9178','{L}':'#3AC9B0',"epsilon" : ORANGE, "delta" : PURPLE_C}

        title = MathTex(r'\varepsilon',' - ',r'\delta',r'\quad definition').scale(2).scale(0.5).set_color_by_tex_to_color_map({"epsilon" : ORANGE, "delta" : PURPLE_C}).shift(UP*3.2+LEFT*5)
        self.add(title)

        axes = Axes(
            x_range=(-5, 6),
            y_range=(-5, 6),
            axis_config={
                "stroke_color": GREY_A
            }
        ).scale(1.2).shift(LEFT)
        func = lambda x: x**2
        graph = axes.plot(
            func,
            color=BLUE,use_smoothing=True,x_range=[-5,6]
        )
        self.play(Create(axes),Create(graph))


        tracker = ValueTracker(0.5)
        tracker2 = ValueTracker(0.5)

        dot = Dot(axes.c2p(1, 0),color=RED).scale(0.2)
        h_line = axes.get_horizontal_line(Dot(axes.c2p(1, func(1))).get_left(),color=GREEN)
        dot_label = Text(f'L=1',font='Microsoft YaHei',font_size=15).next_to(h_line,UP*0.5)


        self.play(Create(dot),Create(h_line),Create(dot_label))

        a = MathTex(r'\lim_{',r'{x}',r' \to ',r'1}',r' {f(',r'{x}',r')=',r'{L}',r'=1',r'}').set_color_by_tex_to_color_map(color_map).scale(1.1).shift(UP*2+RIGHT*3)
        self.play(Write(a))

        word = Text('如果常数L为f(x)当x趋近于x0时的极限值，那么该极限值具有一个"性质"',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(Indicate(h_line),Indicate(dot_label))
        self.wait(_t(7.37))
        self.play(FadeOut(word))
        word = Text('即在极限值附近取任意大小的"误差"，\n都能至少找到一个满足不等式的空心邻域',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.2)

        func2 = lambda n: 1+tracker.get_value()
        func3 = lambda n: 1-tracker.get_value()

        curve_1 = always_redraw(lambda:axes.plot(func2, x_range=[0, 6], color=BLUE_C))
        func2_label = always_redraw(lambda:MathTex(r"\varepsilon").next_to(
            Dot(axes.c2p(5,1+tracker.get_value())),
            UP))
        curve_2 = always_redraw(lambda:axes.plot(func3, x_range=[0, 6], color=BLUE_C))
        func3_label = always_redraw(lambda:MathTex(r"-\varepsilon").next_to(
            Dot(axes.c2p(5,1-tracker.get_value())),
            DOWN))

        area = always_redraw(lambda:axes.get_area(curve_2, [0, 6], bounded_graph=curve_1, color=GREY, opacity=0.5))
        self.play(Create(curve_1),Create(curve_2),Create(area),Create(func2_label),Create(func3_label))

        self.play(FadeIn(word))
        self.play(tracker.animate.set_value(1), run_time=2)

        # 计算x空心邻域大小
        x_1 = math.sqrt(1+tracker.get_value())
        x_2 = math.sqrt(1-tracker.get_value())
        length = (x_1 - x_2)/2
        tracker2.set_value(length)
        line1 = always_redraw(lambda: darw_line2(
            Dot(axes.c2p(1+tracker2.get_value(), 0)),
            Dot(axes.c2p(1+tracker2.get_value(), func(1+tracker2.get_value())))
        ))
        line2 = always_redraw(lambda: darw_line2(
            Dot(axes.c2p(1-tracker2.get_value(), 0)),
            Dot(axes.c2p(1-tracker2.get_value(), func(1-tracker2.get_value())))
        ))
        line3 = always_redraw(lambda: darw_line2(
            Dot(axes.c2p(1,0)),
            Dot(axes.c2p(1+tracker2.get_value(), 0))
        ))
        line3_ = always_redraw(lambda: darw_line2(
            Dot(axes.c2p(1,0)),
            Dot(axes.c2p(1-tracker2.get_value(), 0))
        ))
        Delta_x  =always_redraw(lambda:Brace(line3, direction=DOWN))
        Delta_x_label = always_redraw(lambda:MathTex(r"\delta").next_to(Delta_x,DOWN))
        Delta_x_  =always_redraw(lambda:Brace(line3_, direction=DOWN))
        Delta_x_label_ = always_redraw(lambda:MathTex(r"\delta").next_to(Delta_x_,DOWN))
        self.play(*[Create(i) for i in [line1,line2,line3,line3_,Delta_x,Delta_x_label,Delta_x_,Delta_x_label_]])
        self.play(tracker2.animate.set_value(length/8), run_time=2)

        self.play(tracker.animate.set_value(0.4), run_time=2)

        x_1 = math.sqrt(1+tracker.get_value())
        x_2 = math.sqrt(1-tracker.get_value())
        length = (x_1 - x_2)/2
        self.play(tracker2.animate.set_value(length), run_time=2)

        self.play(FadeOut(word))

        word = Text('在这个空心邻域中，任意点的函数值与极限值之间距离\n始终能保持"误差"之内',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.2)

        x_1 = math.sqrt(1+tracker.get_value())
        x_2 = math.sqrt(1-tracker.get_value())
        length = -(x_1 - x_2)/2

        line4 = always_redraw(lambda: darw_line2(
            Dot(axes.c2p(1+tracker2.get_value(), 0)),
            Dot(axes.c2p(1+tracker2.get_value(), func(1+tracker2.get_value()))),
            c = RED
        ))

        Delta_y  =always_redraw(lambda:Brace(
            darw_line2(
            Dot(axes.c2p(1+tracker2.get_value(), 1)),
            Dot(axes.c2p(1+tracker2.get_value(), func(1+tracker2.get_value())))), direction=RIGHT))
        Delta_y_label = always_redraw(lambda:MathTex(r"|f(x) - L|<\varepsilon").scale(0.5).next_to(Delta_y,RIGHT))
        self.play(Create(Delta_y),Create(Delta_y_label),Create(line4))


        ##摄像机
        self.camera.frame.save_state()
        self.camera.frame.add_updater(
            lambda mob: mob.move_to(Delta_y.get_center())
        )
        self.play(self.camera.frame.animate.scale(0.5).move_to(Delta_y.get_center()))

        self.play(tracker2.animate.set_value(length), run_time=5)

        self.camera.frame.clear_updaters()
        self.play(Restore(self.camera.frame))

        self.play(FadeIn(word))
        self.wait(2.4)
        self.play(FadeOut(word))

        word = Text('那么如果常数L不为极限值，还有该"性质"吗',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(*[FadeOut(i) for i in [line1,line2,line3,line4,Delta_x,Delta_x_,Delta_x_label,Delta_x_label_,Delta_y,Delta_y_label,curve_1,curve_2,area,func2_label,func3_label,a,h_line,dot_label]])
        self.wait(3.8)
        self.play(FadeOut(word))


class chapter6(ZoomedScene):
    '''6章'''
    def construct(self):
        text_t2c = {"x" : '#FFCB13','极限值':'#3AC9B0','趋近':'#3AC9A2','函数值':'#52993E',"ε" : ORANGE, "δ" : PURPLE_C} # 通用
        color_map = {"{x}" : '#FFCB13',"\lim" : '#24ADF3','x_0':'#CE9178','{L}':'#3AC9B0',"epsilon" : ORANGE, "delta" : PURPLE_C}

        title = MathTex(r'\varepsilon',' - ',r'\delta',r'\quad definition').scale(2).scale(0.5).set_color_by_tex_to_color_map({"epsilon" : ORANGE, "delta" : PURPLE_C}).shift(UP*3.2+LEFT*5)
        self.add(title)

        axes = Axes(
            x_range=(-5, 6),
            y_range=(-5, 6),
            axis_config={
                "stroke_color": GREY_A
            }
        ).scale(1.2).shift(LEFT*1.5)
        func = lambda x: x**2
        graph = axes.plot(
            func,
            color=BLUE,use_smoothing=True,x_range=[-5,6]
        )
        self.add(axes,graph)
        word = Text('假设L=1.5为f(x)当x趋近于1时的极限值',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        h_line = axes.get_horizontal_line(Dot(axes.c2p(6, 1.5)).get_left(),color=GREEN)
        h_line2 = axes.get_horizontal_line(Dot(axes.c2p(6, 1)).get_left(),color=RED)
        dot_label = Text(f'L=1.5',font='Microsoft YaHei',font_size=15).next_to(h_line,UP*0.5)
        self.play(FadeIn(word))
        self.play(Create(h_line),Create(dot_label),Create(h_line2))
        self.play(Indicate(h_line))
        self.wait(5.3)
        self.play(FadeOut(word))
        # epsilon
        tracker = ValueTracker(1)
        tracker2 = ValueTracker(1)
        tracker3 = ValueTracker(1)
        func2 = lambda n: 1.5+tracker.get_value()
        func3 = lambda n: 1.5-tracker.get_value()

        curve_1 = always_redraw(lambda:axes.plot(func2, x_range=[0, 6], color=DARK_BROWN))
        Brach_curve_1  =always_redraw(lambda:Brace(
            darw_line2(
                Dot(axes.c2p(6,1.5+tracker.get_value())),
                Dot(axes.c2p(6,1.5))
            ), direction=RIGHT))
        Brach_curve_1_text = always_redraw(lambda:VGroup(
            MathTex(r"\varepsilon = ").scale(0.7),
            Text(f"{round(tracker.get_value(),1)}",font='Microsoft YaHei').scale(0.7)
        ).arrange(RIGHT,buff=0.1).next_to(Brach_curve_1,RIGHT*0.5))
        curve_2 = always_redraw(lambda:axes.plot(func3, x_range=[0, 6], color=DARK_BROWN))
        Brach_curve_2  =always_redraw(lambda:Brace(
            darw_line2(
                Dot(axes.c2p(6,1.5-tracker.get_value())),
                Dot(axes.c2p(6,1.5))
            ), direction=RIGHT))
        Brach_curve_2_text = always_redraw(lambda:VGroup(
            MathTex(r"\varepsilon = ").scale(0.7),
            Text(f"{round(tracker.get_value(),1)}",font='Microsoft YaHei').scale(0.7)
        ).arrange(RIGHT,buff=0.1).next_to(Brach_curve_2,RIGHT*0.5))

        self.play(*[Create(i) for i in [curve_1,curve_2,Brach_curve_1,Brach_curve_1_text,Brach_curve_2,Brach_curve_2_text]])
        #delta
        tracker2.set_value(0.2)
        line1 = always_redraw(lambda: darw_line2(
            Dot(axes.c2p(1+tracker2.get_value(), 0)),
            Dot(axes.c2p(1+tracker2.get_value(), func(1+tracker2.get_value())))
        ))
        line2 = always_redraw(lambda: darw_line2(
            Dot(axes.c2p(1-tracker2.get_value(), 0)),
            Dot(axes.c2p(1-tracker2.get_value(), func(1-tracker2.get_value())))
        ))
        line3 = always_redraw(lambda: darw_line2(
            Dot(axes.c2p(1,0)),
            Dot(axes.c2p(1+tracker2.get_value(), 0))
        ))
        line3_ = always_redraw(lambda: darw_line2(
            Dot(axes.c2p(1,0)),
            Dot(axes.c2p(1-tracker2.get_value(), 0))
        ))
        Delta_x  =always_redraw(lambda:Brace(line3, direction=DOWN))
        Delta_x_label = always_redraw(lambda:VGroup(
            MathTex(r"\delta = ").scale(0.4),
            Text(f"{round(tracker2.get_value(),1)}",font='Microsoft YaHei').scale(0.4)
        ).arrange(RIGHT,buff=0.1).next_to(Delta_x,DOWN))
        Delta_x_  =always_redraw(lambda:Brace(line3_, direction=DOWN))
        self.play(*[Create(i) for i in [line1,line2,line3,line3_,Delta_x,Delta_x_label,Delta_x_]])

        word = Text('当ε为1时，可以发现存在符合条件的x取值范围，例如δ为0.2或0.1等',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2)
        self.play(Indicate(Brach_curve_1_text),Indicate(Brach_curve_2_text),Indicate(Delta_x_label))
        self.wait(6.5)
        self.play(FadeOut(word))
        word = Text('在该x取值范围中，任意函数值与极限值差值的绝对值小于ε',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)

        tracker3.set_value(tracker2.get_value())
        line4 = always_redraw(lambda: darw_line2(
            Dot(axes.c2p(1+tracker3.get_value(), 0)),
            Dot(axes.c2p(1+tracker3.get_value(), func(1+tracker3.get_value()))),
            c = RED
        ))

        Delta_y  =always_redraw(lambda:Brace(
            darw_line2(
            Dot(axes.c2p(1+tracker3.get_value(), 1.5)),
            Dot(axes.c2p(1+tracker3.get_value(), func(1+tracker3.get_value())))), direction=RIGHT))
        Delta_y_label = always_redraw(
            lambda:
                MathTex(r"|f(x) - L|<\varepsilon").scale(0.5).next_to(Delta_y,RIGHT) if abs(func(1+tracker3.get_value())-1.5) < tracker.get_value() else (MathTex(r"|f(x) - L|=\varepsilon").scale(0.5).next_to(Delta_y,RIGHT) if abs(func(1+tracker3.get_value())-1.5) == tracker.get_value() else MathTex(r"|f(x) - L|>\varepsilon").scale(0.5).next_to(Delta_y,RIGHT))
        )
        self.play(Create(Delta_y),Create(Delta_y_label),Create(line4))
        self.play(FadeIn(word))

        self.play(tracker3.animate.set_value(-tracker2.get_value()), run_time=4)
        self.wait(2.3)
        self.play(FadeOut(word))

        word = Text('当δ为0.15时，也满足函数值与极限值的关系',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(tracker2.animate.set_value(0.15), run_time=1.5)

        ##摄像机
        self.camera.frame.save_state()
        self.camera.frame.add_updater(
            lambda mob: mob.move_to(Delta_y.get_center())
        )
        self.play(self.camera.frame.animate.scale(0.3).move_to(Delta_y.get_center()), run_time=2)

        self.play(tracker3.animate.set_value(tracker2.get_value()), run_time=4)

        self.camera.frame.clear_updaters()
        self.play(Restore(self.camera.frame))

        self.play(FadeOut(word))
        
        word = Text('也就是说，在ε为1的情况下，δ<1-(0.5)^0.5\n便可以满足函数值与极限值的关系',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.2)
        self.play(FadeIn(word))
        self.wait(3)
        self.play(Indicate(Delta_x_label),Indicate(Delta_y_label))
        self.wait(6.3)
        self.play(FadeOut(word))
        word = Text('但是ε<0.5时，并不存在符合条件的x取值范围.例如ε=0.4',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2)
        self.play(tracker.animate.set_value(0.4), run_time=2)
        self.wait(4)
        self.play(FadeOut(word))
        word = Text('也就是说，在点x0的附近中，不再是\n任意函数值与极限值差值的绝对值小于ε',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.2)
        self.play(FadeIn(word))
        ##摄像机
        self.camera.frame.save_state()
        self.camera.frame.add_updater(
            lambda mob: mob.move_to(Delta_y.get_center())
        )
        self.play(self.camera.frame.animate.scale(0.3).move_to(Delta_y.get_center()), run_time=2)
        self.play(tracker3.animate.set_value(-tracker2.get_value()), run_time=4)
        self.camera.frame.clear_updaters()
        self.play(Restore(self.camera.frame))
        self.wait(1.1)
        self.play(FadeOut(word))

        word = Text('所以当常数L不为极限值时，便不具备该"性质"',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(4.2)
        self.play(*[FadeOut(i) for i in [word,curve_1,curve_2,Brach_curve_1,Brach_curve_1_text,Brach_curve_2,Brach_curve_2_text,Delta_y,Delta_y_label,line4,line1,line2,line3,line3_,Delta_x,Delta_x_label,Delta_x_,dot_label,h_line,h_line2,graph,axes]])

class chapter7(ZoomedScene):
    '''7章'''
    def construct(self):
        text_t2c = {"x" : '#FFCB13','极限值':'#3AC9B0','趋近':'#3AC9A2','函数值':'#52993E',"ε" : ORANGE, "δ" : PURPLE_C} # 通用
        color_map = {"{x}" : '#FFCB13',"\lim" : '#24ADF3','x_0':'#CE9178','{L}':'#3AC9B0',"epsilon" : ORANGE, "delta" : PURPLE_C}

        title = MathTex(r'\varepsilon',' - ',r'\delta',r'\quad definition').scale(2).scale(0.5).set_color_by_tex_to_color_map({"epsilon" : ORANGE, "delta" : PURPLE_C}).shift(UP*3.2+LEFT*5)
        self.add(title)

        axes = Axes(
            x_range=[-5,5,1],
            y_range=[-1,8,1],
            axis_config={
                "stroke_color": GREY_A
            }
        ).shift(DOWN*0.5)
        func = lambda x: x**2
        graph = axes.plot(
            func,
            color=BLUE_C,use_smoothing=True,x_range=[-5,6]
        )
        
        word = Text('不过现在让我们用集合的角度重新理解 ε-δ definition',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        definition = new_text([
            [
                MathTex(r'\lim_{',r'{x}',r' \to ',r'x_0}',r' {f(',r'{x}',r')=',r'{L}',r'}').set_color_by_tex_to_color_map(color_map)
            ],
            [
                MathTex(r'\Leftrightarrow \forall ',r'\varepsilon',r' >0,\exists ',r'\delta',' >0,').set_color_by_tex_to_color_map(color_map),
                "当",
                MathTex(r'|','{x}','-',r'x_0',r'|<',r'\delta').set_color_by_tex_to_color_map(color_map),
                "时，恒有",
                MathTex(r'|f(','{x}',r')-',r'{L}','|<',r'\varepsilon').set_color_by_tex_to_color_map(color_map)
            ]
        ],font='Microsoft YaHei',s=32).shift(UP)
        self.play(FadeIn(word),FadeIn(definition))
        self.wait(5.2)
        self.play(FadeOut(word))

        word = Text('将不等式变形',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word),
            Transform(
                definition[1][2],
                MathTex(r'A:\quad\quad',r'x_0','-',r'\delta','<','{x}','<',r'x_0',r'+',r'\delta').set_color_by_tex_to_color_map(color_map).next_to(definition[1][1],DOWN)
            ),
            FadeOut(definition[1][3]),
            Transform(
                definition[1][4],
                MathTex(r'B:\quad\quad',r'{L}','-',r'\varepsilon','<',r'f(','{x}',r')<',r'{L}','+',r'\varepsilon').set_color_by_tex_to_color_map(color_map).next_to(definition[1][1],DOWN*3.5)
            )
        )
        self.wait(1.5)
        self.play(FadeOut(word))

        word = Text('因为恒成立，所以不等式A是不等式B的充分条件',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2)
        self.play(Indicate(definition[1][2]))
        self.wait(1.5)
        self.play(Indicate(definition[1][4]))
        self.wait(1)
        self.play(FadeOut(word))

        word = Text('假设函数f(x)在x0-δ到x0+δ开区间中为单调递增',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(7)
        self.play(FadeOut(word))

        word = Text('那么可将不等式A变形为f(x)的形式',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(FadeOut(definition[0]),FadeOut(definition[1][0]),FadeOut(definition[1][1]))
        self.play(Transform(
            definition[1][2],
            MathTex(r'A:\quad\quad','f(',r'x_0','-',r'\delta',')','<','f(','{x}',')','<','f(',r'x_0',r'+',r'\delta',')',r'\Rightarrow').set_color_by_tex_to_color_map(color_map).next_to(definition[1][2],ORIGIN)
        ))
        self.play(definition[1][2].animate.scale(0.7).shift(UP*2.5+LEFT*2),definition[1][4].animate.scale(0.7).shift(UP*2.5+LEFT*2))
        self.wait(3)
        self.play(FadeOut(word))
        word = Text('由于A是B的充分条件,A与B都存在，所以A为B的子集',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(Indicate(definition[1][2]),Indicate(definition[1][4]))
        definition2 = MathTex(r'A \subseteq B').set_color_by_tex_to_color_map(color_map).scale(0.7).next_to(definition[1][4],DOWN*2)
        self.play(Write(definition2))
        self.wait(5.5)
        self.play(FadeOut(word))
        

        word = Text('现在通过函数图像验证这个想法',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(Create(axes),Create(graph))
        self.wait(3)
        self.play(FadeOut(word))
        word = Text('求x趋近于2时的极限值',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(3)
        self.play(FadeOut(word))
        word = Text('从图中可知极限值为4，设L为4',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        h_line = axes.get_horizontal_line(Dot(axes.c2p(5,4)).get_left(),color=GREEN)
        self.play(FadeIn(word),Create(h_line))
        self.wait(3.5)
        self.play(FadeOut(word))

        word = Text('当ε为2，存在δ>0，存在满足不等式B恒成立的x取值范围',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        L = 4
        x0 = 2
        # epsilon
        tracker = ValueTracker(2)
        tracker2 = ValueTracker(1)
        tracker3 = ValueTracker(1)
        func2 = lambda n: L+tracker.get_value()
        func3 = lambda n: L-tracker.get_value()

        curve_1 = always_redraw(lambda:axes.plot(func2, x_range=[0, 5], color=DARK_BROWN))
        Brach_curve_1  =always_redraw(lambda:Brace(
            darw_line2(
                Dot(axes.c2p(4,L+tracker.get_value())),
                Dot(axes.c2p(4,L))
            ), direction=RIGHT))
        Brach_curve_1_text = always_redraw(lambda:VGroup(
            MathTex(r"\varepsilon = ").scale(0.7),
            Text(f"{round(tracker.get_value(),1)}",font='Microsoft YaHei',font_size=20).scale(0.7)
        ).arrange(RIGHT,buff=0.1).next_to(Brach_curve_1,RIGHT*0.5))
        curve_2 = always_redraw(lambda:axes.plot(func3, x_range=[0, 5], color=DARK_BROWN))
        Brach_curve_2  =always_redraw(lambda:Brace(
            darw_line2(
                Dot(axes.c2p(4,L-tracker.get_value())),
                Dot(axes.c2p(4,L))
            ), direction=RIGHT))
        Brach_curve_2_text = always_redraw(lambda:VGroup(
            MathTex(r"\varepsilon = ").scale(0.7),
            Text(f"{round(tracker.get_value(),1)}",font='Microsoft YaHei',font_size=20).scale(0.7)
        ).arrange(RIGHT,buff=0.1).next_to(Brach_curve_2,RIGHT*0.5))

        #delta
        tracker2.set_value(1)
        line1 = always_redraw(lambda: darw_line2(
            Dot(axes.c2p(x0+tracker2.get_value(), 0)),
            Dot(axes.c2p(x0+tracker2.get_value(), func(x0+tracker2.get_value())))
        ))
        line2 = always_redraw(lambda: darw_line2(
            Dot(axes.c2p(x0-tracker2.get_value(), 0)),
            Dot(axes.c2p(x0-tracker2.get_value(), func(x0-tracker2.get_value())))
        ))
        line3 = always_redraw(lambda: darw_line2(
            Dot(axes.c2p(x0,0)),
            Dot(axes.c2p(x0+tracker2.get_value(), 0))
        ))
        line3_ = always_redraw(lambda: darw_line2(
            Dot(axes.c2p(x0,0)),
            Dot(axes.c2p(x0-tracker2.get_value(), 0))
        ))
        Delta_x  =always_redraw(lambda:Brace(line3, direction=DOWN))
        Delta_x_label = always_redraw(lambda:VGroup(
            MathTex(r"\delta = ").scale(0.4),
            Text(f"{round(tracker2.get_value(),x0)}",font='Microsoft YaHei').scale(0.4)
        ).arrange(RIGHT,buff=0.1).next_to(Delta_x,DOWN))
        Delta_x_  =always_redraw(lambda:Brace(line3_, direction=DOWN))

        self.play(*[Create(i) for i in [curve_1,curve_2,Brach_curve_1,Brach_curve_1_text,Brach_curve_2,Brach_curve_2_text,line1,line2,line3,line3_,Delta_x,Delta_x_label,Delta_x_]])
        self.play(Indicate(Brach_curve_1_text),Indicate(Brach_curve_2_text))
        self.play(tracker2.animate.set_value(0.35))
        self.play(Indicate(Delta_x_label))
        self.wait(6.8)
        self.play(FadeOut(word))
        word = Text('图中的红色线段代表不等式A的集合，橙色线段为不等式B的集合',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)

        A = always_redraw(lambda: darw_line2(
            Dot(axes.c2p(x0+tracker2.get_value(),func(x0-tracker2.get_value()))),
            Dot(axes.c2p(x0+tracker2.get_value(), func(x0+tracker2.get_value()))),
            c=RED))
        B = always_redraw(lambda: darw_line2(
            Dot(axes.c2p(math.sqrt(4+tracker.get_value()),4-tracker.get_value())),
            Dot(axes.c2p(math.sqrt(4+tracker.get_value()), 4+tracker.get_value())),
            c=ORANGE))

        self.play(FadeIn(word))
        self.play(Create(A),Create(B))
        self.wait(2)
        self.play(Indicate(A))
        self.wait(3)
        self.play(Indicate(B))
        self.wait(1)
        self.play(FadeOut(word))

        self.play(tracker2.animate.set_value(0.449))
        word = Text('δ从0.449缩小到0.01时,红色长度始终小于橙色,即A仍旧为B的子集',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(tracker2.animate.set_value(0.01),run_time=5)
        self.wait(3)
        self.play(FadeOut(word))
        self.play(*[FadeOut(i,shift=DOWN) for i in [curve_1,curve_2,Brach_curve_1,Brach_curve_1_text,Brach_curve_2,Brach_curve_2_text,line1,line2,line3,line3_,Delta_x,Delta_x_label,Delta_x_,h_line,A,B,graph,axes,definition[1][2],definition[1][4],definition2]])
        word = Text('在代数上则可以表示为A的左右端点在B中',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(4)
        self.play(FadeOut(word))


class chapter8(ZoomedScene):
    '''8章'''
    def construct(self):
        text_t2c = {"x" : '#FFCB13','极限值':'#3AC9B0','趋近':'#3AC9A2','函数值':'#52993E',"ε" : ORANGE, "δ" : PURPLE_C} # 通用
        color_map = {"{x}" : '#FFCB13',"\lim" : '#24ADF3','x_0':'#CE9178','{L}':'#3AC9B0',"epsilon" : ORANGE, "delta" : PURPLE_C}

        title = MathTex(r'\varepsilon',' - ',r'\delta',r'\quad definition').scale(2).scale(0.5).set_color_by_tex_to_color_map({"epsilon" : ORANGE, "delta" : PURPLE_C}).shift(UP*3.2+LEFT*5)
        self.add(title)
        a =VGroup(
            MathTex('f(',r'x_0','-',r'\delta',')','<','f(','{x}',')','<','f(',r'x_0',r'+',r'\delta',')',r'\Rightarrow',r'{L}','-',r'\varepsilon','<',r'f(','{x}',r')<',r'{L}','+',r'\varepsilon').set_color_by_tex_to_color_map(color_map),
            VGroup(
                MathTex(r'f(','x_0','+',r'\delta',')<','{L}',' + ',r'\varepsilon').set_color_by_tex_to_color_map(color_map),
                MathTex(r'f(','x_0','-',r'\delta',')>','{L}',' - ',r'\varepsilon').set_color_by_tex_to_color_map(color_map)
            ).arrange(DOWN, buff=LARGE_BUFF)
        ).arrange(DOWN, buff=LARGE_BUFF)
        b = Brace(a[1],direction=LEFT)
        self.play(Write(a[0]))
        self.play(Indicate(a[0]))
        self.wait(1)
        self.play(
            TransformMatchingTex(
                a[0].copy(), a[1]
            ),
            Write(b),
            run_time=2
        )
        self.wait(1)
        self.play(FadeOut(a[0]),a[1].animate.shift(UP),b.animate.shift(UP))
        c = MathTex(r'\varepsilon' ,'>',r'f(','x_0','+',r'\delta',')',r'-f(','x_0','-',r'\delta',')',r'\over','2').next_to(a[1],ORIGIN+UP).set_color_by_tex_to_color_map(color_map)
        self.play(
            FadeOut(b),
            TransformMatchingTex(
                a[1], c,
                path_arc=90 * DEGREES,
            ),
            run_time=2
        )

        d =VGroup(
            VGroup(
                MathTex(r'\varepsilon' ,'>').set_color_by_tex_to_color_map(color_map),
                MathTex(r'4+',r'\delta','^2','+4',r'\delta',r'-4-',r'\delta','^2','+4',r'\delta',r'\over','2').set_color_by_tex_to_color_map(color_map)
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r'\delta','<').set_color_by_tex_to_color_map(color_map),
                MathTex(r'\varepsilon',r'\over','4').set_color_by_tex_to_color_map(color_map)
            ).arrange(RIGHT, buff=0.1)
        ).arrange(DOWN, buff=LARGE_BUFF).next_to(c,DOWN)

        word = Text('代入函数f(x)=x^2和x0=2',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(
            TransformMatchingTex(
                c.copy(), d[0]
            ),
            run_time=2
        )
        self.play(
            TransformMatchingTex(
                d[0].copy(), d[1]
            ),
            run_time=2
        )
        self.wait(1)
        self.play(FadeOut(word))
        word = Text('以上方法适用于单调区间中辅助理解',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(FadeOut(c,shift=UP),FadeOut(d[0],shift=UP),d[1].animate.shift(UP*2))
        self.play(Indicate(d[1]))
        self.wait(3.5)
        self.play(FadeOut(word),FadeOut(d[1],shift=UP))
        word = Text('实际使用 ε-δ definition 证明极限时',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN)
        self.play(FadeIn(word))
        self.wait(4)
        self.play(FadeOut(word))
        word = Text('是以ε确定δ，得出δ与ε之间的关系',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN)
        self.play(FadeIn(word))
        self.wait(5)
        self.play(FadeOut(word))
        word = Text('使得|f(x)-L|的化简结果可以由δ表示',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN)
        self.play(FadeIn(word))
        self.wait(5)
        self.play(FadeOut(word))
        word = Text('在根据δ与ε之间的关系,便推出|f(x)-L|<ε',font='Microsoft YaHei',font_size=32,t2c=text_t2c).shift(DOWN)
        self.play(FadeIn(word))
        self.wait(7)
        self.play(FadeOut(word))
        self.play(FadeOut(title))
        word = Text('End',font='Microsoft YaHei',font_size=32,t2c=text_t2c)
        self.play(FadeIn(word))
        self.wait(2)
        self.play(FadeOut(word))
