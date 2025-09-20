from django.urls import path
from .views import NormalView

urlpatterns = [
    path("<int:id>/", NormalView.as_view(), name="apis-get"),
    path("", NormalView.as_view(), name="apis-post"),
]
