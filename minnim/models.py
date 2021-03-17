from django.db import models

# Create your models here.
# question은 테이블 이름 / model이 db관련 파일들 
class Question(models.Model): 
    subject = models.CharField(max_length=200)  # () 안은 속성을 나타냄
    create_date = models.DateTimeField()  # 시간을 나타냄
    author = models.CharField(max_length=200)
    def __str__(self):
        return self.subject

class Answer(models.Model):
    question_key = models.ForeignKey(Question, on_delete=models.CASCADE)  # 외래키 클래스당 하나
    context = models.TextField()
    def __str__(self):
        return self.context