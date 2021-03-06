# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import commands_pb2 as commands__pb2


class CommandsStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetCommands = channel.unary_stream(
        '/Commands/GetCommands',
        request_serializer=commands__pb2.GetCommandsRequest.SerializeToString,
        response_deserializer=commands__pb2.GetCommandsResult.FromString,
        )


class CommandsServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetCommands(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CommandsServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetCommands': grpc.unary_stream_rpc_method_handler(
          servicer.GetCommands,
          request_deserializer=commands__pb2.GetCommandsRequest.FromString,
          response_serializer=commands__pb2.GetCommandsResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Commands', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
