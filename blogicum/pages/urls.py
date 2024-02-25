from django.urls import path
from . import views
# from django.views.generic import TemplateView


app_name = 'pages'

urlpatterns = [
    path('pages/about/', views.about, name='about'),
    path('pages/rules/', views.rules, name='rules'),

    # Удолил views.py, удолил все что связано с views в urls.py здесь
    # Все сломалось.
    # Не до конца понял как обойтись без views.py

    # path('about/', TemplateView.as_view(template_name="about.html")),
    # path('rules/', TemplateView.as_view(template_name="rules.html")),
]
