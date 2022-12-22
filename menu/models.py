from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=250)
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='children'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True
    )
    link = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ('menu__name', 'parent__title', 'title')

    def __str__(self):
        return f'{self.title}'

    @property
    def has_children(self):
        return not self.children.count() == 0
