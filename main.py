#!usr/bin/env python

import vpython as v
import math as m
#from pynput import keyboard as kb
import keyboard
from matplotlib import widgets
import tkinter as tk

#ESTE ES EL BUENO AHORA MISMO
fps =24

faces = {4:(v.color.orange), #Naranja
         3:(v.color.yellow), #Amarillo
         6:(v.color.blue),   #Azul
         5:(v.color.green),   #Verde
         1:(v.color.white), #Blanco
         2:(v.color.red)    #Rojo
         }

stickers = [] 
angulo = 0
angulo2 = m.pi/2

for face_color in faces.values():
    if angulo<2*(m.pi): #caras inferiores LADOS
        for x in (-1,0,1):
            for y in (-1,0,1):
                if (x in (0,0,0) and y in (0,0,0)):
                    sticker=v.box(color=v.color.black, pos=v.vector(x,y,1.5), length=0.98, height=0.98, width=0.05)
                    sticker.rotate(angle=angulo,axis=v.vector(0,1,0), origin=v.vector(0,0,0))
                    stickers.append(sticker)
                else:
                    sticker=v.box(color=face_color, pos=v.vector(x,y,1.5), length=0.98, height=0.98, width=0.05)
                    sticker.rotate(angle=angulo, axis=v.vector(0,1,0), origin=v.vector(0,0,0))
                    stickers.append(sticker)
    
        angulo = angulo + (m.pi/2)
    else: #caras superiores ABAJO Y ARRIBA
        for x in (-1,0,1):
            for y in (-1,0,1):
                if x in (0,0,0) and y in (0,0,0):
                    sticker=v.box(color=v.color.black, pos=v.vector(x,y,1.5), length=0.98, height=0.98, width=0.05)
                    sticker.rotate(angle=angulo,axis=v.vector(1,0,0), origin=v.vector(0,0,0))
                    stickers.append(sticker)
                else:
                    sticker=v.box(color=face_color, pos=v.vector(x,y,1.5), length=0.98, height=0.98, width=0.05)
                    sticker.rotate(angle=angulo2, axis=v.vector(1,0,0), origin=v.vector(0,0,0))
                    stickers.append(sticker)
        angulo2 = -(m.pi)/2
        
while True:
    pass
  #  key = v.scene.keyboard.getkey()
    if keyboard.is_pressed("r"):
        angle = m.pi/2
        for r in v.arange(0,angle,angle/fps):
            v.rate(fps)
            for sticker in stickers:
                if v.dot(sticker.pos,v.vector(1,0,0))> 0.5:
                    sticker.rotate(angle=(angle/fps),axis=v.vector(1,0,0),origin=v.vector(0,0,0))
    elif keyboard.is_pressed("l"):
        angle = -m.pi/2
        for r in v.arange(0,angle,angle/fps):
            v.rate(fps)
            for sticker in stickers:
                if v.dot(sticker.pos,v.vector(-1,0,0))> 0.5:
                    sticker.rotate(angle=(angle/fps),axis=v.vector(-1,0,0),origin=v.vector(0,0,0))
    elif keyboard.is_pressed("u"):
        angle = -m.pi/2
        for r in v.arange(0,angle,angle/fps):
            v.rate(fps)
            for sticker in stickers:
                if v.dot(sticker.pos,v.vector(0,1,0))> 0.5:
                    sticker.rotate(angle=(angle/fps),axis=v.vector(0,1,0),origin=v.vector(0,0,0))          
    elif keyboard.is_pressed("d"):
        angle = m.pi/2
        for r in v.arange(0,angle,angle/fps):
            v.rate(fps)
            for sticker in stickers:
                if v.dot(sticker.pos,v.vector(0,-1,0))> 0.5:
                    sticker.rotate(angle=(angle/fps),axis=v.vector(0,-1,0),origin=v.vector(0,0,0))
    elif keyboard.is_pressed("1"):
        angle = -m.pi/2
        for r in v.arange(0,angle,angle/fps):
            v.rate(fps)
            for sticker in stickers:
                if v.dot(sticker.pos,v.vector(1,0,0))> 0.5:
                    sticker.rotate(angle=(angle/fps),axis=v.vector(1,0,0),origin=v.vector(0,0,0))
    elif keyboard.is_pressed("2"):
        angle = m.pi/2
        for r in v.arange(0,angle,angle/fps):
            v.rate(fps)
            for sticker in stickers:
                if v.dot(sticker.pos,v.vector(-1,0,0))> 0.5:
                    sticker.rotate(angle=(angle/fps),axis=v.vector(-1,0,0),origin=v.vector(0,0,0))
    elif keyboard.is_pressed("3"):
        angle = m.pi/2
        for r in v.arange(0,angle,angle/fps):
            v.rate(fps)
            for sticker in stickers:
                if v.dot(sticker.pos,v.vector(0,1,0))> 0.5:
                    sticker.rotate(angle=(angle/fps),axis=v.vector(0,1,0),origin=v.vector(0,0,0))          
    elif keyboard.is_pressed("4"):
        angle = -m.pi/2
        for r in v.arange(0,angle,angle/fps):
            v.rate(fps)
            for sticker in stickers:
                if v.dot(sticker.pos,v.vector(0,-1,0))> 0.5:
                    sticker.rotate(angle=(angle/fps),axis=v.vector(0,-1,0),origin=v.vector(0,0,0))

    '''def funcion():
        v.set("Hola")

    frame = tk.Frame()
    button= tk.Button(frame, text="hola", command=funcion)
    button.pack(side=tk.LEFT)
        
    v = tk.StringVar()
    text = tk.Entry(frame, textvariable=v )
    text.pack(side=tk.LEFT);
        
    frame.pack()
    frame.mainloop()'''
    
    '''
    def _initialize_widgets(self):
        self._ax_reset = self.figure.add_axes([0.75, 0.05, 0.2, 0.075])
        self._btn_reset = widgets.Button(self._ax_reset, 'Reset View')
        self._btn_reset.on_clicked(self._reset_view)

        self._ax_solve = self.figure.add_axes([0.55, 0.05, 0.2, 0.075])
        self._btn_solve = widgets.Button(self._ax_solve, 'Solve Cube')
        self._btn_solve.on_clicked(self._solve_cube)
        
    def _solve_cube(self, *args):
        move_list = self.cube._move_list[:]
        for (face, n, layer) in move_list[::-1]:
            self.rotate_face(face, -n, layer, steps=3)
        self.cube._move_list = []'''

#algoritmo resolucion cubo
        

                    


                

