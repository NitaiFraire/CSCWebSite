from django.db import models
from django import forms
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_save, post_save

import os
import shutil


###################################
#############[ MEDIA ]#############
###################################

def event_banner(instance, filename):
    try:
        old_instance = Detail.objects.get(pk=instance.pk)
        old_instance.photo.delete()
    finally:
        return f'events/{instance.slug}/banner/{filename}'

def event_gallery(instance, filename):
    return f'events/{instance.event_id.slug}/gallery/{filename}'

def update_gallery(photo):
    if os.path.isfile(os.path.join(settings.MEDIA_ROOT, photo)):
        os.remove(os.path.join(settings.MEDIA_ROOT, photo))


####################################
#############[ MODELS ]#############
####################################

class Type(models.Model):  
    name     = models.CharField(max_length=30, blank=False, unique=True)
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tipo de evento'
        ordering = ['name']
    
class Detail(models.Model):
    event_type_id   = models.ForeignKey(Type,
                            on_delete=models.CASCADE,
                            verbose_name="tipo de evento")
    name            = models.CharField(max_length=30, blank=False, unique=True,
                                       verbose_name="nombre")
    slug            = models.SlugField(allow_unicode=True, unique=True)
    description     = models.TextField(blank=False, verbose_name="descripcion")
    photo           = models.ImageField(upload_to=event_banner, null=False,
                                        verbose_name="flyer")
    price           = models.DecimalField(max_digits=6, decimal_places=2,
                                        verbose_name="precio")
    capacity        = models.PositiveSmallIntegerField(verbose_name="capacidad")
    place           = models.CharField(max_length=100, blank=False,
                                       verbose_name="lugar")
    address         = models.CharField(max_length=100, blank=False,
                                       verbose_name="dirección")
    hour            = models.TimeField(blank=False, verbose_name="hora")
    start_date      = models.DateField(blank=False, verbose_name="inicia")
    end_date        = models.DateField(blank=False, verbose_name="termina")
    event_url       = models.URLField(blank=True, verbose_name="url")
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name


    class Meta:
        ordering = ['name']
        verbose_name = 'detalle de evento'

        constraints = [
            # models.CheckConstraint(check=models.Q(start_date__lte=end_date),
            #                        name="start_date_lte_end_date"),
            # models.CheckConstraint(check=models.Q(start_date__gte=timezone.now()),
            #                        name="start_date_gte_current_time")
        ]

class Gallery(models.Model):
    event_id    = models.OneToOneField(Detail,
                                       on_delete=models.CASCADE,
                                       verbose_name="galeria de evento")
    name        = models.CharField(max_length=30, blank=True)
    photo1      = models.ImageField(upload_to=event_gallery, null=True, blank=True, verbose_name="foto 1") 
    photo2      = models.ImageField(upload_to=event_gallery, null=True, blank=True, verbose_name="foto 2") 
    photo3      = models.ImageField(upload_to=event_gallery, null=True, blank=True, verbose_name="foto 3") 
    photo4      = models.ImageField(upload_to=event_gallery, null=True, blank=True, verbose_name="foto 4") 
    photo5      = models.ImageField(upload_to=event_gallery, null=True, blank=True, verbose_name="foto 5") 
    photo6      = models.ImageField(upload_to=event_gallery, null=True, blank=True, verbose_name="foto 6") 
    photo7      = models.ImageField(upload_to=event_gallery, null=True, blank=True, verbose_name="foto 7") 
    photo8      = models.ImageField(upload_to=event_gallery, null=True, blank=True, verbose_name="foto 8") 
    photo9      = models.ImageField(upload_to=event_gallery, null=True, blank=True, verbose_name="foto 9") 
    photo10     = models.ImageField(upload_to=event_gallery, null=True, blank=True, verbose_name="foto 10") 
    photo11     = models.ImageField(upload_to=event_gallery, null=True, blank=True, verbose_name="foto 11") 
    photo12     = models.ImageField(upload_to=event_gallery, null=True, blank=True, verbose_name="foto 12") 
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'galeria'


#####################################
#############[ SIGNALS ]#############
#####################################

@receiver(post_delete, sender=Detail)
def delete_event_banner(sender, instance, *args, **kwargs):
    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, f'events/{instance.slug}/banner/'))
    if not os.path.exists(os.path.join(settings.MEDIA_ROOT, f'events/{instance.slug}/gallery/')):
        os.rmdir(os.path.join(settings.MEDIA_ROOT, f'events/{instance.slug}'))

@receiver(post_delete, sender=Gallery)
def delete_event_gallery(sender, instance, *args, **kwargs):
    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, f'events/{instance.event_id.slug}/gallery/'))
    if not os.path.exists(os.path.join(settings.MEDIA_ROOT, f'events/{instance.event_id.slug}/banner/')):
        os.rmdir(os.path.join(settings.MEDIA_ROOT, f'events/{instance.slug}'))

@receiver(pre_save, sender=Gallery)
def delete_update_pictures(sender, instance, *args, **kwargs, ):
    try:
        gallery = sender.objects.filter(name__exact=instance.event_id.name).values(
                                                'photo1', 'photo2', 'photo3',
                                                'photo4', 'photo5', 'photo6',
                                                'photo7', 'photo8', 'photo9',
                                                'photo10', 'photo11', 'photo12')
        if gallery:
            if not gallery[0]['photo1'] == instance.photo1:
                update_gallery(gallery[0]['photo1'])
            if not gallery[0]['photo2'] == instance.photo2:
                update_gallery(gallery[0]['photo2'])
            if not gallery[0]['photo3'] == instance.photo3:
                update_gallery(gallery[0]['photo3'])
            if not gallery[0]['photo4'] == instance.photo4:
                update_gallery(gallery[0]['photo4'])
            if not gallery[0]['photo5'] == instance.photo5:
                update_gallery(gallery[0]['photo5'])
            if not gallery[0]['photo6'] == instance.photo6:
                update_gallery(gallery[0]['photo6'])
            if not gallery[0]['photo7'] == instance.photo7:
                update_gallery(gallery[0]['photo7'])
            if not gallery[0]['photo8'] == instance.photo8:
                update_gallery(gallery[0]['photo8'])
            if not gallery[0]['photo9'] == instance.photo9:
                update_gallery(gallery[0]['photo9'])
            if not gallery[0]['photo10'] == instance.photo10:
                update_gallery(gallery[0]['photo10'])
            if not gallery[0]['photo11'] == instance.photo11:
                update_gallery(gallery[0]['photo11'])
            if not gallery[0]['photo12'] == instance.photo12:
                update_gallery(gallery[0]['photo12'])
    except sender.DoesNotExist:
        pass

