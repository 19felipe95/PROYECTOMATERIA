# import tkinter as tk
# from tkinter import ttk
# #from model.pelicula_dao import crear_tabla, borrar_tabla 
# #from model.pelicula_dao import pelicula, guardar

# def barra_menu(root):
#     barra_menu = tk.Menu(root)
#     root.config(menu=barra_menu, width=300, height=300)

#     menu_inicio = tk.Menu(barra_menu, tearoff=0)
#     barra_menu.add_cascade(label ='consultar', menu = menu_inicio)

#     menu_inicio.add_command(label='Crear Registro en DB')#,command=crear_tabla )
#     menu_inicio.add_command(label='Eliminar Registro en DB')#,command=borrar_tabla)
#     menu_inicio.add_command(label='Salir', command = root.destroy)

   
   
   
#     barra_menu.add_cascade(label ='Consultar')
#     barra_menu.add_cascade(label ='Configuracion')
#     barra_menu.add_cascade(label ='Ayuda')



   

# class Frame(tk.Frame):
#     def __init__(self, root = None):
#         super().__init__(root, width=480, height=320)
#         self.root = root
#         self.pack()
#         # self.config(bg = 'green')

#         self.campos_pelicula()
#         self.deshabilitar_campos()
#         self.tabla_peliculas()


#     def campos_pelicula(self):
#         #LABELS DE CADA CAMPO
#         self.label_nombre = tk.Label(self, text = 'Nombre:') 
#         self.label_nombre.config(font = ('Arial', 12, 'bold'))
#         self.label_nombre.grid(row = 0, column = 0, padx = 10, pady = 10)

#         self.label_duracion = tk.Label(self, text = 'Duracion:') 
#         self.label_duracion.config(font = ('Arial', 12, 'bold'))
#         self.label_duracion.grid(row = 1, column = 0, padx = 10, pady = 10)

#         self.label_genero = tk.Label(self, text = 'Genero:') 
#         self.label_genero.config(font = ('Arial', 12, 'bold'))
#         self.label_genero.grid(row = 2, column = 0, padx = 10, pady = 10)

#         #campos de entradas entrys
#         self.mi_nombre = tk.StringVar()
#         self.entry_nombre = tk.Entry(self, textvariable = self.mi_nombre)
#         self.entry_nombre.config(width=50, font = ('Arial', 12,))
#         self.entry_nombre.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan = 2 )

#         self.mi_duracion = tk.StringVar()
#         self.entry_duracion = tk.Entry(self, textvariable = self.mi_duracion)
#         self.entry_duracion.config(width=50, font = ('Arial', 12,))
#         self.entry_duracion.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 2)

#         self.mi_genero = tk.StringVar()
#         self.entry_genero = tk.Entry(self, textvariable = self.mi_genero)
#         self.entry_genero.config(width=50, font = ('Arial', 12,))
#         self.entry_genero.grid(row = 2, column = 1, padx = 10, pady = 10, columnspan = 2)

#         #BOTONES nuevo
#         self.boton_nuevo = tk.Button(self, text='Nuevo', command = self.habilitar_campos)
#         self.boton_nuevo.config(width= 20, font = ('Arial', 12,), fg = '#DAD5D6', bg = '#158645', cursor='hand2', activebackground='#35BD6F')
#         self.boton_nuevo.grid(row = 3, column = 0, padx = 10, pady = 10)
#         #BOTON GUARDAR
#         self.boton_guardar = tk.Button(self, text='Guardar', command =self.guardar_datos)
#         self.boton_guardar.config(width= 20, font = ('Arial', 12,), fg = '#DAD5D6', bg = '#1658A2', cursor='hand2', activebackground='#3586DF')
#         self.boton_guardar.grid(row = 3, column = 1, padx = 10, pady = 10)
#         #BOTON CANCELAR
#         self.boton_cancelar = tk.Button(self, text='Cancelar', command= self.deshabilitar_campos)
#         self.boton_cancelar.config(width= 20, font = ('Arial', 12,), fg = '#DAD5D6', bg = '#BD152E', cursor='hand2', activebackground='#E15370')
#         self.boton_cancelar.grid(row = 3, column = 2, padx = 10, pady = 10)

#     def habilitar_campos(self):
#         self.mi_nombre.set('')
#         self.mi_duracion.set('')
#         self.mi_genero.set('')

#         self.entry_nombre.config(state='normal')
#         self.entry_duracion.config(state='normal')
#         self.entry_genero.config(state='normal')

#         self.boton_guardar.config(state='normal')
#         self.boton_cancelar.config(state='normal')


#     def deshabilitar_campos(self):
#         self.mi_nombre.set('')
#         self.mi_duracion.set('')
#         self.mi_genero.set('')

#         self.entry_nombre.config(state='disabled')
#         self.entry_duracion.config(state='disabled')
#         self.entry_genero.config(state='disabled')

#         self.boton_guardar.config(state='disabled')
#         self.boton_cancelar.config(state='disabled')

#     def guardar_datos(self):



#         self.deshabilitar_campos()

#     def tabla_peliculas(self):

#         self.tabla = ttk.Treeview(self,column = ('Nombre', 'Duracion', 'Genero'))
#         self.tabla.grid(row=4, column =0, columnspan= 4)
        
#         self.tabla.heading('#0', text= 'ID')
#         self.tabla.heading('#1', text= 'NOMBRE')
#         self.tabla.heading('#2', text= 'DURACION')
#         self.tabla.heading('#3', text= 'GENERO')

#         self.tabla.insert('', 0, text='4',values = ('Los vengadores', '2.35', 'Accion'))
#         self.tabla.insert('', 0, text='3',values = ('elver galarga', '2.50', "Accion"))
#         self.tabla.insert('', 0, text='2',values = ('La venganza de los chamos ', '3.40', 'Comedia'))
#         self.tabla.insert('', 0, text='1',values = ('Cenicienta se sienta', '4.35', 'Accion'))

#         #BOTON EDITAR
#         self.boton_editar = tk.Button(self, text='Editar')
#         self.boton_editar.config(width= 20, font = ('Arial', 12,), fg = '#DAD5D6', bg = '#158645', cursor='hand2', activebackground='#35BD6F')
#         self.boton_editar.grid(row = 5, column = 0, padx = 10, pady = 10)

#         #BOTON ELIMINAR
#         self.boton_eliminar = tk.Button(self, text='Eliminar')
#         self.boton_eliminar.config(width= 20, font = ('Arial', 12,), fg = '#DAD5D6', bg = '#BD152E', cursor='hand2', activebackground='#E15370')
#         self.boton_eliminar.grid(row = 5, column = 1, padx = 10, pady = 10)

