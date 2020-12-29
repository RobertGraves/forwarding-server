from rest_framework.views import APIView


class HookView(APIView)
    def get(self,request,*args,**kwargs):
        print(f"request {request}")
        print(f"request.data {request.data}")
        return Response(data={'data':'goes_here'}status=200)