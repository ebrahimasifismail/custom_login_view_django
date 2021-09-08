from django.contrib.auth.models import UserManager


class MyUserManager(UserManager):

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user



    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        SuperUser = self.create_user(
            email,
            password=password,
        )
        SuperUser.staff = True
        SuperUser.admin = True
        SuperUser.save(using=self._db)
        return SuperUser