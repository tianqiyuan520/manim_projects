from manim import *
from u import *
from u import _t

class Chapter0(Scene):
    def construct(self):

        axes = Axes(
            x_range=(-6, 8),
            y_range=(-6,9),
            axis_config={
                "stroke_color": GREY_A
            }
        ).scale(1.1)
        func = lambda x: -0.02*x**4+0.09*x**3+0.56*x**2-2*x+1.36
        graph = axes.plot(
            func,
            color=BLUE,use_smoothing=False,x_range=[-7,8]
        )
        
        self.play(Write(graph))
        trackers = [
            ValueTracker(-4.5),
            ValueTracker(0),
            ValueTracker(3.7),
            ValueTracker(6.3)
        ]
        p = always_redraw(lambda :Dot(axes.c2p(trackers[0].get_value(),func(trackers[0].get_value())),color=GREEN_A))
        q = always_redraw(lambda :Dot(axes.c2p(trackers[1].get_value(),func(trackers[1].get_value())),color=GREEN_A))
        e = always_redraw(lambda :Dot(axes.c2p(trackers[2].get_value(),func(trackers[2].get_value())),color=GREEN_A))
        f = always_redraw(lambda :Dot(axes.c2p(trackers[3].get_value(),func(trackers[3].get_value())),color=GREEN_A))
        Dots = VGroup(p,q,e,f)
        pl = always_redraw(lambda:darw_t_line(
                axes,trackers[0].get_value(),graph,5,c=GREEN_A
            ))
        ql = always_redraw(lambda:darw_t_line(
                axes,trackers[1].get_value(),graph,5,c=GREEN_A
            ))
        el = always_redraw(lambda:darw_t_line(
                axes,trackers[2].get_value(),graph,5,c=GREEN_A
            ))
        fl = always_redraw(lambda:darw_t_line(
                axes,trackers[3].get_value(),graph,5,c=GREEN_A
            ))
        t_lines = VGroup(pl,ql,el,fl)
        self.play(Write(Dots))
        self.play(*[Write(i) for i in t_lines])
        self.play(trackers[0].animate.set_value(-3.263),trackers[1].animate.set_value(1.487),trackers[2].animate.set_value(5.15),trackers[3].animate.set_value(5.15),run_time=3.5)
        self.play(*[i.animate.shift(DOWN*1.5) for i in self.mobjects])
        axes.shift(DOWN*1.5)
        for i in [p,q,e,f]: i.shift(DOWN*1.5)
        for i in [pl,ql,el,fl]: i.shift(DOWN*1.5)
        self.wait(0.5)
        title = Text('''导数'''
        ,font='Microsoft YaHei',t2f={'应用篇':'Minecraft AE'},font_size=92,t2c={'导数':'#FFBB44','应用篇':PURPLE_B}
        ).shift(UP*2)
        title2 = Text('''「应用篇」'''
        ,font='Microsoft YaHei',t2f={'「应用篇」':'Minecraft AE'},font_size=62,t2c={'导数':'#FFBB44','应用篇':PURPLE_B}
        ).next_to(title,DOWN*1.5)
        self.play(Write(title))
        self.wait(0.6)
        self.play(
            Transform(
                title.copy(),title2
            )
        )
        self.wait(1)
        self.play(*[FadeOut(i) for i in self.mobjects])

class Chapter1(Scene):
    def construct(self):

        axes = Axes(
            x_range=(-6, 8),
            y_range=(-6,9),
            axis_config={
                "stroke_color": GREY_A
            }
        ).shift(LEFT*2+DOWN*2)
        func = lambda x: (1/2)*x**2
        graph = axes.plot(
            func,
            color=BLUE,use_smoothing=False,x_range=[-5,5]
        )
        graph_lable = axes.get_graph_label(graph,r"{x^2}\over{2}",-3).scale(0.5).shift(UP)
        

        word = Text('本期视频，将会进一步解释导数在函数研究中的应用',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(5)
        self.play(FadeOut(word))
        word = Text('现在让我们从函数单调性开始',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2)
        self.play(FadeOut(word))
        self.play(Write(axes))
        self.play(Write(graph),Write(graph_lable))

        word = Text('观察函数图像，可以发现函数在x>=0时单调递增，x<0单调递减',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(7)
        self.play(FadeOut(word))
        word = Text('请注意，单调性只是函数的局部性质',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(3)
        self.play(FadeOut(word))
        word = Text('那么该怎么证明单调性呢',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2)
        self.play(FadeOut(word))
        word = Text('最基本方法便是使用作差法',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2)
        self.play(FadeOut(word))
        color_map = {'{x_1}':BLUE,'{x_2}':GREEN,"D" : ORANGE,"{\Delta x}":GREEN_E,"{x}":BLUE}
        a = new_text([
                [
                    MathTex(r'\forall ','{x_1}',',','{x_2}',' \in ','D').set_color_by_tex_to_color_map(color_map),
                    "且",
                    MathTex('{x_2}','>','{x_1}').set_color_by_tex_to_color_map(color_map),
                    "都有"
                ],
                [
                    MathTex('f(','{x_2}',')','>','f(','{x_1}',')').set_color_by_tex_to_color_map(color_map)
                ],
                [
                    "则",
                    MathTex(r'f(','{x}',')').set_color_by_tex_to_color_map(color_map),
                    '在',
                    MathTex('D').set_color_by_tex_to_color_map(color_map),
                    "区间内单调递增"
                ]
            ],
        font='Microsoft YaHei',s=28).shift(RIGHT*3.4+UP*2)
        word = Text('D为函数定义域某个区间',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(Write(a))
        self.wait(2)
        self.play(FadeOut(word))
        word = Text('在该区间中取x2,x1且x2>x1',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(1.5)
        self.play(Indicate(a[0][0]))
        self.wait(1)
        self.play(Indicate(a[0][2]))
        self.wait(1.5)
        self.play(FadeOut(word))
        word = Text('都有f(x2)>f(x1),那么在该区间中函数单调递增',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(6)
        self.play(FadeOut(word))
        word = Text('相反f(x2)<f(x1),那么在该区间中函数单调递减',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(6)
        self.play(FadeOut(word))
        word = Text('在该式子中由于x2-x1>0,f(x2)-f(x1)>0',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(7)
        self.play(FadeOut(word))
        word = Text('所以，根据不等式的性质，可以将该式子转化成另一种形式',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(5)
        self.play(FadeOut(word))
        self.play(
            a[0].animate.shift(UP*0.5),
            a[2].animate.shift(DOWN*0.5)
            )
        self.play(
            Transform(
                a[1][0],VGroup(
                    MathTex('f(','{x_2}',')','-','f(','{x_1}',')',r'\over','{x_2}','-','{x_1}',font_size=38).set_color_by_tex_to_color_map(color_map),
                    MathTex('> 0',font_size=38).set_color_by_tex_to_color_map(color_map)
                ).arrange(RIGHT).move_to(a[1][0]).shift(RIGHT*0.5)
            )
        )
        word = Text('这种形式则为斜率式',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2)
        self.play(FadeOut(word))

        word = Text('取x1=0,取大于0的数为x2',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(4)

        tracker = ValueTracker(5)
        x1 = Dot(axes.c2p(0,0),color=WHITE)
        x2 = always_redraw(lambda :Dot(axes.c2p(tracker.get_value(),func(tracker.get_value())),color=WHITE))
        line = always_redraw(lambda :darw_line2(
            x1,x2
        ).set_length(8))
        line2 = darw_line2(Dot(axes.c2p(0,0)),Dot(axes.c2p(1,0)))
        self.play(Write(x1),Write(x2),Write(line))
        self.play(Indicate(x1),Indicate(x2))
        self.wait(1)
        self.play(FadeOut(word))

        word = Text('其中斜率值为tanθ',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        angle = always_redraw(lambda: Angle(line2, line, radius=0.5, other_angle=False))
        angle_tex = always_redraw(lambda: MathTex(r"\theta").move_to(
            angle.point_from_proportion(0.5)
        ))
        self.play(Write(angle),Write(angle_tex))
        self.wait(1)
        self.play(FadeOut(word))
        self.play(tracker.animate.set_value(0.1),run_time=4)
        self.play(tracker.animate.set_value(2.001),run_time=1.5)
        self.play(Transform(
            x1,Dot(axes.c2p(2,func(2)),color=WHITE)
        ))
        self.play(Transform(
            line2,darw_line2(Dot(axes.c2p(2,func(2))),Dot(axes.c2p(3,func(2))))
        ))
        self.play(tracker.animate.set_value(5),run_time=3)

        word = Text('从中可以看出在该区间中x2>x1时，斜率始终大于0',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(6)
        self.play(FadeOut(word))

        word = Text('而当x2不断趋于x1时，此时两点的斜率便可表示x1点的斜率',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(tracker.animate.set_value(2.001),run_time=3)
        self.wait(2)
        self.play(FadeOut(word))

        word = Text('所以，该式子可以替换为导数的形式',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(
            a[2].animate.shift(DOWN*2)
            )
        
        self.play(
            Transform(
                a[1][0],VGroup(
                    MathTex('\lim_{','{x_2}',r' \to ','{x_1}','} ',font_size=40).set_color_by_tex_to_color_map(color_map),
                    MathTex('f(','{x_2}',')','-','f(','{x_1}',')',r'\over','{x_2}','-','{x_1}',font_size=38).set_color_by_tex_to_color_map(color_map),
                    MathTex('> 0',font_size=38).set_color_by_tex_to_color_map(color_map)
                ).arrange(RIGHT).move_to(a[1][0])
            )
        )
        self.wait(3)
        self.play(FadeOut(word))
        self.wait(1)
        b = VGroup(
                    MathTex('\lim_{','{\Delta x}',r' \to ','0','} ',font_size=40).set_color_by_tex_to_color_map(color_map),
                    MathTex('f(','{x_1}','+','{\Delta x}',')','-','f(','{x_1}',')',r'\over','{\Delta x}',font_size=38).set_color_by_tex_to_color_map(color_map),
                    MathTex('> 0',font_size=38).set_color_by_tex_to_color_map(color_map)
                ).arrange(RIGHT).move_to(a[1][0]).shift(DOWN)
        self.play(
            TransformMatchingTex(
                a[1][0].copy(),b
            )
        )

        word = Text('不过需要注意的是f(x)需在该区间内可导',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        c = VGroup(
                    MathTex('f\'(x)',font_size=38).set_color_by_tex_to_color_map(color_map),
                    MathTex('> 0',font_size=38).set_color_by_tex_to_color_map(color_map)
                ).arrange(RIGHT).move_to(a[1][0]).shift(DOWN*2)
        self.play(
            TransformMatchingTex(
                a[1][0].copy(),c
            )
        )
        self.wait(4)
        self.play(FadeOut(word))

        self.play(*[FadeOut(i) for i in [x1,x2,angle,angle_tex,line,line2]])
        tracker = ValueTracker(-3)
        x1 = always_redraw(lambda :Dot(axes.c2p(tracker.get_value(),func(tracker.get_value())),color=WHITE))
        line = always_redraw(lambda :darw_t_line(axes,tracker.get_value(),graph,5))
        self.play(Write(x1),Write(line))
        self.play(tracker.animate.set_value(4),run_time=5)
        word = Text('所以在该区间中，当f(x)的导数大于0时,f(x)为单调递增',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(6.3)
        self.play(FadeOut(word))
        word = Text('f(x)的导数小于0时,f(x)为单调递减',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(4.3)
        self.play(FadeOut(word))

        self.play(*[FadeOut(i) for i in [axes,graph,line,x1,graph_lable,b,c]])
        self.play(Transform(
            a,
            new_text([
                [
                    MathTex(r'\forall ','{x}',' \in ','D').set_color_by_tex_to_color_map(color_map)
                ],
                [
                    "如果",
                    MathTex('f\'(','{x}',')','>','0').set_color_by_tex_to_color_map(color_map)
                ],
                [
                    "那么",
                    MathTex(r'f(','{x}',')').set_color_by_tex_to_color_map(color_map),
                    '在',
                    MathTex('D').set_color_by_tex_to_color_map(color_map),
                    "区间内单调递增"
                ],
                [
                    "如果",
                    MathTex('f\'(','{x}',')','<','0').set_color_by_tex_to_color_map(color_map)
                ],
                [
                    "那么",
                    MathTex(r'f(','{x}',')').set_color_by_tex_to_color_map(color_map),
                    '在',
                    MathTex('D').set_color_by_tex_to_color_map(color_map),
                    "区间内单调递减"
                ]
            ],
            font='Microsoft YaHei',s=62)
        ))

        self.wait(5)
        self.play(*[FadeOut(i) for i in self.mobjects])

class Chapter2(Scene):
    def construct(self):

        axes = Axes(
            x_range=(-6, 8),
            y_range=(-6,9),
            axis_config={
                "stroke_color": GREY_A
            }
        ).scale(1.2).shift(LEFT*2+DOWN)
        func = lambda x: 0.03*x**5-0.5*x**3+1.4*x
        func2 = lambda x: 0.03*5*x**4-0.5*3*x**2+1.4
        graph = axes.plot(
            func,
            color=RED,use_smoothing=False,x_range=[-5,5]
        )
        graph2 = axes.plot(
            func2,
            color=BLUE,use_smoothing=False,x_range=[0,1.02]
        )
        graph3 = axes.plot(
            func2,
            color=BLUE,use_smoothing=False,x_range=[1.02,2]
        )
        graph_lable = axes.get_graph_label(graph,r"0.03x^{5}-0.5x^{3}+1.4x",-3.62).scale(0.5).shift(UP*3+LEFT)
        
        self.play(Write(axes))
        self.play(Write(graph))
        self.play(Write(graph_lable))
        word = Text('如果f(x0)为极大值，那么在x0的去心邻域内所有f(x)<f(x0)',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(7.5)
        self.play(FadeOut(word))
        word = Text('如果f(x0)为极小值，那么在x0的去心邻域内所有f(x)>f(x0)',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(7.5)
        self.play(FadeOut(word))
        word = Text('去心邻域代表x0邻近的点的集合',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(3)
        self.play(FadeOut(word))
        word = Text('那么对于函数极值问题，我们可以从一阶导中获取到什么信息呢',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(5)
        self.play(FadeOut(word))
        tracker = ValueTracker(0)
        x1 = always_redraw(lambda :Dot(axes.c2p(tracker.get_value(),func(tracker.get_value())),color=WHITE))
        line = always_redraw(lambda :darw_t_line(axes,tracker.get_value(),graph,5))
        self.play(Write(x1),Write(line))
        self.play(tracker.animate.set_value(1.02),run_time=2)
        word = Text('当函数值为极值时,一阶导的值为0',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(1)
        self.play(FadeOut(word))
        self.play(tracker.animate.set_value(2),run_time=2)
        self.play(FadeOut(x1),FadeOut(line))
        word = Text('并且可以从中发现',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2)
        self.play(FadeOut(word))
        word = Text('若函数值为极大值时，极值点左侧的一阶导大于0，代表函数处于上升趋势',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(Write(graph2))
        self.play(Write(graph3))
        self.wait(3.5)
        self.play(Indicate(graph2))
        self.wait(3.5)
        self.play(FadeOut(word))

        word = Text('极值点右侧的一阶导小于0，代表函数处于下降趋势',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(3)
        self.play(Indicate(graph3))
        self.wait(1.5)
        self.play(FadeOut(word))

        self.play(
            FadeOut(graph3),
            Transform(
                graph2,
                axes.plot(
                            func2,
                            color=BLUE,use_smoothing=False,x_range=[-5,5]
                        )
            )
        )

        word = Text('若是极小值，则一阶导的数值与极大值的相反',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(4)
        self.play(FadeOut(word))

        self.play(*[FadeOut(i) for i in [graph,graph2,graph_lable]])

        func = lambda x: (1/9)*x**3
        func2 = lambda x: (1/3)*x**2
        graph = axes.plot(
            func,
            color=RED,use_smoothing=False,x_range=[-5,5]
        )
        graph2 = axes.plot(
            func2,
            color=BLUE,use_smoothing=False,x_range=[-5,0]
        )
        graph3 = axes.plot(
            func2,
            color=BLUE,use_smoothing=False,x_range=[0,5]
        )
        self.play(Write(graph),Write(graph2),Write(graph3))

        word = Text('如果只是该点的一阶导数值为0,并且左右两侧一阶导数值同号',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2)
        self.play(Indicate(graph2))
        self.wait(2)
        self.play(Indicate(graph3))
        self.wait(1)
        self.play(FadeOut(word))
        
        word = Text('则并不能说明该点为极值点',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2)
        self.play(FadeOut(word))

        self.play(*[FadeOut(i) for i in self.mobjects])

class Chapter3(Scene):
    def construct(self):
        color_map = {'{x_1}':BLUE,'{x_2}':GREEN_E,'{x_0}':GREEN,"D" : ORANGE,"{\Delta x}":GREEN_E,"{x}":BLUE,r'\delta':PURPLE_C}

        word = Text('总结规律',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(1)
        self.play(FadeOut(word))

        a = new_text([
                [
                    MathTex(r'f(','{x}',')').set_color_by_tex_to_color_map(color_map),
                    "在",
                    MathTex(r'{x_0}').set_color_by_tex_to_color_map(color_map),
                    "的邻域",
                    MathTex(r'U(','{x_0}',',',r'\delta',')').set_color_by_tex_to_color_map(color_map),
                    "内可导",
                    MathTex(r'\forall ','{x}',' \in ','D').set_color_by_tex_to_color_map(color_map)
                ],
                [
                    "当",
                    MathTex(r'{x}',r'\in','(','{x_0}','-',r'\delta',',','{x_0}',')').set_color_by_tex_to_color_map(color_map),
                    "时",
                    MathTex('f\'(','{x}',')','>','0').set_color_by_tex_to_color_map(color_map)
                ],
                [
                    "且当",
                    MathTex(r'{x}',r'\in','(','{x_0}',',','{x_0}','+',r'\delta',')').set_color_by_tex_to_color_map(color_map),
                    "时",
                    MathTex('f\'(','{x}',')','<','0').set_color_by_tex_to_color_map(color_map)
                ],
                [
                    "那么",
                    MathTex(r'f(','{x}',')').set_color_by_tex_to_color_map(color_map),
                    '在',
                    MathTex('{x}','=','{x_0}').set_color_by_tex_to_color_map(color_map),
                    Text("处取得极大值",font='Microsoft YaHei'),
                ],
                [
                    "当",
                    MathTex(r'{x}',r'\in','(','{x_0}','-',r'\delta',',','{x_0}',')').set_color_by_tex_to_color_map(color_map),
                    "时",
                    MathTex('f\'(','{x}',')','<','0').set_color_by_tex_to_color_map(color_map)
                ],
                [
                    "且当",
                    MathTex(r'{x}',r'\in','(','{x_0}',',','{x_0}','+',r'\delta',')').set_color_by_tex_to_color_map(color_map),
                    "时",
                    MathTex('f\'(','{x}',')','>','0').set_color_by_tex_to_color_map(color_map)
                ],
                [
                    "那么",
                    MathTex(r'f(','{x}',')').set_color_by_tex_to_color_map(color_map),
                    '在',
                    MathTex('{x}','=','{x_0}').set_color_by_tex_to_color_map(color_map),
                    Text("处取得极小值",font='Microsoft YaHei'),
                ]
            ],
            font='Microsoft YaHei',s=42).shift(UP*0.4)

        self.play(Write(a))

        word = Text('其中邻域时代表该点邻近点集合',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(Indicate(a[0][4]))
        self.wait(3)
        self.play(FadeOut(word))
        word = Text('等价为一个开区间',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(
            a[0][0:4].animate.shift(LEFT*0.33),
            a[0][5:].animate.shift(RIGHT*0.33),
            TransformMatchingTex(
                a[0][4],MathTex('(','{x_0}','-',r'\delta',',','{x_0}','+',r'\delta',')',font_size=38).set_color_by_tex_to_color_map(color_map).move_to(a[0][4])
            )
        )
        self.wait(1)
        self.play(FadeOut(word))

        word = Text('总的来说，对于一个极值点，其邻域是包含单调递增与单调递减',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2.2)
        self.play(
            Indicate(a[1][3]),
            Indicate(a[2][3]),
            Indicate(a[4][3]),
            Indicate(a[5][3])
        )
        self.wait(3.8)
        self.play(FadeOut(word))

        word = Text('即比如取得极大值时，函数是经过上升，取得极值之后下降',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2)
        self.play(
            Indicate(a[1][3]),
            Indicate(a[2][3])
        )
        self.wait(3)
        self.play(FadeOut(word))
        word = Text('取得极小值时，函数是经过下降，取得极值之后上升',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2)
        self.play(
            Indicate(a[4][3]),
            Indicate(a[5][3])
        )
        self.wait(3)
        self.play(FadeOut(word))

        word = Text('上述公式正是 判断极值的第一充分条件',font='Microsoft YaHei',font_size=28,t2c={"第一充分条件":YELLOW}).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(1)
        self.play(
            Transform(
                word,Text('判断极值的第一充分条件',font='Microsoft YaHei',font_size=22,t2c={"判断极值的第一充分条件":YELLOW}).next_to(a[0],UP)
            )
        )
        self.wait(2.5)
        self.play(*[FadeOut(i,shift=UP) for i in self.mobjects])


class Chapter4(Scene):
    def construct(self):
        color_map = {'{x_1}':BLUE,'{x_2}':GREEN,'{x_0}':GREEN,"D" : ORANGE,"{\Delta x}":GREEN_E,"{x}":BLUE}

        word = Text('既然可以通过一阶导研究函数极值，那么二阶导呢',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(4)
        self.play(FadeOut(word))
        axess = [
            Axes(x_range=(-5,5),y_range=(-5,5),axis_config={"stroke_color": GREY_A}).scale(0.3).shift(LEFT*4+UP*1.5),
            Axes(x_range=(-5,5),y_range=(-5,5),axis_config={"stroke_color": GREY_A}).scale(0.3).shift(UP*1.5),
            Axes(x_range=(-5,5),y_range=(-5,5),axis_config={"stroke_color": GREY_A}).scale(0.3).shift(RIGHT*4+UP*1.5),
            Axes(x_range=(-5,5),y_range=(-5,5),axis_config={"stroke_color": GREY_A}).scale(0.3).shift(LEFT*4+DOWN*1.5),
            Axes(x_range=(-5,5),y_range=(-5,5),axis_config={"stroke_color": GREY_A}).scale(0.3).shift(DOWN*1.5),
            Axes(x_range=(-5,5),y_range=(-5,5),axis_config={"stroke_color": GREY_A}).scale(0.3).shift(RIGHT*4+DOWN*1.5)
        ]
        funcs = [
            lambda x: (1/2)*x**2,
            lambda x: x,
            lambda x: 1,
            lambda x: -(1/2)*x**2,
            lambda x: -x,
            lambda x: -1
        ]
        graphs = [
            axess[0].plot(funcs[0],color=BLUE,use_smoothing=True,x_range=[-5,5]),
            axess[1].plot(funcs[1],color=BLUE,use_smoothing=True,x_range=[-5,5]),
            axess[2].plot(funcs[2],color=BLUE,use_smoothing=True,x_range=[-5,5]),
            axess[3].plot(funcs[3],color=BLUE,use_smoothing=True,x_range=[-5,5]),
            axess[4].plot(funcs[4],color=BLUE,use_smoothing=True,x_range=[-5,5]),
            axess[5].plot(funcs[5],color=BLUE,use_smoothing=True,x_range=[-5,5])
            ]
        self.play(*[Write(i) for i in axess])
        self.play(*[Write(i) for i in graphs])
        word = Text('通过图像，可以发现',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(1.5)
        self.play(FadeOut(word))
        word = Text('函数极值与极值点对应的二阶导数值正负有关',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2)
        self.play(Indicate(graphs[2]))
        self.play(Indicate(graphs[5]))
        self.wait(2.1)
        self.play(FadeOut(word))
        self.play(*[FadeOut(i) for i in self.mobjects])

class Chapter5(Scene):
    def construct(self):
        color_map = {'{x_1}':BLUE,'{x_2}':GREEN_E,'{x_0}':GREEN,"D" : ORANGE,"{\Delta x}":GREEN_E,"{x}":BLUE,r'\delta':PURPLE_C}

        word = Text('在此引入判断极值的第二充分条件',font='Microsoft YaHei',font_size=28,t2c={"判断极值的第二充分条件":YELLOW}).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(3)
        self.play(FadeOut(word))

        a = new_text([
                [
                    MathTex(r'f(','{x}',')').set_color_by_tex_to_color_map(color_map),
                    '在',
                    MathTex('{x}','=','{x_0}').set_color_by_tex_to_color_map(color_map),
                    Text("处二阶可导",font='Microsoft YaHei'),
                ],
                [
                    "且",
                    MathTex('f\'(','{x_0}',')','=','0').set_color_by_tex_to_color_map(color_map),
                    "那么"
                ],
                [
                    "若",
                    MathTex('f\'\'(','{x_0}',')','<','0').set_color_by_tex_to_color_map(color_map),
                    "则",
                    MathTex(r'f(','{x}',')').set_color_by_tex_to_color_map(color_map),
                    '在',
                    MathTex('{x}','=','{x_0}').set_color_by_tex_to_color_map(color_map),
                    Text("处取得极大值",font='Microsoft YaHei'),
                ],
                [
                    "若",
                    MathTex('f\'\'(','{x_0}',')','>','0').set_color_by_tex_to_color_map(color_map),
                    "则",
                    MathTex(r'f(','{x}',')').set_color_by_tex_to_color_map(color_map),
                    '在',
                    MathTex('{x}','=','{x_0}').set_color_by_tex_to_color_map(color_map),
                    Text("处取得极小值",font='Microsoft YaHei'),
                ],
                [
                    "若",
                    MathTex('f\'\'(','{x_0}',')','=','0').set_color_by_tex_to_color_map(color_map),
                    "则",
                    MathTex(r'f(','{x}',')').set_color_by_tex_to_color_map(color_map),
                    '在',
                    MathTex('{x}','=','{x_0}').set_color_by_tex_to_color_map(color_map),
                    Text("不能判断是否为极值",font='Microsoft YaHei'),
                ]
            ],
            font='Microsoft YaHei',s=32).shift(UP*1.5)
        b = Text('判断极值的第二充分条件',font='Microsoft YaHei',font_size=32,t2c={"判断极值的第二充分条件":YELLOW}).next_to(a[0],UP)
        self.play(Write(b))
        self.play(Write(a))
        word = Text('由二阶导定义来证明',font='Microsoft YaHei',font_size=28,t2c={"判断极值的第二充分条件":YELLOW}).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(1.4)
        self.play(FadeOut(word))
        proof = VGroup(
            MathTex('f\'\'(','{x_0}',')','=',font_size=48).set_color_by_tex_to_color_map(color_map),
            MathTex('\lim_{','{x}',r' \to ','{x_0}','} ',font_size=48).set_color_by_tex_to_color_map(color_map),
            MathTex('f\'(','{x}',')','-','f\'(','{x_0}',')',r'\over','{x}','-','{x_0}',font_size=48).set_color_by_tex_to_color_map(color_map)
        ).arrange(RIGHT).next_to(a,DOWN).shift(LEFT*0.5)
        self.play(*[Write(i) for i in proof])

        word = Text('由于该点一阶导为0，则可以化简',font='Microsoft YaHei',font_size=28,t2c={"判断极值的第二充分条件":YELLOW}).shift(DOWN*3.5)
        self.play(FadeIn(word))
        c = VGroup(
            MathTex('f\'\'(','{x_0}',')',font_size=48).set_color_by_tex_to_color_map(color_map),
            MathTex('=','\lim_{','{x}',r' \to ','{x_0}','} ',font_size=48).set_color_by_tex_to_color_map(color_map),
            MathTex('f\'(','{x}',')',r'\over','{x}','-','{x_0}',font_size=48).set_color_by_tex_to_color_map(color_map)).arrange(RIGHT).next_to(a,DOWN).shift(LEFT*0.5)
        self.play(TransformMatchingTex(proof,c))

        self.wait(2.8)
        self.play(FadeOut(word))

        word = Text('假如该点为极大值点，那么根据判断极值的第一充分条件',font='Microsoft YaHei',font_size=28,t2c={"第一充分条件":YELLOW}).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(5)
        self.play(FadeOut(word))

        word = Text('x左侧趋近于x0时',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2)
        self.play(FadeOut(word))
        word = Text('公式右侧分母<0,分子>0',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2)
        self.remove(c)
        proof = VGroup(
            MathTex('f\'\'(','{x_0}',')',font_size=48).set_color_by_tex_to_color_map(color_map),
            MathTex('=','\lim_{','{x}',r' \to ','{x_0}','} ',font_size=48).set_color_by_tex_to_color_map(color_map),
            MathTex('f\'(','{x}',')',r'\over','{x}','-','{x_0}',font_size=48).set_color_by_tex_to_color_map(color_map)).arrange(RIGHT).next_to(a,DOWN).shift(LEFT*0.5)
        self.add(proof)
        self.play(Indicate(proof[2][4:]))
        self.play(Indicate(proof[2][0:3]))
        self.wait(1)
        self.play(FadeOut(word))
        word = Text('即得出公式左侧<0',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(Indicate(proof[0]))
        self.play(Indicate(a[2]))
        self.wait(2)
        self.play(FadeOut(word))

        word = Text('x右侧趋近于x0时',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2)
        self.play(FadeOut(word))
        word = Text('公式右侧分母>0,分子>0',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2)
        self.play(Indicate(proof[2][4:]))
        self.play(Indicate(proof[2][0:3]))
        self.wait(1)
        self.play(FadeOut(word))
        word = Text('即得出公式左侧<0',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(Indicate(proof[0]))
        self.play(Indicate(a[2]))
        self.wait(2)
        self.play(FadeOut(word))

        word = Text('判断极小值同理',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(Indicate(a[3]))
        self.wait(1.3)
        self.play(FadeOut(word))

        self.play(*[FadeOut(i) for i in self.mobjects])

class Chapter6(Scene):
    def construct(self):
        color_map = {'{x_1}':BLUE,'{x_2}':GREEN,'{x_0}':GREEN,"D" : ORANGE,"{\Delta x}":GREEN_E,"{x}":BLUE}

        word = Text('但当二阶导为0时，便不好判断该极值点是极大值点或极小值点',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        
        axess = [
            Axes(x_range=(-5,5),y_range=(-5,5),axis_config={"stroke_color": GREY_A}).scale(0.3).shift(LEFT*4+UP*1.5),
            Axes(x_range=(-5,5),y_range=(-5,5),axis_config={"stroke_color": GREY_A}).scale(0.3).shift(UP*1.5),
            Axes(x_range=(-5,5),y_range=(-5,5),axis_config={"stroke_color": GREY_A}).scale(0.3).shift(RIGHT*4+UP*1.5),
            Axes(x_range=(-5,5),y_range=(-5,5),axis_config={"stroke_color": GREY_A}).scale(0.3).shift(LEFT*4+DOWN*1.5),
            Axes(x_range=(-5,5),y_range=(-5,5),axis_config={"stroke_color": GREY_A}).scale(0.3).shift(DOWN*1.5)
        ]
        funcs = [
            lambda x: (1/12)*x**4,
            lambda x: (1/3)*x**3,
            lambda x: x**2,
            lambda x: 2*x,
            lambda x: 2
        ]
        graphs = [
            axess[0].plot(funcs[0],color=BLUE,use_smoothing=True,x_range=[-2.5,2.5]),
            axess[1].plot(funcs[1],color=BLUE,use_smoothing=True,x_range=[-2.5,2.5]),
            axess[2].plot(funcs[2],color=BLUE,use_smoothing=True,x_range=[-2.5,2.5]),
            axess[3].plot(funcs[3],color=BLUE,use_smoothing=True,x_range=[-2.5,2.5]),
            axess[4].plot(funcs[4],color=BLUE,use_smoothing=True,x_range=[-2.5,2.5])
            ]
        self.play(*[Write(i) for i in axess])
        self.play(Write(graphs[0]))
        for i in range(0,4):
            self.play(
                Transform(
                    graphs[i].copy(),
                    graphs[i+1]
                )
            )
            self.wait(0.3)
        
        self.wait(5)
        self.play(FadeOut(word))

        word = Text('对此我们需要扩充第二充分条件',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2.3)
        self.play(FadeOut(word))
        word = Text('研究n阶导与极值的关系',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2.3)
        self.play(*[FadeOut(i) for i in self.mobjects])

class Chapter7(Scene):
    def construct(self):
        color_map = {'{x_1}':BLUE,'{x_2}':GREEN_E,'{x_0}':GREEN,"D" : ORANGE,"{\Delta x}":GREEN_E,"{x}":BLUE,r'\delta':PURPLE_C}

        word = Text('在此引入判断极值的第三充分条件',font='Microsoft YaHei',font_size=28,t2c={"判断极值的第三充分条件":YELLOW}).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(3)
        self.play(FadeOut(word))

        a = new_text([
                [
                    MathTex(r'f(','{x}',')').set_color_by_tex_to_color_map(color_map),
                    '在',
                    MathTex('{x_0}').set_color_by_tex_to_color_map(color_map),
                    Text("处n阶可导",font='Microsoft YaHei'),
                ],
                [
                    "且",
                    MathTex('f\'(','{x_0}',')','=','f\'\'(','{x_0}',')','=',r'\cdots','f^{(n-1)}(','{x_0}',')','= 0').set_color_by_tex_to_color_map(color_map),
                    MathTex(',f^{(n)}(','{x_0}',')',r'\ne 0').set_color_by_tex_to_color_map(color_map),
                    "则"
                ],
                [
                    "1.若",
                    MathTex('n').set_color_by_tex_to_color_map(color_map),
                    "为奇数",
                    MathTex(r'f(','{x}',')').set_color_by_tex_to_color_map(color_map),
                    '在',
                    MathTex('{x_0}').set_color_by_tex_to_color_map(color_map),
                    Text("没有极值",font='Microsoft YaHei'),
                ],
                [
                    "2.若",
                    MathTex('n').set_color_by_tex_to_color_map(color_map),
                    "为偶数",
                ],
                [
                    MathTex('f^{(n)}(','{x_0}',')',r'> 0',r'\Rightarrow ').set_color_by_tex_to_color_map(color_map),
                    MathTex(r'f(','{x_0}',')').set_color_by_tex_to_color_map(color_map),
                    Text("为极小值",font='Microsoft YaHei'),
                ],
                [
                    MathTex('f^{(n)}(','{x_0}',')',r'< 0',r'\Rightarrow ').set_color_by_tex_to_color_map(color_map),
                    MathTex(r'f(','{x_0}',')').set_color_by_tex_to_color_map(color_map),
                    Text("为极大值",font='Microsoft YaHei'),
                ]
            ],
            font='Microsoft YaHei',s=32).shift(UP*0.5)
        b = Text('判断极值的第三充分条件',font='Microsoft YaHei',font_size=32,t2c={"判断极值的第三充分条件":YELLOW}).next_to(a[0],UP)
        self.play(Write(b))
        self.play(Write(a))
        word = Text('借助泰勒展开来证明',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(2)
        self.play(FadeOut(word))

        self.wait(2)

        self.play(*[FadeOut(i) for i in self.mobjects])


class Chapter8(Scene):
    def construct(self):
        color_map = {'{x_1}':BLUE,'{x_2}':GREEN_E,'{x_0}':GREEN,"D" : ORANGE,"{\Delta x}":GREEN_E,"{x}":BLUE,r'\delta':PURPLE_C}
        title = MathTex('proof:').set_color_by_tex_to_color_map(color_map).shift(UP*3.5+LEFT*5)
        proof = MathTex(r"f (x) = &f({x_0}) + f'({x_0})(x-{x_0})+ \cdots+\\\\& \frac{f^{(n-1)}({x_0})({x-x_0})^{n-1}}{(n-1)!}+ \frac{f^{(n)}({x_0})({x-x_0})^{n}}{(n)!}+o(({x-x_0})^{n})",font_size=38).shift(UP*2)
        self.play(Write(title))

        word = Text('将f(x)在x0处泰勒展开',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(Write(proof[0]))
        self.wait(3)
        self.play(FadeOut(word))
        word = Text('由于f(x)在x0处,一到n-1阶导为0,则公式可化为',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(
            Transform(
                proof,MathTex(r"f (x) -f({x_0}) = \frac{f^{(n)}({x_0})({x-x_0})^{n}}{n!}+o(({x-x_0})^{n})",font_size=38).shift(UP*2)
            )
        )

        self.wait(6)
        self.play(FadeOut(word))

        word = Text('由于只是研究f(x)在x0处极值，研究函数局部性质',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(5.2)
        self.play(FadeOut(word))
        word = Text('可将高阶无穷小即佩亚诺余项忽略',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        b = MathTex(r"\frac{f (x) -f({x_0})}{({x-x_0})^{n}}",r" = ",r"\frac{f^{(n)}({x_0})}{n!}",font_size=38).shift(UP*2)
        self.play(
            TransformMatchingTex(
                proof,b
            )
        )
        self.wait(3)
        self.play(FadeOut(word))

        word = Text('故公式左右两侧同号',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.remove(b)
        proof = MathTex(r"\frac{f (x) -f({x_0})}{({x-x_0})^{n}}",r" = ",r"\frac{f^{(n)}({x_0})}{n!}",font_size=38).shift(UP*2)
        self.add(proof)
        self.play(Indicate(proof[0]))
        self.wait(2)
        self.play(FadeOut(word))

        axes = Axes(x_range=(-5,5),y_range=(-5,5),axis_config={"stroke_color": GREY_A}).scale(0.2).shift(RIGHT*5)
        axes2 = Axes(x_range=(-5,5),y_range=(-5,5),axis_config={"stroke_color": GREY_A}).scale(0.2).shift(RIGHT*5+DOWN*2)
        func = lambda x: -(1/2)*x**2
        func2 = lambda x: (1/2)*x**2
        graph = axes.plot(func,color=BLUE,use_smoothing=True,x_range=[-5,5])
        # graph2 = axes2.plot(func2,color=BLUE,use_smoothing=True,x_range=[-5,5])

        word = Text('先来研究，当x0为极大值点时f(x0)的n阶导的数值大小',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(Write(graph))
        # self.play(Write(graph2))
        self.wait(6)
        self.play(FadeOut(word))

        
        proofs = VGroup(
            VGroup(
                Text('当n为奇数时:',font='Microsoft YaHei',font_size=28),
                VGroup(
                    Text('当x从右侧趋近于x0时,左侧小于0,则',font='Microsoft YaHei',font_size=28),
                    MathTex(r"f^{(n)}({x_0}) < 0",font_size=38)
                ).arrange(RIGHT),
                VGroup(
                    Text('当x从左侧趋近于x0时,左侧大于0,则',font='Microsoft YaHei',font_size=28),
                    MathTex(r"f^{(n)}({x_0}) > 0",font_size=38)
                ).arrange(RIGHT),
                VGroup(
                    MathTex(r"f^{(n)}({x_0})",font_size=38),
                    Text('为函数的性质,并不会随x取值而改变',font='Microsoft YaHei',font_size=28)
                ).arrange(RIGHT),
                Text('故x0不是极值点',font='Microsoft YaHei',font_size=28)
            ).arrange(DOWN)
        ).arrange(DOWN,aligned_edge=LEFT).next_to(proof,DOWN).shift(LEFT*2)
        proofs_ = VGroup(
            VGroup(
                Text('当n为偶数时:',font='Microsoft YaHei',font_size=28),
                VGroup(
                    Text('当x从右侧趋近于x0时,左侧小于0,则',font='Microsoft YaHei',font_size=28),
                    MathTex(r"f^{(n)}({x_0}) < 0",font_size=38)
                ).arrange(RIGHT),
                VGroup(
                    Text('当x从左侧趋近于x0时,左侧小于0,则',font='Microsoft YaHei',font_size=28),
                    MathTex(r"f^{(n)}({x_0}) < 0",font_size=38)
                ).arrange(RIGHT),
                VGroup(
                    Text('因为',font='Microsoft YaHei',font_size=28),
                    MathTex(r"f^{(n)}({x_0}) < 0",font_size=38),
                    Text('故x0为极大值点',font='Microsoft YaHei',font_size=28)
                ).arrange(RIGHT)
            ).arrange(DOWN)
        ).arrange(DOWN,aligned_edge=LEFT).next_to(proof,DOWN).shift(LEFT*2)
        
        self.play(Write(proofs))
        
        self.wait(26)

        self.play(
            Transform(
                proofs,proofs_
            )
        )

        self.wait(26)

        word = Text('如果x0为极小值点，同理可得f(x0)>0',font='Microsoft YaHei',font_size=28).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(5)
        self.play(FadeOut(word))


        self.play(*[FadeOut(i) for i in self.mobjects])

        a = new_text([
                [
                    MathTex(r'f(','{x}',')').set_color_by_tex_to_color_map(color_map),
                    '在',
                    MathTex('{x_0}').set_color_by_tex_to_color_map(color_map),
                    Text("处n阶可导",font='Microsoft YaHei'),
                ],
                [
                    "且",
                    MathTex('f\'(','{x_0}',')','=','f\'\'(','{x_0}',')','=',r'\cdots','f^{(n-1)}(','{x_0}',')','= 0').set_color_by_tex_to_color_map(color_map),
                    MathTex(',f^{(n)}(','{x_0}',')',r'\ne 0').set_color_by_tex_to_color_map(color_map),
                    "则"
                ],
                [
                    "1.若",
                    MathTex('n').set_color_by_tex_to_color_map(color_map),
                    "为奇数",
                    MathTex(r'f(','{x}',')').set_color_by_tex_to_color_map(color_map),
                    '在',
                    MathTex('{x_0}').set_color_by_tex_to_color_map(color_map),
                    Text("没有极值",font='Microsoft YaHei'),
                ],
                [
                    "2.若",
                    MathTex('n').set_color_by_tex_to_color_map(color_map),
                    "为偶数",
                ],
                [
                    MathTex('f^{(n)}(','{x_0}',')',r'> 0',r'\Rightarrow ').set_color_by_tex_to_color_map(color_map),
                    MathTex(r'f(','{x_0}',')').set_color_by_tex_to_color_map(color_map),
                    Text("为极小值",font='Microsoft YaHei'),
                ],
                [
                    MathTex('f^{(n)}(','{x_0}',')',r'< 0',r'\Rightarrow ').set_color_by_tex_to_color_map(color_map),
                    MathTex(r'f(','{x_0}',')').set_color_by_tex_to_color_map(color_map),
                    Text("为极大值",font='Microsoft YaHei'),
                ]
            ],
            font='Microsoft YaHei',s=32).shift(UP*0.5)
        b = Text('判断极值的第三充分条件',font='Microsoft YaHei',font_size=32,t2c={"判断极值的第三充分条件":YELLOW}).next_to(a[0],UP)
        self.play(Write(b))
        self.play(Write(a))

        self.wait(2)

        self.play(*[FadeOut(i) for i in self.mobjects])

        self.wait(1)
        word = Text('End',font='Microsoft YaHei',font_size=52)
        self.play(FadeIn(word))
        self.wait(2)
        self.play(FadeOut(word))

