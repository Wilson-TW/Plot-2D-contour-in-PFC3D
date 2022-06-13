"""
Created on Mon June 13 23:33:23 2022

@author: Yu-Sen,Lai

A simple tool for user to draw 2D contour plot in PFC3D
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
import itasca as it
from matplotlib.colors import LightSource
from PySide2 import QtCore, QtGui, QtWidgets, shiboken2
from vec import vec

dockWidget = it.dockWidget("Contour and Hillshade tool","",True)
dockWidget = shiboken2.wrapInstance(int(dockWidget),QtWidgets.QDockWidget)
widget = dockWidget.widget()
  
class Window(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(mainLayout)
        self.setWindowTitle(self.tr("Contour and Hillshade tool"))
        self.samplex = 0.0
        self.sampley = 0.0
        self.samplez = 0.0
        
        spinboxs = []
        #--------------------------------------------------------
        verticalGroupBox = QtWidgets.QGroupBox("Settings")
        layout1 = QtWidgets.QVBoxLayout()
        
        layout2 = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Sampling range in the x direction(min,max)")
        layout2.addWidget(label)
        layout1.addLayout(layout2)
        
        layout2 = QtWidgets.QHBoxLayout()
        spinBox = QtWidgets.QDoubleSpinBox()
        spinBox.setDecimals(5)
        spinBox.setRange(-sys.float_info.max, sys.float_info.max)
        spinBox.setValue(0.0)
        spinBox.setAlignment(QtCore.Qt.AlignRight)
        spinboxs.append(spinBox)  
        layout2.addWidget(spinboxs[0],1)
        
        spinBox = QtWidgets.QDoubleSpinBox(self)
        spinBox.setDecimals(5)
        spinBox.setRange(-sys.float_info.max, sys.float_info.max)
        spinBox.setValue(0.0)
        spinBox.setAlignment(QtCore.Qt.AlignRight)
        spinboxs.append(spinBox)
        layout2.addWidget(spinboxs[1],1)
        layout1.addLayout(layout2)
        
        layout2 = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Sampling range in the y direction(min,max)")
        layout2.addWidget(label)
        layout1.addLayout(layout2)
        
        layout2 = QtWidgets.QHBoxLayout()
        spinBox = QtWidgets.QDoubleSpinBox(self)
        spinBox.setDecimals(5)
        spinBox.setRange(-sys.float_info.max, sys.float_info.max)
        spinBox.setValue(0.0)
        spinBox.setAlignment(QtCore.Qt.AlignRight)
        spinboxs.append(spinBox)
        layout2.addWidget(spinboxs[2],1)
        
        spinBox = QtWidgets.QDoubleSpinBox(self)
        spinBox.setDecimals(5)
        spinBox.setRange(-sys.float_info.max, sys.float_info.max)
        spinBox.setValue(0.0)
        spinBox.setAlignment(QtCore.Qt.AlignRight)
        spinboxs.append(spinBox)
        layout2.addWidget(spinboxs[3],1)        
        layout1.addLayout(layout2)
        
        layout2 = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("The number of samples in the x direction")
        layout2.addWidget(label)
        layout1.addLayout(layout2)
        
        layout2 = QtWidgets.QHBoxLayout()
        spinBox = QtWidgets.QSpinBox(self)
        spinBox.setRange(-2**sys.int_info.bits_per_digit, 2**sys.int_info.bits_per_digit)
        spinBox.setValue(0)
        spinBox.setAlignment(QtCore.Qt.AlignRight)
        spinboxs.append(spinBox)
        layout2.addWidget(spinboxs[4],1)
        layout1.addLayout(layout2)
        
        layout2 = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("The number of samples in the y direction")
        layout2.addWidget(label)
        layout1.addLayout(layout2)
        
        layout2 = QtWidgets.QHBoxLayout()
        spinBox = QtWidgets.QSpinBox(self)
        spinBox.setRange(0, 10000)
        spinBox.setValue(0)
        spinBox.setAlignment(QtCore.Qt.AlignRight)
        spinboxs.append(spinBox)
        layout2.addWidget(spinboxs[5],1)
        layout1.addLayout(layout2)
        
        verticalGroupBox.setLayout(layout1)
        mainLayout.addWidget(verticalGroupBox)
        #--------------------------------------------------------
        verticalGroupBox = QtWidgets.QGroupBox("Hillshade settings")
        layout1 = QtWidgets.QVBoxLayout()

        layout2 = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Azimuth")
        layout2.addWidget(label)
        layout1.addLayout(layout2)
        
        layout2 = QtWidgets.QHBoxLayout()
        spinBox = QtWidgets.QSpinBox(self)
        spinBox.setRange(0, 360)
        spinBox.setValue(315)
        spinBox.setAlignment(QtCore.Qt.AlignRight)
        spinboxs.append(spinBox)        
        layout2.addWidget(spinboxs[6],1) 
        layout1.addLayout(layout2)
        
        layout2 = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Altitude")
        layout2.addWidget(label)
        layout1.addLayout(layout2)
        
        layout2 = QtWidgets.QHBoxLayout()
        spinBox = QtWidgets.QSpinBox(self)
        spinBox.setRange(0, 90)
        spinBox.setValue(45)
        spinBox.setAlignment(QtCore.Qt.AlignRight)
        spinboxs.append(spinBox)        
        layout2.addWidget(spinboxs[7],1)  
        layout1.addLayout(layout2)
 
        verticalGroupBox.setLayout(layout1)
        mainLayout.addWidget(verticalGroupBox)
        #--------------------------------------------------------
        verticalGroupBox = QtWidgets.QGroupBox("Contour settings")
        layout1 = QtWidgets.QVBoxLayout()

        layout2 = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Transparency")
        layout2.addWidget(label)
        layout1.addLayout(layout2)
        
        
        layout2 = QtWidgets.QHBoxLayout()
        spinBox = QtWidgets.QSpinBox(self)
        spinBox.setRange(0, 100)
        spinBox.setValue(60)
        spinBox.setAlignment(QtCore.Qt.AlignRight)
        spinboxs.append(spinBox)        
        
        Slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        Slider.setRange(0, 100)
        Slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        Slider.setValue(spinBox.value())
        spinBox.valueChanged.connect(Slider.setValue)
        Slider.valueChanged.connect(spinboxs[8].setValue)
        
        layout2.addWidget(Slider,1)
        layout2.addWidget(spinboxs[8])        
        layout1.addLayout(layout2)

        layout2 = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Number of contour lines")
        layout2.addWidget(label)
        layout1.addLayout(layout2)
        
        layout2 = QtWidgets.QHBoxLayout()
        spinBox = QtWidgets.QSpinBox(self)
        spinBox.setRange(0, 2**sys.int_info.bits_per_digit)
        spinBox.setValue(10)
        spinBox.setAlignment(QtCore.Qt.AlignRight)
        spinboxs.append(spinBox)        
        layout2.addWidget(spinboxs[9],1)
        layout1.addLayout(layout2)

        verticalGroupBox.setLayout(layout1)
        mainLayout.addWidget(verticalGroupBox)
        #--------------------------------------------------------        
        horizontalGroupBox = QtWidgets.QGroupBox("")
        layout = QtWidgets.QHBoxLayout()
        buttons = []
        for i in range(6):
            button = QtWidgets.QPushButton("Button %d" % (i + 1))
            layout.addWidget(button,1)
            buttons.append(button)
        horizontalGroupBox.setLayout(layout)
        mainLayout.addWidget(horizontalGroupBox)

        buttons[0].setText("DEM")
        def onButton0():
            sample_in_x = spinboxs[4].value()
            sample_in_y = spinboxs[5].value()
            self.samplex = np.linspace(spinboxs[0].value(), spinboxs[1].value(), num=sample_in_x)
            self.sampley = np.linspace(spinboxs[2].value(), spinboxs[3].value(), num=sample_in_y)
            self.samplez = np.zeros((sample_in_y,sample_in_x))           
            step_x = self.samplex[1] - self.samplex[0]
            step_y = self.sampley[1] - self.sampley[0]
            d_minz = it.domain_min_z()
            d_maxz = it.domain_max_z()
            l_bond = vec((self.samplex[0]-step_x*1.0,self.sampley[0]-step_y*1.0,d_minz))
            u_bond = vec((self.samplex[0]+step_x*1.0,self.sampley[0]+step_y*1.0,d_maxz))       
            xvec = vec((step_x,0.0,0.0))
            yvec = vec((0.0,step_y,0.0))
            max_z = 0.0                  
            for x in range(sample_in_x):
                for y in range(sample_in_y):
                    b_tuple = it.ball.inbox(l_bond, u_bond, intersect=True)
                    for b in b_tuple:
                        if max_z <= b.pos_z():
                          max_z = b.pos_z()
                          b_id = b.id()                         
                    self.samplez[y,x] = max_z            
                    l_bond = l_bond + yvec
                    u_bond = u_bond + yvec
                    max_z = 0.0
                l_bond = l_bond - yvec * (sample_in_y)
                u_bond = u_bond - yvec * (sample_in_y)
                l_bond = l_bond + xvec
                u_bond = u_bond + xvec
            plt.figure(figsize=(19.2,10.8), dpi = 100)
            cm = plt.cm.get_cmap('gist_gray')
            C1 = plt.contourf(self.samplex, self.sampley, self.samplez,spinboxs[9].value(), cmap = cm)
            plt.colorbar(C1)
            plt.title('DEM')
            plt.show()            
        buttons[0].clicked.connect(onButton0)

        #change the name of the first button to new and connect to a command
        buttons[1].setText("Contour")
        def onButton1():
            if self.samplez.sum() != 0.0:
                plt.figure(figsize=(19.2,10.8), dpi = 100)
                cm = plt.cm.get_cmap('terrain')
                C1 = plt.contourf(self.samplex, self.sampley, self.samplez,spinboxs[9].value(), cmap = cm, alpha = (1.0 - spinboxs[8].value()/100.0))
                plt.colorbar(C1)
                plt.title('Contour')
                plt.show()            
        buttons[1].clicked.connect(onButton1)
        
        #change the names of the later buttons
        buttons[2].setText("Contour line")
        def onButton2():
            if self.samplez.sum() != 0.0:
                plt.figure(figsize=(19.2,10.8), dpi = 100)
                cm = plt.cm.get_cmap('terrain')
                C1 = plt.contour(self.samplex, self.sampley, self.samplez,spinboxs[9].value(), cmap = cm, alpha = (1.0 - spinboxs[8].value()/100.0))
                plt.clabel(CS, inline=1, fontsize = 10, colors = 'red')
                plt.rcParams["font.weight"] = "bold"
                plt.colorbar(C1)
                plt.title('Contour line')            
                plt.show()                
        buttons[2].clicked.connect(onButton2)

        buttons[3].setText("Contour + Contour line")
        def onButton3():
            if self.samplez.sum() != 0.0:
                plt.figure(figsize=(19.2,10.8), dpi = 100)
                cm = plt.cm.get_cmap('terrain')
                C1 = plt.contourf(samplex, sampley, samplez, spinboxs[9].value(), cmap = cm, alpha = (1.0 - spinboxs[8].value()/100.0))
                CS = plt.contour(samplex, sampley, samplez, spinboxs[9].value(), colors = 'black')
                plt.clabel(CS, inline=1, fontsize = 12, colors = 'red')
                plt.rcParams["font.weight"] = "bold"
                plt.title('Contour + Contour line')            
                plt.colorbar(C1)
                plt.show()                
        buttons[3].clicked.connect(onButton3)

        buttons[4].setText("Hillshaded")
        def onButton4():
            if self.samplez.sum() != 0.0:           
                step_x = self.samplex[1] - self.samplex[0]
                step_y = self.sampley[1] - self.sampley[0]            
                ls = LightSource(azdeg=spinboxs[6].value(), altdeg= spinboxs[7].value())
                H0 = ls.hillshade(self.samplez, dx=step_x, dy=step_y, vert_exag=100.0, fraction = 1.0)
                plt.figure(figsize=(19.2,10.8), dpi = 100)
                C1 = plt.imshow(H0, extent=(self.samplex.min(), self.samplex.max(), self.sampley.min(), self.sampley.max()), cmap = 'gist_gray', interpolation='none')
                plt.title('Hillshaded') 
                plt.colorbar(C1)
                plt.show()            
        buttons[4].clicked.connect(onButton4)

        buttons[5].setText("Hillshaded + Contour")
        def onButton5():
            if self.samplez.sum() != 0.0:            
                ls = LightSource(azdeg=spinboxs[6].value(), altdeg= spinboxs[7].value()) 
                plt.figure(figsize=(12,9), dpi = 100)
                cm = plt.cm.get_cmap('terrain')
                step_x = self.samplex[1] - self.samplex[0]
                step_y = self.sampley[1] - self.sampley[0]                       
                H0 = ls.hillshade(self.samplez, dx=step_x, dy=step_y, vert_exag=100.0, fraction = 1.0)
                C1 = plt.imshow(self.samplez, extent=(self.samplex.min(), self.samplex.max(), self.sampley.min(), self.sampley.max()), interpolation='none', cmap = 'terrain')
                C0 = plt.imshow(H0, extent=(self.samplex.min(), self.samplex.max(), self.sampley.min(), self.sampley.max()), interpolation='none', cmap = 'gist_gray',alpha = (1.0 - spinboxs[8].value()/100.0), origin = 'lower')       
                plt.title('Hillshaded + Contour') 
                plt.colorbar(C1)
                plt.show()            
        buttons[5].clicked.connect(onButton5)

widget.layout().addWidget(Window())
dockWidget.show()
dockWidget.raise_()
