from django.urls import path
from libraryapp import views
 
urlpatterns = [

    path("signaction/",views.signaction,name="signaction"),
    path("",views.loginaction,name="loginaction"),
    path("addbook/",views.addbook,name="addbook"),
    path("dashborad/",views.dashborad,name="dashborad"),
    path("update/",views.update,name="update"),
    path("updatebook/",views.updatebook,name="updatebook"),
    path("deletebook/",views.deletebook,name="deletebook"),
    path("registration/",views.registration,name="registration"),
    path("login/",views.login,name="login"),
    path("deletebook/",views.deletebook,name="deletebook"),

]