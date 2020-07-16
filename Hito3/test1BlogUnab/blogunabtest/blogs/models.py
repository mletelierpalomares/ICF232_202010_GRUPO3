from django.db import models
from ckeditor.fields import RichTextField
#antes de la db
#constructor con atributos

class Blog(models.Model):
    titulo=models.CharField(max_length=35)
    contenido= RichTextField()
    #fecha=models.datetime.datetime.now()
    blogs=models.Manager()

    def __str__(self):
        return "{}".format(self.titulo)

    
    def getBlog(self,titulo):
        for blog in self.blogs:
            if blog.titulo==titulo:
                return blog
        return None       




