from django.urls import path

from . import views

urlpatterns = [
        path("", views.Step1.as_view(), name="step1"),
        path("step2/", views.Step2.as_view(), name="step2"),
        path("step3/", views.Step3.as_view(), name="step3"),
        path("step4/", views.Step4.as_view(), name="step4"),
        path("step5/", views.Step5.as_view(), name="step5"),
        ]
