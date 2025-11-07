from django.urls import path
from .views import EnhanceView, HistoryView

urlpatterns = [
    path('enhance/', EnhanceView.as_view()),
    path('history/', HistoryView.as_view()),
]