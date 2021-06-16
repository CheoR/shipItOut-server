"""Document model"""

from django.db import models


class Document(models.Model):
    """
        Document model.
    """
    are_docs_ready = models.BooleanField()
