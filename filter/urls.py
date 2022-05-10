
from django.urls import path
from .views import FilterViews
app_name = "filters"
urlpatterns = [
    path('', FilterViews.as_view()),
]