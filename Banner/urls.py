from django.urls import path
from .views import BanneraddViews
app_name = "banner"
urlpatterns = [
    path('', BanneraddViews.as_view()),
]