from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse

from .models import Comment
# Create your views here.
def CreateComment(request):
    if request.method == "POST" and request.is_ajax():
        json_dict = json.loads(request.body.decode('utf-8'))
        comment = json_dict['comment']
        comment = Comment.objects.create(comment = comment)
        data = {"comment": comment.comment, "timestamp": comment.timestamp}
        return JsonResponse(data, content_type="application/json")
    data = {"valid": 0}
    return JsonResponse(data, content_type="application/json")


def HomePage(request):
    return render(request, "home.html", {})
