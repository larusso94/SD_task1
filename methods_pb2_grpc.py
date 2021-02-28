# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import methods_pb2 as methods__pb2


class workerCreateStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.workerCreate = channel.unary_unary(
                '/workerCreate/workerCreate',
                request_serializer=methods__pb2.createMessage.SerializeToString,
                response_deserializer=methods__pb2.createMessage.FromString,
                )


class workerCreateServicer(object):
    """Missing associated documentation comment in .proto file."""

    def workerCreate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_workerCreateServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'workerCreate': grpc.unary_unary_rpc_method_handler(
                    servicer.workerCreate,
                    request_deserializer=methods__pb2.createMessage.FromString,
                    response_serializer=methods__pb2.createMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'workerCreate', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class workerCreate(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def workerCreate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/workerCreate/workerCreate',
            methods__pb2.createMessage.SerializeToString,
            methods__pb2.createMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class workerDeleteStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.workerDelete = channel.unary_unary(
                '/workerDelete/workerDelete',
                request_serializer=methods__pb2.deleteMessage.SerializeToString,
                response_deserializer=methods__pb2.deleteMessage.FromString,
                )


class workerDeleteServicer(object):
    """Missing associated documentation comment in .proto file."""

    def workerDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_workerDeleteServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'workerDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.workerDelete,
                    request_deserializer=methods__pb2.deleteMessage.FromString,
                    response_serializer=methods__pb2.deleteMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'workerDelete', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class workerDelete(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def workerDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/workerDelete/workerDelete',
            methods__pb2.deleteMessage.SerializeToString,
            methods__pb2.deleteMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class listWorkersStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.listWorkers = channel.unary_unary(
                '/listWorkers/listWorkers',
                request_serializer=methods__pb2.listMessage.SerializeToString,
                response_deserializer=methods__pb2.listMessage.FromString,
                )


class listWorkersServicer(object):
    """Missing associated documentation comment in .proto file."""

    def listWorkers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_listWorkersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'listWorkers': grpc.unary_unary_rpc_method_handler(
                    servicer.listWorkers,
                    request_deserializer=methods__pb2.listMessage.FromString,
                    response_serializer=methods__pb2.listMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'listWorkers', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class listWorkers(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def listWorkers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/listWorkers/listWorkers',
            methods__pb2.listMessage.SerializeToString,
            methods__pb2.listMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class countWordsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.countWords = channel.unary_unary(
                '/countWords/countWords',
                request_serializer=methods__pb2.countMessage.SerializeToString,
                response_deserializer=methods__pb2.countMessage.FromString,
                )


class countWordsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def countWords(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_countWordsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'countWords': grpc.unary_unary_rpc_method_handler(
                    servicer.countWords,
                    request_deserializer=methods__pb2.countMessage.FromString,
                    response_serializer=methods__pb2.countMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'countWords', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class countWords(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def countWords(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/countWords/countWords',
            methods__pb2.countMessage.SerializeToString,
            methods__pb2.countMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class enumerateWordsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.enumerateWords = channel.unary_unary(
                '/enumerateWords/enumerateWords',
                request_serializer=methods__pb2.enumerateMessage.SerializeToString,
                response_deserializer=methods__pb2.enumerateMessage.FromString,
                )


class enumerateWordsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def enumerateWords(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_enumerateWordsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'enumerateWords': grpc.unary_unary_rpc_method_handler(
                    servicer.enumerateWords,
                    request_deserializer=methods__pb2.enumerateMessage.FromString,
                    response_serializer=methods__pb2.enumerateMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'enumerateWords', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class enumerateWords(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def enumerateWords(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/enumerateWords/enumerateWords',
            methods__pb2.enumerateMessage.SerializeToString,
            methods__pb2.enumerateMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)