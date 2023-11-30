from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
import json
# Serializers
from .serializers import Humedad_Serializer
from utils.database import searchPostgres
from rest_framework.renderers import JSONRenderer
# Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class GetHumedad(viewsets.GenericViewSet):

    # @swagger_auto_schema(
    #     operation_description="Obtiene información de acceso.",
    #     responses={
    #         status.HTTP_200_OK: openapi.Response(description="Responde los datos de acceso",
    #                                              schema=openapi.Schema(
    #                                                  type=openapi.TYPE_ARRAY,
    #                                                  items=openapi.Schema(
    #                                                      type=openapi.TYPE_OBJECT,
    #                                                      properties={
    #                                                          'id': openapi.Schema(type=openapi.TYPE_NUMBER, description="es el id de acceso"),
    #                                                          'nombre': openapi.Schema(type=openapi.TYPE_STRING, description="Es el nombre del acceso"),
                                                             
                                                             
    #                                                      },
    #                                                  ),
    #                                              ),),
    #         status.HTTP_204_NO_CONTENT: openapi.Response(
    #             description="No se encontraron datos para el acceso",
    #             schema=openapi.Schema(
    #                 type=openapi.TYPE_OBJECT,
    #                 properties={
    #                     'msg': openapi.Schema(type=openapi.TYPE_STRING, description="vacio"),
    #                 },
    #             ),
    #         ),
    #     },
    # )
    @action(detail=False, methods=['POST'])
    def humedadMax(self, request):
        data = json.loads(request.body)
        id_estacion = data.get('id_estacion')
        anio=data.get('anio')
        query = f"SELECT * FROM mensuales.vta_9111M WHERE id_estacion = {id_estacion} AND anio = {anio};"

        acceso = searchPostgres(query)
        # Convierte ReturnList en una lista de Python
        python_list = [Humedad_Serializer(
            instance).data for instance in acceso]
        if len(python_list) == 0:
            data = {
                'success': True,
                'msg': 'vacio',
                'data': python_list,

            }
        else:
            data = {
                'success': True,
                'msg': 'ok',
                'data': python_list,

            }

        return Response(data, status=status.HTTP_200_OK)



