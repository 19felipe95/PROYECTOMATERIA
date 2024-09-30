# from conexion_db import conexionDB
# from tkinter import messagebox


# def crear_tabla():
#     conexion = conexionDB()

#     sql = '''
#     CREATE TABLE peliculas(
#         id_pelicula INTEGER,
#         nombre VARCHAR(100),
#         duracion VARCHAR(10),
#         genero VARCHAR(100),
#         PRIMARY KEY(id_pelicula AUTOINCREMENT)
#     )'''

#     try:
#         conexion.cursor.execute(sql)
#         conexion.cerrar()
#         titulo = 'Crear Registro'
#         mensaje = 'Se creo la tabla en la base de datos'
#         messagebox.showinfo(titulo, mensaje)

#     except:
#         titulo = 'Crear Registro'
#         mensaje = 'La tabla ya esta creada'
#         messagebox.showwarning(titulo, mensaje)


# def borrar_tabla():
#     conexion = conexionDB()
#     sql = 'DROP TABLE peliculas'
    
#     try:
#         conexion.cursor.execute(sql)
#         conexion.cerrar()
#         titulo = 'Borrar Registro'
#         mensaje = 'La tabla de la base de datos se borro con exito'
#         messagebox.showinfo(titulo, mensaje)

#     except:
#         titulo = 'Borrar Registro'
#         mensaje = 'No hay tabla para borrar'
#         messagebox.showerror(titulo, mensaje)

#     class pelicula:
#         def __init__(self, nombre, duracion, genero):
#             self.id_pelicula = None
#             self.nombre = nombre
#             self.duracion = duracion
#             self.genero = genero

#         def __str__(self):
#             return f'pelicula[{self.nombre}, {self.duracion}, {self.genero}]'

#         def guardar(pelicula):
#             conexion = conexionDB

#             sql = """INSERT INTO peliculas (nombre, duracion, genero)
#             VALUES('{pelicula.nombre}', '{pelicula.duracion}, '{pelicula.genero}')"""    
        
#         try:
#             conexion.cursor.execute(sql)
#             conexion.cerrar

#         except:
           
#                 pass
            



   


