from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.forms import ValidationError


####################################
#############[ MODELS ]#############
####################################

class Total(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name="Total")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    def __str__(self):
        return f'${self.total}'
    

    class Meta:
        ordering = ['id']
        verbose_name = 'Total'
        verbose_name_plural = 'Total'


class Entry(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Monto")
    description = models.CharField(max_length=255, verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")

    def __str__(self):
        return f'${self.amount}'
    

    class Meta:
        ordering = ['-id']
        verbose_name = 'Ingreso'
        verbose_name_plural = 'Ingresos'


class Egress(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Monto")
    description = models.CharField(max_length=255, verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")

    def __str__(self):
        return f'${self.amount}'
    

    class Meta:
        ordering = ['-id']
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'


#####################################
#############[ SIGNALS ]#############
#####################################

@receiver(post_save, sender=Entry)
def add_amount_to_total(sender, instance, *args, **kwargs):
    total = Total.objects.filter(pk=1).values('total')
    
    if not total:
        total = Total(total=instance.amount)
        total.save()
    else:
        total = total[0]['total']
        total = float(total)
        amount = float(instance.amount)
        total += amount

        Total.objects.filter(pk=1).update(total=total)

@receiver(pre_save, sender=Egress)
def substract_amount_to_total(sender, instance, *args, **kwargs):
    total = Total.objects.filter(pk=1).values('total')

    # if not total:
    #     raise ValidationError("Cuenta vacia")
    # else:
    total = total[0]['total']

    total = float(total)
    amount = float(instance.amount)
    total -= amount

        # if total < 0:
        #     raise ValidationError("La cuenta no puede quedar vacia")

    Total.objects.filter(pk=1).update(total=total)

