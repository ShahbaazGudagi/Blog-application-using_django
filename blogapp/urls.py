from django.urls import path
from .import views

app_name="blogapp"

urlpatterns = [
    path('hello/',views.homepage ,name="homepage"),
    path('contact/',views.contact,name="contact"),
    path('login/',views.login_user,name="login_user"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.logout_user,name="logout_user"),
    path('about/',views.about,name="about"),
 
    path('<id>/',views.single_post,name="single_post"),
    path('add_comment/<post_id>/',views.add_comment,name="add_comment"),
]
