from django.db import models

# Create your models here.

class Brain(models.Model):
    iq = models.IntegerField()
    weight = models.IntegerField()

class Human(models.Model):
    SEX = (
        ('male', 'мужской'),
        ('famale', 'жеский'),
        ('think', 'неопределённый'),
        ('fight helicopter', 'боевой вертолёт')
    )
    name = models.CharField(max_length= 50)
    sex = models.CharField(max_length=20, choices=SEX)
    brain = models.OneToOneField(
        Brain,
        on_delete= models.CASCADE,
        related_name='human'

    )

# brain1 = Brain.objects.create(iq= 160 , weight= 70)
# human1 = Human.objects.create(name = 'Einshetein', sex= 'male', brain=brain1)
# brain1.human
# <Human: Human object (1)>
# human1.brain
# <Brain: Brain object (1)>