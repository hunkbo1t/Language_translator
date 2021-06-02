from .com.google_trans import google_translator
from .com.constant import *
from django.http import HttpResponse
from django.shortcuts import render

trs=google_translator(DEFAULT_SERVICE_URLS)

class gt:
        key : str
        Text : list
