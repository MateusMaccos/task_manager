from django.contrib import admin
from django.urls import include, path
from todos.views import (
    TodoCreateView,
    TodoListView,
    TodoUpdateView,
    TodoDeleteView,
    TodoCompleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TodoListView.as_view(), name="todo_list"),
    path("create", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),
    path("", include("accounts.urls")),
]
