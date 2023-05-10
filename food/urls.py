from django.urls import path, include
from food.views import *

from django.conf import settings
from django.conf.urls.static import static
urlpatterns= [
    path('',home, name="home"),
    path('login',login,name="login"),
    path('signup', signup, name="signup"),
    path('logout',logout,name = "logout"),
    path('foodmenu/<str:food>', breakfast, name="breakfast"),
    path('foodmenu/<str:food>/addcart/<str:name>/<str:price>/<str:quantity>',addcart),
    path("viewcart",viewcart,name = "view"),

    path('contactus',contactus, name="contactus"),
    path('removeitem/<str:id>',remove),
    
]

urlpatterns= urlpatterns+static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
