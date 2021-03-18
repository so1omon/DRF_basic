from django.urls import path
from .views import QuestionDetail, QuestionList

urlpatterns = [
    path('all/', QuestionList.as_view()),
    path('<int:id>/', QuestionDetail.as_view())
    # <int:id>값을 QuestionDetail 함수에 넘겨주겠다는 뜻
]
