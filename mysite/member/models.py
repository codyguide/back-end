from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, UserManager as BaseUserManager

class User(AbstractBaseUser):
    username = models.CharField(max_length=60, unique=True)
    email = models.EmailField(max_length=20, unique=False, default="email@test.com")
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    phone = models.CharField(max_length=11, null=True, unique=True)
    img_profile = models.FileField(upload_to='user', blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username + "," + self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Types(models.TextChoices):
        PERSON = "PERSON", "Person"
        ADMINUSER = "ADMINUSER", "AdminUser"

    base_type = Types.PERSON


    type = models.CharField(max_length=10,
                            choices=Types.choices, default=base_type)
    objects = BaseUserManager()

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)

    def create_user(self, email, password,  username):
        if not username:
            raise ValueError("이름을 입력해 주세요")
            if not email:
                raise ValueError("이메일을 입력해 주세요")
        user = self.model(
            username=self.normalize_username(username),
            password=password,
            email=email,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username):
        user = self.create_user(
            username=self.normalize_username(username),
            password=password,
            email=email,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class PersonManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.PERSON)


class AdminUserManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.ADMINUSER)




class Person(User):
    base_type = User.Types.PERSON
    objects = PersonManager()

    class Meta:
        proxy = True


class AdminUser(User):
    base_type = User.Types.ADMINUSER
    objects = AdminUserManager()

    class Meta:
        proxy = True