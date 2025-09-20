import factory
from apis.models import NormalModel


class NormalModelFactory(factory.django.DjangoModelFactory):

    user_id = factory.Faker("random_int", min=1, max=10)
    name = factory.Faker("word")
    age = factory.Faker("random_int", min=1, max=10)

    class Meta:
        model = NormalModel
