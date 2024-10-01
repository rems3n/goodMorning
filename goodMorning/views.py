# goodMornning/views.py
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import TriggerWorkflowForm
import requests
import json

@ensure_csrf_cookie
def index(request):
    if request.method == 'POST':
        form = TriggerWorkflowForm(request.POST)
        if form.is_valid():
            webhook_url = 'https://remsen.app.n8n.cloud/webhook-test/a89b866e-8e0b-4aa6-889c-5a0291c50fc1'
            
            data = {
                "name": form.cleaned_data['name'],
                "relation": form.cleaned_data['relation'],
                "style": form.cleaned_data['style'],
                "additional_info": form.cleaned_data['additional_info']
            }
            
            try:
                response = requests.post(webhook_url, json=data)
                response_content = json.loads(response.text)
                
                return HttpResponseRedirect(reverse('home'))
                # return JsonResponse({
                #     'success': response.status_code == 200,
                #     'message': "Workflow triggered successfully!" if response.status_code == 200 else f"Unexpected response: {response.status_code}, {response.text}"
                # })
            except requests.RequestException as e:
                return JsonResponse({
                    'success': False,
                    'message': f"Error occurred: {str(e)}"
                })
        else:
            return JsonResponse({
                'success': False,
                'message': "Form validation failed."
            })
    else:
        form = TriggerWorkflowForm()
    
    return render(request, 'index.html', {'form': form})

def page2(request):
    return HttpResponse("This is the second page.")
