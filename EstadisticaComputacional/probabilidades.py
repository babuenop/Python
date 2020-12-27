import random

from bokeh.io import output_file, show
from bokeh.plotting import figure

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,0,'00']


def tirar_dado(numero_de_tiros):
    secuencia_de_tiros=[]
    
    for _ in range(numero_de_tiros):
        tiro = random.choice(numbers)
        secuencia_de_tiros.append(tiro)
    return secuencia_de_tiros
    

def main(numero_de_tiros, numero_de_intentos):
    tiros = []
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)

    t1=t2=t3=t2=t3=t4=t5=t6=t7=t8=t9=t10=t11=t12=t13=t14=t15=t16=t17=t18=t19=t20=t21=t22=t23=t24=t25=t26=t27=t28=t29=t30=t31=t32=t33=t34=t35=t36=t0=t00=0
    for tiro in tiros: 
        if 1 in tiro:
            t1 +=1
        elif 2 in tiro: 
            t2 +=1
        elif 3 in tiro: 
            t3 +=1
        elif 4 in tiro: 
            t4 +=1        
        elif 5 in tiro: 
            t5 +=1
        elif 6 in tiro: 
            t6 +=1
        elif 7 in tiro: 
            t7 +=1
        elif 8 in tiro: 
            t8 +=1        
        elif 9 in tiro: 
            t9 +=1
        elif 10 in tiro: 
            t10 +=1
        elif 11 in tiro: 
            t11 +=1
        elif 12 in tiro: 
            t12 +=1        
        elif 13 in tiro: 
            t13 +=1
        elif 14 in tiro: 
            t14 +=1
        elif 15 in tiro: 
            t15 +=1
        elif 16 in tiro: 
            t16 +=1        
        elif 17 in tiro: 
            t17 +=1
        elif 18 in tiro: 
            t18 +=1
        elif 19 in tiro: 
            t19 +=1
        elif 20 in tiro: 
            t20 +=1        
        elif 21 in tiro: 
            t21 +=1
        elif 22 in tiro: 
            t22 +=1
        elif 23 in tiro: 
            t23 +=1
        elif 24 in tiro: 
            t24 +=1        
        elif 25 in tiro: 
            t25 +=1
        elif 26 in tiro: 
            t26 +=1
        elif 27 in tiro: 
            t27 +=1
        elif 28 in tiro: 
            t28 +=1        
        elif 29 in tiro: 
            t29 +=1
        elif 30 in tiro: 
            t30 +=1
        elif 31 in tiro: 
            t31 +=1
        elif 32 in tiro: 
            t32 +=1        
        elif 33 in tiro: 
            t33 +=1
        elif 34 in tiro: 
            t34 +=1
        elif 35 in tiro: 
            t35 +=1
        elif 36 in tiro: 
            t36 +=1
        elif '00' in tiro: 
            t00 +=1
        elif 0 in tiro: 
            t0 +=1        

    p1 = t1/numero_de_intentos
    p2 = t2/numero_de_intentos
    p3 = t3/numero_de_intentos
    p4 = t4/numero_de_intentos
    p5 = t5/numero_de_intentos
    p6 = t6/numero_de_intentos
    p7 = t7/numero_de_intentos
    p8 = t8/numero_de_intentos
    p9 = t9/numero_de_intentos
    p10 = t10/numero_de_intentos
    p11 = t11/numero_de_intentos
    p12 = t12/numero_de_intentos
    p13 = t13/numero_de_intentos
    p14 = t14/numero_de_intentos
    p15 = t15/numero_de_intentos
    p16 = t16/numero_de_intentos
    p17 = t17/numero_de_intentos
    p18 = t18/numero_de_intentos
    p19 = t19/numero_de_intentos
    p20 = t20/numero_de_intentos
    p21 = t21/numero_de_intentos
    p22 = t22/numero_de_intentos
    p23 = t23/numero_de_intentos
    p24 = t24/numero_de_intentos
    p25 = t25/numero_de_intentos
    p26 = t26/numero_de_intentos
    p27 = t27/numero_de_intentos
    p28 = t28/numero_de_intentos
    p29 = t29/numero_de_intentos
    p30 = t30/numero_de_intentos
    p31 = t31/numero_de_intentos
    p32 = t32/numero_de_intentos
    p33 = t33/numero_de_intentos
    p34 = t34/numero_de_intentos
    p35 = t35/numero_de_intentos
    p36 = t36/numero_de_intentos
    p0 = t0/numero_de_intentos
    p00 = t00/numero_de_intentos

    media = (t1+t2+t3+t2+t3+t4+t5+t6+t7+t8+t9+t10+t11+t12+t13+t14+t15+t16+t17+t18+t19+t20+t21+t22+t23+t24+t25+t26+t27+t28+t29+t30+t31+t32+t33+t34+t35+t36+t0+t00)/38
    print (f'la media de tiros por numero es = {media}')
    print(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,p31,p32,p33,p34,p35,p36,p00,p0)

    graficar(numbers,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,p31,p32,p33,p34,p35,p36,p00,p0)

def graficar(numbers,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,p31,p32,p33,p34,p35,p36,p00,p0):
    output_file("bars.html")
    numbers=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','0','00']
    p = figure(x_range=numbers,  plot_height=250, title="Probabilidad de que juegue un numero en una Ruleta de Casino en 10000 intentos",x_axis_label='Numeros', y_axis_label='Probabilidad',toolbar_location=None, tools="")
    p.vbar(x=numbers, top=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,p31,p32,p33,p34,p35,p36,p00,p0], width=0.8)
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    show(p)

if __name__ == "__main__":
    numero_de_tiros = int(input('Cuantos tiros del dado: '))
    numero_de_intentos = int(input('Cuantos intentos quieres realizar: '))

    main(numero_de_tiros, numero_de_intentos)
   
