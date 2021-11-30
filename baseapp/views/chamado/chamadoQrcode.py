# coding=utf-8
from PIL import  Image
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import *
import pyqrcode
from base.settings import  MEDIA_ROOT

class ChamadoQrcodeView(View):
        def get(self,request,**kwargs):
            logo = Image.open(MEDIA_ROOT + '/chamado/imagem/logoti.png')
            get_qrcode(None, str(kwargs.get('pk')), logo, request)
            print(str(kwargs.get('pk')))
            return HttpResponseRedirect((reverse_lazy('chamado-detail', kwargs={"pk": str(kwargs.get('pk'))})))

def get_qrcode(setor,id,imagem,request):
        url = reverse_lazy('chamado-detail', kwargs={"pk": id})
        url = 'http://'+ request.META.get('HTTP_HOST') + str(url)
        url = pyqrcode.QRCode(url)
        url.png(MEDIA_ROOT+'/qrcode/chamado/'+ str(id) +'.png',scale=8)
        im = Image.open(MEDIA_ROOT+'/qrcode/chamado/'+ str(id) +'.png')
        im = im.convert("RGBA")
        logo = imagem
        box = (135,135,235,235)
        im.crop(box)
        region = logo
        region = region.resize((box[2] - box[0], box[3] - box[1]))
        im.paste(region,box)
        im.save(MEDIA_ROOT+'/qrcode/chamado/'+ str(id) +'.png',scale=10)
        return True