from django.db import models
from django.contrib.auth.models import User
import datetime
import .calc
import .eq

User._meta.get_field('email')._blank = False # TODO email validator

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    signup_date = models.DateTimeField()
    description = models.CharField(max_length=200, null=True)
    website_url = models.CharField(max_length=200, null=True) # TODO url validator

    def __str__(self):
        return '{}, {}'.format(self.user.username, self.signup_date)

class Document(models.Model):
    title = models.CharField(max_length=200)
    date_submitted = models.DateTimeField()
    text = models.TextField()
    sentences = models.IntegerField()
    words = models.IntegerField()
    syllables = models.IntegerField()
    characters = models.IntegerField()
    polysyllables = models.IntegerField()
    readability_index = models.FloatField()
    fk_grade_level = models.FloatField()
    ari = models.FloatField()
    smog = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def submit(self):
        """
            Process submitted text.
        """
        self.date_submitted = timezone.now()

        self.sentences, self.words, self.syllables, \
        self.characters, self.poly_syllables = calc.analyze_string(self.text)

        self.readability_index = eq.fk_re(self.words, self.sentences, self.syllables)
        self.fk_grade_level = eq.fk_gl(self.words, self.sentences, self.syllables)
        self.ari = eq.ari(self.words, self.sentences, self.characters)
        self.smog = eq.smog(self.poly_syllables)


    def __str__(self):
        return '{}, {}'.format(self.title, self.date_submitted)
