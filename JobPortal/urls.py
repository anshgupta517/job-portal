        from django.urls import path, include
        from django.contrib import admin

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('jobs.urls')), # Include app URLs
            # Add other paths like accounts/ if needed
        ]