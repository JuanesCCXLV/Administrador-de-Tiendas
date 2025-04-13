from tkinter import *
from tkinter import ttk
import tkinter as tk 
import os
from tkinter import filedialog
import pandas as pd 
from tkinter import messagebox 
from openpyxl import Workbook 
from openpyxl import load_workbook 
login=Tk() 
login.title("Login") 
login.geometry("300x300")
login.resizable(width=False, height=False)
usuario=StringVar() 
usuario_label=Label(login, text="Ingrese Usuario") 
usuario_label.pack() 
usuario_entry=Entry(login, width=30, show="*", textvariable=usuario)
usuario_entry.pack() 
password=StringVar()
password_label=Label(login, text="Ingrese Contraseña")
password_label.pack()
password_entry=Entry(login, width=30, show="*", textvariable=password)
password_entry.pack() 
def ingresar(): 
    if usuario_entry.get()=="ardidas" and password_entry.get()=="123456":
        login.title("Correcto") 
        arididas()
        login.deiconify
        login.iconify
        login.destroy
    elif usuario_entry.get()=="caleñito" and password_entry.get()=="123456":
        login.title("Correcto") 
        calenito()
        login.deiconify
        login.iconify
        login.destroy
    elif usuario_entry.get()=="agacher" and password_entry.get()=="123456":
        login.title("Correcto") 
        agacheR()
        login.deiconify
        login.iconify
        login.destroy
    elif usuario_entry.get()=="pasteles" and password_entry.get()=="123456":
        login.title("Correcto") 
        pasteles()
        login.deiconify
        login.iconify
        login.destroy
    elif usuario_entry.get()=="asados" and password_entry.get()=="123456":
        login.title("Correcto") 
        asados()
        login.deiconify
        login.iconify
        login.destroy
    elif usuario_entry.get()=="empanadas" and password_entry.get()=="123456":
        login.title("Correcto") 
        empanadas()
        login.deiconify
        login.iconify
        login.destroy
    elif usuario_entry.get()=="samsung" and password_entry.get()=="123456":
        login.title("Correcto") 
        samgung()
        login.deiconify
        login.iconify
        login.destroy
    elif usuario_entry.get()=="applepera" and password_entry.get()=="123456":
        login.title("Correcto") 
        applepera()
        login.deiconify
        login.iconify
        login.destroy
    elif usuario_entry.get()=="tecnicos" and password_entry.get()=="123456":
        login.title("Correcto") 
        tecnicos()
        login.deiconify
        login.iconify
        login.destroy
    else: 
        login.title("Incorrecto")

b1=Button(login, text="Ingresar", command=ingresar)
b1.pack()

def arididas(): 
    ardidas2=Toplevel()
    ardidas2.geometry("1400x1000")
    ardidas2.title("Tienda Ardidas")
    def almacenaArchivo(nombreFile, cadenaAlmacenar):
        print('Inicia Registro de Ventas')
        file=open(nombreFile,'a')
        file.write(cadenaAlmacenar)
        file.close()
        print('Finaliza Registro de venta')
        
    def validararchivo(nombreFile):
        if os.stat(nombreFile).st_size==0:
         cadenaEncabezado="NOMBRE | FECHA | CODIGO | PRECIO | CANTIDAD \n"
         almacenaArchivo(nombreFile,cadenaEncabezado)

    def seleccionado():
        nombr.delete(0, END)
        fech.delete(0, END)
        codig.delete(0, END)
        precio_entry(0, END)
        cantida.delete(0, END)
        selected=trev.focus() 
        valr=trev.item(selected, "values")
        nombr.insert(0, valr[0])
        fech.insert(0, valr[1])
        codig.insert(0, valr[2])
        precio_entry.insert(0, valr[3])
        cantida.insert(0, valr[4])   

    def eliminarcasillas(): 
        nombr.delete(0, END)
        fech.delete(0, END)
        codig.delete(0, END)
        precio_entry.delete(0, END)
        cantida.delete(0, END)

    def enviardatos(): 
        nombredata=nombre.get()
        fechadata=fecha.get() 
        codigodata=codigo.get() 
        preciodata=precio_entry.get()
        cantidaddata=cantidad.get()
        print(nombredata, fechadata, codigodata, cantidaddata)
        cadenaRegistro = nombredata + '|' + fechadata + '|' + str(codigodata) + '|' + str(preciodata) + '|'  + str(cantidaddata) +'\n'
        validararchivo("registroventas.txt")
        almacenaArchivo("registroventas.txt", cadenaRegistro)
        trev.insert("", END,  text="Activo", values=(nombr.get(), fech.get(), codig.get(),  precio_entry.get(), cantida.get()))
       

    def abrir_archivo():

        archivo = filedialog.askopenfilename(initialdir ='/', 
        title='Selecione archivo', 
        filetype=(('xlsx files', '*.xlsx*'),('All files', '*.*')))
        indica['text'] = archivo


    def datos_excel():

        datos_obtenidos = indica['text']
        try:
            archivoexcel = r'{}'.format(datos_obtenidos)
            

            df = pd.read_excel(archivoexcel)

        except ValueError:
            messagebox.showerror('Informacion', 'Formato incorrecto')
            return None

        except FileNotFoundError:
            messagebox.showerror('Informacion', 'El archivo esta \n malogrado')
            return None

        Limpiar()

        tabla['column'] = list(df.columns)
        tabla['show'] = "headings"  #encabezado
        

        for columna in tabla['column']:
            tabla.heading(columna, text= columna)
        

        df_fila = df.to_numpy().tolist()
        for fila in df_fila:
            tabla.insert('', 'end', values =fila)


    def Limpiar():
        tabla.delete(*tabla.get_children())
    #---------Defino algunas variables que usare en diferentes funciones----------------------
    nombre=StringVar()
    fecha=StringVar()
    codigo=IntVar() 
    prec=DoubleVar() 
    cantidad=IntVar() 
    #---------------Panel de pestañas----------------------------------------------
    panel=ttk.Notebook(ardidas2) 
    panel.pack(fill="both", expand="yes")   
    #Pestaña 1-------------------------------------------------------------------------------
    tab1=ttk.Frame(panel)
    panel.add(tab1, text="Ventas") 
    indica=Label(tab1, fg="blue", text="Ubicación del archivo", font=("Arial", 10, "bold")).place(x=400, y=70)
    nombrA = Label(tab1, text="Nombre:").place(x=22, y=70)
    nombr = Entry(tab1, textvariable=nombre, width="40")
    nombr.place(x=22, y=100)
    fechA=Label(tab1, text="Fecha D/M/A: ").place(x=22, y=130) 
    fech=Entry(tab1, textvariable=fecha, width="40")
    fech.place(x=22, y=160)  
    codigA=Label(tab1, text="Código:").place(x=22, y=190)
    codig=Entry(tab1, textvariable=codigo, width="40")
    codig.place(x=22, y=220)
    precio_label=Label(tab1, text="Precio: ").place(x=22, y=250)
    precio_entry=Entry(tab1, textvariable=prec, width="40")
    precio_entry.place(x=22, y=270)
    cantidaA=Label(tab1, text="Cantidad:").place(x=22, y=300)
    cantida=Entry(tab1, textvariable=cantidad, width="40")
    cantida.place(x=22, y=330)   
    #----------------Botones--------------------------------------------
    etiqueta=Label(tab1, text="Sección de registro de ventas").place(x=400, y=5)
    datost=Label(tab1, text="Para efectuar una venta y enviar los datos del cliente, clique el siguiente boton:").place(x=400, y=150)
    botonenviar=ttk.Button(tab1, text="Enviar datos de registro", command=enviardatos).place(x=400, y=100) 
    borrarlabel=Label(tab1, text="Para limpiar los campos de entrada de texto pulse: Limpiar").place(x=400, y=200)
    botonlimpiar=ttk.Button(tab1, text="Limpiar", command=eliminarcasillas).place(x=400, y=250)
    labelusuario=Label(tab1, text="Tienda: " + usuario_entry.get(), font="Helvetica 20 bold", fg="red" ).place(x=700,  y=5)
    #Treeview--------------------
    trev=ttk.Treeview(tab1, columns=("col1", "col2", "col3", "col4", "col5"))
    trev.column("#0", width=150, anchor=CENTER)
    trev.heading("#0", text="Venta", anchor=CENTER)
    trev.heading("col1", text="Producto", anchor=CENTER)
    trev.column("col1", width=150, anchor=CENTER)
    trev.heading("col2", text="Fecha", anchor=CENTER)
    trev.column("col3", width=150, anchor=CENTER)
    trev.heading("col3", text="Código", anchor=CENTER)
    trev.column("col4", width=150, anchor=CENTER)
    trev.heading("col4", text="Precio", anchor=CENTER)
    trev.column("col5", width=150, anchor=CENTER)
    trev.heading("col5", text="Cantidad", anchor=CENTER)
    trev.place(y=500)
    #Pestaña 2 Inventario de recursos---------------------------------------------------------------------------------------------------------------------
    tab2=ttk.Frame(panel)
    panel.add(tab2, text="Inventario")
    tab2.columnconfigure(0, weight = 25)
    tab2.rowconfigure(0, weight= 25)
    tab2.columnconfigure(0, weight = 1)
    tab2.rowconfigure(1, weight= 1)

    frame1 = Frame(tab2, bg='gray26')
    frame1.grid(column=0,row=0,sticky='nsew')
    frame2 = Frame(tab2, bg='gray26')
    frame2.grid(column=0,row=1,sticky='nsew')

    frame1.columnconfigure(0, weight = 1)
    frame1.rowconfigure(0, weight= 1)

    frame2.columnconfigure(0, weight = 1)
    frame2.rowconfigure(0, weight= 1)
    frame2.columnconfigure(1, weight = 1)
    frame2.rowconfigure(0, weight= 1)

    frame2.columnconfigure(2, weight = 1)
    frame2.rowconfigure(0, weight= 1)

    frame2.columnconfigure(3, weight = 2)
    frame2.rowconfigure(0, weight= 1)

    tabla = ttk.Treeview(tab2, height=10)
    tabla.grid(column=0, row=0, sticky='nsew') 

    ladox = Scrollbar(frame1, orient = HORIZONTAL, command= tabla.xview)
    ladox.grid(column=0, row = 1, sticky='ew') 

    ladoy = Scrollbar(frame1, orient =VERTICAL, command = tabla.yview)
    ladoy.grid(column = 1, row = 0, sticky='ns')

    tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)

    estilo = ttk.Style(frame1)
    estilo.theme_use('clam') #  ('clam', 'alt', 'default', 'classic')
    estilo.configure(".",font= ('Arial', 14))
    estilo.configure("Treeview", font= ('Helvetica', 12))
    estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

    boton1 = Button(frame2, text= 'Abrir', bg='green2', command= abrir_archivo)
    boton1.grid(column = 0, row = 0, sticky='nsew', padx=10, pady=10)

    boton2 = Button(frame2, text= 'Mostrar', bg='magenta', command= datos_excel)
    boton2.grid(column = 1, row = 0, sticky='nsew', padx=10, pady=10)

    boton3 = Button(frame2, text= 'Limpiar', bg='red', command= Limpiar)
    boton3.grid(column = 2, row = 0, sticky='nsew', padx=10, pady=10)

    indica = Label(frame2, fg= 'white', bg='gray26', text= 'Ubicación del archivo', font= ('Arial',10,'bold') )
    indica.grid(column=3, row = 0)
    

def calenito(): 
    calenito=Toplevel()
    calenito.geometry("1400x1000")
    calenito.title("Tienda El Caleñito")
    def almacenaArchivo(nombreFile, cadenaAlmacenar):
        print('Inicia Registro de Ventas')
        file=open(nombreFile,'a')
        file.write(cadenaAlmacenar)
        file.close()
        print('Finaliza Registro de venta')
        
    def validararchivo(nombreFile):
        if os.stat(nombreFile).st_size==0:
         cadenaEncabezado="NOMBRE | FECHA | CODIGO | PRECIO | CANTIDAD \n"
         almacenaArchivo(nombreFile,cadenaEncabezado)

    def seleccionado():
        nombr.delete(0, END)
        fech.delete(0, END)
        codig.delete(0, END)
        precio_entry(0, END)
        cantida.delete(0, END)
        selected=trev.focus() 
        valr=trev.item(selected, "values")
        nombr.insert(0, valr[0])
        fech.insert(0, valr[1])
        codig.insert(0, valr[2])
        precio_entry.insert(0, valr[3])
        cantida.insert(0, valr[4])   

    def eliminarcasillas(): 
        nombr.delete(0, END)
        fech.delete(0, END)
        codig.delete(0, END)
        precio_entry.delete(0, END)
        cantida.delete(0, END)

    def enviardatos(): 
        nombredata=nombre.get()
        fechadata=fecha.get() 
        codigodata=codigo.get() 
        preciodata=precio_entry.get()
        cantidaddata=cantidad.get()
        print(nombredata, fechadata, codigodata, cantidaddata)
        cadenaRegistro = nombredata + '|' + fechadata + '|' + str(codigodata) + '|' + str(preciodata) + '|'  + str(cantidaddata) +'\n'
        validararchivo("registroventas.txt")
        almacenaArchivo("registroventas.txt", cadenaRegistro)
        trev.insert("", END,  text="Activo", values=(nombr.get(), fech.get(), codig.get(),  precio_entry.get(), cantida.get()))

    def abrir_archivo():

        archivo = filedialog.askopenfilename(initialdir ='/', 
        title='Selecione archivo', 
        filetype=(('xlsx files', '*.xlsx*'),('All files', '*.*')))
        indica['text'] = archivo


    def datos_excel():

        datos_obtenidos = indica['text']
        try:
            archivoexcel = r'{}'.format(datos_obtenidos)
            

            df = pd.read_excel(archivoexcel)

        except ValueError:
            messagebox.showerror('Informacion', 'Formato incorrecto')
            return None

        except FileNotFoundError:
            messagebox.showerror('Informacion', 'El archivo esta \n malogrado')
            return None

        Limpiar()

        tabla['column'] = list(df.columns)
        tabla['show'] = "headings"  #encabezado
        

        for columna in tabla['column']:
            tabla.heading(columna, text= columna)
        

        df_fila = df.to_numpy().tolist()
        for fila in df_fila:
            tabla.insert('', 'end', values =fila)


    def Limpiar():
        tabla.delete(*tabla.get_children())
    #---------Defino algunas variables que usare en diferentes funciones----------------------
    nombre=StringVar()
    fecha=StringVar()
    codigo=IntVar() 
    prec=DoubleVar() 
    cantidad=IntVar() 
    #---------------Panel de pestañas----------------------------------------------
    panel=ttk.Notebook(calenito) 
    panel.pack(fill="both", expand="yes")   
    #Pestaña 1-------------------------------------------------------------------------------
    tab1=ttk.Frame(panel)
    panel.add(tab1, text="Ventas") 
    indica=Label(tab1, fg="blue", text="Ubicación del archivo", font=("Arial", 10, "bold")).place(x=400, y=70)
    nombrA = Label(tab1, text="Nombre:").place(x=22, y=70)
    nombr = Entry(tab1, textvariable=nombre, width="40")
    nombr.place(x=22, y=100)
    fechA=Label(tab1, text="Fecha D/M/A: ").place(x=22, y=130) 
    fech=Entry(tab1, textvariable=fecha, width="40")
    fech.place(x=22, y=160)  
    codigA=Label(tab1, text="Código:").place(x=22, y=190)
    codig=Entry(tab1, textvariable=codigo, width="40")
    codig.place(x=22, y=220)
    precio_label=Label(tab1, text="Precio: ").place(x=22, y=250)
    precio_entry=Entry(tab1, textvariable=prec, width="40")
    precio_entry.place(x=22, y=270)
    cantidaA=Label(tab1, text="Cantidad:").place(x=22, y=300)
    cantida=Entry(tab1, textvariable=cantidad, width="40")
    cantida.place(x=22, y=330)   
    #----------------Botones--------------------------------------------
    etiqueta=Label(tab1, text="Sección de registro de ventas").place(x=400, y=5)
    datost=Label(tab1, text="Para efectuar una venta y enviar los datos del cliente, clique el siguiente boton:").place(x=400, y=150)
    botonenviar=ttk.Button(tab1, text="Enviar datos de registro", command=enviardatos).place(x=400, y=100) 
    borrarlabel=Label(tab1, text="Para limpiar los campos de entrada de texto pulse: Limpiar").place(x=400, y=200)
    botonlimpiar=ttk.Button(tab1, text="Limpiar", command=eliminarcasillas).place(x=400, y=250)
    labelusuario=Label(tab1, text="Tienda: " + usuario_entry.get(), font="Helvetica 20 bold", fg="red" ).place(x=700,  y=5)
    #Treeview--------------------
    trev=ttk.Treeview(tab1, columns=("col1", "col2", "col3", "col4", "col5"))
    trev.column("#0", width=150, anchor=CENTER)
    trev.heading("#0", text="Venta", anchor=CENTER)
    trev.heading("col1", text="Producto", anchor=CENTER)
    trev.column("col1", width=150, anchor=CENTER)
    trev.heading("col2", text="Fecha", anchor=CENTER)
    trev.column("col3", width=150, anchor=CENTER)
    trev.heading("col3", text="Código", anchor=CENTER)
    trev.column("col4", width=150, anchor=CENTER)
    trev.heading("col4", text="Precio", anchor=CENTER)
    trev.column("col5", width=150, anchor=CENTER)
    trev.heading("col5", text="Cantidad", anchor=CENTER)
    trev.place(y=500)
    #Pestaña 2 Inventario de recursos---------------------------------------------------------------------------------------------------------------------
    tab2=ttk.Frame(panel)
    panel.add(tab2, text="Inventario")
    tab2.columnconfigure(0, weight = 25)
    tab2.rowconfigure(0, weight= 25)
    tab2.columnconfigure(0, weight = 1)
    tab2.rowconfigure(1, weight= 1)

    frame1 = Frame(tab2, bg='gray26')
    frame1.grid(column=0,row=0,sticky='nsew')
    frame2 = Frame(tab2, bg='gray26')
    frame2.grid(column=0,row=1,sticky='nsew')

    frame1.columnconfigure(0, weight = 1)
    frame1.rowconfigure(0, weight= 1)

    frame2.columnconfigure(0, weight = 1)
    frame2.rowconfigure(0, weight= 1)
    frame2.columnconfigure(1, weight = 1)
    frame2.rowconfigure(0, weight= 1)

    frame2.columnconfigure(2, weight = 1)
    frame2.rowconfigure(0, weight= 1)

    frame2.columnconfigure(3, weight = 2)
    frame2.rowconfigure(0, weight= 1)

    tabla = ttk.Treeview(tab2, height=10)
    tabla.grid(column=0, row=0, sticky='nsew') 

    ladox = Scrollbar(frame1, orient = HORIZONTAL, command= tabla.xview)
    ladox.grid(column=0, row = 1, sticky='ew') 

    ladoy = Scrollbar(frame1, orient =VERTICAL, command = tabla.yview)
    ladoy.grid(column = 1, row = 0, sticky='ns')

    tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)

    estilo = ttk.Style(frame1)
    estilo.theme_use('clam') #  ('clam', 'alt', 'default', 'classic')
    estilo.configure(".",font= ('Arial', 14))
    estilo.configure("Treeview", font= ('Helvetica', 12))
    estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

    boton1 = Button(frame2, text= 'Abrir', bg='green2', command= abrir_archivo)
    boton1.grid(column = 0, row = 0, sticky='nsew', padx=10, pady=10)

    boton2 = Button(frame2, text= 'Mostrar', bg='magenta', command= datos_excel)
    boton2.grid(column = 1, row = 0, sticky='nsew', padx=10, pady=10)

    boton3 = Button(frame2, text= 'Limpiar', bg='red', command= Limpiar)
    boton3.grid(column = 2, row = 0, sticky='nsew', padx=10, pady=10)

    indica = Label(frame2, fg= 'white', bg='gray26', text= 'Ubicación del archivo', font= ('Arial',10,'bold') )
    indica.grid(column=3, row = 0)
def agacheR(): 
    agache=Toplevel()
    agache.geometry("1400x1000")
    agache.title("Tienda Agache y Recoja")
    def almacenaArchivo(nombreFile, cadenaAlmacenar):
        print('Inicia Registro de Ventas')
        file=open(nombreFile,'a')
        file.write(cadenaAlmacenar)
        file.close()
        print('Finaliza Registro de venta')
        
    def validararchivo(nombreFile):
        if os.stat(nombreFile).st_size==0:
         cadenaEncabezado="NOMBRE | FECHA | CODIGO | PRECIO | CANTIDAD \n"
         almacenaArchivo(nombreFile,cadenaEncabezado)

    def seleccionado():
        nombr.delete(0, END)
        fech.delete(0, END)
        codig.delete(0, END)
        precio_entry(0, END)
        cantida.delete(0, END)
        selected=trev.focus() 
        valr=trev.item(selected, "values")
        nombr.insert(0, valr[0])
        fech.insert(0, valr[1])
        codig.insert(0, valr[2])
        precio_entry.insert(0, valr[3])
        cantida.insert(0, valr[4])   

    def eliminarcasillas(): 
        nombr.delete(0, END)
        fech.delete(0, END)
        codig.delete(0, END)
        precio_entry.delete(0, END)
        cantida.delete(0, END)

    def enviardatos(): 
        nombredata=nombre.get()
        fechadata=fecha.get() 
        codigodata=codigo.get() 
        preciodata=precio_entry.get()
        cantidaddata=cantidad.get()
        print(nombredata, fechadata, codigodata, cantidaddata)
        cadenaRegistro = nombredata + '|' + fechadata + '|' + str(codigodata) + '|' + str(preciodata) + '|'  + str(cantidaddata) +'\n'
        validararchivo("registroventas.txt")
        almacenaArchivo("registroventas.txt", cadenaRegistro)
        trev.insert("", END,  text="Activo", values=(nombr.get(), fech.get(), codig.get(),  precio_entry.get(), cantida.get()))

    def abrir_archivo():

        archivo = filedialog.askopenfilename(initialdir ='/', 
        title='Selecione archivo', 
        filetype=(('xlsx files', '*.xlsx*'),('All files', '*.*')))
        indica['text'] = archivo


    def datos_excel():

        datos_obtenidos = indica['text']
        try:
            archivoexcel = r'{}'.format(datos_obtenidos)
            

            df = pd.read_excel(archivoexcel)

        except ValueError:
            messagebox.showerror('Informacion', 'Formato incorrecto')
            return None

        except FileNotFoundError:
            messagebox.showerror('Informacion', 'El archivo esta \n malogrado')
            return None

        Limpiar()

        tabla['column'] = list(df.columns)
        tabla['show'] = "headings"  #encabezado
        

        for columna in tabla['column']:
            tabla.heading(columna, text= columna)
        

        df_fila = df.to_numpy().tolist()
        for fila in df_fila:
            tabla.insert('', 'end', values =fila)


    def Limpiar():
        tabla.delete(*tabla.get_children())
    #---------Defino algunas variables que usare en diferentes funciones----------------------
    nombre=StringVar()
    fecha=StringVar()
    codigo=IntVar() 
    prec=DoubleVar() 
    cantidad=IntVar() 
    #---------------Panel de pestañas----------------------------------------------
    panel=ttk.Notebook(agache) 
    panel.pack(fill="both", expand="yes")   
    #Pestaña 1-------------------------------------------------------------------------------
    tab1=ttk.Frame(panel)
    panel.add(tab1, text="Ventas") 
    indica=Label(tab1, fg="blue", text="Ubicación del archivo", font=("Arial", 10, "bold")).place(x=400, y=70)
    nombrA = Label(tab1, text="Nombre:").place(x=22, y=70)
    nombr = Entry(tab1, textvariable=nombre, width="40")
    nombr.place(x=22, y=100)
    fechA=Label(tab1, text="Fecha D/M/A: ").place(x=22, y=130) 
    fech=Entry(tab1, textvariable=fecha, width="40")
    fech.place(x=22, y=160)  
    codigA=Label(tab1, text="Código:").place(x=22, y=190)
    codig=Entry(tab1, textvariable=codigo, width="40")
    codig.place(x=22, y=220)
    precio_label=Label(tab1, text="Precio: ").place(x=22, y=250)
    precio_entry=Entry(tab1, textvariable=prec, width="40")
    precio_entry.place(x=22, y=270)
    cantidaA=Label(tab1, text="Cantidad:").place(x=22, y=300)
    cantida=Entry(tab1, textvariable=cantidad, width="40")
    cantida.place(x=22, y=330)   
    #----------------Botones--------------------------------------------
    etiqueta=Label(tab1, text="Sección de registro de ventas").place(x=400, y=5)
    datost=Label(tab1, text="Para efectuar una venta y enviar los datos del cliente, clique el siguiente boton:").place(x=400, y=150)
    botonenviar=ttk.Button(tab1, text="Enviar datos de registro", command=enviardatos).place(x=400, y=100) 
    borrarlabel=Label(tab1, text="Para limpiar los campos de entrada de texto pulse: Limpiar").place(x=400, y=200)
    botonlimpiar=ttk.Button(tab1, text="Limpiar", command=eliminarcasillas).place(x=400, y=250)
    labelusuario=Label(tab1, text="Tienda: " + usuario_entry.get(), font="Helvetica 20 bold", fg="red" ).place(x=700,  y=5)
    #Treeview--------------------
    trev=ttk.Treeview(tab1, columns=("col1", "col2", "col3", "col4", "col5"))
    trev.column("#0", width=150, anchor=CENTER)
    trev.heading("#0", text="Venta", anchor=CENTER)
    trev.heading("col1", text="Producto", anchor=CENTER)
    trev.column("col1", width=150, anchor=CENTER)
    trev.heading("col2", text="Fecha", anchor=CENTER)
    trev.column("col3", width=150, anchor=CENTER)
    trev.heading("col3", text="Código", anchor=CENTER)
    trev.column("col4", width=150, anchor=CENTER)
    trev.heading("col4", text="Precio", anchor=CENTER)
    trev.column("col5", width=150, anchor=CENTER)
    trev.heading("col5", text="Cantidad", anchor=CENTER)
    trev.place(y=500)
    #Pestaña 2 Inventario de recursos---------------------------------------------------------------------------------------------------------------------
    tab2=ttk.Frame(panel)
    panel.add(tab2, text="Inventario")
    tab2.columnconfigure(0, weight = 25)
    tab2.rowconfigure(0, weight= 25)
    tab2.columnconfigure(0, weight = 1)
    tab2.rowconfigure(1, weight= 1)

    frame1 = Frame(tab2, bg='gray26')
    frame1.grid(column=0,row=0,sticky='nsew')
    frame2 = Frame(tab2, bg='gray26')
    frame2.grid(column=0,row=1,sticky='nsew')

    frame1.columnconfigure(0, weight = 1)
    frame1.rowconfigure(0, weight= 1)

    frame2.columnconfigure(0, weight = 1)
    frame2.rowconfigure(0, weight= 1)
    frame2.columnconfigure(1, weight = 1)
    frame2.rowconfigure(0, weight= 1)

    frame2.columnconfigure(2, weight = 1)
    frame2.rowconfigure(0, weight= 1)

    frame2.columnconfigure(3, weight = 2)
    frame2.rowconfigure(0, weight= 1)

    tabla = ttk.Treeview(tab2, height=10)
    tabla.grid(column=0, row=0, sticky='nsew') 

    ladox = Scrollbar(frame1, orient = HORIZONTAL, command= tabla.xview)
    ladox.grid(column=0, row = 1, sticky='ew') 

    ladoy = Scrollbar(frame1, orient =VERTICAL, command = tabla.yview)
    ladoy.grid(column = 1, row = 0, sticky='ns')

    tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)

    estilo = ttk.Style(frame1)
    estilo.theme_use('clam') #  ('clam', 'alt', 'default', 'classic')
    estilo.configure(".",font= ('Arial', 14))
    estilo.configure("Treeview", font= ('Helvetica', 12))
    estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

    boton1 = Button(frame2, text= 'Abrir', bg='green2', command= abrir_archivo)
    boton1.grid(column = 0, row = 0, sticky='nsew', padx=10, pady=10)

    boton2 = Button(frame2, text= 'Mostrar', bg='magenta', command= datos_excel)
    boton2.grid(column = 1, row = 0, sticky='nsew', padx=10, pady=10)

    boton3 = Button(frame2, text= 'Limpiar', bg='red', command= Limpiar)
    boton3.grid(column = 2, row = 0, sticky='nsew', padx=10, pady=10)

    indica = Label(frame2, fg= 'white', bg='gray26', text= 'Ubicación del archivo', font= ('Arial',10,'bold') )
    indica.grid(column=3, row = 0)
    

def pasteles(): 
    pastel=Toplevel()
    pastel.geometry("1400x1000")
    pastel.title("Tienda de Pasteles")
    def almacenaArchivo(nombreFile, cadenaAlmacenar):
        print('Inicia Registro de Ventas')
        file=open(nombreFile,'a')
        file.write(cadenaAlmacenar)
        file.close()
        print('Finaliza Registro de venta')
        
    def validararchivo(nombreFile):
        if os.stat(nombreFile).st_size==0:
         cadenaEncabezado="NOMBRE | FECHA | CODIGO | PRECIO | CANTIDAD \n"
         almacenaArchivo(nombreFile,cadenaEncabezado)

    def seleccionado():
        nombr.delete(0, END)
        fech.delete(0, END)
        codig.delete(0, END)
        precio_entry(0, END)
        cantida.delete(0, END)
        selected=trev.focus() 
        valr=trev.item(selected, "values")
        nombr.insert(0, valr[0])
        fech.insert(0, valr[1])
        codig.insert(0, valr[2])
        precio_entry.insert(0, valr[3])
        cantida.insert(0, valr[4])   

    def eliminarcasillas(): 
        nombr.delete(0, END)
        fech.delete(0, END)
        codig.delete(0, END)
        precio_entry.delete(0, END)
        cantida.delete(0, END)

    def enviardatos(): 
        nombredata=nombre.get()
        fechadata=fecha.get() 
        codigodata=codigo.get() 
        preciodata=precio_entry.get()
        cantidaddata=cantidad.get()
        print(nombredata, fechadata, codigodata, cantidaddata)
        cadenaRegistro = nombredata + '|' + fechadata + '|' + str(codigodata) + '|' + str(preciodata) + '|'  + str(cantidaddata) +'\n'
        validararchivo("registroventas.txt")
        almacenaArchivo("registroventas.txt", cadenaRegistro)
        trev.insert("", END,  text="Activo", values=(nombr.get(), fech.get(), codig.get(),  precio_entry.get(), cantida.get()))

    def abrir_archivo():

        archivo = filedialog.askopenfilename(initialdir ='/', 
        title='Selecione archivo', 
        filetype=(('xlsx files', '*.xlsx*'),('All files', '*.*')))
        indica['text'] = archivo


    def datos_excel():

        datos_obtenidos = indica['text']
        try:
            archivoexcel = r'{}'.format(datos_obtenidos)
            

            df = pd.read_excel(archivoexcel)

        except ValueError:
            messagebox.showerror('Informacion', 'Formato incorrecto')
            return None

        except FileNotFoundError:
            messagebox.showerror('Informacion', 'El archivo esta \n malogrado')
            return None

        Limpiar()

        tabla['column'] = list(df.columns)
        tabla['show'] = "headings"  #encabezado
        

        for columna in tabla['column']:
            tabla.heading(columna, text= columna)
        

        df_fila = df.to_numpy().tolist()
        for fila in df_fila:
            tabla.insert('', 'end', values =fila)


    def Limpiar():
        tabla.delete(*tabla.get_children())
    #---------Defino algunas variables que usare en diferentes funciones----------------------
    nombre=StringVar()
    fecha=StringVar()
    codigo=IntVar() 
    prec=DoubleVar() 
    cantidad=IntVar() 
    #---------------Panel de pestañas----------------------------------------------
    panel=ttk.Notebook(pastel) 
    panel.pack(fill="both", expand="yes")   
    #Pestaña 1-------------------------------------------------------------------------------
    tab1=ttk.Frame(panel)
    panel.add(tab1, text="Ventas") 
    indica=Label(tab1, fg="blue", text="Ubicación del archivo", font=("Arial", 10, "bold")).place(x=400, y=70)
    nombrA = Label(tab1, text="Nombre:").place(x=22, y=70)
    nombr = Entry(tab1, textvariable=nombre, width="40")
    nombr.place(x=22, y=100)
    fechA=Label(tab1, text="Fecha D/M/A: ").place(x=22, y=130) 
    fech=Entry(tab1, textvariable=fecha, width="40")
    fech.place(x=22, y=160)  
    codigA=Label(tab1, text="Código:").place(x=22, y=190)
    codig=Entry(tab1, textvariable=codigo, width="40")
    codig.place(x=22, y=220)
    precio_label=Label(tab1, text="Precio: ").place(x=22, y=250)
    precio_entry=Entry(tab1, textvariable=prec, width="40")
    precio_entry.place(x=22, y=270)
    cantidaA=Label(tab1, text="Cantidad:").place(x=22, y=300)
    cantida=Entry(tab1, textvariable=cantidad, width="40")
    cantida.place(x=22, y=330)   
    #----------------Botones--------------------------------------------
    etiqueta=Label(tab1, text="Sección de registro de ventas").place(x=400, y=5)
    datost=Label(tab1, text="Para efectuar una venta y enviar los datos del cliente, clique el siguiente boton:").place(x=400, y=150)
    botonenviar=ttk.Button(tab1, text="Enviar datos de registro", command=enviardatos).place(x=400, y=100) 
    borrarlabel=Label(tab1, text="Para limpiar los campos de entrada de texto pulse: Limpiar").place(x=400, y=200)
    botonlimpiar=ttk.Button(tab1, text="Limpiar", command=eliminarcasillas).place(x=400, y=250)
    labelusuario=Label(tab1, text="Tienda: " + usuario_entry.get(), font="Helvetica 20 bold", fg="red" ).place(x=700,  y=5)
    #Treeview--------------------
    trev=ttk.Treeview(tab1, columns=("col1", "col2", "col3", "col4", "col5"))
    trev.column("#0", width=150, anchor=CENTER)
    trev.heading("#0", text="Venta", anchor=CENTER)
    trev.heading("col1", text="Producto", anchor=CENTER)
    trev.column("col1", width=150, anchor=CENTER)
    trev.heading("col2", text="Fecha", anchor=CENTER)
    trev.column("col3", width=150, anchor=CENTER)
    trev.heading("col3", text="Código", anchor=CENTER)
    trev.column("col4", width=150, anchor=CENTER)
    trev.heading("col4", text="Precio", anchor=CENTER)
    trev.column("col5", width=150, anchor=CENTER)
    trev.heading("col5", text="Cantidad", anchor=CENTER)
    trev.place(y=500)
    #Pestaña 2 Inventario de recursos---------------------------------------------------------------------------------------------------------------------
    tab2=ttk.Frame(panel)
    panel.add(tab2, text="Inventario")
    tab2.columnconfigure(0, weight = 25)
    tab2.rowconfigure(0, weight= 25)
    tab2.columnconfigure(0, weight = 1)
    tab2.rowconfigure(1, weight= 1)

    frame1 = Frame(tab2, bg='gray26')
    frame1.grid(column=0,row=0,sticky='nsew')
    frame2 = Frame(tab2, bg='gray26')
    frame2.grid(column=0,row=1,sticky='nsew')

    frame1.columnconfigure(0, weight = 1)
    frame1.rowconfigure(0, weight= 1)

    frame2.columnconfigure(0, weight = 1)
    frame2.rowconfigure(0, weight= 1)
    frame2.columnconfigure(1, weight = 1)
    frame2.rowconfigure(0, weight= 1)

    frame2.columnconfigure(2, weight = 1)
    frame2.rowconfigure(0, weight= 1)

    frame2.columnconfigure(3, weight = 2)
    frame2.rowconfigure(0, weight= 1)

    tabla = ttk.Treeview(tab2, height=10)
    tabla.grid(column=0, row=0, sticky='nsew') 

    ladox = Scrollbar(frame1, orient = HORIZONTAL, command= tabla.xview)
    ladox.grid(column=0, row = 1, sticky='ew') 

    ladoy = Scrollbar(frame1, orient =VERTICAL, command = tabla.yview)
    ladoy.grid(column = 1, row = 0, sticky='ns')

    tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)

    estilo = ttk.Style(frame1)
    estilo.theme_use('clam') #  ('clam', 'alt', 'default', 'classic')
    estilo.configure(".",font= ('Arial', 14))
    estilo.configure("Treeview", font= ('Helvetica', 12))
    estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

    boton1 = Button(frame2, text= 'Abrir', bg='green2', command= abrir_archivo)
    boton1.grid(column = 0, row = 0, sticky='nsew', padx=10, pady=10)

    boton2 = Button(frame2, text= 'Mostrar', bg='magenta', command= datos_excel)
    boton2.grid(column = 1, row = 0, sticky='nsew', padx=10, pady=10)

    boton3 = Button(frame2, text= 'Limpiar', bg='red', command= Limpiar)
    boton3.grid(column = 2, row = 0, sticky='nsew', padx=10, pady=10)

    indica = Label(frame2, fg= 'white', bg='gray26', text= 'Ubicación del archivo', font= ('Arial',10,'bold') )
    indica.grid(column=3, row = 0)
    

def asados(): 
    asados=Toplevel()
    asados.geometry("1400x1000")
    asados.title("Asados")
    def almacenaArchivo(nombreFile, cadenaAlmacenar):
        print('Inicia Registro de Ventas')
        file=open(nombreFile,'a')
        file.write(cadenaAlmacenar)
        file.close()
        print('Finaliza Registro de venta')
        
    def validararchivo(nombreFile):
        if os.stat(nombreFile).st_size==0:
         cadenaEncabezado="NOMBRE | FECHA | CODIGO | PRECIO | CANTIDAD \n"
         almacenaArchivo(nombreFile,cadenaEncabezado)

    def seleccionado():
        nombr.delete(0, END)
        fech.delete(0, END)
        codig.delete(0, END)
        precio_entry(0, END)
        cantida.delete(0, END)
        selected=trev.focus() 
        valr=trev.item(selected, "values")
        nombr.insert(0, valr[0])
        fech.insert(0, valr[1])
        codig.insert(0, valr[2])
        precio_entry.insert(0, valr[3])
        cantida.insert(0, valr[4])   

    def eliminarcasillas(): 
        nombr.delete(0, END)
        fech.delete(0, END)
        codig.delete(0, END)
        precio_entry.delete(0, END)
        cantida.delete(0, END)

    def enviardatos(): 
        nombredata=nombre.get()
        fechadata=fecha.get() 
        codigodata=codigo.get() 
        preciodata=precio_entry.get()
        cantidaddata=cantidad.get()
        print(nombredata, fechadata, codigodata, cantidaddata)
        cadenaRegistro = nombredata + '|' + fechadata + '|' + str(codigodata) + '|' + str(preciodata) + '|'  + str(cantidaddata) +'\n'
        validararchivo("registroventas.txt")
        almacenaArchivo("registroventas.txt", cadenaRegistro)
        trev.insert("", END,  text="Activo", values=(nombr.get(), fech.get(), codig.get(),  precio_entry.get(), cantida.get()))

    def abrir_archivo():

        archivo = filedialog.askopenfilename(initialdir ='/', 
        title='Selecione archivo', 
        filetype=(('xlsx files', '*.xlsx*'),('All files', '*.*')))
        indica['text'] = archivo


    def datos_excel():

        datos_obtenidos = indica['text']
        try:
            archivoexcel = r'{}'.format(datos_obtenidos)
            

            df = pd.read_excel(archivoexcel)

        except ValueError:
            messagebox.showerror('Informacion', 'Formato incorrecto')
            return None

        except FileNotFoundError:
            messagebox.showerror('Informacion', 'El archivo esta \n malogrado')
            return None

        Limpiar()

        tabla['column'] = list(df.columns)
        tabla['show'] = "headings"  #encabezado
        

        for columna in tabla['column']:
            tabla.heading(columna, text= columna)
        

        df_fila = df.to_numpy().tolist()
        for fila in df_fila:
            tabla.insert('', 'end', values =fila)


    def Limpiar():
        tabla.delete(*tabla.get_children())
    #---------Defino algunas variables que usare en diferentes funciones----------------------
    nombre=StringVar()
    fecha=StringVar()
    codigo=IntVar() 
    prec=DoubleVar() 
    cantidad=IntVar() 
    #---------------Panel de pestañas----------------------------------------------
    panel=ttk.Notebook(asados) 
    panel.pack(fill="both", expand="yes")   
    #Pestaña 1-------------------------------------------------------------------------------
    tab1=ttk.Frame(panel)
    panel.add(tab1, text="Ventas") 
    indica=Label(tab1, fg="blue", text="Ubicación del archivo", font=("Arial", 10, "bold")).place(x=400, y=70)
    nombrA = Label(tab1, text="Nombre:").place(x=22, y=70)
    nombr = Entry(tab1, textvariable=nombre, width="40")
    nombr.place(x=22, y=100)
    fechA=Label(tab1, text="Fecha D/M/A: ").place(x=22, y=130) 
    fech=Entry(tab1, textvariable=fecha, width="40")
    fech.place(x=22, y=160)  
    codigA=Label(tab1, text="Código:").place(x=22, y=190)
    codig=Entry(tab1, textvariable=codigo, width="40")
    codig.place(x=22, y=220)
    precio_label=Label(tab1, text="Precio: ").place(x=22, y=250)
    precio_entry=Entry(tab1, textvariable=prec, width="40")
    precio_entry.place(x=22, y=270)
    cantidaA=Label(tab1, text="Cantidad:").place(x=22, y=300)
    cantida=Entry(tab1, textvariable=cantidad, width="40")
    cantida.place(x=22, y=330)   
    #----------------Botones--------------------------------------------
    etiqueta=Label(tab1, text="Sección de registro de ventas").place(x=400, y=5)
    datost=Label(tab1, text="Para efectuar una venta y enviar los datos del cliente, clique el siguiente boton:").place(x=400, y=150)
    botonenviar=ttk.Button(tab1, text="Enviar datos de registro", command=enviardatos).place(x=400, y=100) 
    borrarlabel=Label(tab1, text="Para limpiar los campos de entrada de texto pulse: Limpiar").place(x=400, y=200)
    botonlimpiar=ttk.Button(tab1, text="Limpiar", command=eliminarcasillas).place(x=400, y=250)
    labelusuario=Label(tab1, text="Tienda: " + usuario_entry.get(), font="Helvetica 20 bold", fg="red" ).place(x=700,  y=5)
    #Treeview--------------------
    trev=ttk.Treeview(tab1, columns=("col1", "col2", "col3", "col4", "col5"))
    trev.column("#0", width=150, anchor=CENTER)
    trev.heading("#0", text="Venta", anchor=CENTER)
    trev.heading("col1", text="Producto", anchor=CENTER)
    trev.column("col1", width=150, anchor=CENTER)
    trev.heading("col2", text="Fecha", anchor=CENTER)
    trev.column("col3", width=150, anchor=CENTER)
    trev.heading("col3", text="Código", anchor=CENTER)
    trev.column("col4", width=150, anchor=CENTER)
    trev.heading("col4", text="Precio", anchor=CENTER)
    trev.column("col5", width=150, anchor=CENTER)
    trev.heading("col5", text="Cantidad", anchor=CENTER)
    trev.place(y=500)
    #Pestaña 2 Inventario de recursos---------------------------------------------------------------------------------------------------------------------
    tab2=ttk.Frame(panel)
    panel.add(tab2, text="Inventario")
    tab2.columnconfigure(0, weight = 25)
    tab2.rowconfigure(0, weight= 25)
    tab2.columnconfigure(0, weight = 1)
    tab2.rowconfigure(1, weight= 1)

    frame1 = Frame(tab2, bg='gray26')
    frame1.grid(column=0,row=0,sticky='nsew')
    frame2 = Frame(tab2, bg='gray26')
    frame2.grid(column=0,row=1,sticky='nsew')

    frame1.columnconfigure(0, weight = 1)
    frame1.rowconfigure(0, weight= 1)

    frame2.columnconfigure(0, weight = 1)
    frame2.rowconfigure(0, weight= 1)
    frame2.columnconfigure(1, weight = 1)
    frame2.rowconfigure(0, weight= 1)

    frame2.columnconfigure(2, weight = 1)
    frame2.rowconfigure(0, weight= 1)

    frame2.columnconfigure(3, weight = 2)
    frame2.rowconfigure(0, weight= 1)

    tabla = ttk.Treeview(tab2, height=10)
    tabla.grid(column=0, row=0, sticky='nsew') 

    ladox = Scrollbar(frame1, orient = HORIZONTAL, command= tabla.xview)
    ladox.grid(column=0, row = 1, sticky='ew') 

    ladoy = Scrollbar(frame1, orient =VERTICAL, command = tabla.yview)
    ladoy.grid(column = 1, row = 0, sticky='ns')

    tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)

    estilo = ttk.Style(frame1)
    estilo.theme_use('clam') #  ('clam', 'alt', 'default', 'classic')
    estilo.configure(".",font= ('Arial', 14))
    estilo.configure("Treeview", font= ('Helvetica', 12))
    estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

    boton1 = Button(frame2, text= 'Abrir', bg='green2', command= abrir_archivo)
    boton1.grid(column = 0, row = 0, sticky='nsew', padx=10, pady=10)

    boton2 = Button(frame2, text= 'Mostrar', bg='magenta', command= datos_excel)
    boton2.grid(column = 1, row = 0, sticky='nsew', padx=10, pady=10)

    boton3 = Button(frame2, text= 'Limpiar', bg='red', command= Limpiar)
    boton3.grid(column = 2, row = 0, sticky='nsew', padx=10, pady=10)

    indica = Label(frame2, fg= 'white', bg='gray26', text= 'Ubicación del archivo', font= ('Arial',10,'bold') )
    indica.grid(column=3, row = 0)
    
def empanadas(): 
    empanada=Toplevel()
    empanada.geometry("1400x1000")
    empanada.title("Tienda de Empanadas")
    def almacenaArchivo(nombreFile, cadenaAlmacenar):
        print('Inicia Registro de Ventas')
        file=open(nombreFile,'a')
        file.write(cadenaAlmacenar)
        file.close()
        print('Finaliza Registro de venta')
        
    def validararchivo(nombreFile):
        if os.stat(nombreFile).st_size==0:
         cadenaEncabezado="NOMBRE | FECHA | CODIGO | PRECIO | CANTIDAD \n"
         almacenaArchivo(nombreFile,cadenaEncabezado)

    def seleccionado():
        nombr.delete(0, END)
        fech.delete(0, END)
        codig.delete(0, END)
        precio_entry(0, END)
        cantida.delete(0, END)
        selected=trev.focus() 
        valr=trev.item(selected, "values")
        nombr.insert(0, valr[0])
        fech.insert(0, valr[1])
        codig.insert(0, valr[2])
        precio_entry.insert(0, valr[3])
        cantida.insert(0, valr[4])   

    def eliminarcasillas(): 
        nombr.delete(0, END)
        fech.delete(0, END)
        codig.delete(0, END)
        precio_entry.delete(0, END)
        cantida.delete(0, END)

    def enviardatos(): 
        nombredata=nombre.get()
        fechadata=fecha.get() 
        codigodata=codigo.get() 
        preciodata=precio_entry.get()
        cantidaddata=cantidad.get()
        print(nombredata, fechadata, codigodata, cantidaddata)
        cadenaRegistro = nombredata + '|' + fechadata + '|' + str(codigodata) + '|' + str(preciodata) + '|'  + str(cantidaddata) +'\n'
        validararchivo("registroventas.txt")
        almacenaArchivo("registroventas.txt", cadenaRegistro)
        trev.insert("", END,  text="Activo", values=(nombr.get(), fech.get(), codig.get(),  precio_entry.get(), cantida.get()))

    def abrir_archivo():

        archivo = filedialog.askopenfilename(initialdir ='/', 
        title='Selecione archivo', 
        filetype=(('xlsx files', '*.xlsx*'),('All files', '*.*')))
        indica['text'] = archivo


    def datos_excel():

        datos_obtenidos = indica['text']
        try:
            archivoexcel = r'{}'.format(datos_obtenidos)
            

            df = pd.read_excel(archivoexcel)

        except ValueError:
            messagebox.showerror('Informacion', 'Formato incorrecto')
            return None

        except FileNotFoundError:
            messagebox.showerror('Informacion', 'El archivo esta \n malogrado')
            return None

        Limpiar()

        tabla['column'] = list(df.columns)
        tabla['show'] = "headings"  #encabezado
        

        for columna in tabla['column']:
            tabla.heading(columna, text= columna)
        

        df_fila = df.to_numpy().tolist()
        for fila in df_fila:
            tabla.insert('', 'end', values =fila)


    def Limpiar():
        tabla.delete(*tabla.get_children())
    #---------Defino algunas variables que usare en diferentes funciones----------------------
    nombre=StringVar()
    fecha=StringVar()
    codigo=IntVar() 
    prec=DoubleVar() 
    cantidad=IntVar() 
    #---------------Panel de pestañas----------------------------------------------
    panel=ttk.Notebook(empanada) 
    panel.pack(fill="both", expand="yes")   
    #Pestaña 1-------------------------------------------------------------------------------
    tab1=ttk.Frame(panel)
    panel.add(tab1, text="Ventas") 
    indica=Label(tab1, fg="blue", text="Ubicación del archivo", font=("Arial", 10, "bold")).place(x=400, y=70)
    nombrA = Label(tab1, text="Nombre:").place(x=22, y=70)
    nombr = Entry(tab1, textvariable=nombre, width="40")
    nombr.place(x=22, y=100)
    fechA=Label(tab1, text="Fecha D/M/A: ").place(x=22, y=130) 
    fech=Entry(tab1, textvariable=fecha, width="40")
    fech.place(x=22, y=160)  
    codigA=Label(tab1, text="Código:").place(x=22, y=190)
    codig=Entry(tab1, textvariable=codigo, width="40")
    codig.place(x=22, y=220)
    precio_label=Label(tab1, text="Precio: ").place(x=22, y=250)
    precio_entry=Entry(tab1, textvariable=prec, width="40")
    precio_entry.place(x=22, y=270)
    cantidaA=Label(tab1, text="Cantidad:").place(x=22, y=300)
    cantida=Entry(tab1, textvariable=cantidad, width="40")
    cantida.place(x=22, y=330)   
    #----------------Botones--------------------------------------------
    etiqueta=Label(tab1, text="Sección de registro de ventas").place(x=400, y=5)
    datost=Label(tab1, text="Para efectuar una venta y enviar los datos del cliente, clique el siguiente boton:").place(x=400, y=150)
    botonenviar=ttk.Button(tab1, text="Enviar datos de registro", command=enviardatos).place(x=400, y=100) 
    borrarlabel=Label(tab1, text="Para limpiar los campos de entrada de texto pulse: Limpiar").place(x=400, y=200)
    botonlimpiar=ttk.Button(tab1, text="Limpiar", command=eliminarcasillas).place(x=400, y=250)
    labelusuario=Label(tab1, text="Tienda: " + usuario_entry.get(), font="Helvetica 20 bold", fg="red" ).place(x=700,  y=5)
    #Treeview--------------------
    trev=ttk.Treeview(tab1, columns=("col1", "col2", "col3", "col4", "col5"))
    trev.column("#0", width=150, anchor=CENTER)
    trev.heading("#0", text="Venta", anchor=CENTER)
    trev.heading("col1", text="Producto", anchor=CENTER)
    trev.column("col1", width=150, anchor=CENTER)
    trev.heading("col2", text="Fecha", anchor=CENTER)
    trev.column("col3", width=150, anchor=CENTER)
    trev.heading("col3", text="Código", anchor=CENTER)
    trev.column("col4", width=150, anchor=CENTER)
    trev.heading("col4", text="Precio", anchor=CENTER)
    trev.column("col5", width=150, anchor=CENTER)
    trev.heading("col5", text="Cantidad", anchor=CENTER)
    trev.place(y=500)
    #Pestaña 2 Inventario de recursos---------------------------------------------------------------------------------------------------------------------
    tab2=ttk.Frame(panel)
    panel.add(tab2, text="Inventario")
    tab2.columnconfigure(0, weight = 25)
    tab2.rowconfigure(0, weight= 25)
    tab2.columnconfigure(0, weight = 1)
    tab2.rowconfigure(1, weight= 1)

    frame1 = Frame(tab2, bg='gray26')
    frame1.grid(column=0,row=0,sticky='nsew')
    frame2 = Frame(tab2, bg='gray26')
    frame2.grid(column=0,row=1,sticky='nsew')

    frame1.columnconfigure(0, weight = 1)
    frame1.rowconfigure(0, weight= 1)

    frame2.columnconfigure(0, weight = 1)
    frame2.rowconfigure(0, weight= 1)
    frame2.columnconfigure(1, weight = 1)
    frame2.rowconfigure(0, weight= 1)

    frame2.columnconfigure(2, weight = 1)
    frame2.rowconfigure(0, weight= 1)

    frame2.columnconfigure(3, weight = 2)
    frame2.rowconfigure(0, weight= 1)

    tabla = ttk.Treeview(tab2, height=10)
    tabla.grid(column=0, row=0, sticky='nsew') 

    ladox = Scrollbar(frame1, orient = HORIZONTAL, command= tabla.xview)
    ladox.grid(column=0, row = 1, sticky='ew') 

    ladoy = Scrollbar(frame1, orient =VERTICAL, command = tabla.yview)
    ladoy.grid(column = 1, row = 0, sticky='ns')

    tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)

    estilo = ttk.Style(frame1)
    estilo.theme_use('clam') #  ('clam', 'alt', 'default', 'classic')
    estilo.configure(".",font= ('Arial', 14))
    estilo.configure("Treeview", font= ('Helvetica', 12))
    estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

    boton1 = Button(frame2, text= 'Abrir', bg='green2', command= abrir_archivo)
    boton1.grid(column = 0, row = 0, sticky='nsew', padx=10, pady=10)

    boton2 = Button(frame2, text= 'Mostrar', bg='magenta', command= datos_excel)
    boton2.grid(column = 1, row = 0, sticky='nsew', padx=10, pady=10)

    boton3 = Button(frame2, text= 'Limpiar', bg='red', command= Limpiar)
    boton3.grid(column = 2, row = 0, sticky='nsew', padx=10, pady=10)

    indica = Label(frame2, fg= 'white', bg='gray26', text= 'Ubicación del archivo', font= ('Arial',10,'bold') )
    indica.grid(column=3, row = 0)



def samgung(): 
    sam=Toplevel()
    sam.geometry("1400x1000")
    sam.title("Samsung")
    def almacenaArchivo(nombreFile, cadenaAlmacenar):
        print('Inicia Registro de Ventas')
        file=open(nombreFile,'a')
        file.write(cadenaAlmacenar)
        file.close()
        print('Finaliza Registro de venta')
        
    def validararchivo(nombreFile):
        if os.stat(nombreFile).st_size==0:
         cadenaEncabezado="NOMBRE | FECHA | CODIGO | PRECIO | CANTIDAD \n"
         almacenaArchivo(nombreFile,cadenaEncabezado)

    def seleccionado():
        nombr.delete(0, END)
        fech.delete(0, END)
        codig.delete(0, END)
        precio_entry(0, END)
        cantida.delete(0, END)
        selected=trev.focus() 
        valr=trev.item(selected, "values")
        nombr.insert(0, valr[0])
        fech.insert(0, valr[1])
        codig.insert(0, valr[2])
        precio_entry.insert(0, valr[3])
        cantida.insert(0, valr[4])   

    def eliminarcasillas(): 
        nombr.delete(0, END)
        fech.delete(0, END)
        codig.delete(0, END)
        precio_entry.delete(0, END)
        cantida.delete(0, END)

    def enviardatos(): 
        nombredata=nombre.get()
        fechadata=fecha.get() 
        codigodata=codigo.get() 
        preciodata=precio_entry.get()
        cantidaddata=cantidad.get()
        print(nombredata, fechadata, codigodata, cantidaddata)
        cadenaRegistro = nombredata + '|' + fechadata + '|' + str(codigodata) + '|' + str(preciodata) + '|'  + str(cantidaddata) +'\n'
        validararchivo("registroventas.txt")
        almacenaArchivo("registroventas.txt", cadenaRegistro)
        trev.insert("", END,  text="Activo", values=(nombr.get(), fech.get(), codig.get(),  precio_entry.get(), cantida.get()))

    def abrir_archivo():

        archivo = filedialog.askopenfilename(initialdir ='/', 
        title='Selecione archivo', 
        filetype=(('xlsx files', '*.xlsx*'),('All files', '*.*')))
        indica['text'] = archivo


    def datos_excel():

        datos_obtenidos = indica['text']
        try:
            archivoexcel = r'{}'.format(datos_obtenidos)
            

            df = pd.read_excel(archivoexcel)

        except ValueError:
            messagebox.showerror('Informacion', 'Formato incorrecto')
            return None

        except FileNotFoundError:
            messagebox.showerror('Informacion', 'El archivo esta \n malogrado')
            return None

        Limpiar()

        tabla['column'] = list(df.columns)
        tabla['show'] = "headings"  #encabezado
        

        for columna in tabla['column']:
            tabla.heading(columna, text= columna)
        

        df_fila = df.to_numpy().tolist()
        for fila in df_fila:
            tabla.insert('', 'end', values =fila)


    def Limpiar():
        tabla.delete(*tabla.get_children())
    #---------Defino algunas variables que usare en diferentes funciones----------------------
    nombre=StringVar()
    fecha=StringVar()
    codigo=IntVar() 
    prec=DoubleVar() 
    cantidad=IntVar() 
    #---------------Panel de pestañas----------------------------------------------
    panel=ttk.Notebook(sam) 
    panel.pack(fill="both", expand="yes")   
    #Pestaña 1-------------------------------------------------------------------------------
    tab1=ttk.Frame(panel)
    panel.add(tab1, text="Ventas") 
    indica=Label(tab1, fg="blue", text="Ubicación del archivo", font=("Arial", 10, "bold")).place(x=400, y=70)
    nombrA = Label(tab1, text="Nombre:").place(x=22, y=70)
    nombr = Entry(tab1, textvariable=nombre, width="40")
    nombr.place(x=22, y=100)
    fechA=Label(tab1, text="Fecha D/M/A: ").place(x=22, y=130) 
    fech=Entry(tab1, textvariable=fecha, width="40")
    fech.place(x=22, y=160)  
    codigA=Label(tab1, text="Código:").place(x=22, y=190)
    codig=Entry(tab1, textvariable=codigo, width="40")
    codig.place(x=22, y=220)
    precio_label=Label(tab1, text="Precio: ").place(x=22, y=250)
    precio_entry=Entry(tab1, textvariable=prec, width="40")
    precio_entry.place(x=22, y=270)
    cantidaA=Label(tab1, text="Cantidad:").place(x=22, y=300)
    cantida=Entry(tab1, textvariable=cantidad, width="40")
    cantida.place(x=22, y=330)   
    #----------------Botones--------------------------------------------
    etiqueta=Label(tab1, text="Sección de registro de ventas").place(x=400, y=5)
    datost=Label(tab1, text="Para efectuar una venta y enviar los datos del cliente, clique el siguiente boton:").place(x=400, y=150)
    botonenviar=ttk.Button(tab1, text="Enviar datos de registro", command=enviardatos).place(x=400, y=100) 
    borrarlabel=Label(tab1, text="Para limpiar los campos de entrada de texto pulse: Limpiar").place(x=400, y=200)
    botonlimpiar=ttk.Button(tab1, text="Limpiar", command=eliminarcasillas).place(x=400, y=250)
    labelusuario=Label(tab1, text="Tienda: " + usuario_entry.get(), font="Helvetica 20 bold", fg="red" ).place(x=700,  y=5)
    #Treeview--------------------
    trev=ttk.Treeview(tab1, columns=("col1", "col2", "col3", "col4", "col5"))
    trev.column("#0", width=150, anchor=CENTER)
    trev.heading("#0", text="Venta", anchor=CENTER)
    trev.heading("col1", text="Producto", anchor=CENTER)
    trev.column("col1", width=150, anchor=CENTER)
    trev.heading("col2", text="Fecha", anchor=CENTER)
    trev.column("col3", width=150, anchor=CENTER)
    trev.heading("col3", text="Código", anchor=CENTER)
    trev.column("col4", width=150, anchor=CENTER)
    trev.heading("col4", text="Precio", anchor=CENTER)
    trev.column("col5", width=150, anchor=CENTER)
    trev.heading("col5", text="Cantidad", anchor=CENTER)
    trev.place(y=500)
    #Pestaña 2 Inventario de recursos---------------------------------------------------------------------------------------------------------------------
    tab2=ttk.Frame(panel)
    panel.add(tab2, text="Inventario")
    tab2.columnconfigure(0, weight = 25)
    tab2.rowconfigure(0, weight= 25)
    tab2.columnconfigure(0, weight = 1)
    tab2.rowconfigure(1, weight= 1)

    frame1 = Frame(tab2, bg='gray26')
    frame1.grid(column=0,row=0,sticky='nsew')
    frame2 = Frame(tab2, bg='gray26')
    frame2.grid(column=0,row=1,sticky='nsew')

    frame1.columnconfigure(0, weight = 1)
    frame1.rowconfigure(0, weight= 1)

    frame2.columnconfigure(0, weight = 1)
    frame2.rowconfigure(0, weight= 1)
    frame2.columnconfigure(1, weight = 1)
    frame2.rowconfigure(0, weight= 1)

    frame2.columnconfigure(2, weight = 1)
    frame2.rowconfigure(0, weight= 1)

    frame2.columnconfigure(3, weight = 2)
    frame2.rowconfigure(0, weight= 1)

    tabla = ttk.Treeview(tab2, height=10)
    tabla.grid(column=0, row=0, sticky='nsew') 

    ladox = Scrollbar(frame1, orient = HORIZONTAL, command= tabla.xview)
    ladox.grid(column=0, row = 1, sticky='ew') 

    ladoy = Scrollbar(frame1, orient =VERTICAL, command = tabla.yview)
    ladoy.grid(column = 1, row = 0, sticky='ns')

    tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)

    estilo = ttk.Style(frame1)
    estilo.theme_use('clam') #  ('clam', 'alt', 'default', 'classic')
    estilo.configure(".",font= ('Arial', 14))
    estilo.configure("Treeview", font= ('Helvetica', 12))
    estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

    boton1 = Button(frame2, text= 'Abrir', bg='green2', command= abrir_archivo)
    boton1.grid(column = 0, row = 0, sticky='nsew', padx=10, pady=10)

    boton2 = Button(frame2, text= 'Mostrar', bg='magenta', command= datos_excel)
    boton2.grid(column = 1, row = 0, sticky='nsew', padx=10, pady=10)

    boton3 = Button(frame2, text= 'Limpiar', bg='red', command= Limpiar)
    boton3.grid(column = 2, row = 0, sticky='nsew', padx=10, pady=10)

    indica = Label(frame2, fg= 'white', bg='gray26', text= 'Ubicación del archivo', font= ('Arial',10,'bold') )
    indica.grid(column=3, row = 0)





def applepera(): 
    app=Toplevel()
    app.geometry("1400x1000")
    app.title("Tienda Applepera")
    def almacenaArchivo(nombreFile, cadenaAlmacenar):
        print('Inicia Registro de Ventas')
        file=open(nombreFile,'a')
        file.write(cadenaAlmacenar)
        file.close()
        print('Finaliza Registro de venta')
        
    def validararchivo(nombreFile):
        if os.stat(nombreFile).st_size==0:
         cadenaEncabezado="NOMBRE | FECHA | CODIGO | PRECIO | CANTIDAD \n"
         almacenaArchivo(nombreFile,cadenaEncabezado)

    def seleccionado():
        nombr.delete(0, END)
        fech.delete(0, END)
        codig.delete(0, END)
        precio_entry(0, END)
        cantida.delete(0, END)
        selected=trev.focus() 
        valr=trev.item(selected, "values")
        nombr.insert(0, valr[0])
        fech.insert(0, valr[1])
        codig.insert(0, valr[2])
        precio_entry.insert(0, valr[3])
        cantida.insert(0, valr[4])   

    def eliminarcasillas(): 
        nombr.delete(0, END)
        fech.delete(0, END)
        codig.delete(0, END)
        precio_entry.delete(0, END)
        cantida.delete(0, END)

    def enviardatos(): 
        nombredata=nombre.get()
        fechadata=fecha.get() 
        codigodata=codigo.get() 
        preciodata=precio_entry.get()
        cantidaddata=cantidad.get()
        print(nombredata, fechadata, codigodata, cantidaddata)
        cadenaRegistro = nombredata + '|' + fechadata + '|' + str(codigodata) + '|' + str(preciodata) + '|'  + str(cantidaddata) +'\n'
        validararchivo("registroventas.txt")
        almacenaArchivo("registroventas.txt", cadenaRegistro)
        trev.insert("", END,  text="Activo", values=(nombr.get(), fech.get(), codig.get(),  precio_entry.get(), cantida.get()))

    def abrir_archivo():

        archivo = filedialog.askopenfilename(initialdir ='/', 
        title='Selecione archivo', 
        filetype=(('xlsx files', '*.xlsx*'),('All files', '*.*')))
        indica['text'] = archivo


    def datos_excel():

        datos_obtenidos = indica['text']
        try:
            archivoexcel = r'{}'.format(datos_obtenidos)
            

            df = pd.read_excel(archivoexcel)

        except ValueError:
            messagebox.showerror('Informacion', 'Formato incorrecto')
            return None

        except FileNotFoundError:
            messagebox.showerror('Informacion', 'El archivo esta \n malogrado')
            return None

        Limpiar()

        tabla['column'] = list(df.columns)
        tabla['show'] = "headings"  #encabezado
        

        for columna in tabla['column']:
            tabla.heading(columna, text= columna)
        

        df_fila = df.to_numpy().tolist()
        for fila in df_fila:
            tabla.insert('', 'end', values =fila)


    def Limpiar():
        tabla.delete(*tabla.get_children())
    #---------Defino algunas variables que usare en diferentes funciones----------------------
    nombre=StringVar()
    fecha=StringVar()
    codigo=IntVar() 
    prec=DoubleVar() 
    cantidad=IntVar() 
    #---------------Panel de pestañas----------------------------------------------
    panel=ttk.Notebook(app) 
    panel.pack(fill="both", expand="yes")   
    #Pestaña 1-------------------------------------------------------------------------------
    tab1=ttk.Frame(panel)
    panel.add(tab1, text="Ventas") 
    indica=Label(tab1, fg="blue", text="Ubicación del archivo", font=("Arial", 10, "bold")).place(x=400, y=70)
    nombrA = Label(tab1, text="Nombre:").place(x=22, y=70)
    nombr = Entry(tab1, textvariable=nombre, width="40")
    nombr.place(x=22, y=100)
    fechA=Label(tab1, text="Fecha D/M/A: ").place(x=22, y=130) 
    fech=Entry(tab1, textvariable=fecha, width="40")
    fech.place(x=22, y=160)  
    codigA=Label(tab1, text="Código:").place(x=22, y=190)
    codig=Entry(tab1, textvariable=codigo, width="40")
    codig.place(x=22, y=220)
    precio_label=Label(tab1, text="Precio: ").place(x=22, y=250)
    precio_entry=Entry(tab1, textvariable=prec, width="40")
    precio_entry.place(x=22, y=270)
    cantidaA=Label(tab1, text="Cantidad:").place(x=22, y=300)
    cantida=Entry(tab1, textvariable=cantidad, width="40")
    cantida.place(x=22, y=330)   
    #----------------Botones--------------------------------------------
    etiqueta=Label(tab1, text="Sección de registro de ventas").place(x=400, y=5)
    datost=Label(tab1, text="Para efectuar una venta y enviar los datos del cliente, clique el siguiente boton:").place(x=400, y=150)
    botonenviar=ttk.Button(tab1, text="Enviar datos de registro", command=enviardatos).place(x=400, y=100) 
    borrarlabel=Label(tab1, text="Para limpiar los campos de entrada de texto pulse: Limpiar").place(x=400, y=200)
    botonlimpiar=ttk.Button(tab1, text="Limpiar", command=eliminarcasillas).place(x=400, y=250)
    labelusuario=Label(tab1, text="Tienda: " + usuario_entry.get(), font="Helvetica 20 bold", fg="red" ).place(x=700,  y=5)
    #Treeview--------------------
    trev=ttk.Treeview(tab1, columns=("col1", "col2", "col3", "col4", "col5"))
    trev.column("#0", width=150, anchor=CENTER)
    trev.heading("#0", text="Venta", anchor=CENTER)
    trev.heading("col1", text="Producto", anchor=CENTER)
    trev.column("col1", width=150, anchor=CENTER)
    trev.heading("col2", text="Fecha", anchor=CENTER)
    trev.column("col3", width=150, anchor=CENTER)
    trev.heading("col3", text="Código", anchor=CENTER)
    trev.column("col4", width=150, anchor=CENTER)
    trev.heading("col4", text="Precio", anchor=CENTER)
    trev.column("col5", width=150, anchor=CENTER)
    trev.heading("col5", text="Cantidad", anchor=CENTER)
    trev.place(y=500)
    #Pestaña 2 Inventario de recursos---------------------------------------------------------------------------------------------------------------------
    tab2=ttk.Frame(panel)
    panel.add(tab2, text="Inventario")
    tab2.columnconfigure(0, weight = 25)
    tab2.rowconfigure(0, weight= 25)
    tab2.columnconfigure(0, weight = 1)
    tab2.rowconfigure(1, weight= 1)

    frame1 = Frame(tab2, bg='gray26')
    frame1.grid(column=0,row=0,sticky='nsew')
    frame2 = Frame(tab2, bg='gray26')
    frame2.grid(column=0,row=1,sticky='nsew')

    frame1.columnconfigure(0, weight = 1)
    frame1.rowconfigure(0, weight= 1)

    frame2.columnconfigure(0, weight = 1)
    frame2.rowconfigure(0, weight= 1)
    frame2.columnconfigure(1, weight = 1)
    frame2.rowconfigure(0, weight= 1)

    frame2.columnconfigure(2, weight = 1)
    frame2.rowconfigure(0, weight= 1)

    frame2.columnconfigure(3, weight = 2)
    frame2.rowconfigure(0, weight= 1)

    tabla = ttk.Treeview(tab2, height=10)
    tabla.grid(column=0, row=0, sticky='nsew') 

    ladox = Scrollbar(frame1, orient = HORIZONTAL, command= tabla.xview)
    ladox.grid(column=0, row = 1, sticky='ew') 

    ladoy = Scrollbar(frame1, orient =VERTICAL, command = tabla.yview)
    ladoy.grid(column = 1, row = 0, sticky='ns')

    tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)

    estilo = ttk.Style(frame1)
    estilo.theme_use('clam') #  ('clam', 'alt', 'default', 'classic')
    estilo.configure(".",font= ('Arial', 14))
    estilo.configure("Treeview", font= ('Helvetica', 12))
    estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

    boton1 = Button(frame2, text= 'Abrir', bg='green2', command= abrir_archivo)
    boton1.grid(column = 0, row = 0, sticky='nsew', padx=10, pady=10)

    boton2 = Button(frame2, text= 'Mostrar', bg='magenta', command= datos_excel)
    boton2.grid(column = 1, row = 0, sticky='nsew', padx=10, pady=10)

    boton3 = Button(frame2, text= 'Limpiar', bg='red', command= Limpiar)
    boton3.grid(column = 2, row = 0, sticky='nsew', padx=10, pady=10)

    indica = Label(frame2, fg= 'white', bg='gray26', text= 'Ubicación del archivo', font= ('Arial',10,'bold') )
    indica.grid(column=3, row = 0)




def tecnicos(): 
    tec=Toplevel()
    tec.geometry("1400x1000")
    tec.title("Tienda de Técnicos")
    def almacenaArchivo(nombreFile, cadenaAlmacenar):
        print('Inicia Registro de Ventas')
        file=open(nombreFile,'a')
        file.write(cadenaAlmacenar)
        file.close()
        print('Finaliza Registro de venta')
        
    def validararchivo(nombreFile):
        if os.stat(nombreFile).st_size==0:
         cadenaEncabezado="NOMBRE | FECHA | CODIGO | PRECIO | CANTIDAD \n"
         almacenaArchivo(nombreFile,cadenaEncabezado)

    def seleccionado():
        nombr.delete(0, END)
        fech.delete(0, END)
        codig.delete(0, END)
        precio_entry(0, END)
        cantida.delete(0, END)
        selected=trev.focus() 
        valr=trev.item(selected, "values")
        nombr.insert(0, valr[0])
        fech.insert(0, valr[1])
        codig.insert(0, valr[2])
        precio_entry.insert(0, valr[3])
        cantida.insert(0, valr[4])   

    def eliminarcasillas(): 
        nombr.delete(0, END)
        fech.delete(0, END)
        codig.delete(0, END)
        precio_entry.delete(0, END)
        cantida.delete(0, END)

    def enviardatos(): 
        nombredata=nombre.get()
        fechadata=fecha.get() 
        codigodata=codigo.get() 
        preciodata=precio_entry.get()
        cantidaddata=cantidad.get()
        print(nombredata, fechadata, codigodata, cantidaddata)
        cadenaRegistro = nombredata + '|' + fechadata + '|' + str(codigodata) + '|' + str(preciodata) + '|'  + str(cantidaddata) +'\n'
        validararchivo("registroventas.txt")
        almacenaArchivo("registroventas.txt", cadenaRegistro)
        trev.insert("", END,  text="Activo", values=(nombr.get(), fech.get(), codig.get(),  precio_entry.get(), cantida.get()))

    def abrir_archivo():

        archivo = filedialog.askopenfilename(initialdir ='/', 
        title='Selecione archivo', 
        filetype=(('xlsx files', '*.xlsx*'),('All files', '*.*')))
        indica['text'] = archivo


    def datos_excel():

        datos_obtenidos = indica['text']
        try:
            archivoexcel = r'{}'.format(datos_obtenidos)
            

            df = pd.read_excel(archivoexcel)

        except ValueError:
            messagebox.showerror('Informacion', 'Formato incorrecto')
            return None

        except FileNotFoundError:
            messagebox.showerror('Informacion', 'El archivo esta \n malogrado')
            return None

        Limpiar()

        tabla['column'] = list(df.columns)
        tabla['show'] = "headings"  #encabezado
        

        for columna in tabla['column']:
            tabla.heading(columna, text= columna)
        

        df_fila = df.to_numpy().tolist()
        for fila in df_fila:
            tabla.insert('', 'end', values =fila)


    def Limpiar():
        tabla.delete(*tabla.get_children())
    #---------Defino algunas variables que usare en diferentes funciones----------------------
    nombre=StringVar()
    fecha=StringVar()
    codigo=IntVar() 
    prec=DoubleVar() 
    cantidad=IntVar() 
    #---------------Panel de pestañas----------------------------------------------
    panel=ttk.Notebook(tec) 
    panel.pack(fill="both", expand="yes")   
    #Pestaña 1-------------------------------------------------------------------------------
    tab1=ttk.Frame(panel)
    panel.add(tab1, text="Ventas") 
    indica=Label(tab1, fg="blue", text="Ubicación del archivo", font=("Arial", 10, "bold")).place(x=400, y=70)
    nombrA = Label(tab1, text="Nombre:").place(x=22, y=70)
    nombr = Entry(tab1, textvariable=nombre, width="40")
    nombr.place(x=22, y=100)
    fechA=Label(tab1, text="Fecha D/M/A: ").place(x=22, y=130) 
    fech=Entry(tab1, textvariable=fecha, width="40")
    fech.place(x=22, y=160)  
    codigA=Label(tab1, text="Código:").place(x=22, y=190)
    codig=Entry(tab1, textvariable=codigo, width="40")
    codig.place(x=22, y=220)
    precio_label=Label(tab1, text="Precio: ").place(x=22, y=250)
    precio_entry=Entry(tab1, textvariable=prec, width="40")
    precio_entry.place(x=22, y=270)
    cantidaA=Label(tab1, text="Cantidad:").place(x=22, y=300)
    cantida=Entry(tab1, textvariable=cantidad, width="40")
    cantida.place(x=22, y=330)   
    #----------------Botones--------------------------------------------
    etiqueta=Label(tab1, text="Sección de registro de ventas").place(x=400, y=5)
    datost=Label(tab1, text="Para efectuar una venta y enviar los datos del cliente, clique el siguiente boton:").place(x=400, y=150)
    botonenviar=ttk.Button(tab1, text="Enviar datos de registro", command=enviardatos).place(x=400, y=100) 
    borrarlabel=Label(tab1, text="Para limpiar los campos de entrada de texto pulse: Limpiar").place(x=400, y=200)
    botonlimpiar=ttk.Button(tab1, text="Limpiar", command=eliminarcasillas).place(x=400, y=250)
    labelusuario=Label(tab1, text="Tienda: " + usuario_entry.get(), font="Helvetica 20 bold", fg="red" ).place(x=700,  y=5)
    #Treeview--------------------
    trev=ttk.Treeview(tab1, columns=("col1", "col2", "col3", "col4", "col5"))
    trev.column("#0", width=150, anchor=CENTER)
    trev.heading("#0", text="Venta", anchor=CENTER)
    trev.heading("col1", text="Producto", anchor=CENTER)
    trev.column("col1", width=150, anchor=CENTER)
    trev.heading("col2", text="Fecha", anchor=CENTER)
    trev.column("col3", width=150, anchor=CENTER)
    trev.heading("col3", text="Código", anchor=CENTER)
    trev.column("col4", width=150, anchor=CENTER)
    trev.heading("col4", text="Precio", anchor=CENTER)
    trev.column("col5", width=150, anchor=CENTER)
    trev.heading("col5", text="Cantidad", anchor=CENTER)
    trev.place(y=500)
    #Pestaña 2 Inventario de recursos---------------------------------------------------------------------------------------------------------------------
    tab2=ttk.Frame(panel)
    panel.add(tab2, text="Inventario")
    tab2.columnconfigure(0, weight = 25)
    tab2.rowconfigure(0, weight= 25)
    tab2.columnconfigure(0, weight = 1)
    tab2.rowconfigure(1, weight= 1)

    frame1 = Frame(tab2, bg='gray26')
    frame1.grid(column=0,row=0,sticky='nsew')
    frame2 = Frame(tab2, bg='gray26')
    frame2.grid(column=0,row=1,sticky='nsew')

    frame1.columnconfigure(0, weight = 1)
    frame1.rowconfigure(0, weight= 1)

    frame2.columnconfigure(0, weight = 1)
    frame2.rowconfigure(0, weight= 1)
    frame2.columnconfigure(1, weight = 1)
    frame2.rowconfigure(0, weight= 1)

    frame2.columnconfigure(2, weight = 1)
    frame2.rowconfigure(0, weight= 1)

    frame2.columnconfigure(3, weight = 2)
    frame2.rowconfigure(0, weight= 1)

    tabla = ttk.Treeview(tab2, height=10)
    tabla.grid(column=0, row=0, sticky='nsew') 

    ladox = Scrollbar(frame1, orient = HORIZONTAL, command= tabla.xview)
    ladox.grid(column=0, row = 1, sticky='ew') 

    ladoy = Scrollbar(frame1, orient =VERTICAL, command = tabla.yview)
    ladoy.grid(column = 1, row = 0, sticky='ns')

    tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)

    estilo = ttk.Style(frame1)
    estilo.theme_use('clam') #  ('clam', 'alt', 'default', 'classic')
    estilo.configure(".",font= ('Arial', 14))
    estilo.configure("Treeview", font= ('Helvetica', 12))
    estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

    boton1 = Button(frame2, text= 'Abrir', bg='green2', command= abrir_archivo)
    boton1.grid(column = 0, row = 0, sticky='nsew', padx=10, pady=10)

    boton2 = Button(frame2, text= 'Mostrar', bg='magenta', command= datos_excel)
    boton2.grid(column = 1, row = 0, sticky='nsew', padx=10, pady=10)

    boton3 = Button(frame2, text= 'Limpiar', bg='red', command= Limpiar)
    boton3.grid(column = 2, row = 0, sticky='nsew', padx=10, pady=10)

    indica = Label(frame2, fg= 'white', bg='gray26', text= 'Ubicación del archivo', font= ('Arial',10,'bold') )
    indica.grid(column=3, row = 0)
    

    



mainloop()