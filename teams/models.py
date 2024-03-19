from django.db import models

# Create your models here.

class team(models.Model):
    idTeam = models.AutoField(primary_key=True)
    nameTeam = models.CharField(max_length=93)
    sedeTeam = models.CharField(max_length=93)

    def __str__(self):
        return self.nameTeam

class player(models.Model):
    idPlayer = models.AutoField(primary_key=True)
    playerName = models.CharField(max_length=93)
    playerHeight = models.FloatField()
    playerWeight = models.FloatField()
    positionPlayer = models.CharField(max_length=93)
    fkIdTeam = models.ForeignKey(team, name = "idTeam", 
                                    on_delete=models.DO_NOTHING,
                                    blank=True, null=True)

    def __str__(self):
        return self.playerName
