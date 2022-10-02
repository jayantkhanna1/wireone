from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Price, DBP, TMF, DAP
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
    data = request.POST['data']
    enabled = request.POST['enabled']
    if enabled == "true":
        enabled = True
    else:
        enabled = False
    DBP.objects.create(data = data, enabled = enabled)
    return Response({"Added":True},status.HTTP_200_OK)

@api_view(["POST"])
def new_DAP(request):
    price = request.POST['price']
    enabled = request.POST['enabled']
    if enabled == "true":
        enabled = True
    else:
        enabled = False
    DAP.objects.create(value = price, enabled = enabled)
    return Response({"Added":True},status.HTTP_200_OK)

# to create new TMF in TMF table
@api_view(["POST"])
def new_TMF(request):
    data = request.POST['data']
    enabled = request.POST['enabled']
    if enabled == "true":
        enabled = True
    else:
        enabled = False
    TMF.objects.create(data = data, enabled = enabled)
    return Response({"Added":True},status.HTTP_200_OK)

# to update DAP
@api_view(["POST"])
def update_dap(request):
    idd = request.POST['id']
    enabled = request.POST['enabled']
    value = request.POST['value']
    if enabled == "true":
        enabled = True
    else:
        enabled = False
    DAP.objects.filter(id = idd).update(value = value, enabled = enabled)
    return Response({"Updated":True},status.HTTP_200_OK)

# to update DBP
@api_view(["POST"])
def update_dbp(request):
    idd = request.POST['id']
    enabled = request.POST['enabled']
    data = request.POST['data']
    if enabled == "true":
        enabled = True
    else:
        enabled = False
    DBP.objects.filter(id = idd).update(data = data, enabled = enabled)
    return Response({"Updated":True},status.HTTP_200_OK)

# to update TMF
@api_view(["POST"])
def update_tmf(request):
    idd = request.POST['id']
    enabled = request.POST['enabled']
    data = request.POST['data']
    if enabled == "true":
        enabled = True
    else:
        enabled = False
    TMF.objects.filter(id = idd).update(data = data, enabled = enabled)
    return Response({"Updated":True},status.HTTP_200_OK)

# to create new price in Price table
@api_view(["POST"])
def new_Price(request):
    total_distance = int(request.POST['total_distance'])
    total_time = int(request.POST['total_time'])
    price = Price.objects.create(Total_distance = total_distance, Total_time = total_time)
    data_to_be_returned = {
        "id":price.id,
        "Total_distance":price.Total_distance,
        "Total_time":price.Total_time,
        "Total_price":price.price,
    }
    return Response({"Updated":data_to_be_returned},status.HTTP_200_OK)

