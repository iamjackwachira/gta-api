from django.db import models


class BaseModel(models.Model):
    """
    An abstract base class model that provides self updating
    ``created_on`` and ``modified_on`` fields.
    """
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    modified_on = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class BaseModelWithName(BaseModel):
    name = models.CharField(max_length=70)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
