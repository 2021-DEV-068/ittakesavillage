from django.urls import path, include

urlpatterns = [
    path('', include('website.views.parent.urls', namespace='parent')),
    path('pro/', include('website.views.caregiver.urls', namespace='caregiver')),
]
