__author__ = 'abu'
from rest_framework.routers import DefaultRouter
from stu import views
router=DefaultRouter()
router.register(r'school',views.schoolViewsset,basename='school')
router.register(r'class_t',views.class_tViewsset,basename='class_t')
router.register(r'subject',views.subjectViewsset,basename='subject')
urlpatterns=router.urls

