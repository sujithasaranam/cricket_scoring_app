from tkinter import CASCADE
from django.db import models

class Team(models.Model):
    tid=models.AutoField(primary_key=True)
    team_name=models.CharField(max_length=20)
    Score=models.IntegerField(default=0)
    Wickets=models.IntegerField(default=0)
    extras=models.IntegerField(default=0)
    overs=models.IntegerField(default=0)


class Player(models.Model):  
    pid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=100)
    address=models.CharField(max_length=150) 
    age=models.IntegerField()
    phone_num=models.CharField(max_length=10)
    totalRuns=models.IntegerField(default=0)
    Wickets=models.IntegerField(default=0)
    tid=models.ForeignKey(Team,on_delete=models.CASCADE)

