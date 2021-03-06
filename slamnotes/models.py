"""slamnotes Models Configuration

Several class-based models. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/db/models/
"""
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, URLValidator
from django.db import models
from django.forms import ModelForm, Textarea, PasswordInput, EmailInput, TextInput


class School(models.Model):
    """School model"""
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100, validators=[URLValidator, ])

    def __str__(self):
        return self.name


class Instructor(models.Model):
    """Instructor model"""
    name_first = models.CharField(max_length=30)
    name_last = models.CharField(max_length=40)

    def __str__(self):
        return self.name_first + self.name_last


class Course(models.Model):
    """Course model"""
    school = models.ForeignKey(School, blank=True)
    instructor = models.ForeignKey(Instructor, blank=True)
    title = models.CharField(max_length=100)
    prefix = models.CharField(max_length=2)
    number = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(9999),
            MinValueValidator(0)
        ])
    postfix = models.CharField(max_length=1)

    def __str__(self):
        return self.title


class Section(models.Model):
    """Section model"""
    course = models.ForeignKey(Course, blank=True)
    instructor = models.ForeignKey(Instructor, blank=True)
    number = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(999),
            MinValueValidator(0)
        ])
    special = models.CharField(max_length=8)

    def __str__(self):
        if not self.special:
            return self.number
        return self.special


class Day(models.Model):
    """Class day model"""
    date = models.DateField()

    def __str__(self):
        return self.date


class Note(models.Model):
    """Note model"""
    body_text = models.TextField()
    author = models.ForeignKey(User, null=True, blank=True)
    section = models.ForeignKey(Section, null=True, blank=True)
    day = models.ForeignKey(Day, null=True, blank=True)
    created_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.body_text


class NoteForm(ModelForm):
    """Note model form"""
    class Meta:
        model = Note
        fields = ['body_text']
        labels = {
            'body_text': '',
        }
        widgets = {
            'body_text': Textarea(attrs={'placeholder': 'Write a note...'}),
        }


class UserForm(ModelForm):
    """User model form"""
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

        labels = {
            'email': '',
            'username': '',
            'password': '',
        }
        help_texts = {
            'username': '',
        }
        widgets = {
            'email': EmailInput(attrs={'placeholder': 'Email'}),
            'username': TextInput(attrs={'placeholder': 'Username'}),
            'password': PasswordInput(attrs={'placeholder': 'Password'}),
        }


class LoginForm(ModelForm):
    """Login model form"""
    class Meta:
        model = User
        fields = ['email', 'password']

        labels = {
            'email': '',
            'password': '',
        }
        help_texts = {
            'username': '',
        }
        widgets = {
            'email': EmailInput(attrs={'placeholder': 'Email'}),
            'password': PasswordInput(attrs={'placeholder': 'Password'}),
        }