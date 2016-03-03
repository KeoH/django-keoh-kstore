#encoding:utf-8
from django.db import models

class BasicConfiguration(models.Model):
    company_name = models.CharField('Nombre de la empresa', max_length=255)
    theme = models.CharField('Theme', max_length=255, default="one")

    def get_theme_url(self):
        return 'themes/'+ self.theme

    def __unicode__(self):
        return self.company_name + ' configuration'
