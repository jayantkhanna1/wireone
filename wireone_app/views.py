from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Price, DBP, TMF
from .serializer import PriceSerializer
from rest_framework import status

# To get all prices
@api_view(["GET"])
def get_price(request):
    price = Price.objects.all()
    serializer = PriceSerializer(price,many=True)
    return Response({"data":serializer.data},status.HTTP_200_OK)

# to get price by id
@api_view(["GET"])
def get_price_by_id(request):
    price = Price.objects.filter(id = request.query_params.get('id'))
    serializer = PriceSerializer(price,many=True)
    return Response({"data":serializer.data},status.HTTP_200_OK)

# to create new DBP in DBP table
@api_view(["POST"])
def new_DBP(request):
    distance = request.POST['distance']
    price = request.POST['price']
    DBP.objects.create(distance = distance, price = price)
    return Response({"Added":True},status.HTTP_200_OK)

# to create new TMF in TMF table
@api_view(["POST"])
def new_TMF(request):
    time = request.POST['time']
    # Price is similar to price in DBP table hence names are kept similar for simplicity
    price = request.POST['factor']
    TMF.objects.create(Time = time, price = price)
    return Response({"Added":True},status.HTTP_200_OK)

# to create new price in Price table
@api_view(["POST"])
def new_Price(request):
    total_distance = int(request.POST['total_distance'])
    total_time = int(request.POST['total_time'])
    dap = int(request.POST['dap'])
    Price.objects.create(Total_distance = total_distance, Total_time = total_time,dap = dap)
    return Response({"Added":True},status.HTTP_200_OK)

