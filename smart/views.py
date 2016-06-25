from django.shortcuts import render ,render_to_response
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from smart.models import posts
# Create your views here.



@csrf_exempt
def availability(request):
	if request.method == 'POST':        
		name = string(request.POST['name'])
		availability = string(request.POST['availability'])
		location = string(request.POST['location'])
		time = string(request.POST['time'])
		reason = string(request.POST['reason'])

		user = CustomUser.objects.get(email=email)
		Availability.objects.create(user_id = user.id, availability = availability, location = location, time = time, reason = reason)
		return HttpResponse("Score saved")

	return HttpResponse("Score not saved")

def home(request):
	entries=posts.objects.all()
	return render_to_response('index.html',{'posts':entries})

def onleave(request):
	entries=absent.objects.all()
	return render_to_response('indexa.html',{'absent':entries})
