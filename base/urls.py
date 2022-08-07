from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('client_messages/', views.client_message, name='client_messages'),
    path('client_messages/delete/<int:id>', views.del_client_message, name='del-client-msg'),
    path('donate-card/', views.donate_cards, name='donate_cards'),
    path('donate-card/<int:pk>/successfully_donated/', views.donation_successfull, name='donated_successful_page'),
    path('donated_people/<int:pk>/', views.donated_people_card, name='donated-people-for-card'),
    path('donated_people/<int:pk>/autherization', views.donation_autharization, name='donated-people-autherization'),
    path('donated_people/<int:pk>/<int:card_num>/autherized', views.donation_autherized, name='donation_autherized'),
    path('donated_people/<int:pk>/not_autherized', views.donation_not_autherized, name='donation_not_autherized'),
]
