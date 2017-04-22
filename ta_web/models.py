from django.db import models
from django.contrib.auth.models import User
import datetime

User._meta.get_field('email')_blank = False # TODO email validator

class Profile(models.Model):
"""
    Extension of user model
"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    signup_date = models.DateTimeField()
    description = models.CharField(max_length=200, null=True)
    website_url = models.CharField(max_length=200, null=True) # TODO url validator

    def __str__(self):
        return '{}, {}'.format(self.user.username, self.signup_date)

class Document(models.Model):
"""
    Model for a user-submitted document.
    Stores the title, submission date, and text.

    Analytic information stored:
        - number of sentences
        - number of words
        - number of syllables
        - number of characters
        - number of polysyllables
        - the Flesch Readability Index
        - the Flesch-Kincaid Grade Level
        - the Automated Readability Index
        - SMOG (if the equation can be worked out)
    PK: Django-supplied
    FK: User (many-to-one)
"""
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
        self.date_submitted = timezone.now()
        #TODO issue 2

    def __str__(self):
        return '{}, {}'.format(self.title, self.date_submitted)
