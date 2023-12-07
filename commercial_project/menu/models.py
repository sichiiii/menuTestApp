from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=50, null=False)
    url = models.CharField(max_length=255, null=False)
    parent_menu = models.ForeignKey('Menu', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
