import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
#no pude importar guardar, listar, eliminar, editar solo lo importo y resolveria todo (me siento soolo jj)


#  nueva conexion  ################

class conexionDB:
    conexion = sqlite3.connect('BD_peliculas.db')
    cursor = conexion.cursor()
    def __init__(self):
        self.base_datos = 'BD_peliculas.db'
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()


def crear_tabla():
    conexion = sqlite3.connect('BD_peliculas.db')
    cursor = conexion.cursor()
    #conexion = conexionDB()

    sql = '''
    CREATE TABLE IF NOT EXISTS peliculas(
        id_pelicula INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(100)
    )'''

    try:
        #conexion = sqlite3.connect('BD_peliculas.db')
        #cursor = conexion.cursor()
        #conexion.cursor.execute(sql)
        #conexion.cerrar()
        cursor.execute(sql)
        conexion.commit()
        conexion.close()

        titulo = 'Crear Registro'
        mensaje = 'Se creo la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)

    except:
        titulo = 'Crear Registro'
        mensaje = 'La tabla ya esta creada'
        messagebox.showwarning(titulo, mensaje)


def borrar_tabla():
    conexion = conexionDB()
    sql = 'DROP TABLE peliculas'
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar Registro'
        mensaje = 'La tabla de la base de datos se borro con exito'
        messagebox.showinfo(titulo, mensaje)

    except:
        titulo = 'Borrar Registro'
        mensaje = 'No hay tabla para borrar'
        messagebox.showerror(titulo, mensaje)




    class pelicula:
        def __init__(self, nombre, duracion, genero):
            self.id_pelicula = None
            self.nombre = nombre
            self.duracion = duracion
            self.genero = genero

        def __str__(self):
            return f'pelicula[{self.nombre}, {self.duracion}, {self.genero}]'

#######  insertar registro  insercion ##################     

def guardar(pelicula):
    Peli = pelicula
    
    
    ##conexion = conexionDB

    conexion = sqlite3.connect('BD_peliculas.db')
    cursor = conexion.cursor()

    sql = f"""INSERT INTO peliculas(nombre, duracion, genero) VALUES(?,?,?)"""    
    
    try:
        cursor.execute(sql,Peli)
        conexion.commit()
        conexion.close()

        messagebox.showinfo("Registro de peliculas","Pelicula registrada exitosamente")

    except:
        titulo = 'Conexion al registro'
        mensaje = 'La tabla pelicula no esta creado en la base de datos'
        messagebox.showerror(titulo, mensaje)

def listar():
    lista_peliculas = []
    conexion = sqlite3.connect('BD_peliculas.db')
    cursor = conexion.cursor()
    #conexion = conexionDB

    #lista_peliculas = []
    sql = 'SELECT * FROM peliculas'

    try:
        cursor.execute(sql,listar)
        conexion.commit()
        conexion.close()

        # conexion.cursor.execute(sql,listar)
        # lista_peliculas = conexion.cursor.fetchall()
        # conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Crea la tabla en la base de datos'
        messagebox.showwarning(titulo, mensaje)

    return lista_peliculas

def editar(pelicula,id_pelicula):
    conexion = conexionDB()

    sql = f"""update peliculas
    SET nombre = '{pelicula.nombre}', '{pelicula.duracion}' genero = '{pelicula.genero}',  WHERE id_pelicula ={id_pelicula}
    """
    try:
        conexion.cursor.execute(sql)
        #conexion.cursor()
        conexion.cerrar()

    except:
        titulo = 'Edicion de datos'
        mensaje = 'No se ha podido editar este registro'
        messagebox.showerror(titulo, mensaje)


def eliminar(id_pelicula):
    conexion = conexionDB()
    sql = f'DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}'

    try:
        conexion.cursor.execute(sql)
        #conexion.cursor()
        conexion.cerrar()

    except:
        titulo = 'Edicion de datos'
        mensaje = 'No se ha podido editar este registro'
        messagebox.showerror(titulo, mensaje)


                
    







def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label ='inicio', menu = menu_inicio)

    menu_inicio.add_command(label='Crear Registro en DB',command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Registro en DB',command=borrar_tabla)
    menu_inicio.add_command(label='Salir', command=root.destroy)

    barra_menu.add_cascade(label ='consultas')
    barra_menu.add_cascade(label ='configuracion')
    barra_menu.add_cascade(label ='ayuda')

   
   
   



   

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        # self.config(bg = 'green')
        self.id_pelicula = None

        self.campos_pelicula()
        self.deshabilitar_campos()
        self.tabla_peliculas()


    def campos_pelicula(self):
        #LABELS DE CADA CAMPO
        self.label_nombre = tk.Label(self, text = 'Nombre:') 
        self.label_nombre.config(font = ('Arial', 12, 'bold'))
        self.label_nombre.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.label_duracion = tk.Label(self, text = 'Duracion:') 
        self.label_duracion.config(font = ('Arial', 12, 'bold'))
        self.label_duracion.grid(row = 1, column = 0, padx = 10, pady = 10)

        self.label_genero = tk.Label(self, text = 'Genero:') 
        self.label_genero.config(font = ('Arial', 12, 'bold'))
        self.label_genero.grid(row = 2, column = 0, padx = 10, pady = 10)

        #campos de entradas entrys
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable = self.mi_nombre)
        self.entry_nombre.config(width=50, font = ('Arial', 12,))
        self.entry_nombre.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan = 2 )

        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable = self.mi_duracion)
        self.entry_duracion.config(width=50, font = ('Arial', 12,))
        self.entry_duracion.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 2)

        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable = self.mi_genero)
        self.entry_genero.config(width=50, font = ('Arial', 12,))
        self.entry_genero.grid(row = 2, column = 1, padx = 10, pady = 10, columnspan = 2)

        #######BOTONES nuevo #####

        self.boton_nuevo = tk.Button(self, text='Nuevo', command = self.habilitar_campos)
        self.boton_nuevo.config(width= 20, font = ('Arial', 12,), fg = '#DAD5D6', bg = '#158645', cursor='hand2', activebackground='#35BD6F')
        self.boton_nuevo.grid(row = 3, column = 0, padx = 10, pady = 10)
        
        #### BOTON GUARDAR ########

        self.boton_guardar = tk.Button(self, text='Guardar', command =self.guardar_datos)#guardar_datos
        self.boton_guardar.config(width= 20, font = ('Arial', 12,), fg = '#DAD5D6', bg = '#1658A2', cursor='hand2', activebackground='#3586DF')
        self.boton_guardar.grid(row = 3, column = 1, padx = 10, pady = 10)
        
        ###### BOTON CANCELAR #######

        self.boton_cancelar = tk.Button(self, text='Cancelar', command= self.deshabilitar_campos)
        self.boton_cancelar.config(width= 20, font = ('Arial', 12,), fg = '#DAD5D6', bg = '#BD152E', cursor='hand2', activebackground='#E15370')
        self.boton_cancelar.grid(row = 3, column = 2, padx = 10, pady = 10)

    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')

        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')


    def deshabilitar_campos(self):

        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')

        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')


    def guardar_datos(self):
        pelicula = list((self.mi_nombre.get(),
            self.mi_duracion.get(),
            self.mi_genero.get()))
        
        if self.id_pelicula == None:
            guardar(pelicula)

        else :
            editar(pelicula, self.id_pelicula)
        
        guardar(pelicula)

        self.tabla_peliculas()

    
        self.deshabilitar_campos()

    def tabla_peliculas(self):
        self.lista_peliculas = listar()
        self.lista_peliculas.reverse()

        self.tabla = ttk.Treeview(self,column = ('Nombre', 'Duracion', 'Genero'))
        self.tabla.grid(row=4, column =0, columnspan= 4, sticky= 'nse')

        ###### scrollbar para la tabla si existen 10 registros ######
        self.scroll = ttk.Scrollbar(self,orient= 'vertical', command= self.tabla.yview)
        self.scroll.grid(row=4, column= 4, sticky= 'nse')
        self.tabla.configure(yscrollcommand= self.scroll.set)
        
        self.tabla.heading('#0', text= 'ID')
        self.tabla.heading('#1', text= 'NOMBRE')
        self.tabla.heading('#2', text= 'DURACION')
        self.tabla.heading('#3', text= 'GENERO')

        ## iteracion de la lista  #####
        for p in self.lista_peliculas:
        
            self.tabla.insert('', 0, text=p[0],values = (p[1], p[2], p[3])) #('la caida de los enanos', '2.50', "Accion"))
            # self.tabla.insert('', 1, text='1',values = ('La venganza de los chamos ', '3.40', 'Comedia'))
            # self.tabla.insert('', 2, text='2',values = ('Cenicienta', '4.35', 'Accion'))
            # self.tabla.insert('', 3, text='3',values = ('Cenicienta ', '4.35', 'Accion'))
            # self.tabla.insert('', 0, text='4',values = ('Cenicienta ', '4.35', 'Accion'))
            # self.tabla.insert('', 0, text='5',values = ('Cenicienta ', '4.35', 'Accion'))

        #BOTON EDITAR
        self.boton_editar = tk.Button(self, text='Editar', command= self.editar_datos)
        self.boton_editar.config(width= 20, font = ('Arial', 12,), fg = '#DAD5D6', bg = '#158645', cursor='hand2', activebackground='#35BD6F')
        self.boton_editar.grid(row = 5, column = 0, padx = 10, pady = 10)

        #BOTON ELIMINAR
        self.boton_eliminar = tk.Button(self, text='Eliminar') #,command= self.eliminar_datos)
        self.boton_eliminar.config(width= 20, font = ('Arial', 12,), fg = '#DAD5D6', bg = '#BD152E', cursor='hand2', activebackground='#E15370')
        self.boton_eliminar.grid(row = 5, column = 1, padx = 10, pady = 10)

    def editar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula = self.tabla.item(self.tabla.selection())['values'][0]
            self.duracion_pelicula = self.tabla.item(self.tabla.selection())['values'][1]
            self.genero_pelicula = self.tabla.item(self.tabla.selection())['values'][0]

            self.habilitar_campos()

            self.entry_nombre.insert(0, self.nombre_pelicula)
            self.entry_duracion.insert(0, self.duracion_pelicula)
            self.entry_genero.insert(0, self.genero_pelicula)
        except:
            titulo = 'Edicion de datos'
            mensaje = 'no ha seleccionado ningun registro'
            messagebox.showerror(titulo, mensaje)


#def eliminar_datos(self):
   # eliminar = eliminar_datos
    # try:
    #     self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
    #     eliminar(self.id_pelicula)

    #     self.tabla_peliculas()
    #     self.id_peliculas = None



    # except:
    #     titulo = 'Edicion de datos'
    #     mensaje = 'no ha seleccionado ningun registro'
    #     messagebox.showerror(titulo, mensaje)




def main():
    root = tk.Tk()
    root.title('Catalogo de Peliculas')
    root.iconbitmap('C:/Users/57320/Desktop/proyectoMateria/proyectoMateria/catalogo_peliculas/img/library-regular-24.ico')
    root.resizable(0,1)
    
    barra_menu(root)
    
    
    app = Frame(root = root)
    
    app.mainloop()
    
if __name__ == '__main__':
    main()
    