from .models import ExternalRemedyData, LocationUser
from rest_framework.response import Response
from rest_framework import status
from .services import api_google_search
from rest_framework.views import APIView

class RemedyOrderListView(APIView):
    def get_external_data(self, remedy_name, city, region):
        external_api = api_google_search
        response = external_api.search_google(remedy_name, city, region)

        if response:
            location_data = {"city": city,"region": region}
            for item in response:
                item['location'] = location_data
            return response
        else:
            return None

    def post(self, request, *args, **kwargs):
        data = request.data
        remedy_name = data.get('remedy_name')
        city = data.get('city')
        region = data.get('region')

        if not remedy_name or not city or not region:
            return Response({"message": "Parâmetros 'remedy_name', 'city' e 'region' são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            location_query = LocationUser.objects.filter(city=city, region=region).first()
            if location_query:
                dados = ExternalRemedyData.objects.filter(location__city=location_query.city).all()
                data = [
                    {
                        'title': item.title,
                        'snippet': item.snippet,
                        'link': item.link,
                        'image': item.image,
                        'location': {
                            'city': item.location.city,
                            'region': item.location.region
                        }
                    }
                    for item in dados
                ]
                return Response(data)

            external_data = self.get_external_data(remedy_name, city, region)
            if external_data:

                location, created = LocationUser.objects.get_or_create(city=city,region=region)
                for item in external_data:
                    ExternalRemedyData.objects.create(
                        title=item['title'],
                        snippet=item['snippet'],
                        link=item['link'],
                        image=item['image'],
                        location=location
                    )
                return Response(external_data)
            else:
                return Response({"message": "Erro ao obter dados da API externa"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"message": f"Erro ao processar a solicitação: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)