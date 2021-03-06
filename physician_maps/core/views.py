from django.shortcuts import render
from core.models import Doctor
from django.http import JsonResponse, HttpResponse

# Create your views here.
def mapsearch(request):
    return render(request, 'index.html')

def doctorsearch(request):
    query = request.GET.get('query')
    #this view is designed to serve as an api to grab longitude and latitude from a doctor model id
    doctors = Doctor.objects.filter(name__istartswith= query).order_by('pk')
    if len(doctors) > 0:
        chosen_doc = doctors[0]
        lat, lng = chosen_doc.get_coordinates()
        title = chosen_doc.get_title()
        body = chosen_doc.get_body()
        data = {'latitude': lat, 'longitude': lng, 'title' : title, 'body': body}
    else:
        data = {'latitude': 'fail', 'longitude': 'fail', 'title' : 'fail' , 'body': 'fail'}
    return JsonResponse(data)

import json
def get_doctors(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        docs = Doctor.objects.filter(name__istartswith= q ).order_by('pk')[:10]
        results = []
        for doc in docs:
            doc_json = {}
            doc_json['id'] = doc.pk
            doc_json['label'] = doc.name
            doc_json['value'] = doc.name
            results.append(doc_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

