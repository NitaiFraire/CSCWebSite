from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


###################################
#############[ MEDIA ]#############
###################################

def photo_account(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.photo.delete()
        
    return f'accounts/{instance.control_number}/{filename}'


####################################
#############[ MODELS ]#############
####################################

def replace_str_user(self):
    return f'{self.first_name} {self.last_name}'

User.add_to_class('__str__', replace_str_user)


class ControlNumber(models.Model):
    control_number = models.CharField(verbose_name="numero de control",
                                      primary_key=True,
                                      serialize=False, max_length=10)
    is_active      = models.BooleanField(verbose_name="activado", default=False)

    def __str__(self):
        return self.control_number


    class Meta:
        ordering = ['control_number']
        verbose_name = 'numero de control'
        verbose_name_plural = 'numeros de control'

class Profile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ]

    SEMESTER_CHOICES = [
        ('1', 'Primero'),
        ('2', 'Segundo'),
        ('3', 'Tercero'),
        ('4', 'Cuarto'),
        ('5', 'Quinto'),
        ('6', 'Sexto'),
        ('7', 'Séptimo'),
        ('8', 'Octavo'),
        ('9', 'Noveno'),
        ('10', 'Décimo'),
        ('11', 'Onceavo'),
        ('12', 'Doceavo'),
    ]
    
    control_number  = models.OneToOneField(ControlNumber, on_delete=models.CASCADE,
                                           verbose_name="número de control", null=True) # y
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    first_last_name = models.CharField(verbose_name="apellido paterno", max_length=50, blank=True) # y
    photo           = models.ImageField(verbose_name="foto de perfil",
                                        upload_to=photo_account,
                                        blank=True) 
    semester        = models.CharField(verbose_name="semestre", max_length=1,
                                       choices=SEMESTER_CHOICES, blank=True) # x
    birthday        = models.DateField(verbose_name="fecha de nacimiento", null=True) # x
    gender          = models.CharField(verbose_name="genero", max_length=1,
                                       choices=GENDER_CHOICES, blank=True) # y
    phone           = models.CharField(verbose_name="telefono", max_length=10, blank=True) # y
    facebook        = models.URLField(verbose_name="facebook", blank=True)
    instagram       = models.URLField(verbose_name="instagram", blank=True)
    github          = models.URLField(verbose_name="gitHub", blank=True)
    gitlab          = models.URLField(verbose_name="gitLab", blank=True)

    def __str__(self):
        return self.user.username
    

    class Meta:
        ordering = ['control_number']
        verbose_name = 'cuenta'
    

#####################################
#############[ SIGNALS ]#############
#####################################

@receiver(post_save, sender=User)
def update(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)