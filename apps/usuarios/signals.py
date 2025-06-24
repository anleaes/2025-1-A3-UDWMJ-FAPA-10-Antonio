
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


from .models import ClienteProfile, LeiloeiroProfile


from apps.cliente.models import Cliente


from apps.leiloeiro.models import Leiloeiro



@receiver(post_save, sender=ClienteProfile)
def create_or_update_cliente_from_profile(sender, instance, created, **kwargs):
    """
    Cria ou atualiza um objeto Cliente no app 'cliente'
    sempre que um ClienteProfile no app 'usuarios' é salvo.
    """
   
    full_name = f"{instance.name} {instance.second_name}".strip()

    if created: 
        print(f"DEBUG_SIGNAL: Criando Cliente para novo ClienteProfile: {instance.email}")
        Cliente.objects.create(
            name=full_name, 
            cell=instance.cell,
            email=instance.email
        )
    else: 
        print(f"DEBUG_SIGNAL: Atualizando Cliente para ClienteProfile existente: {instance.email}")
        Cliente.objects.filter(email=instance.email).update(
            name=full_name, 
            cell=instance.cell
        )


@receiver(post_save, sender=LeiloeiroProfile)
def create_or_update_leiloeiro_from_profile(sender, instance, created, **kwargs):
    """
    Cria ou atualiza um objeto Leiloeiro no app 'leiloeiro'
    sempre que um LeiloeiroProfile no app 'usuarios' é salvo.
    """
    if created:
        print(f"DEBUG_SIGNAL: Criando Leiloeiro para novo LeiloeiroProfile: {instance.email}")
        Leiloeiro.objects.create(
            name=instance.name,
            cell=instance.cell,
            email=instance.email
        )
    else:
        print(f"DEBUG_SIGNAL: Atualizando Leiloeiro para LeiloeiroProfile existente: {instance.email}")
        Leiloeiro.objects.filter(email=instance.email).update(
            name=instance.name,
            cell=instance.cell
        )
