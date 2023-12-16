"""This module providing Base Model object for the entire application"""
from django.db import models

class BaseModel(models.Model):
    """This is Base Model object for the entire application

    Args:
        models (object): Models object from Django
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50, blank=True)
    modified_by = models.CharField(max_length=50, blank=True)

    class Meta:
        """This is meta class for Base Model object
        """
        abstract = True

    def save(self, *args: tuple, **kwargs: dict) -> None:
        """This is override save function of base model
        """
        if not self.pk:
            self.created_by = kwargs['username']
        self.modified_by = kwargs['username']
        super(BaseModel, self).save(*args, **kwargs)
