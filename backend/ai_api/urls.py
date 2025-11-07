from django.urls import path
from .views import EnhanceView

urlpatterns = [
    path('enhance/', EnhanceView.as_view()),
]