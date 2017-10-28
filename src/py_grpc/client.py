"""
GRPC Client
"""
import sys

import grpc

import grpc_proto.commands_pb2 as commands_messages
import grpc_proto.commands_pb2_grpc as commands_services


def run_client():
    """
    GRPC Client function
    """
    channel = grpc.insecure_channel('localhost:50051')
    try:
        grpc.channel_ready_future(channel).result(timeout=10)
    except grpc.FutureTimeoutError:
        sys.exit('Error connecting to server')
    else:
        stub = commands_services.CommandsStub(channel)
        request = commands_messages.GetCommandsRequest()
        response = stub.GetCommands(request)
        for resp in response:
            print(resp)


def main():
    """
    Main Client entry point
    """
    run_client()
