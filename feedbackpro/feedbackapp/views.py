from django.shortcuts import render,redirect
from .forms import FeedbackForm
from .models import FeedbackData
from django.http import HttpResponse
import datetime as dt
time1=dt.datetime.now()
def feedbaclView(request):
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            name=request.POST.get('name','')
            rating=request.POST.get('rating','')
            feedback=request.POST.get('feedback','')
            fb=FeedbackData(
                name=name,
                rating=rating,
                time=time1,
                feedback=feedback
            )
            fb.save()
            return HttpResponse("data inserted")
        else:
            return HttpResponse("data is not inserted")
    else:
        data=FeedbackData.objects.all()
        form=FeedbackForm()
        return render(request,"feedbackfile.html",{'form':form,'data':data})