from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DashboardValor
from .serializers import DashboardValorSerializer
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib
matplotlib.use('Agg')

class ConsultarDatosAPIView(APIView):
    def get(self, request, *args, **kwargs):
        nombre_campo = request.query_params.get('nombre_campo', '')
        cantidad_valores = int(request.query_params.get('cantidad_valores', 0))

        try:
            queryset = DashboardValor.objects.filter(campo__nombre_de_campo=nombre_campo).order_by('-id')[:cantidad_valores]
            serializer = DashboardValorSerializer(queryset, many=True)

            resultados_json = []

            for row in serializer.data:
                valor_decimal = round(float(row['valor']) / 10, 2) if nombre_campo.lower() == 'humedad' else round(float(row['valor']), 2)
                if valor_decimal >= 0:
                    resultados_json.append({"ID": row['id'], "Valor": valor_decimal})

            x = [item['ID'] for item in resultados_json]
            y = [item['Valor'] for item in resultados_json]

            # Ajustar el tamaño de la gráfica
            plt.figure(figsize=(10, 6))  # Ancho: 10 pulgadas, Alto: 6 pulgadas

            plt.plot(x, y)
            plt.xlabel('ID')
            plt.ylabel('Valor')
            plt.title('Gráfico de Datos')

            image_stream = BytesIO()
            plt.savefig(image_stream, format='png')
            plt.close()

            image_stream.seek(0)
            base64_image = base64.b64encode(image_stream.read()).decode('utf-8')

            return Response({"datos": resultados_json, "grafico_base64": base64_image, "ancho": 10, "alto": 6}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
def post(self, request, *args, **kwargs):
        nombre_campo = request.data.get('nombre_campo', '')
        cantidad_valores = int(request.data.get('cantidad_valores', 0))

        try:
            queryset = DashboardValor.objects.filter(campo__nombre_de_campo=nombre_campo).order_by('-id')[:cantidad_valores]
            serializer = DashboardValorSerializer(queryset, many=True)

            resultados_json = []

            for row in serializer.data:
                valor_decimal = round(float(row['valor']) / 10, 2) if nombre_campo.lower() == 'humedad' else round(float(row['valor']), 2)
                if valor_decimal >= 0:
                    resultados_json.append({"ID": row['id'], "Valor": valor_decimal})

            x = [item['ID'] for item in resultados_json]
            y = [item['Valor'] for item in resultados_json]

            # Ajustar el tamaño de la gráfica
            plt.figure(figsize=(10, 6))  # Ancho: 10 pulgadas, Alto: 6 pulgadas

            plt.plot(x, y)
            plt.xlabel('ID')
            plt.ylabel('Valor')
            plt.title('Gráfico de Datos')

            image_stream = BytesIO()
            plt.savefig(image_stream, format='png')
            plt.close()

            image_stream.seek(0)
            base64_image = base64.b64encode(image_stream.read()).decode('utf-8')

            return Response({"datos": resultados_json, "grafico_base64": base64_image}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
