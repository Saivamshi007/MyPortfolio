from mybio import views
from django.urls import path


urlpatterns=[
    path('',views.index,name=('index')),
    path('backTmsg/',views.backTmsg),
    path('thank_you/',views.thank_you)
    ]