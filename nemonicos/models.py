from django.db import models
# Create your models here.
    
class HUMEDAD_RELATIVA_DEL_AIRE_max(models.Model):
    id_estacion= models.IntegerField()
    valor_mensual= models.FloatField()
    anio=models.IntegerField()
    mes=models.IntegerField()
    
    class Meta:
        managed = False  # Desactiva las migraciones automáticas
        db_table = 'mensuales.vta_9111M'  # Usa el mismo nombre de la tabla en PostgreSQL

    def __str__(self):
        return self.name
    
