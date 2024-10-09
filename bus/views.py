
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from requests import request
from . models import Bus,Tyre,Engine

# Create your views here.


def home(request):
    return render(request,'home.html')


def list(request):
    buses = Bus.objects.all()
    context = {'buses':buses}
    return render(request,'list.html',context)

# def delete(request,pk):

#     if request.method == "POST":
#         bus = get_object_or_404(Bus, pk=pk)
#         vehicle_id = bus.vehicle_id
#         print(vehicle_id)
#         tyre = Tyre.objects.filter(vehicle_id=vehicle_id).first()
#         engine = Engine.objects.filter(vehicle_id=vehicle_id).first()

#         tyre.delete()
#         engine.delete()
#         bus.delete()
#         return redirect('list')
    
#     return render(request,'list.html')
        





def delete(self, *args, **kwargs):
    self.object = self.get_object()
    vehicle_id = self.object.vehicle_id  
    print(f"Deleting bus with vehicle_id: {vehicle_id}") 

        # Fetch the associated engine
    engine = Engine.objects.filter(vehicle_id=vehicle_id).first()

        # Check if engine exists before deleting
    if engine:
        engine.delete()  # Safely delete the engine if it exists

        # Now delete the bus
    self.object.delete()
        
        # Redirect to the list page after deletion
    return redirect('list')
