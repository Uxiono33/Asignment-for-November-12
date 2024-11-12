import numpy

#Esta altura es positiva y se mide con respecto al origen el altura 0 el suelo
initial_Heigh= float(input('Enter the initial height in meters'))
#He establecido la gravedad como negativa para denotar que tomo el suelo como referncia
g = -9.81


    #Este tf hace referencia al momento en el que el objeto toca el suelo lo úso como valor final de mi lista para que no me den alturas negativas
tf= (((-float(initial_Heigh) )*2)/g)**(1/2)
Times = numpy.linspace(0,tf,num=int(tf+1))
    
    #Ya que no es exactamente cada segundo sino una aproximación mi programa printea también la liosta de tiempos , junto con la posición en cada uno de esos instantes
print(Times,"s")
y = (initial_Heigh + ((1/2)* g * Times**2))
    #Es apreciable que al no tener en cuenta el rozamiento con el aire el objeto no alcanza velocidad terminal por lo que su velocidad crece de forma indefinida, haciendo que el objeto tarde segundos en recorrer kilómetros
print(y,"m")
z=numpy.mean(y)
print(z,"m")

