import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "users.User"
        django_get_or_create = ("username",)

    username = "kk6"
