# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import methods_pb2 as methods__pb2


class operationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.operation = channel.unary_unary(
                '/operation/operation',
                request_serializer=methods__pb2.message.SerializeToString,
                response_deserializer=methods__pb2.message.FromString,
                )


class operationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def operation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_operationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'operation': grpc.unary_unary_rpc_method_handler(
                    servicer.operation,
                    request_deserializer=methods__pb2.message.FromString,
                    response_serializer=methods__pb2.message.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'operation', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class operation(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def operation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/operation/operation',
            methods__pb2.message.SerializeToString,
            methods__pb2.message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
