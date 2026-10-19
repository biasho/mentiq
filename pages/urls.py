from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),         # URL: /
    path('flowchart/', views.flowchart, name='flowchart'), # URL: /flowchart/
    path('privacy/', views.privacy, name='privacy'), # URL: /privacy/
    path('terms/', views.terms, name='terms'), # URL: /terms/
    path('sitemap/', views.sitemap, name='sitemap'), # URL: /about/
    path('guide/', views.guide, name='guide'), # URL: /about/
    path('about/', views.about, name='about'), # URL: /about/
    path('about-us/', views.about_us, name='about_us'),   # Trang Về chúng tôi
    path('methodology/', views.methodology, name='methodology'),   # Trang Về chúng tôi
    path('learning-journey/', views.learning_journey, name='learning_journey'),   # Trang Về chúng tôi
    path('features/', views.features, name='features'),   # Trang Về chúng tôi
]