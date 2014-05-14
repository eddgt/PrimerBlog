from django.db import models

# Create your models here.
 
class Post(models.Model):
    autor = models.CharField(max_length = 30)
    titulo = models.CharField(max_length = 100)
    texto = models.TextField()
    fecha = models.DateTimeField()

    
#esta linea sirve para cuando entremos a inicio/blog/posts
#se nos muestre como link vista previa autor, titulo y fecha de cada post
    def __unicode__(self):
        return u'%s - %s %s' %(self.autor, self.titulo, self.fecha)