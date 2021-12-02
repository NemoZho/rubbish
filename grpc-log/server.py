import os
import os.path as osp
import sys
BUILD_DIR = osp.join(osp.dirname(osp.abspath(__file__)), "build/service/")
sys.path.insert(0, BUILD_DIR)
import argparse

import grpc
from concurrent import futures
import log_pb2
import log_pb2_grpc
import time
import psutil
import paho.mqtt.client as mqtt
import threading



log = []

def on_message(client, obj, msg):
        order = str(msg.payload)
        order = order[2:-1]
        log.append(int(order))


class LogCalculatorServicer(log_pb2_grpc.LogCalculatorServicer):

    def __init__(self):
        pass

    def Compute(self, request, context):
        response = log_pb2.LogResponse()
        response.data.extend(log)

        return response

def get_log():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(host="localhost",port=1883)
    client.subscribe("order",0)

    try:
        client.loop_forever()
    except KeyboardInterrupt as e:
        pass
t = threading.Thread(target = get_log)
t.start()

if __name__ == "__main__":

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    servicer = LogCalculatorServicer()
    log_pb2_grpc.add_LogCalculatorServicer_to_server(servicer, server)

    try:
        server.add_insecure_port("localhost:8081")
        server.start()
        print("Run gRPC Server at localhost:8081")
        server.wait_for_termination()
    except KeyboardInterrupt:
        pass
