from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from . import face_distance

import base64
import hashlib

def index(request):
    provided_image = face_distance.get_rand_img()
    context = {"input_image": provided_image.split("/")[-1]}
    return render(request, "FacialExpression/index.html", context)

@csrf_exempt
def process(request):
    if request.method == "POST":
        if "imgBase64" in request.POST:
            prefix = "data:image/jpeg;base64,"
            if request.POST["imgBase64"].startswith(prefix):
                image_bin = base64.b64decode(
                    request.POST["imgBase64"][len(prefix):]
                )
                image_name = "temp-" + hashlib.sha224(image_bin).hexdigest() + ".jpeg"
                with open(image_name, "wb"
                ) as f:
                    f.write(image_bin)
                provided_image = request.POST["provided_image"]
                face_distance.face_dist(image_name, provided_image)
                return HttpResponse(status=201)
        return HttpRseponse(status=422)
    else:
        return HttpResponseNotFound
