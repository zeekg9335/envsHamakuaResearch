from django.shortcuts import render
from .models import Hamakua_Data
from .models import Hamakua_After_Disking
from django.http import HttpResponse

# Create your views here.
def about(request):
    return render(request, 'about.html', {'name': 'about'})

def hamakuaData(request):
    labels = []
    data = []
    basinblabels = []
    basinbdata = []
    basinclabels = []
    basincdata = []
    afterDiskLabels = []
    afterDiskData = []
    afterBasinBLabels = []
    afterBasinBData = []
    afterBasinCLabels = []
    afterBasinCData = []
    basinBBiomass = 0
    basinCBiomass=0
    bargraphdata = []
    
    queryset = Hamakua_Data.objects.all()
    for item in queryset:
        labels.append(item.taxonomicResolution)
        data.append(item.specieCount)
        if item.basin == 'B':
            basinblabels.append(item.taxonomicResolution)
            basinbdata.append(item.specieCount)
            basinBBiomass+= item.specieCount

        if item.basin == 'C':
            basinclabels.append(item.taxonomicResolution)
            basincdata.append(item.specieCount)
            basinCBiomass+= item.specieCount
    
    queryset2 = Hamakua_After_Disking.objects.all()
    for item in queryset2:
            afterDiskLabels.append(item.taxonomicResolution)
            afterDiskData.append(item.specieCount)
            if item.basin == 'B':
                afterBasinBLabels.append(item.taxonomicResolution)
                afterBasinBData.append(item.specieCount)
            if item.basin == 'C':
                afterBasinCLabels.append(item.taxonomicResolution)
                afterBasinCData.append(item.specieCount)
    bargraphdata = [basinBBiomass,basinCBiomass]
           


    
    
    context= {
        'labels': labels,
        'data':data,
        'basinblabels': basinblabels,
        'basinbdata':basinbdata,
        'basinclabels':basinclabels,
        'basincdata':basincdata,
        'afterDiskLabels': afterDiskLabels,
        'afterDiskData':afterDiskData,
        'afterBasinBLabels': afterBasinBLabels,
        'afterBasinBData':afterBasinBData,
        'afterBasinCLabels':afterBasinCLabels,
        'afterBasinCData':afterBasinCData,
        'bargraphdata':bargraphdata,
        


    }
        
    return render(request, 'hamakua-data.html',context)

def afterDisking():
    
        afterDiskLabels = []
        afterDiskData = []
        afterBasinBLabels = []
        afterBasinBData = []
        afterBasinCLabels = []
        afterBasinCData = []

        queryset = Hamakua_After_Disking.objects.all()
        for item in queryset:
            afterDiskLabels.append(item.taxonomicResolution)
            afterDiskData.append(item.specieCount)
            if item.basin == 'B':
                afterBasinBLabels.append(item.taxonomicResolution)
                afterBasinBData.append(item.specieCount)
            if item.basin == 'C':
                afterBasinCLabels.append(item.taxonomicResolution)
                afterBasinCData.append(item.specieCount)
        
    
        context= {
            'afterDiskLabels': afterDiskLabels,
            'afterDiskData':afterDiskData,
            'afterBasinBLabels': afterBasinBLabels,
            'afterBasinBData':afterBasinBData,
            'afterBasinCLabels':afterBasinCLabels,
            'afterBasinCData':afterBasinCData,

            }

        return  context
        

       


def hamakuaInformation(request):
    return render(request, 'hamakua-information.html', {'name': 'hamakuaInformation'})

def hamakuaInhabitants(request):
    return render(request, 'hamakua-inhabitants.html', {'name': 'hamakuaInhabitants'})


# These views are for generating charts in the hamakua data page 


