from django.db import models
from user.models import UserModel
from movie.models import Movie


# Create your models here.
class PostModel(models.Model):
    class Meta:
        db_table = "post"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=2, decimal_places=1) #소수점으로 데이터 지정
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

