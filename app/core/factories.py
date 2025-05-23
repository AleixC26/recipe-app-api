from django.utils.timezone import now, get_current_timezone
import factory

from core.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email =  factory.Faker("ascii_safe_email")
    password = factory.django.Password(factory.Faker("password"))
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")

    is_active = True
    last_login = factory.LazyFunction(now)
    date_joined = factory.Faker("past_datetime", tzinfo=get_current_timezone())

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)
