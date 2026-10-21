from django.urls import path

from complaints.views import SignUpView
from complaints.views import ComplaintListCreateView,ComplaintRetrieveUpdateDeleteView
from complaints.views import UnresolvedComplaintsView,ComplaintCountView,ComplaintStatusSummaryView
from complaints.views import HighCriticalComplaintsView

from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [

    path('user-register/',SignUpView.as_view()),

    path('token/',ObtainAuthToken.as_view()),
    
    path('complaints/',ComplaintListCreateView.as_view()),
    path('complaints/<int:pk>/',ComplaintRetrieveUpdateDeleteView.as_view()),
    path('complaints/unresolved/',UnresolvedComplaintsView.as_view()),
    path('complaints/count/',ComplaintCountView.as_view()),
    path('complaints/status-summary/', ComplaintStatusSummaryView.as_view()),
    path('complaints/high-critical/', HighCriticalComplaintsView.as_view()),
]
