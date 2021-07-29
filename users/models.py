from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


DEFAULT_CUSTOMER_ID = 1
DEFAULT_USER_ID = 1

################################################################################
# User
################################################################################
class UserManager(BaseUserManager):
    """ User manager for User that allows users to be created """

    use_in_migrations = True

    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """ User model that extends AbstractBaseUser and PermissionsMixin """

    USER_CATEGORY_CHOICES = (
        ("tilt staff", "tilt staff"),
        ("customer", "customer"),
        ("student", "student"),
    )
    USERNAME_FIELD = "email"

    email = models.EmailField(_("Email Address"),
        unique=True,
        error_messages={
            "unique": _("A user is already registered with this email address"),
        },
    )
    category = models.CharField(
        _("Category"),
        blank=True,
        choices=USER_CATEGORY_CHOICES,
        max_length=20,
    )
    is_active = models.BooleanField(
        _("Active Status"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    is_staff = models.BooleanField(
        _("Staff Status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_superuser = models.BooleanField(
        _("Superuser Status"),
        default=False,
        help_text=_(
            "Designates that this user has all permissions without explicitly assigning them."
        )
    )
    is_test = models.BooleanField(
        _("Test Account"),
        default=False,
        help_text=_(
            "Designates whether we should count this user is a test account."
        )
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.email


################################################################################
# Customer
################################################################################
class Customer(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "customer"
        verbose_name_plural = "customers"

    def __str__(self):
        return self.name


################################################################################
# CustomerUser
################################################################################
class CustomerUser(models.Model):
    user = models.ForeignKey(
        User,
        default=DEFAULT_USER_ID,
        on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        Customer,
        default=DEFAULT_CUSTOMER_ID,
        on_delete=models.CASCADE
    )
    unique_id = models.CharField(max_length=255, blank=True)
    preferred_name = models.CharField(max_length=255, blank=True)
    program = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "customer user"
        verbose_name_plural = "customer users"

    def __str__(self):
        return str(self.user)
