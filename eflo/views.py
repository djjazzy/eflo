from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from eflo.forms import LogMessageForm
from eflo.models import LogMessage, JobListing, KeywordList

# Create your views here.

class JobListView(ListView):
    model = JobListing

    def get_context_data(self, **kwargs):
        job_listings = JobListing.objects.all().order_by('-job_start')

        for item in job_listings:
            print(item)


        keyword_listings = KeywordList.objects.all()     
        context = {
            "job_list" : job_listings,
            "keyword_list" : keyword_listings,
        }
        
        return context

def front_page(request):
    return render(request, "eflo/front_page.html")

#def work_history(request):
#    return render(request, "eflo/work_history.html")

def interact(request):
    return render(request, "eflo/interact.html")

def contact(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "eflo/contact.html", {"form": form})
    #return render(request, "eflo/contact.html")