#Numeros complejos
#MICHAEL BALLESTEROS
#2019-2

import math

def suma(c1,c2):
    """Recibo 2 complejos y los suma -> complejo
    """
    a1,b1,a2,b2=c1[0],c1[1],c2[0],c2[1]
    return (a1+a2,b1+b2)
def resta(c1,c2):
    """Recibo 2 complejos y los resta -> complejo
    """
    a1,b1,a2,b2=c1[0],c1[1],c2[0],c2[1]
    return (a1-a2,b1-b2)
def multiplicacion(c1,c2):
    """Recibo 2 complejos y los multiplica -> complejo
    """
    a1,b1,a2,b2=c1[0],c1[1],c2[0],c2[1]
    return (a1*a2-b1*b2,a1*b2+a2*b1)
def division(c1,c2):
    """Recibo 2 complejos y los divido -> complejo
    """
    a1,b1,a2,b2=c1[0],c1[1],c2[0],c2[1]
    x = float("{0:.1f}".format((a1*a2+b1*b2)/(a2**2+b2**2)))
    y = float("{0:.1f}".format((a2*b1-a1*b2)/(a2**2+b2**2)))
    return (x,y)
def modulo(c1):
    """Complejo y hallo modulo -> entero
    """
    a1,b1=c1[0],c1[1]
    return float("{0:.2f}".format((a1**2+b1**2)**(1/2)))
def conjugado(c1):
    """Recibo complejos y lo conjuga -> complejo
    """
    a1,b1=c1[0],c1[1]
    return (a1,b1*-1)
def fase(c):
    """Recibo complejo hallo fase en grados -> entero
    """
    a,b=c[0],c[1]
    return float("{0:.2f}".format(((math.atan2(b,a))*180)/math.pi))
def convpolaracartesiano(c):
    """Recibo polar (angulo en grados)y doy cartesiano -> Cartesiano
    """
    p,ang=c[0],(c[1]*math.pi)/180
    x=float("{0:.2f}".format(p*math.cos(ang)))
    y=float("{0:.2f}".format(p*math.sin(ang)))
    return (x,y)
def convcartesianoapolar(c):
    """Recibo cartesiano y doy polar -> Polar
    """
    a,b = c[0],c[1]
    p = modulo(c)
    ang = fase(c)
    return (p,ang)

#c = tuple(map(float,input().split(",")))
#c1 = tuple(map(int,input().split(",")))
#c2 = tuple(map(int,input().split(",")))

#print(suma(c1,c2))
#print(resta(c1,c2))
#print(multiplicacion(c1,c2))
#print(division(c1,c2))
#print(modulo(c))
#print(conjugado(c))
#print(convpolaracartesiano(c))
#print(convcartesianoapolar(c))
#print(fase(c))
