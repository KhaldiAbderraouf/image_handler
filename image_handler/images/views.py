from django.http import HttpResponse
from django.shortcuts import render
from glob import glob
import sys, os
# Create your views here.
from rest_framework.views import APIView

from image_handler.settings import STATICFILES_DIRS


def choice(i):
    return i % 4


def get_images(path):
    if not path:
        return []
    if len(path.split('/')[-1].split('.')) == 2:
        if path.split('/')[-1].split('.')[-1] in ['png', 'jpg', 'jpeg', 'gif']:
            return [path]
        else:
            return []
    list_images = []
    for dir in glob(path + '/*'):
        if dir != path:
            list_images.extend(get_images(dir))
    return list_images


class Images(APIView):

    def get(self, request, *args, **kwargs):
        template_name = 'images/image_handler.html'
        list_images = []
        root = STATICFILES_DIRS
        for static in root:
            list_images.extend(get_images(static + "/image/"))
        m_list_images = [[], [], [], []]
        list_images.sort()
        for i in range(len(list_images)):
            m_list_images[choice(i)].append(list_images[i].split('static/')[-1])
        return render(request, template_name, {'images': m_list_images})

    def delete(self, request, id, *args, **kwargs):
        # todo: remove the file
        file_name = self.request._request.path.split('images')[1]
        root = STATICFILES_DIRS
        for static in root:
            try:
                os.remove(static + file_name)
            except IOError:
                continue
        return HttpResponse(status=200)

    def post(self, request, *args, **kwargs):
        # todo: modify the file
        return HttpResponse(status=200)
