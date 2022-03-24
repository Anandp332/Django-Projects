from django.conf.urls import url
from doctor.views import doctorv
from patient.views import patientv
from clinic.views import clinicv

urlpatterns = [
    url(r'^$',doctorv,name='doctorl'),
    url(r'^doctor/$',doctorv,name='doctorl'),
    url(r'^clinic/$',clinicv,name='clinicl'),
    url(r'^patient$',patientv,name='patientl'),
]
