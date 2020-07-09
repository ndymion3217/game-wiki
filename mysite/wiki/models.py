from django.db import models
from django.conf import settings

# Create your models here.

class Page(models.Model):  # 페이지 데이터필드를 담을 모델
    page_name = models.CharField(max_length=20)  # 제목정도의 작은 글을위한 필드
    #page_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(null=True)  # 내용을 담을 필드, 빈공간허용
    pub_date = models.DateTimeField(blank=True, null=True)  # 발행일을 담을 필드