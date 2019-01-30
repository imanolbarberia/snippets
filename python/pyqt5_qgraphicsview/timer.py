#!/usr/bin/env python3

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsEllipseItem, QGraphicsScene
import sys

size = 0

app = QApplication(sys.argv)

graphicsView = QGraphicsView()
graphicsView.setWindowTitle("Timer test")

graphicsView.setGeometry(QtCore.QRect(600,300,250,250))
graphicsView.scene = QGraphicsScene()
graphicsView.setScene(graphicsView.scene)

def draw():
    global size
    size +=1
    
    size2Nd = size * 2
    
    if(size>=240):
        size = 1
        
    if (size2Nd >= 240 ):
        size2Nd = 1
        
    graphicsView.scene.clear()
    
    graphicsView.item = QGraphicsEllipseItem(125 - size/2, 125 - size/2, size, size)
    graphicsView.scene.addItem(graphicsView.item)
    
    graphicsView.item = QGraphicsEllipseItem(125 - size2Nd/2, 125 - size2Nd/2, size2Nd, size2Nd)
    graphicsView.scene.addItem(graphicsView.item)
    
graphicsView.show()

timer = QtCore.QTimer()
timer.timeout.connect(draw)
timer.start(1000)

print( "Pues no es bloqueante")

sys.exit(app.exec_())
