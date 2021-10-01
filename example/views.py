from django.shortcuts import render, get_object_or_404, redirect

from .models import Application

from .forms import ApplicationForm
from mikoa.models import Region, District

def ajax_load_districts(request):
    if request.is_ajax(): 
        region_id = request.GET.get('region_id')
        if region_id == '':
            districts = District.objects.none()
        else:
            region = get_object_or_404(Region, id=region_id)
            districts = District.objects.filter(region=region).order_by('id')
        context = {
            'districts':districts
        }
        template_name = 'example/districts.html'
        return render(request, template_name, context)


def application(request):
    mikoa  = Region.objects.all()

    if request.method == 'POST':
        form = ApplicationForm(request.POST or None)
        region_id = request.POST.get('region')
        district_id = request.POST.get('district')
        region = get_object_or_404(Region, id=region_id)
        district = get_object_or_404(District, id=district_id)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.region = region.name
            obj.district = district.name
            obj.save()

            return redirect('example:application')
    else:
        form = ApplicationForm()
    context = {
        'form':form,
        'mikoa':mikoa
    }
    template_name = 'example/application.html'

    return render(request, template_name, context)
