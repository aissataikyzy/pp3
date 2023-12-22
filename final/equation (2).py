import re, matplotlib.pyplot as plt, numpy as np
from sympy import sin, cos

class Equation:
    def __init__(self, equation):
        self.equation = equation.replace(" ", "")
        print("equation class", equation)
        self.state = self.check()
        self.is_constant = True if re.search("^-?\d+$", self.equation) else False
        self.is_polynomial = False
        self.is_trigonometric = False
        self.dydx = False
        self.d2ydx2 = False
        self.F = None
        self.diff_table = {      # f -> f'
            'e^x': 'e^x',
            '-e^x': '-e^x',
            'sin(x)': 'cos(x)',
            'cos(x)': '-sin(x)',
            '-sin(x)': '-cos(x)',
            '-cos(x)': 'sin(x)',
            'ln(x)': '1/x',
            '-ln(x)': '-1/x'
        }
        self.integral_table = {  # f' -> f
            'e^x': 'e^x',
            '-e^x': '-e^x',
            'cos(x)': 'sin(x)',
            '-cos(x)': '-sin(x)',
            'sin(x)': '-cos(x)',
            '-sin(x)': 'cos(x)',
            '1/x': 'ln(x)',
            '-1/x': '-ln(x)'
        }
    
    def check(self):
        if len(re.findall("^-?\d+$", self.equation)) != 0:
            # print(self.equation)
            return True
        if len(re.findall("^([+-]?\d*\*x\^?\d*)", self.equation)) != 0:
            return True
        if len(re.findall("-?sin\(x\)|-?cos\(x\)|-?e\^x|-?ln\(x\)", self.equation)) != 0:
            return True
        return False

    def derivative_terms(self, term):
        coeff = pow = None
        if re.search("\*x", term):
            coeff = int(re.findall("([+-]?\d*)\*x", term)[-1])
            if re.search("\^", term):
                pow = int(re.findall("x\^(\d+)", term)[-1])
        if pow != None:
            return f"{coeff * pow:+}*x^{pow - 1}" if pow != 2 else f"{coeff * pow:+}*x"
        return f"{coeff:+}"

    def diff_polynomial(self):
        terms = re.findall("([+-]?\d*\*x\^?\d*)", self.equation)
        self.dydx = ""
        for term in terms:
            self.dydx += self.derivative_terms(term)
        return self.dydx.strip("+")
    
    def diff(self):
        if len(re.findall("^-?\d+$", self.equation)) != 0:
            return "0"
        elif len(re.findall("^([+-]?\d*\*x\^?\d*)", self.equation)) != 0: 
            self.is_polynomial = True
            return self.diff_polynomial()
        elif len(re.findall("-?sin\(x\)|-?cos\(x\)|-?e\^x|-?ln\(x\)", self.equation)) != 0:
            self.is_trigonometric = True
            print("diff", self.equation)
            return self.diff_table[self.equation]
        return
        
    def find_const(self, expression):
        const = re.findall("([+-]?\d*\*x\^?\d*)", expression) 
        for i in const:
            expression = expression.replace(i, "")
        const = expression
        return const

    def integral_terms(self, term):
        coeff = pow = None
        if re.search("\*x", term):
            coeff = int(re.findall("([+-]?\d*)\*x", term)[-1])
            if re.search("\^", term):
                pow = int(re.findall("x\^(\d+)", term)[-1])
        if pow != None:
            return f"{coeff / (pow + 1):+.3f}*x^{pow + 1}"
        return f"{coeff / 2:+.3f}*x^2"

    def integrate_polynomial(self):
        terms = re.findall("([+-]?\d*\*x\^?\d*)", self.equation)
        const = self.find_const(self.equation)
        self.F = ""
        for term in terms:
            self.F += self.integral_terms(term)
        self.F = self.F.strip("+")
        return self.F + "+C" if const == "" else self.F + const + "*x+C"

    def integrate(self):
        if len(re.findall("^([+-]?\d*\*x\^?\d*)", self.equation)) != 0:
            print(self.integrate_polynomial())
            return self.integrate_polynomial()
        if re.search("^-?\d+$", self.equation):
            return self.equation + "*x+C"
        if re.search("-?sin\(x\)|-?cos\(x\)|-?e\^x|-?1/x", self.equation):
            self.is_trigonometric = True
            return self.integral_table[self.equation]

    def definite_integral(self, function, a, b):
        print("definite integral", function)
        fa = self.convert_to_numeric(function, a)
        fb = self.convert_to_numeric(function, b)
        return eval(fb) - eval(fa)

    def is_quadratic_equation(self):
        if len(re.findall("^(\d+\*x\^2)([+-]?\d+\*x)?([+-]?\d+)?$", self.equation)):
            return True
        return False

    def solve_quadratic_equation(self, a = 0, b = 0, c = 0):
        terms = re.findall("([+-]?\d*)\*x\^?\d*", self.equation)
        if len(terms) == 1:
            a = int(terms[0].strip("+"))
        else:
            a, b = int(terms[0].strip("+")), int(terms[1].strip("+"))
        c = int(self.find_const(self.equation).strip("+"))
        print(a, b, c)
        D = lambda a, b, c: b*b - 4*a*c
        d = D(a, b, c)
        if d == 0:
            x1 = (-b) / (2*a)
            return [x1]
        elif d > 0:
            x1 = (-b + d**0.5) / (2*a)
            x2 = (-b - d**0.5) / (2*a)
            return [x1, x2]
        return []        

    def convert_to_numeric(self, function, x = None):
        if x != None:
            function = re.sub("x", f"{x}", function)
        print("convert to numeric function", re.sub("\^", "**", function), x)
        return re.sub("\^", "**", function)

    def plot(self, function = None, first_deriv = False, second_deriv = False):
        x = np.linspace(-7.5, 7.5, 1000)
        print("is constant", self.is_constant)
        print("function state", self.state)
        # x = 1
        plt.xlabel("x - axis")
        plt.ylabel("y - axis")
        plt.axvline(x = 0, c = "black")
        plt.axhline(y = 0, c = "black")
        if self.is_constant:
            plt.axhline(y = self.equation, label = f"y={self.equation}")
        else:
            if self.is_trigonometric: 
                if self.equation[0] == "-":
                    f = self.equation.replace("-", "-np.")
                else:
                    f = "np." + self.equation
                print(f)
                f = self.convert_to_numeric(f)
                dydx = Equation(self.diff())
                print("show graph", dydx.equation)
                if dydx.equation != "":
                    if dydx.equation[0] == "-":
                        f_diff = dydx.equation.replace("-", "-np.")
                    else:
                        f_diff = "np." + dydx.equation
                    print(f_diff)
                    f_diff = self.convert_to_numeric(f_diff)
                    plt.plot(x, eval(f_diff), label = f"y'={dydx.equation}")

                plt.plot(x, eval(f), label = f"y={self.equation}")
            else:
                f = self.convert_to_numeric(self.equation) # y = f(x)
                print("f", f)
                # f = self.convert_to_numeric(self.dydx)
                # dydx = self.diff()                         # y' = f'(x)
                dydx = Equation(self.diff())
                print("dydx", dydx.equation)
                d2ydx2 = Equation(dydx.diff())      # y'' = f''(x)
                print("d2ydx2", d2ydx2.equation)
                plt.plot(x, eval(f), label = f"y={self.equation}")
                if dydx.equation != "":
                    if dydx.is_constant:
                        plt.axhline(y = dydx.equation, label = f"y'={dydx.equation}")
                    else:
                        dydx_f = self.convert_to_numeric(dydx.equation)
                        plt.plot(x, eval(dydx_f), label = f"y'={dydx.equation}")
        plt.legend()
        plt.show()
