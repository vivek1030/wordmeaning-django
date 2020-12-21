from django.shortcuts import render,HttpResponse
import http.client
import json
# Create your views here.

def index(request):
    return render(request, 'home.html' ,{})

def search(request):
    # Check if the get request
    if(request.method == 'GET'):
        if(request.GET.get('keyword') == None):
            return HttpResponse('None')
        else:
            keyword = request.GET.get('keyword')
            conn = http.client.HTTPSConnection("mashape-community-urban-dictionary.p.rapidapi.com")
            headers = {
                'x-rapidapi-key': "86d95fddf2msh873bef5d74ca667p15be16jsn6a1e7f6a2793",
                'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
                }
            conn.request("GET", "/define?term="+keyword, headers=headers)
            res = conn.getresponse()
            data = res.read()
            data = json.loads(data.decode('utf-8'))
            context = {
                'data' : data['list']
            }
            return render(request,'result_view.html',context)
    else:
        return HttpResponse('error no search query')
