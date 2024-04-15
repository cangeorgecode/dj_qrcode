from django.shortcuts import render
import qrcode
import time
from django.conf import settings

def home(request):
    context = {}
    if request.method == 'POST':
        data = request.POST.get('data', '')
        img = qrcode.make(data)
        img_name = 'qr' + str(time.time()) + '.png'
        img.save(str(settings.MEDIA_ROOT) + '/' + img_name)
        return render(request, 'qrcodeapp/home.html', {'img_name': img_name})
    return render(request, 'qrcodeapp/home.html')
