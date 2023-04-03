from manim import *
import math



class PartA(Scene):
    def construct(self):
        # section a
        self.triangle_group = VGroup()
        # Triangle
        A = np.array([0, 0.5, 0])
        B = np.array([-1, -2.5, 0])
        C = np.array([5, -2.5, 0])

        triangle = Polygon(A, B, C) 


        self.triangle_group.add(triangle)
        self.play(Create(self.triangle_group))
        point_labels = VGroup(
            Tex("A").move_to(A + [0, 0.2, 0]),
            Tex("B").move_to(B + [-0.2, -0.2, 0]),
            Tex("C").move_to(C + [0.2, -0.2, 0]),
        )
        self.play(Create(point_labels))
        self.triangle_group.add(point_labels)
        
        #P_label = Tex("P").move_to(P + [-0.2, 0, 0])
        #P_group = VGroup(P_point, P_label)

        area_fill = self.triangle_group.copy().set_fill(BLUE, opacity=0.5)
        area_label = Tex("$S$", tex_environment="flushleft").move_to(triangle).shift(DOWN*0.5, LEFT)
        
        self.play(Create(area_fill))
        self.play(Create(area_label))
        S_description = Tex("$S$ = area of the triangle", tex_environment="flushleft", font_size = 40).to_corner(UL)
        self.play(TransformMatchingTex(area_label, S_description))
        self.play(FadeOut(area_fill))


        incircle_group, radius, radius_label = self.incircle(A, B, C)

        r_description = Tex("$r$ = radius of the incircle", tex_environment="flushleft", font_size = 40).next_to(S_description, RIGHT)      
        self.play(TransformMatchingTex(radius_label, r_description))
        self.play(FadeOut(incircle_group, radius))


        circumcircle, circumradius, circumradius_label = self.circumcircle(A, B, C)
                  
        R_description = Tex("$R$ = radius of the circumcircle", tex_environment="flushleft", font_size = 40).next_to(S_description, DOWN).shift(RIGHT)
        self.play(TransformMatchingTex(circumradius_label, R_description))
        self.play(FadeOut(circumcircle, circumradius))


        edge_labels = VGroup(
            Tex("a").move_to((B + C) / 2 + [0, -0.2, 0]),
            Tex("b").move_to((A + C) / 2 + [0.2, 0.2, 0]),
            Tex("c").move_to((A + B) / 2 + [-0.2, 0, 0]),
        )
        self.triangle_group.add(edge_labels)
        self.play(Create(edge_labels))

        #self.triangle_group.shift(RIGHT*2, DOWN)
        #self.play(FadeOut(self.triangle_group), FadeOut(point_labels))
        self.play(self.triangle_group.animate.scale(0.5).shift(RIGHT*2, DOWN*2))



        t1 = MathTex("2p^2 - 2r^2 - 8Rr", r"= 2p^2 - \frac{2p(p-a)(p-b)(p-c)}{p^2} - \frac{2abc}{p}").to_edge(UP).shift(DOWN*2)
        self.play(Create(t1))
        self.wait(0.5)

        t2 = MathTex(r"= \frac{2p^3 - 2(p-c)(p^2-pb-pa-ab)-2abc}{p}").next_to(t1, DOWN)
        self.play(TransformMatchingShapes(t1[1].copy(), t2))
        self.wait(0.5)

        t3 = MathTex(r"= \frac{2p^3 - 2(p^3 - p^2b-p^2a + abp - cp^2 + pbc + acp - abc) - 2abc}{p}").move_to(t2)
        self.play(TransformMatchingShapes(t2, t3))
        self.wait(0.5)


        t4 = MathTex(r"= 2(pb + pa + pc - ab - ac - bc)").move_to(t3)
        self.play(TransformMatchingShapes(t3, t4))
        self.wait(0.5)

        t5 = MathTex(r"= (a + b + c)(a) + (a + b + c)(b) + (a + b + c)(c)").move_to(t4)
        self.play(TransformMatchingShapes(t4, t5))
        self.wait(0.5)

        t6 = MathTex(r"= ab +", "b^2", "+ bc +", "a^2",  "+ ab + ac + ac + bc +", "c^2", "- 2ab - 2ac - 2bc").move_to(t5)
        self.play(TransformMatchingShapes(t5, t6))
        self.wait(0.5)

        t7 = MathTex("=", "a^2", "+", "b^2", "+", "c^2").next_to(t6, DOWN)
        self.play(TransformMatchingTex(t6.copy(), t7))
        self.wait(0.5)

    
    def bisectors(self, A, B, C, P):
        bisectors = VGroup(
            Line(A, P, stroke_width=2), 
            Line(B, P, stroke_width=2), 
            Line(C, P, stroke_width=2)
        )
        bisector_angles = VGroup(
            angle_bisector_equality(C, A, B, P, 1),
            angle_bisector_equality(A, B, C, P, 2),
            angle_bisector_equality(B, C, A, P, 3)
        )
        return bisectors, bisector_angles

    def incircle(self, A, B, C):

        x, y, r = calculate_incircle(A, B, C)
        P = np.array([x, y, 0])

        bisectors, bisector_angles = self.bisectors(A, B, C, P)

        self.play(Create(bisectors))
        self.play(Create(bisector_angles))
        P_point = Circle(radius=0.05, color=RED, fill_opacity=1).move_to(P)
        self.play(Create(P_point))
        self.play(FadeOut(bisectors, bisector_angles))

        incircle_group = VGroup()
        incircle = Circle(radius=r).move_to(P)
        incircle_group.add(incircle)
        radius = Line([x, y, 0], [x+r, y, 0])
        radius_label = Tex("$r$", tex_environment="flushleft").move_to([x+r/2, y+.1, 0])
        incircle_group.add(P_point)
        
        self.play(Create(radius))
        self.play(Create(incircle))
        self.play(Create(radius_label))
        return incircle_group, radius, radius_label
         
    def circumcircle(self, A, B, C):
        x, y, r = calculate_circumcircle(A, B, C)
        P = np.array([x, y, 0])

        m_AB = (A + B)/2
        m_BC = (B + C)/2
        m_AC = (A + C)/2

        perp_bisector_group = VGroup(
            Line(m_AB, P, stroke_width=2),
            Line(m_BC, P, stroke_width=2),
            Line(m_AC, P, stroke_width=2),
            Angle.from_three_points(A, m_AB, P, radius=0.2, elbow=True, stroke_width=2),
            Angle.from_three_points(B, m_BC, P, radius=0.2, elbow=True, stroke_width=2),
            Angle.from_three_points(C, m_AC, P, radius=0.2, elbow=True, stroke_width=2)
        )
        self.triangle_group.add(perp_bisector_group)
        self.play(Create(perp_bisector_group))

        P_point = Circle(radius=0.05, color=RED, fill_opacity=1).move_to(P)
        
        self.play(Create(P_point))

        circumcircle = Circle(radius=r).move_to(P)
        r_start = np.array([x, y, 0])
        radius = Line(r_start, C)
        radius_label = Tex("$R$", tex_environment="flushleft").move_to((r_start + C)/2 + [-0.2, -0.1, 0])
        self.play(Create(radius))
        self.play(Create(circumcircle))
        self.play(Create(radius_label))
        return VGroup(circumcircle, P_point), radius, radius_label


class PartB(Scene):
    def consruct(self):
        # section a
        self.group = VGroup()

        # Triangle
        A = np.array([0, 0.5, 0])
        B = np.array([-1, -2.5, 0])
        C = np.array([5, -2.5, 0])
        point_labels = VGroup(
            Tex("A").move_to(A + [0, 0.2, 0]),
            Tex("B").move_to(B + [-0.2, -0.2, 0]),
            Tex("C").move_to(C + [0.2, -0.2, 0]),
        )

        triangle = Polygon(A, B, C)
        self.play(Create(triangle))
        self.play(Write(point_labels))

        G, G_Label = self.make_centroid(A, B, C)
        center = G.get_center()
        startpos = center + [-1, 0.5, 0]
        M = Dot(color=GREEN).move_to(startpos)
        lineargs = {"stroke_width":2}
        line = Line(G.get_center(), M.get_center(), **lineargs)
        AM = Line(A, M.get_center(), **lineargs)
        BM = Line(B, M.get_center(), **lineargs)
        CM = Line(C, M.get_center(), **lineargs)

        x = ValueTracker(startpos[0])
        y = ValueTracker(startpos[1])
        M.add_updater(lambda z: z.move_to([x.get_value(), y.get_value(), 0]))



        M_label = MathTex("M").move_to(M.get_center() + [-0.3, 0, 0])
        M_label.add_updater(lambda z: z.move_to(M.get_center() + [-0.3, 0, 0]))

        line.add_updater(lambda z: z.become(Line(G.get_center(), M.get_center(), **lineargs)))
        AM.add_updater(lambda z: z.become(Line(A, M.get_center(), **lineargs)))
        BM.add_updater(lambda z: z.become(Line(B, M.get_center(), **lineargs)))
        CM.add_updater(lambda z: z.become(Line(C, M.get_center(), **lineargs)))

        lines = VGroup(line, AM, BM, CM)

        self.play(Create(M))
        self.play(Write(M_label))
        self.play(Create(lines))
        for pos in [(-0.5, -0.3), (2, -0.2), (-1, 0.5)]:
            new_pos = (center[0] + pos[0], center[1] + pos[1], 0)
            print(new_pos)
            self.play(x.animate.set_value(center[0] + pos[0]), 
                      y.animate.set_value(center[1] + pos[1]))
            self.wait(0.5)
        
        v_MG = G.get_center() - M.get_center()
        v_MA = A - M.get_center()
        v_MB = B - M.get_center()
        v_MC = C - M.get_center()


        a_MG = Arrow(start=M.get_center(), end=G.get_center(), buff=0, color=BLUE)
        a_MA = Arrow(start=M.get_center(), end=A, buff=0, color=RED)
        a_MB = Arrow(start=M.get_center(), end=B, buff=0, color=RED)
        a_MC = Arrow(start=M.get_center(), end=C, buff=0, color=RED)
        vector_group = VGroup(a_MG, a_MA, a_MB, a_MC)
        self.play(Create(vector_group))
        self.play(FadeOut(lines), FadeOut(triangle), FadeOut(point_labels), FadeOut(M_label), FadeOut(M), FadeOut(G), FadeOut(G_Label))
        
        a_MG1 = Arrow(start=ORIGIN, end=ORIGIN + v_MG, buff=0, color=BLUE)
        a_MG2 = Arrow(start=ORIGIN+v_MG, end=ORIGIN + v_MG*2, buff=0, color=BLUE)
        a_MG3 = Arrow(start=ORIGIN+v_MG*2, end=ORIGIN + v_MG*3, buff=0, color=BLUE)

        pos = ORIGIN + v_MA
        a_MA1 = Arrow(start=ORIGIN, end=pos, buff=0, color=RED)
        a_MB1 = Arrow(start=pos, end=pos + v_MB, buff=0, color=RED)
        pos += v_MB
        a_MC1 = Arrow(start=pos, end=pos + v_MC, buff=0, color=RED)
        self.play(Transform(a_MG, a_MG1), Transform(a_MA, a_MA1), Transform(a_MB, a_MB1), Transform(a_MC, a_MC1))
        self.play(Create(a_MG2))
        self.play(Create(a_MG3))
        self.wait(1)
        tex_args = {"font_size":40}
        t1 = MathTex(r"3\overrightarrow{MG}", "=", r"\overrightarrow{MA}",  "+",  r"\overrightarrow{MB}",  "+", r"\overrightarrow{MC}", **tex_args).to_edge(UP)
        self.play(Write(t1))
        self.play(FadeOut(a_MG), FadeOut(a_MA), FadeOut(a_MB), FadeOut(a_MC), FadeOut(a_MG1), FadeOut(a_MG2), FadeOut(a_MG3), FadeOut(a_MA1), FadeOut(a_MB1), FadeOut(a_MC1))
        self.play(t1.animate.shift(DOWN*2))
        self.wait(1)
        t2 = MathTex("9MG^2", "=", "MA^2", "+", "MB^2", "+", "MC^2" + "+", r"2\overrightarrow{MA}.\overrightarrow{MB}", "+", r"2\overrightarrow{MB}.\overrightarrow{MC}", "+", r"2\overrightarrow{MB}.\overrightarrow{MC}",
                     **tex_args).next_to(t1, DOWN)
        t2_desc = MathTex(r"(\overrightarrow{MA}.\overrightarrow{MB} = MA^2 + MB^2 - AB^2})", **tex_args).next_to(t2, UP)
        self.play(TransformMatchingShapes(t1.copy(), t2))
        self.wait(1)
        self.play(FadeOut(t1))
        self.wait(0.5)

        self.play(Write(t2_desc))
        self.wait(1)

        t3 = MathTex("9MG^2", "&=", "MA^2", "+", "MB^2", "+", r"MC^2\\" +
                      r"&+ (MA^2 + MB^2 - AB^2)\\",
                      r"&+ (MB^2 + MC^2 - BC^2)\\",
                      r"&+ (MC^2 + MA^2 - AC^2)\\", **tex_args).next_to(t2, DOWN)
        self.play(TransformMatchingShapes(t2.copy(), t3))
        self.wait(1)
        self.play(FadeOut(t2, t2_desc))

        t4 = MathTex("9MG^2", "&=", r"3(MA^2 + MB^2 + MC^2) - (AB^2 + AC^2 + BC2)", **tex_args).next_to(t1, DOWN)
        self.play(TransformMatchingShapes(t3, t4))
        self.wait(1)

        t5 = MathTex("3MG", "&=", r"MA^2 + MB^2 + MC^2 - \tfrac{1}{3}(AB^2 + AC^2 + BC^2)", **tex_args).next_to(t1, DOWN)
        self.play(TransformMatchingShapes(t4, t5))
        self.wait(1)
        # Let M = I


        
    
    def make_centroid(self, A, B, C):
        m_AB = (A + B)/2
        m_BC = (B + C)/2
        m_AC = (A + C)/2

        perp_bisector_group = VGroup(
            Line(m_AB, C, stroke_width=2),
            Line(m_BC, A, stroke_width=2),
            Line(m_AC, B, stroke_width=2)
        )
        self.play(Create(perp_bisector_group))

        centroid = (A + B + C)/3
        centroid_point = Dot(color=RED).move_to(centroid)
        centroid_label = MathTex("G").move_to(centroid + [0, -0.3, 0])
        self.play(Create(centroid_point))
        self.play(FadeOut(perp_bisector_group))
        self.play(Write(centroid_label))
        return centroid_point, centroid_label

class PartC(Scene):
    def construct(self):
       
        # Triangle
        A = np.array([0, 0.5, 0])
        B = np.array([-1, -2.5, 0])
        C = np.array([5, -2.5, 0])

        triangle = Polygon(A, B, C) 
        point_labels = VGroup(
            Tex("A").move_to(A + [0, 0.2, 0]),
            Tex("B").move_to(B + [-0.2, -0.2, 0]),
            Tex("C").move_to(C + [0.2, -0.2, 0]),
        )
        triangle_group = VGroup(triangle, point_labels)
        self.play(Create(triangle_group))

        I, incircle = self.incircle(A, B, C)
        # I = M
        tex_args = {"font_size": 40}
        t0 = MathTex(r"3MG = MA^2 + MB^2 + MC^2 - \tfrac{1}{3}(AB^2 + AC^2 + BC^2)", **tex_args).to_edge(UP)
        self.play(Write(t0))
        self.wait(1)
        t1 = Tex(r"Let $M \equiv I$").next_to(t0, DOWN)
        self.play(Write(t1))
        self.wait(1)
        t2 = MathTex(r"3IG = IA^2 + IB^2 + IC^2 - \tfrac{1}{3}(AB^2 + AC^2 + BC^2)", **tex_args).to_edge(UP)
        self.play(TransformMatchingShapes(t0,t2))
        self.play(FadeOut(t1))

        # Draw IK _|_ AB
        elbow_args = {"radius": 0.2, "color": WHITE, "elbow": True}

        F = foot_of_perpendicular(B, I, C)
        F_label = MathTex("K").move_to(F + [0, -0.3, 0])
        IF = Line(F, I, stroke_width=5, color=WHITE)
        IF_angle = Angle.from_three_points(C, F, I, **elbow_args)
        G = foot_of_perpendicular(A, I, C)
        IG = Line(G, I, stroke_width=5, color=WHITE)
        IG_angle = Angle.from_three_points(A, G, I, **elbow_args)
        E = foot_of_perpendicular(B, I, A)
        IE = Line(E, I, stroke_width=5, color=WHITE)
        IE_angle = Angle.from_three_points(B, E, I, **elbow_args)

        t3 = Tex(r"Draw $IK \perp AB$").next_to(t2, DOWN)
        self.play(Write(t3))
        self.play(Create(IF), Create(IF_angle))
        self.play(Write(F_label))

        t4 = MathTex(r"\triangle AKI (\angle K=90^\circ) \implies", r"IA^2 &= IK^2 + KA^2\\",
                     "&= (p-a)^2 + r^2\\", **tex_args).next_to(t2, DOWN)
        self.play(FadeOut(t3))
        self.play(Write(t4))
        self.wait(1)
        t5 = MathTex(r"IA^2 &= (p-a)^2 + r^2\\", **tex_args).next_to(t2, DOWN).shift(LEFT*2.5)
        t6 = MathTex(r"IB^2 = (p-b)^2 + r^2\\", **tex_args).next_to(t5, DOWN)
        t7 = MathTex(r"IC^2 = (p-c)^2 + r^2\\", **tex_args).next_to(t6, DOWN)
        self.play(TransformMatchingTex(t4, t5), Write(t6), Write(t7))

        #self.play(Create(IG), Create(IG_angle))
        #self.play(Create(IE), Create(IE_angle))
        
        self.wait(1)


    def incircle(self, A, B, C):

        x, y, r = calculate_incircle(A, B, C)
        P = np.array([x, y, 0])

        bisectors, bisector_angles = self.bisectors(A, B, C, P)

        self.play(Create(bisectors))
        self.play(Create(bisector_angles))
        P_point = Circle(radius=0.05, color=RED, fill_opacity=1).move_to(P)
        self.play(Create(P_point))
        self.play(FadeOut(bisectors, bisector_angles))
        incircle = Circle(radius=r).move_to(P)
        self.play(Create(incircle))
        return P, VGroup(P_point, incircle)

    def bisectors(self, A, B, C, P):
        bisectors = VGroup(
            Line(A, P, stroke_width=2), 
            Line(B, P, stroke_width=2), 
            Line(C, P, stroke_width=2)
        )
        bisector_angles = VGroup(
            angle_bisector_equality(C, A, B, P, 1),
            angle_bisector_equality(A, B, C, P, 2),
            angle_bisector_equality(B, C, A, P, 3)
        )
        return bisectors, bisector_angles
    


def angle_bisector_equality(B, A, C, P, n):
        angle_group = VGroup()
        for i in range(n):
            radius = 0.3 + 0.05 * i
            BAP = Angle.from_three_points(B, A, P, radius=radius, other_angle=True, stroke_width=2)
            CAP = Angle.from_three_points(C, A, P, radius=radius, stroke_width=2)
            angle_group.add(BAP, CAP)
        return angle_group

def calculate_incircle(a, b, c):
    # `d`, `e`, `f` are the side lengths of the triangle
    d = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    e = math.sqrt((c[0] - b[0])**2 + (c[1] - b[1])**2)
    f = math.sqrt((c[0] - a[0])**2 + (c[1] - a[1])**2)

    # `s` is the semiperimeter of the triangle
    s = (d + e + f) / 2

    # `r` is the radius of the incircle
    r = math.sqrt(((s - d)*(s - e)*(s - f)) / s)

    # `x`, `y` are the coordinates of the center of the incircle
    x = ((e * a[0]) + (f * b[0]) + (d * c[0])) / (d + e + f)
    y = ((e * a[1]) + (f * b[1]) + (d * c[1])) / (d + e + f)

    return (x, y, r)

def calculate_circumcircle(A, B, C):
    m_AB = (A[1] - B[1]) / (A[0] - B[0])
    m_BC = (B[1] - C[1]) / (B[0] - C[0])

    x = (m_AB * m_BC * (A[1] - C[1]) + m_BC * (A[0] + B[0]) - m_AB * (B[0] + C[0])) / (2 * (m_BC - m_AB))
    y = -1 * (x - (A[0] + B[0]) / 2) / m_AB + (A[1] + B[1]) / 2
    r = math.sqrt((x - A[0])**2 + (y - A[1])**2)

    return x, y, r

def foot_of_perpendicular(A, B, C):
    """Return the foot of perpendicular from A to line BC."""
    AB = B - A
    AC = C - A
    return A + np.dot(AB, AC) / np.dot(AC, AC) * AC