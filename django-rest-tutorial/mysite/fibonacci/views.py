from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
import os
import os.path as osp
import sys
BUILD_DIR = osp.join(osp.dirname(osp.abspath(__file__)), "build/service/")
sys.path.insert(0, BUILD_DIR)
import grpc
import fib_pb2
import fib_pb2_grpc
import log_pb2
import log_pb2_grpc
import json
import time
import psutil
import paho.mqtt.client as mqtt


# Create your views here.
class PostView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        client = mqtt.Client()
        client.connect(host='localhost',port=1883)
        order = json.loads(request.body)["order"]
        client.publish(topic='order',payload=order)
        host = 'localhost:8080'
        with grpc.insecure_channel(host) as channel:
            stub = fib_pb2_grpc.FibCalculatorStub(channel)

            haharequest = fib_pb2.FibRequest()
            haharequest.order = order

            response = stub.Compute(haharequest)
            print(response.value)
            result = response.value
        return Response(data={'result':result}, status=200)
    def get(self, request):
        host = 'localhost:8081'
        with grpc.insecure_channel(host) as channel:
            stub = log_pb2_grpc.LogCalculatorStub(channel)
            
            logrequest = log_pb2.LogRequest()
            
            response = stub.Compute(logrequest)
            print(response.data)
            result = response.data
        return Response(data={'log':result[:]},status = 200)



