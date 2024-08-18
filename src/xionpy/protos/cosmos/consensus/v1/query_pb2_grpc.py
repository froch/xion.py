# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from cosmos.consensus.v1 import query_pb2 as cosmos_dot_consensus_dot_v1_dot_query__pb2


class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Params = channel.unary_unary(
                '/cosmos.consensus.v1.Query/Params',
                request_serializer=cosmos_dot_consensus_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString,
                response_deserializer=cosmos_dot_consensus_dot_v1_dot_query__pb2.QueryParamsResponse.FromString,
                _registered_method=True)


class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Params(self, request, context):
        """Params queries the parameters of x/consensus module.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Params': grpc.unary_unary_rpc_method_handler(
                    servicer.Params,
                    request_deserializer=cosmos_dot_consensus_dot_v1_dot_query__pb2.QueryParamsRequest.FromString,
                    response_serializer=cosmos_dot_consensus_dot_v1_dot_query__pb2.QueryParamsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cosmos.consensus.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cosmos.consensus.v1.Query', rpc_method_handlers)


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
            '/cosmos.consensus.v1.Query/Params',
            cosmos_dot_consensus_dot_v1_dot_query__pb2.QueryParamsRequest.SerializeToString,
            cosmos_dot_consensus_dot_v1_dot_query__pb2.QueryParamsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
