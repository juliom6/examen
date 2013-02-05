from django.db import models

# Create your models here.

class Editorial(models.Model):
	nombre = models.CharField(max_length = 30)
	direccion = models.CharField(max_length = 80)
	ciudad = models.CharField(max_length = 30)
	provincia = models.CharField(max_length = 30)
	pais = models.CharField(max_length = 30)
	email = models.EmailField(blank = True)
	sitio_web = models.URLField(blank = True)
	
	def __unicode__(self):
		return self.nombre
	
	class Meta:
		ordering = ['nombre']
	
class Autor(models.Model):
	nombre = models.CharField(max_length = 40)
	apellido = models.CharField(max_length = 40)
	email = models.EmailField(blank = True)
	
	def __unicode__(self):
		return u'%s %s' % (self.nombre, self.apellido)
	
class Libro(models.Model):
	titulo = models.CharField(max_length = 100)
	autores = models.ManyToManyField(Autor)
	editorial = models.ForeignKey(Editorial)
	fecha_publicacion = models.DateField()
	isbn_13 = models.CharField(max_length = 20)
	isbn_10 = models.CharField(max_length = 15, blank = True)
	edicion = models.IntegerField()
	
	def __unicode__(self):
		return self.titulo
	