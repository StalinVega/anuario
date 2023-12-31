from django.db import models
# Create your models here.
    
class Estaciones(models.Model):
    codigo=models.CharField()
    nombre=models.CharField()
    id_estacion= models.IntegerField()
    id_provincia= models.IntegerField()
    
    class Meta:
        managed = False  # Desactiva las migraciones automáticas
        db_table = 'administrativo.vta_estaciones'  # Usa el mismo nombre de la tabla en PostgreSQL

    def __str__(self):
        return self.name
    
