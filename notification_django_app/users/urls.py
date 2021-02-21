from django.urls import path

from notification_django_app.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    create_notification_view
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("notification/create/", view=create_notification_view, name="create_notification")
]
