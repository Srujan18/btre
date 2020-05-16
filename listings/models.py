from django.db import models

class listing(models.Model):
    realtor = models.Foreignkey(Realtor, on_delete)
