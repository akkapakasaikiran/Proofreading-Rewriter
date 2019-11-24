from django.db import models

# Create your models here.
class Word(models.Model):
    word_text = models.CharField(max_length=200)
    word_pos = models.IntegerField(primary_key=True)
    def __str__(self):
        return str(self.word_pos) + ":" + str(self.word_text)
