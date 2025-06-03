from django.db import models

class Clipath(models.Model):

    CATEGORY_CHOICE = [
        ('header', 'Header'),
        ('footer', 'Footer')
    ]

    image = models.ImageField(upload_to='clipath/')
    alternative = models.TextField(default= 'CSS predesigned clip-path with code.', help_text='Description about the uploaded image.')
    category = models.CharField(max_length=6, choices=CATEGORY_CHOICE)
    code = models.TextField(default="Couldn't Copy the Code." ,help_text='Uploaded Image clip-path Code.')
    sender = models.CharField(max_length=60, help_text='Sender Email Address or GitHub.', blank=True)
    active = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.image} - {self.category} - {self.sender} - {self.active} - {self.date}'

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.email} - {self.date}'