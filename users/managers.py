from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, phone, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser have to be staff")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser have to be superuser")
        self.create_user(email, phone, password, **extra_fields)
