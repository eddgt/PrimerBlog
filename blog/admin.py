from blog.models import * 
from django.contrib import admin
from models import Post
 
#admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    search_fields=['autor','titulo'] # Hacemos que haya un campo de busqueda, y que busque por cedula, nombre o apellido
admin.site.register(Post,PostAdmin) #Definimos que la clase Personas va a ser administrado por PersonasAdmin
