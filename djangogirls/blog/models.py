from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):  # 장고 모델인것을 명시해주어, DB에 저장하게 한다.
    # 아래로는 DB에 저장될 필드들을 정의해준다
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 다른 모델에대한 링크
    title = models.CharField(max_length=200)  # 200자 제한의 텍스트 필드
    text = models.TextField()  # 글자 제한이 없는 텍스트 필드
    created_date = models.DateTimeField(default=timezone.now)  # 날짜와 시간 필드
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
