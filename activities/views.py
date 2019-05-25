from django.shortcuts import get_object_or_404, render
from .models import Activity

# Create your views here.

def index(request):
    activities = Activity.objects.order_by('-id').reverse()
    context = {
        'activities' : activities
    }
    return render(request, 'recent_activities/activities.html', context)

def activity(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    context = {
        'activity' : activity
    }
    return render(request, 'recent_activities/activity.html', context)
