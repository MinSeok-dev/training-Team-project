from django.urls import path
from . import views

urlpatterns = [
    path('', views.psy_test, name="psy_test"),
    path('mind_tree/', views.mind_tree, name="mind_tree"),
    path('secret_diary/', views.secret_diary, name="secret_diary"),
    path('missing_voice/', views.missing_voice, name="missing_voice"),
]
