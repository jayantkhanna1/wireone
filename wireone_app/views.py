from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Price, DBP, TMF
from .serializer import PriceSerializer
from rest_framework import status


@api_view(["GET"])
def get_price(request):
    price = Price.objects.all()
    serializer = PriceSerializer(price,many=True)
    return Response({"data":serializer.data},status.HTTP_200_OK)

@api_view(["GET"])
def get_price_by_id(request):
    price = Price.objects.filter(id = request.query_params.get('id'))
    serializer = PriceSerializer(price,many=True)
    return Response({"data":serializer.data},status.HTTP_200_OK)

@api_view(["POST"])
def new_DBP(request):
    distance = request.POST['distance']
    price = request.POST['price']
    DBP.objects.create(distance = distance, price = price)
    return Response({"Added":True},status.HTTP_200_OK)


@api_view(["POST"])
def new_TMF(request):
    time = request.POST['time']
    price = request.POST['price']
    TMF.objects.create(Time = time, price = price)
    return Response({"Added":True},status.HTTP_200_OK)


@api_view(["POST"])
def new_Price(request):
    total_distance = int(request.POST['total_distance'])
    total_time = int(request.POST['total_time'])
    dap = int(request.POST['dap'])
    Price.objects.create(Total_distance = total_distance, Total_time = total_time,dap = dap)
    return Response({"Added":True},status.HTTP_200_OK)

