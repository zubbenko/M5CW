from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from main.models import Ads
from .serializers import AdsSerializer



@api_view(['GET'])
def ads_detial_api_view(requset,id):
    try:
        item = Ads.objects.get(id=id)
    except Ads.DoesNotExist:
        return Response(data={'error ads not found'},
                        status=status.HTTP_404_NOT_FOUND )


    ads_jsone = AdsSerializer(instance=item).data
    return Response(data=ads_jsone)


@api_view(['GET'])
def ads_list_api_view(request):
    ads_list = Ads.objects.all()
    ads_jsone = AdsSerializer(instance=ads_list, many=True).data
    return Response(data=ads_jsone)




@api_view(['GET'])
def test_api_view(request):
    data_dickt = {
        'text': 'turn off',
        'int': 323424 ,
        'float': 3.14 ,
        'boolean': True ,
        'list': [1,2,3],
    }
    return Response(data=data_dickt, status=status.HTTP_200_OK)


