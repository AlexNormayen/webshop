#!/usr/bi/env pethon3
#-*- coding: utf-8 -*-


from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from ..models import Tovar, Tag 


from django.db import connection
from textwrap import dedent

def drop_tag(request, id_tovar, pk_tag):
    with connection.cursor() as cursor:
        cursor.execute(
            dedent('''\
                delete 
                    from tovar_tovar_tags 
                    where tovar_id = %s
                        and tag_id = %s;'''),
            [ id_tovar, pk_tag ]
        )
    return HttpResponseRedirect(reverse('tovar:tags', args=[id_tovar]))




def drop_tag_для_ламеров(request, id_tovar, pk_tag):
    tovar = get_object_or_404(Tovar, pk=id_tovar)
    tag = get_object_or_404(Tag, pk=pk_tag)
    tovar.tags.remove(tag)
    tovar.save()
    return HttpResponseRedirect(reverse('tovar:tags', args=[id_tovar]))

