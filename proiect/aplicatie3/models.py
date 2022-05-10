from django.db import models
# Sa se realizeze funcțiile de adăugare, modificare, listare, dezactivare și activare a datelor utilizând modelelul denumit Jobs care conține coloanele:
# - type: varchar(11)
# - url: varchar(100)
# - title: varchar(100)
# - description: text
# - how_to_apply: text

tipuri_job = (("JUNIOR", "Junior"), ("MID", "Mid"), ("SENIOR", "Senior"))


class Jobs(models.Model):

    type = models.CharField(max_length=11, choices=tipuri_job)
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(default="fara descriere")
    how_to_apply = models.TextField(default="trimite cv la adresa de pe Site")
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.type} - {self.title} - {self.description}'
