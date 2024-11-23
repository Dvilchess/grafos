import os
from networkx.algorithms.bipartite.cluster import robins_alexander_clustering
from networkx.algorithms.shortest_paths import weighted
from networkx.algorithms.shortest_paths.generic import shortest_path
from networkx.classes.function import path_weight
import networkx as nx 
import random
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt

class Ui_MainWindow(object): #clase para crear el menu
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 419)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 210, 751, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.bEjecutar = QtWidgets.QPushButton(self.groupBox_2)
        self.bEjecutar.setGeometry(QtCore.QRect(650, 40, 91, 31))
        self.bEjecutar.setObjectName("bEjecutar")
        self.bEjecutar.clicked.connect(self.clickejecutar)
        self.boxInterF = QtWidgets.QComboBox(self.groupBox_2)
        self.boxInterF.setGeometry(QtCore.QRect(460, 40, 181, 31))
        self.boxInterF.setObjectName("boxInterF")
        self.boxInterF.addItem("")
        self.boxInterF.addItem("")
        self.boxInterF.addItem("")
        self.boxInterF.addItem("")
        self.boxInterF.addItem("")
        self.boxElegirf = QtWidgets.QComboBox(self.groupBox_2)
        self.boxElegirf.setGeometry(QtCore.QRect(300, 40, 131, 31))
        self.boxElegirf.setObjectName("boxElegirf")
        self.boxElegirf.addItem("")
        self.boxPrincipal = QtWidgets.QComboBox(self.groupBox_2)
        self.boxPrincipal.setGeometry(QtCore.QRect(10, 40, 261, 31))
        self.boxPrincipal.setObjectName("boxPrincipal")
        self.boxPrincipal.addItem("")
        self.boxPrincipal.addItem("")
        self.boxPrincipal.addItem("")
        self.boxPrincipal.addItem("")
        self.boxPrincipal.addItem("")
        self.boxPrincipal.addItem("")
        self.labelcase1 = QtWidgets.QLabel(self.groupBox_2)
        self.labelcase1.setGeometry(QtCore.QRect(460, 20, 171, 16))
        self.labelcase1.setObjectName("labelcase1")
        self.labelRespuesta = QtWidgets.QLabel(self.groupBox_2)
        self.labelRespuesta.setGeometry(QtCore.QRect(10, 80, 731, 101))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.labelRespuesta.setFont(font)
        self.labelRespuesta.setText("")
        self.labelRespuesta.setTextFormat(QtCore.Qt.PlainText)
        self.labelRespuesta.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelRespuesta.setWordWrap(True)
        self.labelRespuesta.setObjectName("labelRespuesta")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 751, 181))
        self.groupBox.setObjectName("groupBox")
        self.bCrearf = QtWidgets.QPushButton(self.groupBox)
        self.bCrearf.setGeometry(QtCore.QRect(50, 50, 220, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bCrearf.setFont(font)
        self.bCrearf.setObjectName("bCrearf")
        self.bCrearf.clicked.connect(self.clickcrearf)
        self.bEliminarf = QtWidgets.QPushButton(self.groupBox)
        self.bEliminarf.setGeometry(QtCore.QRect(500, 50, 220, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bEliminarf.setFont(font)
        self.bEliminarf.setObjectName("bEliminarf")
        self.bEliminarf.clicked.connect(self.clickelimnarf)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bVerciudad = QtWidgets.QPushButton(self.groupBox)
        self.bVerciudad.setGeometry(QtCore.QRect(300, 50, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bVerciudad.setFont(font)
        self.bVerciudad.setObjectName("bVerciudad")
        self.bVerciudad.clicked.connect (self.clickvermap)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionCrear_grafo = QtWidgets.QAction(MainWindow)
        self.actionCrear_grafo.setObjectName("actionCrear_grafo")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionasd = QtWidgets.QAction(MainWindow)
        self.actionasd.setObjectName("actionasd")
        self.actionverificar_caminos = QtWidgets.QAction(MainWindow)
        self.actionverificar_caminos.setObjectName("actionverificar_caminos")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow): #funcion para aseignarles los textos al menu
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "My City"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Interaccion con las familias creadas"))
        self.bEjecutar.setText(_translate("MainWindow", "Ejecutar"))
        self.boxInterF.setItemText(0, _translate("MainWindow", "Elija una opcion"))
        self.bVerciudad.setText(_translate("MainWindow", "Ver mapa ciudad"))
        self.boxInterF.setItemText(1, _translate("MainWindow", "1) Ver miembros familia"))
        self.boxInterF.setItemText(2, _translate("MainWindow", "2) Ruta diaria mañana"))
        self.boxInterF.setItemText(3, _translate("MainWindow", "3) Ruta diaria tarde"))
        self.boxInterF.setItemText(4, _translate("MainWindow", "4) Mover familia"))
        self.boxElegirf.setItemText(0, _translate("MainWindow", "Elija una familia"))
        self.boxPrincipal.setItemText(0, _translate("MainWindow", "Elija una opcion"))
        self.boxPrincipal.setItemText(1, _translate("MainWindow", "1) Familia"))
        self.boxPrincipal.setItemText(2, _translate("MainWindow", "2) Supermercado"))
        self.boxPrincipal.setItemText(3, _translate("MainWindow", "3) Robo"))
        self.boxPrincipal.setItemText(4, _translate("MainWindow", "4) Incendio"))
        self.boxPrincipal.setItemText(5, _translate("MainWindow", "5) Emergencia medica"))
        self.labelcase1.setText(_translate("MainWindow", "Solo en opcion 1) Familia"))
        self.groupBox.setTitle(_translate("MainWindow", "Creacion de familias y ciudad"))
        self.bCrearf.setText(_translate("MainWindow", "Crear familias y ver ciudad"))
        self.bEliminarf.setText(_translate("MainWindow", "Eliminar familias y ciudad"))
        self.actionCrear_grafo.setText(_translate("MainWindow", "Ingresar grafo"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionasd.setText(_translate("MainWindow", "asd"))
        self.actionverificar_caminos.setText(_translate("MainWindow", "verificar caminos"))
      
    def clickcrearf (self): # funcion que ocurrira al clickear el boton crear ciudad
        msg = QtWidgets.QMessageBox()
        nr = random.randint (5,10) # eligira un numero aleatorio del 5 al 10 para crear esa cantidad en familias
        G = nx.Graph ()
        cont = 1
        verificacion = fam.cantidad #verifica que no hay familias ya creadas
        if verificacion == 0:
            while (cont <= nr ): # crea los miembros de la familia de forma aleatorioa
                flist = ["Familia " + str (cont)]
                p = random.randint(1 , 2)
                t1 = random.randint(1 , 2)
                n = 0
                t2 = 0
                if (p == 2):
                    n = random.randint(0 , 3)
                    t2 = 2
                if (p == 2 and t1 == 2 ):
                    t2 = 1
                cont += 1
                self.boxElegirf.addItems (flist)
                fam.crearfamilia (p,n,t1,t2)
            G.add_nodes_from (fam.Edificio) #agrega los nodos de las familias
            G.add_nodes_from (fam.Edificio2) #agrega los nodos de los edificios
            p_new_connection = 0.1
            new_edges = []  
            alpha = ["temp_text"] 
            while alpha!= []: # while para crear las conexiones de los nodos
                contador = 11
                while contador <= nr+7:
                    for node in G.nodes():    
                        connected = [to for (fr, to) in G.edges(node)]
                        unconnected = [n for n in G.nodes() if not n in connected]    

                        # agrega una conexion entre un nodo aleatorio probabilísticamente   
                        if len(unconnected): # solo lo hara si es posible una nueva conexion
                            if random.random() < p_new_connection: 
                                new = random.choice(unconnected)
                                if (node != new ): 
                                    G.add_edge(node, new ,weight = random.randint (1,5))
                                    new_edges.append( (node, new) )    
                                    unconnected.remove(new)    
                                    connected.append(new)   
                                    contador += 1
                alpha = list (nx.isolates(G))
            plt.figure(3,figsize=(10,10))
            pos=nx.fruchterman_reingold_layout(G) 
            nx.draw_networkx (G,pos)
            labels = nx.get_edge_attributes(G,'weight')
            nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,)
            gra.guardargrafo (G,G.nodes)
            plt.show()  #muestra el grafo
            msg.setWindowTitle ("Exito")
            msg.setText ("Se han creado las familias")
            x = msg.exec_() #popup de creacion de familia
        else :
            msg.setWindowTitle ("Error")
            msg.setText ("Ya creo una familia")
            x = msg.exec_() #popup de creacion de familia

    def clickvermap (self): #funcion para moestar el mapa
        G = gra.G
        if (G != 0):
            plt.figure(3,figsize=(10,10))
            pos=nx.fruchterman_reingold_layout(G) 
            nx.draw_networkx (G,pos)
            labels = nx.get_edge_attributes(G,'weight')
            nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,)
            gra.guardargrafo (G,G.nodes)
            plt.show()  #muestra el grafo   
 
    def clickejecutar (self): #lo que ocurrira al hacer click en el boton ejecutar
        content = self.boxPrincipal.currentText ()
        fami = "1) Familia"
        sup = "2) Supermercado"
        rob = "3) Robo"
        inc = "4) Incendio"
        eme = "5) Emergencia medica"
        O = self.boxPrincipal.currentIndex ()
        F = self.boxElegirf.currentIndex ()

        if fam.cantidad == 0: # si no hay ciudad creada avisara de ello
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle ("Error")
            msg.setText ("Aun no crea una ciudad")
            self.labelRespuesta.clear ()
            x=msg.exec_()

        elif (O > 0): # si el contenido de la caja de opciones es sobre el indice 0 trabajara con el resto del codigo
            if (content == fami):
                content2 = self.boxInterF.currentText ()
                noop = "Elija una opcion"
                verf = "1) Ver miembros familia"
                ruma = "2) Ruta diaria mañana"
                rutat = "3) Ruta diaria tarde"
                mofa = "4) Mover familia"
                if (F > 0):
                    if (content2 == noop): # si no elige una opcion para la familia le mostrara un mensaje al usuario de que no eligio un evento a interactuar con la familia
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle ("Error")
                        msg.setText ("Porfavor  elija una interaccion con la familia valida")
                        self.labelRespuesta.clear ()
                        x=msg.exec_()

                    if (content2 == verf): # si el contedio es ver familia mostrara los miembros de la familia y sus trabajos
                        t1 = fam.trabajo1[F-1]
                        t2 = fam.trabajo2[F-1]
                        text = str (fam.Edificio[F-1])
                        text += " \nAdultos:"+ str (fam.personas[F-1])
                        text += "\nNiños: "+ str (fam.ninos[F-1])
                        if t1 == 1 :
                            text += " \nTrabajo Adulto 1: Compañia luz  "
                            if t2 != 0 :
                                text += "\nTrabajo Adulto 2: Compañia agua "
                        if t1 == 2:
                            text += "\nTrabajo Adulto 1: Compañia agua "
                            if t2 !=0:
                                text += "\nTrabajo Adulto 2: Compañia luz "
                        self.labelRespuesta.setText (text)

                    if (content2 == ruma): # si el contenido es ruta mañana realizara esta accion, esta parte del codigo probablemente es completamente optimizable pero por ahora mientras funcione lo dejare asi
                        ruta = "inicia en casa de: "+str (fam.Edificio [F-1])
                        path = 0
                        G = gra.G
                        origen = fam.Edificio [F-1]
                        colegio = fam.Edificio2 [0]
                        n = fam.ninos [F-1]
                        t1 = fam.trabajo1 [F-1]
                        t2 = fam.trabajo2 [F-1]
                        if  n > 0: #verifica si hay niños y si los hay realizara estas acciones
                            path = shortest_path (G, source= origen, target = colegio, weight='weight')
                            ruta += "\n ruta para llegar al colegio"+ str (path)
                            origen = colegio
                            if t2 == 2 : # verifica el trabajo del 2do adulto y de paso verefica si hay un adulto
                                destino = fam.Edificio2 [2]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar a el trabajo Compañia agua del adulto no conductor"+str (path)
                                origen = destino
                                destino = fam.Edificio2 [1]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar a el trabajo Compañia luz del adulto conductor"+str (path)
                                self.labelRespuesta.setText (ruta)
                            else: # accion en caso de que el if anterior no fuera real
                                destino = fam.Edificio2 [1]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar a el trabajo Compañia luz del adulto no conductor"+str (path)
                                origen = destino
                                destino = fam.Edificio2 [2]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar a el trabajo Compañia agua del adulto conductor"+str (path)
                                self.labelRespuesta.setText (ruta)
                        else: # si no hay niños hara esto
                            if t2 == 2: # estos if verifican los trabajos de los adultos 2 adultos y de paso si es que hay 2 adultos
                                destino = fam.Edificio2 [2]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar a el trabajo Compañia agua del adulto no conductor"+str (path)
                                origen = destino
                                destino = fam.Edificio2 [1]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar a el trabajo Compañia luz del adulto conductor"+str (path)
                                self.labelRespuesta.setText (ruta)
                            if t2 == 1: 
                                destino = fam.Edificio2 [1]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar a el trabajo Compañia luz del adulto no conductor"+str (path)
                                origen = destino
                                destino = fam.Edificio2 [2]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar a el trabajo Compañia agua del adulto conductor"+str (path)
                                self.labelRespuesta.setText (ruta)
                            if t2 == 0 and t1 == 1: # estos if comprueban que como t2 es 0 significa que esa familia esta compuesta por 1 solo adulto
                                destino = fam.Edificio2 [1]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar a el trabajo Compañia luz del adulto conductor"+str (path)
                                self.labelRespuesta.setText (ruta)
                            if t2 == 0 and t1 == 2:
                                destino = fam.Edificio2 [2]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar a el trabajo Compañia agua del adulto conductor"+str (path)
                                self.labelRespuesta.setText (ruta)

                    if (content2 == rutat): # realiza acciones en caso de elegir ruta tarde, todos los if y else hacen la misma logica que los de la mañana pero de manera inversa y pasando por el supermercado, reitero que esto se puede optimizar pero mientras funcione lo dejare asi
                        ruta = 0
                        path = 0
                        G = gra.G
                        origen = 0
                        colegio = fam.Edificio2 [0]
                        n = fam.ninos [F-1]
                        t1 = fam.trabajo1 [F-1]
                        t2 = fam.trabajo2 [F-1]
                        if  n > 0:
                            if t2 == 2 :
                                ruta = "inicia en trabajo adulto conductor en Compañia luz:"
                                origen = fam.Edificio2 [1]
                                destino = fam.Edificio2 [2]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar a el trabajo Compañia agua del adulto no conductor"+str (path)
                                origen = destino

                            else:
                                ruta = "inicia en trabajo adulto conductor en Compañia agua:"
                                origen = fam.Edificio2 [2]
                                destino = fam.Edificio2 [1]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar a el trabajo Compañia luz del adulto no conductor"+str (path)
                                origen = destino   
                            path = shortest_path (G, source= origen, target = colegio, weight='weight')
                            ruta += "\n ruta para llegar al colegio"+ str (path)
                            origen = colegio
                            destino = fam.Edificio2 [6]
                            path = shortest_path (G, source= origen, target =destino, weight='weight' )
                            ruta += "\n ruta para llegar al Supermercado"+ str (path)
                            origen = destino
                            destino = fam.Edificio [F-1]
                            path = shortest_path (G, source= origen, target =destino, weight='weight' )
                            ruta += "\n ruta para llegar a la casa de la "+str (destino) + str (path)
                            self.labelRespuesta.setText (ruta)
                        else:
                            if t2 == 2:
                                ruta = "inicia en trabajo adulto conductor en Compañia luz:"
                                origen = fam.Edificio2 [1]
                                destino = fam.Edificio2 [2]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar a el trabajo Compañia agua del adulto no conductor"+str (path)
                                origen = destino
                                destino = fam.Edificio2 [6]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar al Supermercado"+ str (path)
                                origen = destino
                                destino = fam.Edificio [F-1]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar a la casa de la "+str (destino) + str (path)
                                self.labelRespuesta.setText (ruta)
                            if t2 == 1:
                                ruta = "inicia en trabajo adulto conductor en Compañia agua:"
                                origen = fam.Edificio2 [2]
                                destino = fam.Edificio2 [1]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar a el trabajo Compañia luz del adulto no conductor"+str (path)
                                origen = destino
                                destino = fam.Edificio2 [6]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar al Supermercado"+ str (path)
                                origen = destino
                                destino = fam.Edificio [F-1]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar a la casa de la "+str (destino) + str (path)
                                self.labelRespuesta.setText (ruta)
                            if t2 == 0 and t1 == 1:
                                ruta = "inicia en trabajo adulto conductor en Compañia luz:"
                                origen = fam.Edificio2 [2]
                                destino = fam.Edificio2 [6]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar al Supermercado"+ str (path)
                                origen = destino
                                destino = fam.Edificio [F-1]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar a la casa de la "+str (destino) + str (path)
                                self.labelRespuesta.setText (ruta)
                            if t2 == 0 and t1 == 2:
                                ruta = "inicia en trabajo adulto conductor en Compañia agua:"
                                origen = fam.Edificio2 [2]
                                destino = fam.Edificio2 [6]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar al Supermercado"+ str (path)
                                origen = destino
                                destino = fam.Edificio [F-1]
                                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                                ruta += "\n ruta para llegar a la casa de la "+str (destino) + str (path)
                                self.labelRespuesta.setText (ruta)
                    if (content2 == mofa): # si el contenido es mover familia realizara esta accion
                        G = gra.G
                        origen = fam.Edificio [F-1]
                        destino = fam.Edificio2 [random.randint(1,F+6)] #movera la familia a un lugar aleatorio
                        ruta = str (origen) + " movida aleatoriamente a " + str (destino) 
                        path = shortest_path (G, source= origen, target =destino, weight='weight' )
                        if origen != destino: #para evitar que el destino sea el mismo lugar de comienzo
                            ruta += " \nruta tomada :" + str (path)
                            self.labelRespuesta.setText (ruta)
                


            if (content == sup): # si el contenido es supermercado realizara esta accion
                G = gra.G
                res = "La ruta del camion del supermercado es: "
                casas = fam.Edificio.copy ()
                n = len(casas)
                origen = 'Supermercado'
                while (n != 0): # con este while guardo las rutas y remuevo las casas visitadas de la lista
                    cont = 0
                    cal = 100
                    pc = ''
                    while (cont <= n-1 ): # con este while reviso las las casas faltantes para entregar el producto y elige la mas cercana
                        destino = casas [cont] 
                        path = shortest_path (G, source= origen, target =destino, weight='weight' )
                        path_length = path_weight(G, path, weight="weight")
                        if (path_length < cal):
                            cal = path_length
                            pc = destino
                            p = path
                        cont += 1
                    res += str (p) + '  '
                    origen = pc
                    casas.remove (pc)
                    n = len (casas)
                destino = 'Supermercado'
                path = shortest_path (G, source= origen, target =destino, weight='weight' )
                res += str (path)
                self.labelRespuesta.setText (res)    

            if (content == rob ): # si el contenido es robo realizara esta accion generara un "evento" en un lugar aleatorio y buscara la ruta mas corta para llegar a ese destino
                G = gra.G
                casas = fam.Edificio.copy ()
                n = len(casas)
                destino = fam.Edificio2 [random.randint(1,n+6)]
                test = "Ocurrio un robo en: "+ str (destino)
                origen = fam.Edificio2 [4]
                if origen != destino:
                    path = shortest_path (G, source= origen, target =destino, weight='weight' )
                    test += " \nLa ruta mas corta para llegar de la policia es:\n" + str (path)
                    self.labelRespuesta.setText (test)

            if (content == inc):  # si el contenido es incendio realizara esta accion generara un "evento" en un lugar aleatorio y buscara la ruta mas corta para llegar a ese destino
                G = gra.G
                casas = fam.Edificio.copy ()
                n = len(casas)
                destino = fam.Edificio2 [random.randint(1,n+6)]
                test = "Ocurrio un incendio en: "+ str (destino)
                origen = fam.Edificio2 [3]
                if origen != destino:
                    path = shortest_path (G, source= origen, target =destino, weight='weight' )
                    test += " \nLa ruta mas corta para llegar de los bomberos es:\n" + str (path)
                    self.labelRespuesta.setText (test)

            if (content == eme): # si el contenido es emergencia realizara esta accion generara un "evento" en un lugar aleatorio y buscara la ruta mas corta para llegar a ese destino
                G = gra.G
                casas = fam.Edificio.copy ()
                n = len(casas)
                destino = fam.Edificio2 [random.randint(1,n+6)]
                test = "Ocurrio una emergencia medica en: "+ str (destino)
                origen = fam.Edificio2 [5]
                if origen != destino:
                    path = shortest_path (G, source= origen, target =destino, weight='weight' )
                    test += " \nLa ruta mas corta para llegar de servicios de emergencias es:\n" + str (path)
                    self.labelRespuesta.setText (test)




    def clickelimnarf (self): #funcion al boton eliminar
        fam.limpiar()
        gra.limpiar ()
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Exito")
        msg.setText ("Se han borrado todas los familias")
        self.boxElegirf.clear() # estos clear son para eliminar las familias
        self.boxElegirf.addItems (["Elija una familia"])
        self.labelRespuesta.clear ()
        x =msg.exec_()
        



class Familia ():
    def __init__(self): #inicializar las familias
        self.personas = []
        self.ninos = []
        self.trabajo1 = []
        self.trabajo2 = []
        self.cantidad = 0
        self.Edificio = []
        self.Mover = []
        self.Edificio2 = ["Colegio","Compañia luz","Compañia agua","Bomberos","Policia","Hospital","Supermercado"]
    
    def crearfamilia (self, personas, ninos, trabajo1, trabajo2): #creara las familias de la ciudad 
        self.personas.append (personas)
        self.ninos.append (ninos)
        self.trabajo1.append (trabajo1)
        self.trabajo2.append (trabajo2)
        self.cantidad += 1
        self.Edificio.append  ( "Familia "+ str (self.cantidad))
        self.Edificio2.append  ( "Familia "+ str (self.cantidad))
        

    def limpiar(self): #Limpiar las familias
        self.personas = []
        self.ninos = []
        self.trabajo1 = []
        self.trabajo2 = []
        self.cantidad = 0
        self.Edificio = []
        self.Edificio2 = ["Colegio","Compañia luz","Compañia agua","Bomberos","Policia","Hospital","Supermercado"]
   


class grafo (): #clase para guardar el grafo
    def __init__ (self):
        self.G = 0
        self.Nodes = 0
    def guardargrafo (self,grafo,node):
        self.G = grafo
        self.Nodes = node

    def limpiar (self):
        self.G = 0
        self.Nodes = 0
        
gra = grafo ()
fam = Familia ()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())