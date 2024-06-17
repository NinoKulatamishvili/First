from django.urls import path
from . import views


urlpatterns = [
    path(' ', views.home), #ფუნქციას ვაკავშირებთ მიასამრთთან
    path('about/', views.about)


]
