from django.http import FileResponse
from django.http import HttpResponse


def download_file(request):
    filepath = '/home/piloto/git/django_server/files/piloto0618.apk'
    response = HttpResponse()
    response['X-File'] = filepath
    response['Content-Disposition'] = 'attachment; filename=piloto.apk'
    return response

def download_file_response(request):
    response = FileResponse(open('files/piloto0618.apk', 'rb'),
                            content_type='application/force-download')
    return response

def hello_world(request):
    return HttpResponse("Welcome to Loki's world!")
