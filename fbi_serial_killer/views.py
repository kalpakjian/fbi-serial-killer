from django.shortcuts import render
from .models import Capture

def capture_list(request):
    captures = Capture.objects.select_related('agent', 'serial_killer').all()
    return render(request, 'fbi_serial_killer/capture_list.html', {'captures': captures})