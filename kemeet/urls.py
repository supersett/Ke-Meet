
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('achievement/',include("achievement.urls")),
    #path('apply/',include("apply.urls")),
    #path('review/',include("review.urls")),
    #path('room/',include("room.urls")),
    path('user/',include("user.urls")),
]
