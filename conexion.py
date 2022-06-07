from distutils.log import error
import sqlite3
from sqlite3.dbapi2 import connect

class contactos:
    def iniciarConexion(self):
        conexion = sqlite3.connect('sistema.s3db')
        conexion.text_factory = lambda b: b.decode(errors='ignore')
        return conexion

    def leerContactos(self,):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sentenciaSQL = 'select * from contactos'
        cursor.execute(sentenciaSQL)
        return cursor.fetchall()

    def crearContacto(self, datosContacto):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sentenciaSQL = 'insert into contactos(nombre,correo) values(?,?)'
        cursor.execute(sentenciaSQL, datosContacto)
        conexion.commit()
        conexion.close()

    def editarContacto(self, datosContacto):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sentenciaSQL = 'update contactos set nombre=? , correo=? where id=?'
        cursor.execute(sentenciaSQL, datosContacto)
        conexion.commit()
        conexion.close()

    def eliminarContacto(self, id):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sentenciaSQL = 'delete from contactos where id=(?)'
        cursor.execute(sentenciaSQL, [id])
        conexion.commit()
        conexion.close()