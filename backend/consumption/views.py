from django.http import JsonResponse
from .models import Area, Consumption


def consumption_view(request):

    area_name = request.GET.get('area')

    if not area_name:
        return JsonResponse(
            {'error': 'Missing area parameter'},
            status=400
        )

    if len(area_name) > 50:
        return JsonResponse(
            {'error': 'Invalid parameter'},
            status=400
        )

    try:
        area = Area.objects.get(name=area_name)

        latest = Consumption.objects.filter(
            area=area
        ).latest('timestamp')

        return JsonResponse({
            'area': area.name,
            'cpu_usage': latest.cpu_usage,
            'memory_usage': latest.memory_usage,
            'timestamp': latest.timestamp
                .strftime('%Y-%m-%d %H:%M:%S')
        })

    except Area.DoesNotExist:
        return JsonResponse(
            {'error': 'Area not found'},
            status=404
        )

    except Consumption.DoesNotExist:
        return JsonResponse(
            {'error': 'No consumption data'},
            status=404
        )
