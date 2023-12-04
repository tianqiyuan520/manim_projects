from manim import *
from u import *
from u import _t

class Chapter0(ZoomedScene):
    def construct(self):
        axes = Axes(
            x_range=(0, 12),
            y_range=(-1,6),
            axis_config={
                "stroke_color": GREY_A
            }
        )
        func = lambda x: 0.5**x+2
        Sequence = buildSequence(axes,[1,2,3,4,5,6,7,8,9,10,11,12,13],func)
        Sequence = [i.scale(0.5) for i in Sequence]
        line = always_redraw(lambda:DashedVMobject(Line(Dot(axes.c2p(0,2)),Dot(axes.c2p(16,2)),color=GREEN)))
        self.play(Write(axes))
        self.play(Write(Sequence[0]),run_time=0.5)
        
        for i in range(0,len(Sequence)-1):
            a = Sequence[i].copy()
            self.play(
                Transform(a,Sequence[i+1]),run_time=0.5
            )
            self.remove(a)
            self.add(Sequence[i+1])
            if i == 6:self.play(Create(line))

        word = Text('从图看出，数列在趋近于常数2',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(_t(3))
        self.play(FadeOut(word))
        word = Text('常数2则称为该数列的极限值，即该数列收敛于2',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(_t(4))
        self.play(FadeOut(word))
        word = Text('数列极限确定数列收敛，数列极限代表数列的变化趋势',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(_t(5.1))
        self.play(FadeOut(word))
        word = Text('为此，我们需要关注数列变化情况，用变化情况来描述极限',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(_t(5.1))
        self.play(FadeOut(word))
        word = Text('而ε-N定义正好满足我们的需求',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(_t(3.1))
        self.play(FadeOut(word))
        title = MathTex(r'\varepsilon',' - ',r'N',r'\quad definition').scale(2).set_color_by_tex_to_color_map({"epsilon" : ORANGE, "N" : PURPLE_C}).shift(UP)
    
        self.play(Write(title))

        self.wait(1)
        self.play(title.animate.scale(0.5).shift(UP*2.2+LEFT*5))
        self.play(FadeOut(axes),FadeOut(line),*[FadeOut(i) for i in Sequence])
        color_map = {"{n}" : '#FFCB13','{a_n}':'BLUE','{A}':'GREEN',"epsilon" : ORANGE, "N" : PURPLE_C,"{n}":RED}

        definition = new_text([
            [
                '设',
                MathTex(r'\{ ',r'{a_n}',r'\}').set_color_by_tex_to_color_map(color_map),
                '为数列,',
                MathTex('{A}').set_color_by_tex_to_color_map(color_map),
                '为定值.'
            ],
            [
                '若对任给的正数',
                MathTex(r'\varepsilon').set_color_by_tex_to_color_map(color_map),
                ',总存在正整数',
                MathTex(r'N').set_color_by_tex_to_color_map(color_map),
                ',使得当',
                MathTex(r'{n}',r'>','N').set_color_by_tex_to_color_map(color_map),
                '时'
            ],
            [
                MathTex(r'|',r'{a_n}','-','{A}','|<',r'\varepsilon').set_color_by_tex_to_color_map(color_map),
                "恒成立"
            ],
            [
                '那么常数',
                MathTex("{A}").set_color_by_tex_to_color_map(color_map),
                "是数列",
                MathTex(r'\{ ',r'{a_n}',r'\}').set_color_by_tex_to_color_map(color_map),
                "的极限"
            ],
            [
                "记作",
                MathTex(r'\lim_{',r'{n}',r' \to ',r'\infty }',r' {',r'{a_n}',r'=',r'{A}',r'}').set_color_by_tex_to_color_map(color_map)
            ]
            ],
            font='Microsoft YaHei',s=32)
        for mob in definition:
            self.play(Write(mob),run_time=1.5)
        self.play(definition.animate.shift(LEFT*2))

        word = Text('任意ε>0，存在N>0.使得数列在第N项之后的值\n落在以A值为中心2ε为高的矩形中',font='Microsoft YaHei',font_size=24).shift(DOWN*3.5)
        self.play(FadeIn(word))
        definition2 = new_text([
            [
                MathTex(r' \forall',r'\varepsilon',r' > 0,',r'\exists',r'N',r'>0').set_color_by_tex_to_color_map(color_map),
                '使得当',
                MathTex(r'{n}',r'>0').set_color_by_tex_to_color_map(color_map)
            ],
            [
                MathTex(r'|',r'{a_n}','-','{A}','|<',r'\varepsilon').set_color_by_tex_to_color_map(color_map),
                "恒成立"
            ],
            [
                "相当于第",
                MathTex(r'{N}').set_color_by_tex_to_color_map(color_map),
                "项之后的值位于以",
                MathTex(r'2\varepsilon').set_color_by_tex_to_color_map(color_map),
                "为高的矩形中"
            ]
            ],
            font='Microsoft YaHei',s=32).shift(RIGHT*2.6+DOWN*2)
        x = definition.copy()
        self.play(
            Transform(x,definition2)
        )
        self.remove(x)
        self.add(definition2)
        self.wait(_t(8))
        self.play(FadeOut(word))
        self.play(FadeOut(definition))
        self.play(definition2.animate.shift(UP*5))
        self.wait()

class Chapter1(ZoomedScene):
    def construct(self):
        color_map = {"{n}" : '#FFCB13','{a_n}':'BLUE','{A}':'GREEN',"epsilon" : ORANGE, "N" : PURPLE_C,"{n}":RED}
        title = MathTex(r'\varepsilon',' - ',r'N',r'\quad definition').scale(2).set_color_by_tex_to_color_map({"epsilon" : ORANGE, "N" : PURPLE_C}).shift(UP).scale(0.5).shift(UP*2.2+LEFT*5)
        self.add(title)
        definition2 = new_text([
            [
                MathTex(r' \forall',r'\varepsilon',r' > 0',r',',r'\exists',r' {N}',r'>0').set_color_by_tex_to_color_map(color_map),
                '使得当',
                MathTex(r'n>0').set_color_by_tex_to_color_map(color_map)
            ],
            [
                MathTex(r'|',r'{a_n}','-','{A}','|<',r'\varepsilon').set_color_by_tex_to_color_map(color_map),
                "恒成立"
            ],
            [
                "相当于第",
                MathTex(r'{N}').set_color_by_tex_to_color_map(color_map),
                "项之后的值位于以",
                MathTex(r'2\varepsilon').set_color_by_tex_to_color_map(color_map),
                "为高的矩形中"
            ]
            ],
            font='Microsoft YaHei',s=32).shift(RIGHT*2.6+DOWN+UP*4)
        self.add(definition2)

        axes = Axes(
            x_range=(0, 21),
            y_range=(-1,6),
            axis_config={
                "stroke_color": GREY_A
            }
        )
        limitNum = ValueTracker(3) # 极限值
        func = lambda n: (-1)**n/(0.6*n) + 3
        Sequence = buildSequence(axes,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],func)
        Sequence = [i.scale(0.5) for i in Sequence]
        line = always_redraw(lambda:DashedVMobject(Line(Dot(axes.c2p(0,limitNum.get_value())),Dot(axes.c2p(25,limitNum.get_value())),color=GREY)))
        self.play(Write(axes))
        self.play(Write(Sequence[0]),run_time=0.45)
        for i in range(0,13):
            a = Sequence[i].copy()
            self.play(
                Transform(a,Sequence[i+1]),run_time=0.45
            )
            self.remove(a)
            self.add(Sequence[i+1])
            if i==7:self.play(Create(line))
        for i in Sequence:
            self.remove(i)
            self.add(i)
        
        tracker = ValueTracker(1) # epsilon
        tracker2 = ValueTracker(5) # N
        func2 = lambda n: limitNum.get_value()+tracker.get_value()
        func3 = lambda n: limitNum.get_value()-tracker.get_value()
        N_dot = always_redraw(lambda:Dot(axes.c2p(tracker2.get_value(),0)))
        N_line = always_redraw(lambda:DashedVMobject(Line(N_dot,Dot(axes.c2p(tracker2.get_value(),limitNum.get_value()+tracker.get_value())),color=GREEN)))

        curve_1 = always_redraw(lambda:axes.plot(func2, x_range=[0, 25], color=BLUE_C))
        brace_1  =always_redraw(lambda:Brace(Line(Dot(axes.c2p(0,limitNum.get_value())),Dot(axes.c2p(0,limitNum.get_value()+tracker.get_value()))), direction=LEFT))
        label_1 = always_redraw(lambda:MathTex(r"\varepsilon").next_to(brace_1,LEFT))
        curve_2 = always_redraw(lambda:axes.plot(func3, x_range=[0, 25], color=BLUE_C))
        brace_2  =always_redraw(lambda:Brace(Line(Dot(axes.c2p(0,limitNum.get_value())),Dot(axes.c2p(0,limitNum.get_value()-tracker.get_value()))), direction=LEFT))
        label_2 = always_redraw(lambda:MathTex(r"\varepsilon").next_to(brace_2,LEFT))
        area = always_redraw(lambda:axes.get_area(curve_2, [0, 25], bounded_graph=curve_1, color=GREY, opacity=0.2))
        self.play(Create(curve_1),Create(curve_2),Create(brace_1),Create(brace_2),Create(label_1),Create(label_2))

        self.play(Indicate(definition2[0][0][0:3]))

        word = Text('当ε=1时，从中可以发现数列第N项之后的点都落在该矩形中',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(Create(N_dot),Create(N_line))
        self.play(ShowCreationThenFadeOut(area))

        Sequence2 = []
        for i in Sequence:
            if i.get_x() >= N_dot.get_x() +1:
                Sequence2.append(i)
        self.play(*[Indicate(i) for i in Sequence2]) #show pot

        
        self.wait(6)
        self.play(FadeOut(word))

        word = Text('并且N是不唯一的',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(tracker2.animate.set_value(1),run_time=1)
        Sequence2 = []
        for i in Sequence:
            if i.get_x() >= N_dot.get_x() + 1:

                Sequence2.append(i)
        self.play(*[Indicate(i) for i in Sequence2]) #show pot
        self.wait(_t(1.2))
        self.play(FadeOut(word))

        word = Text('当ε=0.3时，仍可找到数列第N项之后的点',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(tracker.animate.set_value(0.3))
        area = always_redraw(lambda:axes.get_area(curve_2, [0, 25], bounded_graph=curve_1, color=GREY, opacity=0.2))
        self.play(ShowCreationThenFadeOut(area))

        self.play(tracker2.animate.set_value(7),run_time=1)
        Sequence2 = []
        for i in Sequence:
            if i.get_x() >= N_dot.get_x() +1:
                Sequence2.append(i)
        self.play(*[Indicate(i) for i in Sequence2]) #show pot

        self.wait(4)
        self.play(FadeOut(word))

        word = Text('当ε再小时，只需确保第N项之后的点在范围内即可',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word))

        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(0.7).move_to(Dot(axes.c2p(tracker2.get_value(), limitNum.get_value())).get_center()),run_time=1.5)
        self.camera.frame.add_updater(
            lambda mob: mob.move_to(Dot(axes.c2p(tracker2.get_value(), limitNum.get_value())).get_center()))
        
        self.play(tracker.animate.set_value(0.15),run_time=1)
        self.play(tracker2.animate.set_value(17),run_time=3)
        self.play(self.camera.frame.animate.scale(1))
        Sequence2 = []
        for i in Sequence:
            if i.get_x() >= N_dot.get_x() +1:
                Sequence2.append(i)
        self.play(*[Indicate(i) for i in Sequence2]) #show pot
        self.wait(1)
        self.camera.frame.clear_updaters()
        self.play(Restore(self.camera.frame),run_time=1)

        self.play(FadeOut(word))

        word = Text('如果A不是极限值呢',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(Indicate(line))
        func2 = lambda n: limitNum.get_value()+tracker.get_value()
        func3 = lambda n: limitNum.get_value()-tracker.get_value()
        line2 = always_redraw(lambda:DashedVMobject(Line(Dot(axes.c2p(0,limitNum.get_value())),Dot(axes.c2p(25,limitNum.get_value())),color=GREY)))
        self.play(tracker.animate.set_value(1),limitNum.animate.set_value(3.2),run_time=1)
        self.remove(line2)
        self.remove(line)
        line = always_redraw(lambda:DashedVMobject(Line(Dot(axes.c2p(0,limitNum.get_value())),Dot(axes.c2p(25,limitNum.get_value())),color=GREY)))
        self.add(line)

        self.wait(_t(1))
        self.play(FadeOut(word),FadeOut(N_dot),FadeOut(N_line))
        self.wait()


class Chapter2(ZoomedScene):
    def construct(self):
        limitNum = ValueTracker(3.2)
        color_map = {"{n}" : '#FFCB13','{a_n}':'BLUE','{A}':'GREEN',"epsilon" : ORANGE, "N" : PURPLE_C,"{n}":RED}
        title = MathTex(r'\varepsilon',' - ',r'N',r'\quad definition').scale(2).set_color_by_tex_to_color_map({"epsilon" : ORANGE, "N" : PURPLE_C}).shift(UP).scale(0.5).shift(UP*2.2+LEFT*5)
        self.add(title)
        definition2 = new_text([
            [
                MathTex(r' \forall',r'\varepsilon',r' > 0',r',',r'\exists',r' {N}',r'>0').set_color_by_tex_to_color_map(color_map),
                '使得当',
                MathTex(r'n>0').set_color_by_tex_to_color_map(color_map)
            ],
            [
                MathTex(r'|',r'{a_n}','-','{A}','|<',r'\varepsilon').set_color_by_tex_to_color_map(color_map),
                "恒成立"
            ],
            [
                "相当于第",
                MathTex(r'{N}').set_color_by_tex_to_color_map(color_map),
                "项之后的值位于以",
                MathTex(r'2\varepsilon').set_color_by_tex_to_color_map(color_map),
                "为高的矩形中"
            ]
            ],
            font='Microsoft YaHei',s=32).shift(RIGHT*2.6+DOWN+UP*4)
        self.add(definition2)

        axes = Axes(
            x_range=(0, 21),
            y_range=(-1,6),
            axis_config={
                "stroke_color": GREY_A
            }
        )
        func = lambda n: (-1)**n/(0.6*n) + 3
        Sequence = buildSequence(axes,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],func)
        Sequence = [i.scale(0.5) for i in Sequence]
        self.add(axes)
        # self.play(*[Write(i) for i in Sequence])
        for i in Sequence:
            self.add(i)
        line = always_redraw(lambda:DashedVMobject(Line(Dot(axes.c2p(0,limitNum.get_value())),Dot(axes.c2p(20,limitNum.get_value())),color=GREY)))
        tracker = ValueTracker(1) # epsilon
        tracker2 = ValueTracker(3) # N
        func2 = lambda n: limitNum.get_value()+tracker.get_value()
        func3 = lambda n: limitNum.get_value()-tracker.get_value()
        N_dot = always_redraw(lambda:Dot(axes.c2p(tracker2.get_value(),0)))
        N_line = always_redraw(lambda:DashedVMobject(Line(N_dot,Dot(axes.c2p(tracker2.get_value(),limitNum.get_value()+tracker.get_value())),color=GREEN)))

        curve_1 = always_redraw(lambda:axes.plot(func2, x_range=[0, 20], color=BLUE_C))
        brace_1  =always_redraw(lambda:Brace(Line(Dot(axes.c2p(0,limitNum.get_value())),Dot(axes.c2p(0,limitNum.get_value()+tracker.get_value()))), direction=LEFT))
        label_1 = always_redraw(lambda:MathTex(r"\varepsilon").next_to(brace_1,LEFT))
        curve_2 = always_redraw(lambda:axes.plot(func3, x_range=[0, 20], color=BLUE_C))
        brace_2  =always_redraw(lambda:Brace(Line(Dot(axes.c2p(0,limitNum.get_value())),Dot(axes.c2p(0,limitNum.get_value()-tracker.get_value()))), direction=LEFT))
        label_2 = always_redraw(lambda:MathTex(r"\varepsilon").next_to(brace_2,LEFT))
        
        for i in [curve_1,curve_2,brace_1,brace_2,label_1,label_2,line]:
            self.add(i)
        self.play(FadeIn(N_dot),FadeIn(N_line))

        word = Text('当ε=1时，可以发现存在满足条件的N',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word))
        Sequence2 = []
        for i in Sequence:
            if i.get_x() >= N_dot.get_x() +1:
                Sequence2.append(i)
        self.play(*[Indicate(i) for i in Sequence2]) #show pot

        self.wait(4)
        self.play(FadeOut(word))

        word = Text('可当ε=0.15时，并不存在满足条件的N',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.play(tracker.animate.set_value(0.15),run_time=1)
        area = always_redraw(lambda:axes.get_area(curve_2, [0, 20], bounded_graph=curve_1, color=GREY, opacity=0.2))
        self.play(ShowCreationThenFadeOut(area))
        self.wait(3)
        self.play(FadeOut(word))

        word = Text('这些点位于矩形之外',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word))
        Sequence2=[]
        for i in Sequence:
            if i.get_y() < Dot(axes.c2p(0,limitNum.get_value() - tracker.get_value())).get_y() or i.get_y() > Dot(axes.c2p(0,limitNum.get_value() + tracker.get_value())).get_y():
                Sequence2.append(i)
        self.play(*[Indicate(i) for i in Sequence2]) #show pot

        
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(Dot(axes.c2p(tracker2.get_value(), limitNum.get_value())).get_center()),run_time=1.5)
        self.camera.frame.add_updater(
            lambda mob: mob.move_to(Dot(axes.c2p(tracker2.get_value(), limitNum.get_value())).get_center()))
        
        self.play(tracker2.animate.set_value(17),run_time=3)
        
        self.camera.frame.clear_updaters()
        self.play(Restore(self.camera.frame),run_time=1)

        self.wait(1)
        self.play(FadeOut(word))

        self.play(*[FadeOut(i) for i in [axes,curve_1,curve_2,brace_1,brace_2,label_1,label_2,line,N_dot,N_line]+Sequence])

        word = Text('对于极限证明题，确定ε与n的关系，再确定N的取值',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(_t(5.3))
        self.play(FadeOut(word))
        word = Text('N的取值范围确定后，无论ε如何取，都存在符合条件的N',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word))
        self.wait(5.5)
        self.play(FadeOut(word))
        self.play(FadeOut(definition2))
        self.wait(0.5)

class Chapter3(ZoomedScene):
    def construct(self):
        color_map = {"{n}" : '#FFCB13','{a_n}':'BLUE','{b_n}':'BLUE','{c_n}':'BLUE','{A}':'GREEN','omega':'GREEN','alpha':'GREEN','beta':'GREEN',"epsilon" : ORANGE, "{N}" : PURPLE_C,"{n}":RED}
        title = MathTex(r'\varepsilon',' - ',r'N',r'\quad definition').scale(2).set_color_by_tex_to_color_map({"epsilon" : ORANGE, "N" : PURPLE_C}).shift(UP).scale(0.5).shift(UP*2.2+LEFT*5)
        self.add(title)
        word = Text('四则运算证明需运用三角不等式',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word))
        sj = MathTex(r'|a+b|\le|a|+|b|',font_size=38).set_color_by_tex_to_color_map(color_map)
        self.play(Write(sj))
        self.wait(1)
        self.play(sj.animate.shift(RIGHT*3.5+UP*3))
        self.wait(1)
        self.play(FadeOut(word))
        word = Text('利用定义证明加减法',font='Microsoft YaHei',font_size=32).shift(DOWN*3.5)
        self.play(FadeIn(word))
        c = MathTex(r'\lim_{n \to \infty}',r'{c_n}',r'=',r'\omega',r'\Leftrightarrow \forall',r'\varepsilon',r'  >0,\exists ',r'{N}',r'\in \mathbb{N_{}} ^+,\forall n>','{N}',r',|',r'{c_n}','-',r'\omega',r'|<',r'\varepsilon',font_size=38).set_color_by_tex_to_color_map(color_map).shift(UP*2)
        de = MathTex(r'\lim_{n \to \infty}',r'{a_n}',r'=',r'\alpha',r'  \quad \lim_{n \to \infty}',r'{b_n}','=',r'\beta ',font_size=38).next_to(c,DOWN).shift(LEFT*2).set_color_by_tex_to_color_map(color_map)
        add = new_text([
            [
                "加减： ",
                MathTex(r'\lim_{n \to \infty}{(',r'{a_n}',r'\pm ',r'{b_n}',')}=',r'\alpha',r' \pm',r'\beta ').set_color_by_tex_to_color_map(color_map)
            ],
            [
                MathTex(r'proof:')
            ],
            [
                MathTex(r'\forall\varepsilon  >0,\exists N_1\in \mathbb{N} ^+,\forall n>N_1,|a_n-\alpha|<\varepsilon')
            ],
            [
                MathTex(r'\forall\varepsilon  >0,\exists N_2\in \mathbb{N} ^+,\forall n>N_2,|b_n-\beta|<\varepsilon')
            ],
            [
                MathTex(r'|a_n-\alpha|+|b_n-\beta|<2\varepsilon')
            ],
            [
                MathTex(r'|a_n-\alpha+b_n-\beta|\le|a_n-\alpha|+|b_n-\beta|<2\varepsilon')
            ],
            [
                MathTex(r'|a_n-\alpha+b_n-\beta|<2\varepsilon')
            ],
            [
                "极限定义：",
                MathTex(r'\forall2\varepsilon  >0,\exists N\in \mathbb{N} ^+,\forall n>N,|a_n-\alpha+b_n-\beta|<2\varepsilon')
            ],
            [
                MathTex(r'\lim_{n \to \infty}{(',r'{a_n}',r'+',r'{b_n}',')}=',r'\alpha',r'+',r'\beta ').set_color_by_tex_to_color_map(color_map)
            ]
            ],
            font='Microsoft YaHei',s=28).next_to(de,DOWN).shift(RIGHT)
        self.play(Write(c),Write(de))
        self.play(Write(add[0]))
        self.play(FadeOut(word))
        self.play(Write(add[1]))
        self.play(Write(add[2]),Write(add[3]))
        self.play(Indicate(add[2]),Indicate(add[3]))
        self.play(Write(add[4]))
        sj2 = sj.copy()
        self.play(
            sj2.animate.move_to(add[5])
        )
        self.wait(1)
        self.play(
            Transform(
                sj2,add[5]
            )
        )
        self.remove(sj2)
        self.add(add[5])

        self.camera.frame.save_state()

        camera_shift = 2 # 摄像头位移值
        self.play(self.camera.frame.animate.shift(DOWN*2.5),run_time=1) # camera

        self.wait(1.2)
        temp = add[5].copy()
        self.play(
            Transform(
                temp,add[6]
            )
        )
        self.remove(temp)
        self.add(add[6])

        self.wait(1.5)

        self.play(
            TransformMatchingShapes(
                add[6],MathTex(r'|(a_n+b_n)-(\alpha+\beta)|<2\varepsilon',font_size=38).move_to(add[6])
            )
        )
        self.play(Indicate(add[6][1:10]),Indicate(add[6][11:25]))
        self.wait(1)
        temp = add[6].copy()
        self.play(
            Transform(
                temp,add[7]
            )
        )
        self.remove(temp)
        self.add(add[7])
        self.wait(1)
        self.play(Indicate(add[7]))
        self.wait(1)
        temp = add[7].copy()
        self.play(
            Transform(
                temp,add[8]
            ),
            self.camera.frame.animate.shift(DOWN*1.5),run_time=1
        )
        self.remove(temp)
        self.add(add[8])
        camera_shift+=2
        # self.play(Restore(self.camera.frame),run_time=1)
        word = Text('同理可得减法证明',font='Microsoft YaHei',font_size=32).shift(DOWN*(3.5+camera_shift))
        self.play(FadeIn(word))
        self.wait(1)
        self.play(FadeOut(word))
        self.wait(1.6)

class Chapter4(ZoomedScene):
    def construct(self):
        color_map = {"{n}" : '#FFCB13','{a_n}':'BLUE','{b_n}':'BLUE','{c_n}':'BLUE','{A}':'GREEN','omega':'GREEN','alpha':'GREEN','beta':'GREEN',"epsilon" : ORANGE, "{N}" : PURPLE_C,"{n}":RED}
        title = MathTex(r'\varepsilon',' - ',r'N',r'\quad definition').scale(2).set_color_by_tex_to_color_map({"epsilon" : ORANGE, "N" : PURPLE_C}).shift(UP).scale(0.5).shift(UP*2.2+LEFT*5)
        self.add(title)
        sj = MathTex(r'|a+b|\le|a|+|b|',font_size=38).set_color_by_tex_to_color_map(color_map).shift(RIGHT*3.5+UP*3)
        self.add(sj)
        c = MathTex(r'\lim_{n \to \infty}',r'{c_n}',r'=',r'\omega',r'\Leftrightarrow \forall',r'\varepsilon',r'  >0,\exists ',r'{N}',r'\in \mathbb{N_{}} ^+,\forall n>','{N}',r',|',r'{c_n}','-',r'\omega',r'|<',r'\varepsilon',font_size=38).set_color_by_tex_to_color_map(color_map).shift(UP*2)
        de = MathTex(r'\lim_{n \to \infty}',r'{a_n}',r'=',r'\alpha',r'  \quad \lim_{n \to \infty}',r'{b_n}','=',r'\beta ',font_size=38).next_to(c,DOWN).shift(LEFT*2).set_color_by_tex_to_color_map(color_map)
        add = new_text([
            [
                "加减： ",
                MathTex(r'\lim_{n \to \infty}{(',r'{a_n}',r'\pm ',r'{b_n}',')}=',r'\alpha',r' \pm',r'\beta ').set_color_by_tex_to_color_map(color_map)
            ],
            [
                MathTex(r'proof:')
            ],
            [
                MathTex(r'\forall\varepsilon  >0,\exists N_1\in \mathbb{N} ^+,\forall n>N_1,|a_n-\alpha|<\varepsilon')
            ],
            [
                MathTex(r'\forall\varepsilon  >0,\exists N_2\in \mathbb{N} ^+,\forall n>N_2,|b_n-\beta|<\varepsilon')
            ],
            [
                MathTex(r'|a_n-\alpha|+|b_n-\beta|<2\varepsilon')
            ],
            [
                MathTex(r'|a_n-\alpha+b_n-\beta|\le|a_n-\alpha|+|b_n-\beta|<2\varepsilon')
            ],
            [
                MathTex(r'|a_n-\alpha+b_n-\beta|<2\varepsilon')
            ],
            [
                "极限定义：",
                MathTex(r'\forall2\varepsilon  >0,\exists N\in \mathbb{N} ^+,\forall n>N,|a_n-\alpha+b_n-\beta|<2\varepsilon')
            ],
            [
                MathTex(r'\lim_{n \to \infty}{(',r'{a_n}',r'+',r'{b_n}',')}=',r'\alpha',r'+',r'\beta ').set_color_by_tex_to_color_map(color_map)
            ]
            ],
            font='Microsoft YaHei',s=28).next_to(de,DOWN).shift(RIGHT)
        self.add(add)
        camera_shift=4# 摄像头位移值
        self.camera.frame.save_state()
        self.camera.frame.shift(DOWN*4)
        mult = new_text([
            [
                "乘法： ",
                MathTex(r'\lim_{n \to \infty}{(',r'{a_n}',r'{b_n}',')}=',r'\alpha',r'\beta ').set_color_by_tex_to_color_map(color_map)
            ],
            [
                MathTex(r'proof:')
            ],
            [
                MathTex(r'\forall\varepsilon  >0,\exists N_1\in \mathbb{N} ^+,\forall n>N_1,',r'|a_n-\alpha|<\varepsilon')
            ],
            [
                MathTex(r'\forall\varepsilon  >0,\exists N_2\in \mathbb{N} ^+,\forall n>N_2,',r'|b_n-\beta|<\varepsilon')
            ],
            [
                MathTex(r'|a_n b_n-\alpha \beta|=|a_n b_n-\alpha \beta-\alpha b_n+\alpha b_n|')
            ],
            [
                MathTex(r'=|b_n(a_n -\alpha)+\alpha(b_n -\beta)|')
            ],
            [
                "由 三角不等式得"
            ],
            [
                MathTex(r'|b_n(a_n -\alpha)+\alpha(b_n -\beta)| \le |b_n||(a_n -\alpha)|+|\alpha||(b_n -\beta)|')
            ],
            [
                MathTex(r'|b_n(a_n -\alpha)+\alpha(b_n -\beta)| < |b_n|\varepsilon+|\alpha|\varepsilon')
            ],
            [
                MathTex(r'|a_n b_n-\alpha \beta| < (|b_n|+|\alpha|)\varepsilon')
            ],
            [
                "极限定义：",
                MathTex(r'\forall2(|b_n|+|\alpha|)\varepsilon  >0,\exists N\in \mathbb{N} ^+,\forall n>N,|a_n b_n-\alpha \beta| < (|b_n|+|\alpha|)\varepsilon')
            ],
            [
                MathTex(r'\lim_{n \to \infty}{(',r'{a_n}',r'{b_n}',')}=',r'\alpha',r'\beta ').set_color_by_tex_to_color_map(color_map)
            ]
            ],
            font='Microsoft YaHei',s=28).next_to(add,DOWN).shift(RIGHT*0.5)
        self.play(self.camera.frame.animate.shift(DOWN*4),run_time=2)
        self.play(Write(mult[0]))
        self.play(Write(mult[1]))
        self.wait(0.8)
        self.play(Write(mult[2]),Write(mult[3]))
        
        self.play(self.camera.frame.animate.shift(DOWN),Write(mult[4]))
        self.wait(1)
        self.play(Write(mult[5]))
        camera_shift+=5
        word = Text('再次利用三角不等式',font='Microsoft YaHei',font_size=32).shift(DOWN*(3.5+camera_shift))
        self.play(FadeIn(word))
        self.play(Create(mult[6]))
        temp = mult[6].copy()
        self.play(
            Transform(
                temp,mult[7]
            )
        )
        self.remove(temp)
        self.add(mult[7])

        self.wait(1)
        self.play(FadeOut(word))

        self.play(Indicate(mult[2][-1]),Indicate(mult[3][-1]))
        self.wait(1)
        
        self.play(Write(mult[8]),self.camera.frame.animate.shift(DOWN))
        self.play(ShowCreationThenFadeOut(
            SurroundingRectangle(mult[4])
        ))
        self.wait(0.5)

        temp = mult[8].copy()
        self.play(
            Transform(
                temp,mult[9]
            )
        )
        self.remove(temp)
        self.add(mult[9])
        self.wait(1)
        self.play(Write(mult[10]),self.camera.frame.animate.shift(DOWN*2))
        self.play(Indicate(mult[10]))
        self.wait(1)

        temp = mult[10].copy()
        self.play(
            Transform(
                temp,mult[11]
            )
        )
        self.remove(temp)
        self.add(mult[11])

        self.wait(1.6)

        camera_shift+=3

class Chapter5(ZoomedScene):
    def construct(self):
        color_map = {"{n}" : '#FFCB13','{a_n}':'BLUE','{b_n}':'BLUE','{c_n}':'BLUE','{A}':'GREEN','omega':'GREEN','alpha':'GREEN','beta':'GREEN',"epsilon" : ORANGE, "{N}" : PURPLE_C,"{n}":RED}
        title = MathTex(r'\varepsilon',' - ',r'N',r'\quad definition').scale(2).set_color_by_tex_to_color_map({"epsilon" : ORANGE, "N" : PURPLE_C}).shift(UP).scale(0.5).shift(UP*2.2+LEFT*5)
        self.add(title)
        sj = MathTex(r'|a+b|\le|a|+|b|',font_size=38).set_color_by_tex_to_color_map(color_map).shift(RIGHT*3.5+UP*3)
        self.add(sj)
        c = MathTex(r'\lim_{n \to \infty}',r'{c_n}',r'=',r'\omega',r'\Leftrightarrow \forall',r'\varepsilon',r'  >0,\exists ',r'{N}',r'\in \mathbb{N_{}} ^+,\forall n>','{N}',r',|',r'{c_n}','-',r'\omega',r'|<',r'\varepsilon',font_size=38).set_color_by_tex_to_color_map(color_map).shift(UP*2)
        de = MathTex(r'\lim_{n \to \infty}',r'{a_n}',r'=',r'\alpha',r'  \quad \lim_{n \to \infty}',r'{b_n}','=',r'\beta ',font_size=38).next_to(c,DOWN).shift(LEFT*2).set_color_by_tex_to_color_map(color_map)
        add = new_text([
            [
                "加减： ",
                MathTex(r'\lim_{n \to \infty}{(',r'{a_n}',r'\pm ',r'{b_n}',')}=',r'\alpha',r' \pm',r'\beta ').set_color_by_tex_to_color_map(color_map)
            ],
            [
                MathTex(r'proof:')
            ],
            [
                MathTex(r'\forall\varepsilon  >0,\exists N_1\in \mathbb{N} ^+,\forall n>N_1,|a_n-\alpha|<\varepsilon')
            ],
            [
                MathTex(r'\forall\varepsilon  >0,\exists N_2\in \mathbb{N} ^+,\forall n>N_2,|b_n-\beta|<\varepsilon')
            ],
            [
                MathTex(r'|a_n-\alpha|+|b_n-\beta|<2\varepsilon')
            ],
            [
                MathTex(r'|a_n-\alpha+b_n-\beta|\le|a_n-\alpha|+|b_n-\beta|<2\varepsilon')
            ],
            [
                MathTex(r'|a_n-\alpha+b_n-\beta|<2\varepsilon')
            ],
            [
                "极限定义：",
                MathTex(r'\forall2\varepsilon  >0,\exists N\in \mathbb{N} ^+,\forall n>N,|a_n-\alpha+b_n-\beta|<2\varepsilon')
            ],
            [
                MathTex(r'\lim_{n \to \infty}{(',r'{a_n}',r'+',r'{b_n}',')}=',r'\alpha',r'+',r'\beta ').set_color_by_tex_to_color_map(color_map)
            ]
            ],
            font='Microsoft YaHei',s=28).next_to(de,DOWN).shift(RIGHT)
        mult = new_text([
            [
                "乘法： ",
                MathTex(r'\lim_{n \to \infty}{(',r'{a_n}',r'{b_n}',')}=',r'\alpha',r'\beta ').set_color_by_tex_to_color_map(color_map)
            ],
            [
                MathTex(r'proof:')
            ],
            [
                MathTex(r'\forall\varepsilon  >0,\exists N_1\in \mathbb{N} ^+,\forall n>N_1,',r'|a_n-\alpha|<\varepsilon')
            ],
            [
                MathTex(r'\forall\varepsilon  >0,\exists N_2\in \mathbb{N} ^+,\forall n>N_2,',r'|b_n-\beta|<\varepsilon')
            ],
            [
                MathTex(r'|a_n b_n-\alpha \beta|=|a_n b_n-\alpha \beta-\alpha b_n -\alpha b_n|')
            ],
            [
                MathTex(r'=|b_n(a_n -\alpha)+\alpha(b_n -\beta)|')
            ],
            [
                "由 三角不等式得"
            ],
            [
                MathTex(r'|b_n(a_n -\alpha)+\alpha(b_n -\beta)| \le |b_n||(a_n -\alpha)|+|\alpha||(b_n -\beta)|')
            ],
            [
                MathTex(r'|b_n(a_n -\alpha)+\alpha(b_n -\beta)| < |b_n|\varepsilon+|\alpha|\varepsilon')
            ],
            [
                MathTex(r'|a_n b_n-\alpha \beta| < (|b_n|+|\alpha|)\varepsilon')
            ],
            [
                "极限定义：",
                MathTex(r'\forall2(|b_n|+|\alpha|)\varepsilon  >0,\exists N\in \mathbb{N} ^+,\forall n>N,|a_n b_n-\alpha \beta| < (|b_n|+|\alpha|)\varepsilon')
            ],
            [
                MathTex(r'\lim_{n \to \infty}{(',r'{a_n}',r'{b_n}',')}=',r'\alpha',r'\beta ').set_color_by_tex_to_color_map(color_map)
            ]
            ],
            font='Microsoft YaHei',s=28).next_to(add,DOWN).shift(RIGHT*0.5)
        self.add(add)
        self.add(mult)
        camera_shift=12# 摄像头位移值
        self.camera.frame.save_state()
        self.camera.frame.shift(DOWN*camera_shift)

        inverse = new_text([
            [
                "倒数： ",
                MathTex(r'\lim_{n \to \infty}{(',r'\frac{1}{b_n}',')}=',r'\frac{1}{\beta}',r'(',r'\beta',r' \ne 0)').set_color_by_tex_to_color_map(color_map)
            ],
            [
                MathTex(r'proof:')
            ],
            [
                "A: ",
                MathTex(r'\forall\varepsilon  >0,\exists N_2\in \mathbb{N} ^+,\forall n>N_2,',r'|b_n-\beta|<\varepsilon')
            ],
            [
                MathTex(r'|\frac{1}{b_n} - \frac{1}{\beta}|')
            ],
            [
                MathTex(r'=|\frac{\beta - b_n}{b_n \beta}|')
            ],
            [
                "由  绝对值的对称性和不等式A得"
            ],
            [
                MathTex(r'=|\frac{b_n- \beta}{b_n \beta}| < \frac{\varepsilon}{b_n \beta}')
            ],
            [
                MathTex(r'|\frac{1}{b_n} - \frac{1}{\beta}| < \frac{\varepsilon}{b_n \beta}')
            ],
            [
                "极限定义：",
                MathTex(r'\forall \frac{\varepsilon}{b_n \beta}  >0,\exists N\in \mathbb{N} ^+,\forall n>N,|\frac{1}{b_n} - \frac{1}{\beta}| < \frac{\varepsilon}{b_n \beta}')
            ],
            [
                MathTex(r'\lim_{n \to \infty}{(',r'\frac{1}{b_n}',')}=',r'\frac{1}{\beta}',r'(',r'\beta',r' \ne 0)').set_color_by_tex_to_color_map(color_map)
            ]
            ],
            font='Microsoft YaHei',s=28).next_to(mult,DOWN).shift(LEFT*1.2)
        self.play(self.camera.frame.animate.shift(DOWN*4),run_time=2.5)
        self.play(Write(inverse[0]))
        # main animate
        self.play(
            AnimationGroup(
                ApplyMethod(self.camera.frame.shift, DOWN*6, run_time=18,rate_func=linear),
                AnimationGroup(
                        Write(inverse[1]),
                        Write(inverse[2]),
                        Wait(1),
                        Write(inverse[3]),
                        Wait(1),
                        TransformFromCopy(
                            inverse[3],inverse[4]
                        ),
                        Wait(0.6),
                        Write(inverse[5]),
                        Write(inverse[6]),
                        Wait(0.5),
                        Circumscribe(inverse[3],Rectangle,False,True),
                        Wait(0.5),
                        TransformFromCopy(
                            inverse[6],inverse[7]
                        ),
                        Wait(1),
                        Write(inverse[8]),
                        Circumscribe(inverse[8],Rectangle),
                        Wait(1),
                        TransformFromCopy(
                            inverse[8],inverse[9]
                        ),
                    lag_ratio=1
                    )
                ))
        # camera_shift = 24
        camera_shift = 22
        self.wait(1)

class Chapter6(ZoomedScene):
    def construct(self):
        color_map = {"{n}" : '#FFCB13','{a_n}':'BLUE','{b_n}':'BLUE','{c_n}':'BLUE','{A}':'GREEN','omega':'GREEN','alpha':'GREEN','beta':'GREEN',"epsilon" : ORANGE, "{N}" : PURPLE_C,"{n}":RED}
        title = MathTex(r'\varepsilon',' - ',r'N',r'\quad definition').scale(2).set_color_by_tex_to_color_map({"epsilon" : ORANGE, "N" : PURPLE_C}).shift(UP).scale(0.5).shift(UP*2.2+LEFT*5)
        self.add(title)
        sj = MathTex(r'|a+b|\le|a|+|b|',font_size=38).set_color_by_tex_to_color_map(color_map).shift(RIGHT*3.5+UP*3)
        self.add(sj)
        c = MathTex(r'\lim_{n \to \infty}',r'{c_n}',r'=',r'\omega',r'\Leftrightarrow \forall',r'\varepsilon',r'  >0,\exists ',r'{N}',r'\in \mathbb{N_{}} ^+,\forall n>','{N}',r',|',r'{c_n}','-',r'\omega',r'|<',r'\varepsilon',font_size=38).set_color_by_tex_to_color_map(color_map).shift(UP*2)
        de = MathTex(r'\lim_{n \to \infty}',r'{a_n}',r'=',r'\alpha',r'  \quad \lim_{n \to \infty}',r'{b_n}','=',r'\beta ',font_size=38).next_to(c,DOWN).shift(LEFT*2).set_color_by_tex_to_color_map(color_map)
        add = new_text([
            [
                "加减： ",
                MathTex(r'\lim_{n \to \infty}{(',r'{a_n}',r'\pm ',r'{b_n}',')}=',r'\alpha',r' \pm',r'\beta ').set_color_by_tex_to_color_map(color_map)
            ],
            [
                MathTex(r'proof:')
            ],
            [
                MathTex(r'\forall\varepsilon  >0,\exists N_1\in \mathbb{N} ^+,\forall n>N_1,|a_n-\alpha|<\varepsilon')
            ],
            [
                MathTex(r'\forall\varepsilon  >0,\exists N_2\in \mathbb{N} ^+,\forall n>N_2,|b_n-\beta|<\varepsilon')
            ],
            [
                MathTex(r'|a_n-\alpha|+|b_n-\beta|<2\varepsilon')
            ],
            [
                MathTex(r'|a_n-\alpha+b_n-\beta|\le|a_n-\alpha|+|b_n-\beta|<2\varepsilon')
            ],
            [
                MathTex(r'|a_n-\alpha+b_n-\beta|<2\varepsilon')
            ],
            [
                "极限定义：",
                MathTex(r'\forall2\varepsilon  >0,\exists N\in \mathbb{N} ^+,\forall n>N,|a_n-\alpha+b_n-\beta|<2\varepsilon')
            ],
            [
                MathTex(r'\lim_{n \to \infty}{(',r'{a_n}',r'+',r'{b_n}',')}=',r'\alpha',r'+',r'\beta ').set_color_by_tex_to_color_map(color_map)
            ]
            ],
            font='Microsoft YaHei',s=28).next_to(de,DOWN).shift(RIGHT)
        mult = new_text([
            [
                "乘法： ",
                MathTex(r'\lim_{n \to \infty}{(',r'{a_n}',r'{b_n}',')}=',r'\alpha',r'\beta ').set_color_by_tex_to_color_map(color_map)
            ],
            [
                MathTex(r'proof:')
            ],
            [
                MathTex(r'\forall\varepsilon  >0,\exists N_1\in \mathbb{N} ^+,\forall n>N_1,',r'|a_n-\alpha|<\varepsilon')
            ],
            [
                MathTex(r'\forall\varepsilon  >0,\exists N_2\in \mathbb{N} ^+,\forall n>N_2,',r'|b_n-\beta|<\varepsilon')
            ],
            [
                MathTex(r'|a_n b_n-\alpha \beta|=|a_n b_n-\alpha \beta-\alpha b_n -\alpha b_n|')
            ],
            [
                MathTex(r'=|b_n(a_n -\alpha)+\alpha(b_n -\beta)|')
            ],
            [
                "由 三角不等式得"
            ],
            [
                MathTex(r'|b_n(a_n -\alpha)+\alpha(b_n -\beta)| \le |b_n||(a_n -\alpha)|+|\alpha||(b_n -\beta)|')
            ],
            [
                MathTex(r'|b_n(a_n -\alpha)+\alpha(b_n -\beta)| < |b_n|\varepsilon+|\alpha|\varepsilon')
            ],
            [
                MathTex(r'|a_n b_n-\alpha \beta| < (|b_n|+|\alpha|)\varepsilon')
            ],
            [
                "极限定义：",
                MathTex(r'\forall2(|b_n|+|\alpha|)\varepsilon  >0,\exists N\in \mathbb{N} ^+,\forall n>N,|a_n b_n-\alpha \beta| < (|b_n|+|\alpha|)\varepsilon')
            ],
            [
                MathTex(r'\lim_{n \to \infty}{(',r'{a_n}',r'{b_n}',')}=',r'\alpha',r'\beta ').set_color_by_tex_to_color_map(color_map)
            ]
            ],
            font='Microsoft YaHei',s=28).next_to(add,DOWN).shift(RIGHT*0.5)
        inverse = new_text([
            [
                "倒数： ",
                MathTex(r'\lim_{n \to \infty}{(',r'\frac{1}{b_n}',')}=',r'\frac{1}{\beta}',r'(',r'\beta',r' \ne 0)').set_color_by_tex_to_color_map(color_map)
            ],
            [
                MathTex(r'proof:')
            ],
            [
                "A: ",
                MathTex(r'\forall\varepsilon  >0,\exists N_2\in \mathbb{N} ^+,\forall n>N_2,',r'|b_n-\beta|<\varepsilon')
            ],
            [
                MathTex(r'|\frac{1}{b_n} - \frac{1}{\beta}|')
            ],
            [
                MathTex(r'=|\frac{\beta - b_n}{b_n \beta}|')
            ],
            [
                "由  绝对值的对称性和不等式A得"
            ],
            [
                MathTex(r'=|\frac{b_n- \beta}{b_n \beta}| < \frac{\varepsilon}{b_n \beta}')
            ],
            [
                MathTex(r'|\frac{1}{b_n} - \frac{1}{\beta}| < \frac{\varepsilon}{b_n \beta}')
            ],
            [
                "极限定义：",
                MathTex(r'\forall \frac{\varepsilon}{b_n \beta}  >0,\exists N\in \mathbb{N} ^+,\forall n>N,|\frac{1}{b_n} - \frac{1}{\beta}| < \frac{\varepsilon}{b_n \beta}')
            ],
            [
                MathTex(r'\lim_{n \to \infty}{(',r'\frac{1}{b_n}',')}=',r'\frac{1}{\beta}',r'(',r'\beta',r' \ne 0)').set_color_by_tex_to_color_map(color_map)
            ]
            ],
            font='Microsoft YaHei',s=28).next_to(mult,DOWN).shift(LEFT*1.2)
        self.add(add)
        self.add(mult)
        self.add(inverse)
        camera_shift=22# 摄像头位移值
        self.camera.frame.save_state()
        self.camera.frame.shift(DOWN*camera_shift)
        self.play(self.camera.frame.animate.shift(DOWN*6),run_time=3)
        div = new_text([
            [
                "除法： ",
                MathTex(r'\lim_{n \to \infty}{(',r'\frac{a_n}{b_n}',')}=',r'\frac{\alpha}{\beta}',r'(',r'\beta',r' \ne 0)').set_color_by_tex_to_color_map(color_map)
            ],
            [
                MathTex(r'proof:')
            ],
            [
                "由  乘法和倒数的公式得"
            ],
            [
                MathTex(r'\lim_{n \to \infty}{(\frac{a_n}{b_n})}')
            ],
            [
                MathTex(r'=\lim_{n \to \infty}{(a_n*\frac{1}{b_n})}')
            ],
            [
                MathTex(r'=\alpha*\frac{1}{\beta}}=\frac{\alpha}{\beta}')
            ]
            ],
            font='Microsoft YaHei',s=28).next_to(inverse,DOWN).shift(LEFT*1.2)
        self.play(Write(div[0]))
        self.wait(1)
        self.play(Write(div[1]))
        self.play(Write(div[2]))
        self.play(
            AnimationGroup(
                Write(div[3]),Write(div[4]),Write(div[5]),
                lag_ratio=1.08
            )
        )
        self.wait(2)
        self.play(*[FadeOut(i) for i in self.mobjects])
        self.wait(1)

class test(ZoomedScene):
    def construct(self):
        t = Text("abc")
        self.play(
            AnimationGroup(
                Write(t),
                Wait(2),
                Circumscribe(t,Rectangle,False,True),
                lag_ratio=1
            )
        )
        # self.play(Write(t))
        # self.play(Wiggle(t))
        self.wait()
