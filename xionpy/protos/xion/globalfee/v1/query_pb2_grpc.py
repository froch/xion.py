# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from xion.globalfee.v1 import query_pb2 as xion_dot_globalfee_dot_v1_dot_query__pb2


class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Params = channel.unary_unary(
                '/xion.globalfee.v1.Query/Params',
                request_serializer=xion_dot_globalfee_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString,
                response_deserializer=xion_dot_globalfee_dot_v1_dot_query__pb2.QueryParamsResponse.FromString,
                _registered_method=True)


class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Params(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Params': grpc.unary_unary_rpc_method_handler(
                    servicer.Params,
                    request_deserializer=xion_dot_globalfee_dot_v1_dot_query__pb2.QueryParamsRequest.FromString,
                    response_serializer=xion_dot_globalfee_dot_v1_dot_query__pb2.QueryParamsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'xion.globalfee.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('xion.globalfee.v1.Query', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def Params(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/xion.globalfee.v1.Query/Params',
            xion_dot_globalfee_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString,
            xion_dot_globalfee_dot_v1_dot_query__pb2.QueryParamsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
