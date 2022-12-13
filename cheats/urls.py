from django.urls import path

from cheats.views import CheatListView, CategoryListView, CheatDetailView, CheatCreateView, CheatUpdateView, \
    CategoryCreateView, CheatDeleteView, CategoryDeleteView

app_name = 'cheats'

urlpatterns = [
    path('', CategoryListView.as_view(),  name='categories'),
    path('cheats/', CheatListView.as_view(), name='cheats'),
    path('cheat/<int:pk>/', CheatDetailView.as_view(), name='cheat'),
    path('cheat/create/', CheatCreateView.as_view(), name='cheat_create'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/create/', CategoryCreateView.as_view(), name='category_update'),
    path('cheat/<int:pk>/update/', CheatUpdateView.as_view(), name='cheat_update'),
    path('cheat/<int:pk>/delete/', CheatDeleteView.as_view(), name='cheat_delete'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]