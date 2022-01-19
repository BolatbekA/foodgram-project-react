from django.contrib.auth.models import BaseUserManager


class AppUserManager(BaseUserManager):
    def create_user(
        self,
        email: str,
        username: str,
        first_name: str,
        last_name: str,
        password: str = None,
    ):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email: str,
        username: str,
        first_name: str,
        last_name: str,
        password: str = None,
    ):
        user = self.create_user(
            email=email,
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
