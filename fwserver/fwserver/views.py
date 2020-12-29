from rest_framework.views import APIView
from rest_framework.response import Response


class HookView(APIView):
    def post(self,request,*args,**kwargs):
        print(f"request {request}")
        print(f"request.POST {request.POST}")
        print(f"request.data {request.data}")

        typical_data = request.data
        
        """
            format/send hook data to google sheets here
        """


        return Response(status=200)