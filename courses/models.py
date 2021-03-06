from turtle import update
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):  
    avatar = models.ImageField(upload_to='uploads/%Y/%m');

class Category(models.Model): #course_category
    name = models.CharField(max_length=100, null=False, unique=True);

    def __str__(self):
        return self.name;

class ModelBase(models.Model):
    subject = models.CharField(max_length=255, null=False);
    image = models.ImageField(upload_to='course/%Y/%m', default=None);
    created_date = models.DateTimeField(auto_now_add=True);
    updated_date = models.DateTimeField(auto_now=True);
    active = models.BooleanField(default=True);

    def __str__(self):
        return self.subject;

    class Meta:
        abstract = True;
    
class Course(ModelBase):
    class Meta:
        # Khong trung ten khoa hoc trong mot danh muc 
        unique_together = ('subject', 'category');
        ordering = ["-id"]
        
    description = models.TextField(null=True, blank=True);
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True);

class Lesson(ModelBase): #course_lesson
    class Meta:
        unique_together = ('subject', 'course');

    content = models.TextField(null=True);
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE);
    tags = models.ManyToManyField('Tag', blank=True, null=True);

    def __str__(self):
        return self.subject;

class Comment(models.Model):
    content = models.TextField();
    lesson = models.ForeignKey(Lesson, related_name="comment_post", on_delete=models.CASCADE);
    creator = models.ForeignKey(User, related_name="creator_set", on_delete=models.CASCADE);
    created_date = models.DateTimeField(auto_now_add=True);
    updated_date = models.DateTimeField(auto_now=True);

    def __str__(self):
        return self.content;

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True);

    def __str__(self):
        return self.name;

class ActionBase(models.Model):
    created_date = models.DateTimeField(auto_now_add=True);
    updated_date = models.DateTimeField(auto_now=True);
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE);
    creator = models.ForeignKey(User, on_delete=models.CASCADE);

    class Meta:
        abstract = True;


class Action(ActionBase):
    LIKE, HAHA, HEART = range(3);
    ACTIONS = [
        (LIKE, 'like'),
        (HAHA, 'haha'),
        (HEART, 'heart')
    ];
    type = models.PositiveSmallIntegerField(choices=ACTIONS, default=LIKE);

class Rating(ActionBase):
    rate = models.PositiveSmallIntegerField(default=0);

class LessonView(models.Model):
    created_date = models.DateTimeField(auto_now_add=True);
    updated_date = models.DateTimeField(auto_now_add=True);
    views = models.IntegerField(default=0);
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE);