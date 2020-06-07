from django.urls import path, include
from . import views

urlpatterns = [
    # path('<int:detail_id>/<int:comment_id>/comment_edit', views.comment_edit, name = "comment_edit"),
    path('<int:detail_id>/<int:comment_id>/comment_delete', views.comment_delete, name = "comment_delete"),
    path('<int:detail_id>/<int:addcomment_id>/addcomment_delete', views.addcomment_delete, name = "addcomment_delete"),
    path('<int:detail_id>/<int:comment_id>/comment_subcomment', views.subcomment, name = "subcomment"),
    path('<int:detail_id>', views.detail, name = "detail"),
    path('<int:detail_id>/delete', views.delete, name = "delete"),
    path('<int:detail_id>/edit', views.edit, name = "edit"),
    path('<int:detail_id>/who', views.who, name="who"),
    path('<int:detail_id>/<int:comment_id>/who', views.who_comment, name="who_comment"),
]