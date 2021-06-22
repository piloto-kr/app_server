from django.http import FileResponse
from django.http import HttpResponse


def download_file(request):
    filepath = '/home/piloto/git/app_server/files/piloto.apk'
    response = HttpResponse()
    response['X-File'] = filepath
    response['Content-Disposition'] = 'attachment; filename=piloto.apk'
    return response

def download_file_response(request):
    response = FileResponse(open('files/piloto.apk', 'rb'),
                            content_type='application/force-download')
    return response

def hello_world(request):
    return HttpResponse("Welcome to Loki's world!")
