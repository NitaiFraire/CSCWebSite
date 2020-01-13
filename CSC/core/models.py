from django.db import models


class Contact(models.Model):
    name    = models.CharField(max_length=40, verbose_name="nombre")
    email   = models.EmailField(max_length=100, )
    phone   = models.CharField(max_length=10, verbose_name="telefono")
    message = models.TextField(verbose_name="mensaje")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.phone}'

    
    class Meta:
        ordering = ['-created']
        verbose_name = 'contacto'
 