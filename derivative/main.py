from manim import *
from manim.utils import *
import math
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
        label = VGroup(Tex('f\'(x)= '),DecimalNumber(number=((func(x_tracker.get_value()+0.001)-func(x_tracker.get_value()))/0.001))).arrange(RIGHT).move_to(dot,UP*1.5)
        
        f_always(
            label[1].set_value,
            lambda: ((func(x_tracker.get_value()+0.001)-func(x_tracker.get_value()))/0.001)
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



class chapter1(ZoomedScene):
    '''序章'''
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
        ##先渲染个函数
        axes = Axes(
            x_range=(-10, 26),
            x_length=9,
            y_length=9,
            y_range=(-10, 26),
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            }
        )
        axis_labels = axes.get_axis_labels()
        axes.shift(LEFT*3+DOWN)
        axis_labels.shift(LEFT*3+DOWN)
        def darw_line(x1:2,y1:2,x2:1,y2:1,**kwargs)->VMobject:
            '''直线'''
            k= (y2-y1)/(x2-x1)
            b = (y1+y2-k*x1-k*x2)/2
            curve = axes.plot(lambda n: k*n+b, color=WHITE,x_range=[-10, 10])
            return curve

        def darw_line2(pos1,pos2,color:WHITE,**kwargs)->Line:
            '''连线'''
            return Line(pos1,pos2,color=color)

        func = lambda x: x**2
        graph = axes.plot(
            func,
            color=RED_C,
            x_range=[-10, 10], use_smoothing=True
        )
        self.play(Write(axes, lag_ratio=0.01, run_time=1),FadeIn(axis_labels))
        func_label = axes.get_graph_label(graph, "x^2")
        self.play(Create(graph),run_time=2)
        self.play(FadeIn(func_label))

        

        #两点连线 动态线
        dot1 = Dot(axes.i2gp(2, graph))
        tracker = ValueTracker(5)
        dot2 = Dot(axes.i2gp(5, graph))
        ##点移动
        f_always(dot2.move_to,lambda: axes.i2gp(tracker.get_value(), graph))
        line = darw_line(2,func(2),5,func(5)).add_updater(lambda mob: line.become(darw_line(2,func(2),tracker.get_value(),func(tracker.get_value()))))
        ##
        line2 = darw_line2(axes.c2p(2,func(2)),axes.c2p(5,func(2)), color=WHITE).add_updater(lambda mob: line2.become(darw_line2(axes.c2p(2,func(2)),axes.c2p(tracker.get_value(),func(2)), color=WHITE)))

        line3 = darw_line2(axes.c2p(5,func(2)),axes.c2p(tracker.get_value(),func(tracker.get_value())), color=WHITE).add_updater(lambda mob: line3.become(darw_line2(axes.c2p(tracker.get_value(),func(2)),axes.c2p(tracker.get_value(),func(tracker.get_value())), color=WHITE)))
        
        ##dx dy
        Delta_x  = Brace(line2).add_updater(lambda mob: Delta_x.become(Brace(line2, direction=DOWN*2)))
        Delta_y  = Brace(line3).add_updater(lambda mob: Delta_y.become(Brace(line3, direction=RIGHT*2)))

        Delta_x_text = Delta_x.get_tex("\Delta x").add_updater(lambda mob: Delta_x_text.next_to(Delta_x,DOWN))
        Delta_y_text  = Delta_y.get_tex("\Delta y").next_to(Delta_y,RIGHT).add_updater(lambda mob: Delta_y_text.next_to(Delta_y,RIGHT))

        self.play(Create(dot1),Create(dot2),Create(line),Create(line2),Create(line3),FadeIn(Delta_x),FadeIn(Delta_y),Create(Delta_x_text),Create(Delta_y_text))

        ##公式
        text = VGroup(MathTex('k = \\frac{\\Delta y}{\\Delta x}',' = '),DecimalNumber(
            (func(tracker.get_value()) - func(2))/(tracker.get_value()-2)
        )).arrange(RIGHT).shift(RIGHT*3+DOWN).add_updater(lambda mob: text[1].set_value(
            (func(tracker.get_value()) - func(2))/(tracker.get_value()-2)
        ))
        self.play(Write(text))

        self.play(tracker.animate.set_value(3), run_time=3)


        ##相机
        zoomed_camera = self.zoomed_camera
        ##渲染框
        zoomed_display = self.zoomed_display
        ##选择框
        frame = zoomed_camera.frame
        ##渲染框里的 帧
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(dot1).shift(RIGHT*0.3+UP*0.3)
        # frame.add_updater(lambda mob: frame.move_to(dot1))
        frame.set_color(WHITE)
        zoomed_display_frame.set_color(GOLD)
        zoomed_display.scale([0.3, 0.3, 0])
        zoomed_display.shift(UP*3+RIGHT*2)

        self.play(Create(frame))
        self.activate_zooming()
        self.play(FadeIn(zoomed_display_frame))
        self.play(tracker.animate.set_value(2.0001), run_time=3)
        frame.remove_updater(lambda mob: frame.move_to(dot2))
        dot2.remove_updater(lambda mob: mob.move_to(axes.i2gp(3, graph)))
        line.remove_updater(lambda mob: line.become(darw_line(2,func(2),tracker.get_value(),func(tracker.get_value()))))
        line2.clear_updaters()
        line3.clear_updaters()
        self.wait()

        self.play(FadeOut(frame),FadeOut(zoomed_display_frame))
        self.play(FadeOut(Delta_x_text),FadeOut(Delta_y_text),FadeOut(dot1),FadeOut(dot2),Unwrite(line),Unwrite(line2),Unwrite(line3),Unwrite(text),FadeOut(axis_labels),Unwrite(graph),FadeOut(func_label),Unwrite(axes))
        self.clear()
        self.wait()


class chapter2(ZoomedScene):
    '''1章'''
    def construct(self):
        ##标题
        title = Text('''
                导数

            derivative
            '''
        ,font='Microsoft YaHei',t2s={'derivative':ITALIC},t2f={'derivative':'Minecraft AE'},font_size=52
        )
        self.play(Write(title))
        self.wait(0.5)
        self.play(title.animate._set_color_by_t2g({'导数':['#FFBB44','#FFC031'],'derivative':[PURPLE_B,PURPLE_C]}))
        self.wait(0.5)
        self.play(Transform(title,Text('导数',font_size=32).shift(UP*3.5+LEFT*6.5)))

        self.wait(0.3)

        text = Text('那么什么是导数\n导数的定义又是什么呢',font='Microsoft YaHei')
        self.play(FadeIn(text, shift=UP))
        self.wait(0.8)
        self.play(FadeOut(text, shift=UP))
        text = Text('通俗而言，导数为该函数变化趋势\n为该点切线的斜率\n这也是非常直观的几何意义',font='Microsoft YaHei')
        self.play(FadeIn(text, shift=UP))
        self.wait(1.2)
        self.play(FadeOut(text, shift=UP))
        self.wait()

class chapter3(ZoomedScene):
    '''2章'''
    def construct(self):
        title = Text('导数',font_size=32).shift(UP*3.5+LEFT*6.5)
        self.add(title)
        def text_(a,t,t2):
            '''台词'''
            self.play(FadeIn(a),run_time=t2)
            self.wait(t)
            self.play(FadeOut(a),run_time=t2)

        axes = Axes(
            x_range=(-5, 6),
            y_range=(-5, 6),
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            }
        )
        axis_labels = axes.get_axis_labels()

        def darw_line2(pos1,pos2,color:WHITE,**kwargs)->Line:
            '''连线'''
            return Line(pos1,pos2,color=color)

        func = lambda x: x-1
        graph = axes.plot(
            func,
            color=WHITE,
            x_range=[-6, 6], use_smoothing=True
        )
        text = Text('对于线性函数而言，我们可以通过点斜式计算斜率',font='Microsoft YaHei',t2c={'点斜式':'#DB861E'},font_size=32).shift(DOWN*3)
        self.play(Write(axes, lag_ratio=0.01, run_time=1),FadeIn(axis_labels,text))
        func_label = axes.get_graph_label(graph, "x-1").shift(UP*0.8)
        self.play(Create(graph),run_time=2)

        dot1 = Dot(axes.c2p(1,func(1)))
        dot2 = Dot(axes.c2p(3,func(3)))
        line = darw_line2(axes.c2p(1,func(1)),axes.c2p(3,func(3)),BLUE_B)

        self.play(FadeIn(func_label,dot1,dot2),Create(line))

        line2 = darw_line2(axes.c2p(1,func(1)),axes.c2p(3,func(1)), color=WHITE)
        line3 = darw_line2(axes.c2p(3,func(3)),axes.c2p(3,func(1)), color=WHITE)
        ##dx dy
        Delta_x  = Brace(line2, direction=DOWN*2)
        Delta_y  = Brace(line3, direction=RIGHT*2)
        Delta_x_text = Delta_x.get_tex("\Delta x").next_to(Delta_y,DOWN)
        Delta_y_text  = Delta_y.get_tex("\Delta y").next_to(Delta_y,RIGHT)

        self.play(Create(line2),Create(line3))
        self.play(FadeIn(Delta_x,Delta_y,Delta_x_text,Delta_y_text))
        self.play(FadeOut(text),run_time=0.6)

        text = Text('点斜式(其中Δx与Δy分别为变化的x值与变化的y值)',font='Microsoft YaHei',t2c={'点斜式':'#DB861E'},font_size=32).shift(DOWN*3)
        self.play(FadeIn(text),run_time=0.6)
        text2 = MathTex('k = ','\\frac{\\Delta y}{\\Delta x}').shift(RIGHT*4+DOWN*2)
        self.play(Write(text2))
        self.play(Transform(VGroup(Delta_x_text,Delta_y_text),MathTex('k = ','\\frac{2}{2}').shift(RIGHT*4+DOWN*2)),FadeOut(text2))
        self.play(Transform(VGroup(Delta_x_text,Delta_y_text),MathTex('k = ','1').shift(RIGHT*4+DOWN*2)))
        self.wait(1.6)
        ##变
        func = lambda x: -2*x+1
        self.play(
            Transform(graph,axes.plot(
            func,
            color=WHITE,
            x_range=[-6, 6], use_smoothing=True
        )),
        Transform(func_label,axes.get_graph_label(axes.plot(
            func,
            color=WHITE,
            x_range=[-6, 6], use_smoothing=True
        ), "-2*x+1", x_val=-1, direction=UP)),
        Transform(dot1,Dot(axes.c2p(1,func(1)))),
        Transform(dot2,Dot(axes.c2p(-2,func(-2)))),
        Transform(line,darw_line2(axes.c2p(1,func(1)),axes.c2p(-2,func(-2)),BLUE_B)),
        Transform(line2,darw_line2(axes.c2p(1,func(1)),axes.c2p(-2,func(1)), color=WHITE)),
        Transform(line3,darw_line2(axes.c2p(-2,func(-2)),axes.c2p(-2,func(1)), color=WHITE)))
        self.play(
        Transform(Delta_x,Brace(line2, direction=DOWN*3)),
        Transform(Delta_y,Brace(line3, direction=RIGHT*3))
        )
        self.play(
        Transform(Delta_x_text, Delta_x.get_tex("\Delta x").next_to(Delta_y,DOWN)),
        Transform(Delta_y_text,Delta_y.get_tex("\Delta y").next_to(Delta_y,RIGHT))
        )
        self.wait(1.2)
        text2 = MathTex('k = ','\\frac{\\Delta y}{\\Delta x}').shift(RIGHT*4+DOWN*2)
        self.play(Write(text2))
        self.play(Transform(VGroup(Delta_x_text,Delta_y_text),MathTex('k = ','\\frac{-6}{3}').shift(RIGHT*4+DOWN*2)),FadeOut(text2))
        self.play(Transform(VGroup(Delta_x_text,Delta_y_text),MathTex('k = ','-2').shift(RIGHT*4+DOWN*2)))
        self.wait(2)
        ##线性函数结束
        self.play(FadeOut(func_label,graph,dot1,dot2,line,line2,line3,Delta_x,Delta_y,Delta_x_text,Delta_y_text,text,axes,axis_labels))
        text = Text('对于非线性函数，我们也可以通过点斜式计算斜率',font='Microsoft YaHei',t2c={'点斜式':'#DB861E'},font_size=32).shift(DOWN*3)
        self.play(FadeIn(text))
        self.wait(0.8)
        self.play(FadeOut(text))
        self.wait()


class chapter4(ZoomedScene):
    '''3章'''
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
        title = Text('导数',font_size=32).shift(UP*3.5+LEFT*6.5)
        self.add(title)
        ##先渲染个函数
        axes = Axes(
            x_range=(-10, 26),
            x_length=9,
            y_length=9,
            y_range=(-10, 26),
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            }
        )
        axis_labels = axes.get_axis_labels()
        axes.shift(LEFT*3+DOWN)
        axis_labels.shift(LEFT*3+DOWN)
        def darw_line(x1:2,y1:2,x2:1,y2:1,**kwargs)->VMobject:
            '''直线'''
            k= (y2-y1)/(x2-x1)
            b = (y1+y2-k*x1-k*x2)/2
            curve = axes.plot(lambda n: k*n+b, color=WHITE,x_range=[-10, 10])
            return curve

        def darw_line2(pos1,pos2,color:WHITE,**kwargs)->Line:
            '''连线'''
            return Line(pos1,pos2,color=color)

        func = lambda x: x**2
        graph = axes.plot(
            func,
            color=RED_C,
            x_range=[-10, 10], use_smoothing=True
        )
        self.play(Write(axes, lag_ratio=0.01, run_time=1),FadeIn(axis_labels))
        func_label = axes.get_graph_label(graph, "x^2")
        self.play(Create(graph),run_time=2)
        self.play(FadeIn(func_label))

        text = Text('对于非线性函数的斜率，可以选取两个点进行计算',font='Microsoft YaHei',t2c={'两个点':'#DB861E'},font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(text))

        #两点连线 动态线
        dot1 = Dot(axes.i2gp(2, graph))
        tracker = ValueTracker(5)
        dot2 = Dot(axes.i2gp(5, graph))
        ##点移动
        f_always(dot2.move_to,lambda: axes.i2gp(tracker.get_value(), graph))
        line = darw_line(2,func(2),5,func(5)).add_updater(lambda mob: line.become(darw_line(2,func(2),tracker.get_value(),func(tracker.get_value()))))
        ##
        line2 = darw_line2(axes.c2p(2,func(2)),axes.c2p(5,func(2)), color=WHITE).add_updater(lambda mob: line2.become(darw_line2(axes.c2p(2,func(2)),axes.c2p(tracker.get_value(),func(2)), color=WHITE)))

        line3 = darw_line2(axes.c2p(5,func(2)),axes.c2p(tracker.get_value(),func(tracker.get_value())), color=WHITE).add_updater(lambda mob: line3.become(darw_line2(axes.c2p(tracker.get_value(),func(2)),axes.c2p(tracker.get_value(),func(tracker.get_value())), color=WHITE)))
        
        ##dx dy
        Delta_x  = Brace(line2).add_updater(lambda mob: Delta_x.become(Brace(line2, direction=DOWN*2)))
        Delta_y  = Brace(line3).add_updater(lambda mob: Delta_y.become(Brace(line3, direction=RIGHT*2)))

        Delta_x_text = Delta_x.get_tex("\Delta x").add_updater(lambda mob: Delta_x_text.next_to(Delta_x,DOWN))
        Delta_y_text  = Delta_y.get_tex("\Delta y").next_to(Delta_y,RIGHT).add_updater(lambda mob: Delta_y_text.next_to(Delta_y,RIGHT))

        self.play(Create(dot1),Create(dot2),Create(line),Create(line2),Create(line3),FadeIn(Delta_x),FadeIn(Delta_y),Create(Delta_x_text),Create(Delta_y_text))

        ##公式
        text_ = VGroup(MathTex('k = \\frac{\\Delta y}{\\Delta x}',' = '),DecimalNumber(
            (func(tracker.get_value()) - func(2))/(tracker.get_value()-2)
        )).arrange(RIGHT).shift(RIGHT*3+DOWN)
        text_.add_updater(lambda mob: text_[1].set_value(((func(tracker.get_value()) - func(2))/(tracker.get_value()-2))))
        self.play(Write(text_))

        self.play(tracker.animate.set_value(3), run_time=3)

        self.play(FadeOut(text))
        text = Text('当这两个点的Δx趋近于0时，两点的直线越趋近于该点切线',font='Microsoft YaHei',t2c={'趋近于':RED},font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(text))
        ##相机
        zoomed_camera = self.zoomed_camera
        ##渲染框
        zoomed_display = self.zoomed_display
        ##选择框
        frame = zoomed_camera.frame
        ##渲染框里的 帧
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(dot1).shift(RIGHT*0.3+UP*0.3)
        # frame.add_updater(lambda mob: frame.move_to(dot1))
        frame.set_color(WHITE)
        zoomed_display_frame.set_color(GOLD)
        zoomed_display.scale([0.3, 0.3, 0])
        zoomed_display.shift(UP*3+RIGHT*2)

        self.play(Create(frame))
        self.activate_zooming()
        self.play(FadeIn(zoomed_display_frame))
        self.play(tracker.animate.set_value(2.0001), run_time=3)
        frame.remove_updater(lambda mob: frame.move_to(dot2))
        dot2.remove_updater(lambda mob: mob.move_to(axes.i2gp(3, graph)))
        line.remove_updater(lambda mob: line.become(darw_line(2,func(2),tracker.get_value(),func(tracker.get_value()))))
        line2.clear_updaters()
        line3.clear_updaters()
        self.wait()

        self.play(FadeOut(frame),FadeOut(zoomed_display_frame))
        self.play(FadeOut(Delta_x_text),FadeOut(Delta_y_text),FadeOut(dot1),FadeOut(dot2),Unwrite(line),Unwrite(line2),Unwrite(line3),Unwrite(text_),FadeOut(axis_labels),Unwrite(graph),FadeOut(func_label),Unwrite(axes))
        self.clear()
        self.wait()



class chapter5(ZoomedScene):
    '''4章'''
    def construct(self):
        ##标题
        title = Text('导数',font_size=32).shift(UP*3.5+LEFT*6.5)
        self.add(title)

        text = Text('接下来，再来看导数的定义就轻松多了',font='Microsoft YaHei')
        self.play(FadeIn(text, shift=UP))
        self.wait(0.8)
        self.play(FadeOut(text, shift=UP))
        text = Text('设函数y=f( x )在点x0的某个邻域内有定义，\n当自变量 x 在x0处有增量Δx，(x0+Δx)也在该邻域内时\n相应地函数取得增量Δy=f(x0+Δx)-f(x0)\n如果Δy与Δx之比当Δx→0时极限存在，\n则称函数y=f( x )在点x0处可导\n并称这个极限为函数y=f( x )在点x0处的导数',font='Microsoft YaHei',t2c={' x ':RED,'x0':BLUE,'Δx':YELLOW,'Δy':YELLOW_E},font_size=32)
        self.play(FadeIn(text, shift=UP))
        self.wait(5)
        self.play(Transform(text,MathTex("f'(x)","=","\\lim_{\\Delta x \\to 0}\\frac{f(x+\\Delta x) - f(x)}{\\Delta x}=\\frac{d}{dx}f(x)")
        ))
        text2 = Text('lim为极限：当Δx→0;dx与df为微小增长量',font='Microsoft YaHei',t2c={'lim':RED,'Δx':RED,'dx':GREEN,'df':GREEN},font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(text2))
        self.wait(5.8)
        self.play(FadeOut(text2))

        text2 = Text('结合下函数图像',font='Microsoft YaHei',t2c={'函数图像':RED},font_size=32).shift(DOWN*3.5)
        self.add(text2)
        self.wait(0.8)
        self.remove(text2)
        self.play(FadeOut(text))
        self.wait()

class chapter6(ZoomedScene):
    '''5章'''
    def construct(self):
        axes = Axes(
            x_range=(-5, 6),
            y_range=(-5, 6),
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            }
        ).shift(DOWN+LEFT*3)
        axis_labels = axes.get_axis_labels()

        def darw_line2(pos1,pos2,color:WHITE,**kwargs)->Line:
            '''连线'''
            return Line(pos1,pos2,color=color)

        func = lambda x: x**2
        graph = axes.plot(
            func,
            color=WHITE,
            x_range=[-6, 6], use_smoothing=True
        )
        self.play(Write(axes, lag_ratio=0.01, run_time=1),FadeIn(axis_labels))
        func_label = axes.get_graph_label(graph, "x^2",x_val=1).shift(UP*2.5)
        self.play(Create(graph),run_time=2)
        dot1 = Dot(axes.c2p(2,func(2)))
        line = darw_line2(axes.c2p(2,func(2)),axes.c2p(2.001,func(2.001)),BLUE_B)
        self.play(FadeIn(func_label,dot1),Create(line))

        text2 = MathTex("f'(x)=\lim_{\Delta x \\to 0}\\frac{f(2+\Delta x) - f(2)}{\Delta x}\\\\=\\frac{4+4\Delta x + {\Delta x}^2-4}{\Delta x}\\\\=4").shift(RIGHT*3.2+UP*2)
        self.play(Write(text2),run_time=1.8)
        self.wait(3)
        self.play(FadeOut(text2,graph,dot1,line,func_label,axis_labels,axes))

class MovingZoomedSceneAround(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            zoomed_display_height=3,
            zoomed_display_width=3,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
                },
            **kwargs
        )

    def construct(self):
        dot = Dot().shift(UL * 2)
        image = ImageMobject(np.uint8([[0, 100, 30, 200],[255, 0, 5, 33]]))
        image.height = 7
        ##文字
        frame_text = Text("Frame", color=PURPLE, font_size=67)
        zoomed_camera_text = Text("Zoomed camera", color=RED, font_size=67)

        self.add(image, dot)

        ##相机
        zoomed_camera = self.zoomed_camera
        ##聚焦框
        zoomed_display = self.zoomed_display
        ##选择框
        frame = zoomed_camera.frame
        ##渲染
        zoomed_display_frame = zoomed_display.display_frame

        frame.move_to(dot)
        frame.set_color(WHITE)
        zoomed_display_frame.set_color(GOLD)
        zoomed_display.scale([1, 1, 0])

        frame_text.next_to(frame, DOWN)

        self.play(Create(frame), FadeIn(frame_text, shift=UP))
        self.activate_zooming()

        zoomed_camera_text.next_to(zoomed_display_frame, DOWN)

        self.play(FadeIn(zoomed_camera_text, shift=UP))
        self.play(FadeOut(zoomed_camera_text),FadeOut(frame_text))
        self.wait()
        self.play(frame.animate.shift(2.5 * DOWN+LEFT*3))
        self.wait()
        self.play(Uncreate(zoomed_display_frame), FadeOut(frame))
        self.wait()

class GraphAreaPlot(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 5],
            y_range=[0, 6],
            x_axis_config={"numbers_to_include": [2, 3]},
            tips=False,
        )

        labels = ax.get_axis_labels()
        ##两个函数
        curve_1 = ax.plot(lambda x: 4 * x - x ** 2, x_range=[0, 4], color=BLUE_C)
        curve_2 = ax.plot(
            lambda x: 0.8 * x ** 2 - 3 * x + 4,
            x_range=[0, 4],
            color=GREEN_B,
        )
        line3 = ax.get_horizontal_line(ax.i2gp(3, curve_1))
        line_1 = ax.get_vertical_line(ax.input_to_graph_point(2, curve_1), color=YELLOW)
        line_2 = ax.get_vertical_line(ax.i2gp(3, curve_1), color=YELLOW)

        riemann_area = ax.get_riemann_rectangles(curve_1, x_range=[0.3, 0.6], dx=0.03, color=BLUE, fill_opacity=0.5)
        area = ax.get_area(curve_2, [2, 3], bounded_graph=curve_1, color=GREY, opacity=0.5)

        # self.add(ax, labels, curve_1, curve_2, line_1, line_2, riemann_area, area)
        self.add(ax, labels)
        self.play(FadeIn(curve_1),FadeIn(curve_2))
        self.play(FadeIn(line_1),FadeIn(line_2),FadeIn(line3))
        self.wait()
        self.play(FadeIn(riemann_area),FadeIn(area))
        self.wait()
