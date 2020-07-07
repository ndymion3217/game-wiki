from django.db import models

# Create your models here.

class Page(models.Model):  # 페이지 데이터필드를 담을 모델
    page_name = models.CharField(max_length=20)  # 제목정도의 작은 글을위한 필드
    content = models.TextField(null=True)  # 내용을 담을 필드, 빈공간허용
    pub_date = models.DateTimeField('date published')  # 발행일을 담을 필드