from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

import base64
import hashlib

def index(request):
    context = {"input_image": "image0.jpg"}
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
                with open(
                        "temp-"
                        + hashlib.sha224(image_bin).hexdigest()
                        + ".jpeg", "wb"
                ) as f:
                    f.write(image_bin)
                return HttpResponse(status=201)
        return HttpRseponse(status=422)
    else:
        return HttpResponseNotFound
