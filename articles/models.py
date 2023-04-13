from django.db import models

# Create your models here.
class Article(models.Model): # 상속
    # 기본키(Primary Key=PK) id(PK)와 created_at은 자동으로 만들어집니다.
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)