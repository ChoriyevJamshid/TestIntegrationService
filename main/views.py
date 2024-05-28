import aiohttp
from rest_framework import generics
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer


class GetEmployeesView(generics.GenericAPIView):
    serializer_class = EmployeeSerializer
    url = "https://google.com/"

    async def get(self, request, *args, **kwargs):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url) as response:
                    response_data = response.json()
                    print(response_data)
        except Exception as e:
            return Response(f"ERROR: {e}")

        emps_data = list()
        for data in response_data:
            emp_data = {
                'id': data.get('id', ''),
                'name': data.get('name', ''),
                'last_name': data.get('last_name', ''),
                'phone': data.get('phone', ''),
                'image_url': data.get('image_url', ''),
            }
            emps_data.append(emp_data)
        serializer = self.get_serializer(data=emps_data, many=True)
        serializer.is_valid()
        return Response(serializer.data)
