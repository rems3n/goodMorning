# goodMornning/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .forms import TriggerWorkflowForm
import requests

@csrf_protect
def index(request):
    if request.method == 'POST':
        form = TriggerWorkflowForm(request.POST)
        if form.is_valid():
            # Update the webhook URL to match exactly what's in n8n
            webhook_url = 'https://remsen.app.n8n.cloud/webhook-test/a89b866e-8e0b-4aa6-889c-5a0291c50fc1'
            
            try:
                response = requests.post(webhook_url)
                return HttpResponse(f"Response status: {response.status_code}, Content: {response.text}")
            except requests.RequestException as e:
                return HttpResponse(f"Error occurred: {str(e)}")
    else:
        form = TriggerWorkflowForm()
    
    return render(request, 'index.html', {'form': form})


def page2(request):
    return HttpResponse("This is the second page.")
