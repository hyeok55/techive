from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=200, verbose_name = '회사명')

    def __str__(self):
        return f'{self.company_name}'

class Post(models.Model):
    #post_id  pk
    title = models.CharField(max_length=200, verbose_name = '제목')
    company = models.ForeignKey(Company, on_delete=models.CASCADE,verbose_name='회사')
    date = models.DateTimeField(verbose_name = '작성일')
    url = models.URLField(max_length=200,verbose_name = '링크')

    def save(self, *args, **kwargs):
        # 'created' 변수를 사용하여 새로운 객체가 생성되었는지, 기존 객체가 업데이트되었는지 확인
        created = self.pk is None
        super().save(*args, **kwargs)  # Post 객체를 저장

        if created:  # 만약 새로운 Post 객체가 생성되었다면
            View.objects.create(post=self)  # 관련 View 객체를 생성
            Like.objects.create(post=self)

    def __str__(self):
        return f'{self.title},{self.company.company_name},{self.date}'

## view 조회수
class View(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    views = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.post.title}'
    
# like 조회수   
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.IntegerField(default = 0)

class Tag(models.Model):
    # tag_id pk
    tag_name = models.CharField(max_length=200, verbose_name = '태그 내용')

    def __str__(self):
        return f'{self.tag_name}'


class Post_tag(models.Model):
    # post_tag_id pk
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='게시글') #class Post
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,verbose_name='태그') # class Tag

    def __str__(self):
        return f'{self.post.title},{self.tag.tag_name}'
    


class Company_Tag(models.Model):
    #company_tag_id pk
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='회사') #class Post
    tag  = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='태그 내용') #class Post# tag table
    count = models.IntegerField(default = 0)
    updates = models.DateTimeField(verbose_name = '업데이트 날짜')

    def __str__(self):
        return f'{self.company.company_name},{self.tag.tag_name}'

