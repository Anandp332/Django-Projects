from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from empdata.views import emphome,empsignup,empreg,allempv,getempdetail,getresultv,updatedetailv,updategetv,updatev,signinv,signinstatusv,deletev,deletedetail
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'$^',emphome),
    url(r'home/',emphome,name='emphomel'),
    url(r'signup/',empsignup,name='empsignupl'),
    url(r'registeration/',empreg,name='empregprocessl'),
    url(r'allempdetail/',allempv,name='empallviewl'),
    url(r'getempdetail/',getempdetail,name='getempdetall'),
    url(r'getresult/',getresultv,name='getresultl'),
    url(r'updatedetail/',updatedetailv,name='updatedetaill'),
    url(r'updateget/',updategetv,name='updategetl'),
    url(r'update/',updatev,name='updatel'),
    url(r'signin/',signinv,name='signinl'),
    url(r'signinstatus/',signinstatusv,name='signinstatusl'),
    url(r'delete/',deletev,name='deletel'),
    url(r'deletedetail/',deletedetail,name='deletedetaill'),



]
