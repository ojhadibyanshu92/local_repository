from django.shortcuts import render
from .models import FeedbackData
from .forms import FeedBackForm
from django.http import HttpResponse
import datetime as dt
date1 = dt.datetime.now()

def feedback_view(request):
    if request.method== 'POST':
        fform = FeedBackForm(request.POST)
        if fform.is_valid():
            name= request.POST.get('name')
            rating= request.POST.get('rating')
            feedback= request.POST.get('feedback')

            data= FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date1
            )
            data.save()
            fform = FeedBackForm()
            fdata = FeedbackData.objects.all()
            return render(request, 'feedback.html', {'fform': fform, 'fdata': fdata})
        else:
            return HttpResponse('invalid user data')

    else:
        fform = FeedBackForm()
        fdata= FeedbackData.objects.all()
        return render(request, 'feedback.html', {'fform': fform,'fdata':fdata })