from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class UserModel(AbstractUser):
	class Meta:
		db_table = "user"