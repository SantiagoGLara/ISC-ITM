import matplotlib.pyplot as plt;
fig, ax = plt.subplots();
ax.plot([1,1,4,4,1],[10,20,20,10,10]);

yMin=10;
yMax=20;
xMin=1;
xMax=4;
# en el primer arreglo le estamos pasando los puntos de x de la grafica y en el segundo los y, viendolo asi como 4 pares ordenados la siguiente manera: (1,10),(1,20),(4,20),(4,10) y de regreso (1,10). La funcion va pintando las lineas en ese orden, es decir, que primero marca el punto (1,10), marca el (1,20) y el camino hasta el (1,20) y asi sucesivamente, por eso al final repetimos el (1,10), para cerrar la figura
ax.set_title("Cuadrado");
ax.set_xlabel("eje x");
ax.set_ylabel("eje Y");
ax.grid(True);
plt.show();