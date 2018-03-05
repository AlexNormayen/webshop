 

from django.shortcuts import render

from ..models import Group






def group_index(request):
    all_group = Group.objects.all()
    return render(request, 'tovar/allgroup.html', locals())
