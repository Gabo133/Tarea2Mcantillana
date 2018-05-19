from django.db import models
from basket.defines import POSITION_PLAYER_CHOICES


class Team(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos')
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=120)
    nickname = models.CharField(max_length=120)
    birthday = models.DateField(default="2018-05-19")
    age = models.PositiveIntegerField()
    email = models.EmailField()
    height = models.PositiveIntegerField(help_text="Altura en cm")
    weight = models.PositiveIntegerField(help_text="Peso en gramos")
    picture = models.ImageField(upload_to='picture_players')
    position = models.CharField(max_length=60)
    team = models.ForeignKey(Team, on_delete=models.CASCADE,default=None)

    rut = models.CharField(max_length=8)
    dv = models.PositiveIntegerField()

    def full_rut(self):
        return '{}-{}' . format(self.rut, self.dv)

    def __str__(self):
        return self.name


class Coach(models.Model):
    name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    nickname = models.CharField(max_length=120)

    rut = models.CharField(max_length=8)
    dv = models.PositiveIntegerField()

    def __str__(self):
        return self.name
