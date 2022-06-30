from django.shortcuts import render

# Create your views here.
import json, re

from django.views   import View
from django.http    import JsonResponse, HttpResponse

from .models        import User

