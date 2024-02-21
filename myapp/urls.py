from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contact', views.contact, name="contact"),
    path('checkoutform', views.checkoutform, name="checkoutform"),
    path('checkout/<int:id>', views.checkout, name="checkout"),
    path('book', views.book, name="book"),
    path('services', views.service, name="service"),
    path('vehicles', views.vehicles, name="vehicles"),
    path('index', views.index, name="index2"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('lgout', views.lgout, name="logout"),
    path('contactfill', views.contactfill, name="contact"),
    path('bookcar', views.bookcar, name="bookcar"),
    path('history',views.history,name='history'),
    path('feedback',views.feedback1,name='feedback'),
    path('feedbackfill',views.feedbackfill,name='feedbackfill')
]