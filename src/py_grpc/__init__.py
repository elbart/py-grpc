from concurrent import futures
import time
import sys

import grpc

import commands_pb2 as commands_messages
import commands_pb2_grpc as commands_services


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class CommandsService(commands_services.CommandsServicer):

    def GetCommands(self, request, context):
        command = commands_messages.Command(id="abc", verb="GET", path="/commands", name="Get Commands")
        yield commands_messages.GetCommandsResult(command=command)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    commands_services.add_CommandsServicer_to_server(CommandsService(), server)
    server.add_insecure_port('127.0.0.1:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


def main():
    serve()


def client_run():
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
