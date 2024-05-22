from django.urls import path
from eflo import views
from eflo.models import JobListing
#from eflo.views import JobListView

# job_list_view = views.JobListView.as_view(
#     queryset=JobListing.objects.order_by("-job_start"),
#     context_object_name="job_list",
#     template_name="eflo/work_history.html",
# )

job_list_view = views.JobListView.as_view(
    queryset=JobListing.objects.order_by("-job_start"),
    #context_object_name="job_list",
    
    template_name="eflo/work_history.html",
)

urlpatterns = [
    path("", views.front_page, name="front_page"),
    #path('work_history/', views.work_history, name="work_history"),
    path('work_history/', job_list_view, name="work_history"),
    path('interact/', views.interact, name="interact"),
    path('contact/', views.contact, name="contact"),
]