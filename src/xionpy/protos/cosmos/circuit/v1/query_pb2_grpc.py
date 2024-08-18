# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from cosmos.circuit.v1 import query_pb2 as cosmos_dot_circuit_dot_v1_dot_query__pb2


class QueryStub(object):
    """Query defines the circuit gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Account = channel.unary_unary(
                '/cosmos.circuit.v1.Query/Account',
                request_serializer=cosmos_dot_circuit_dot_v1_dot_query__pb2.QueryAccountRequest.SerializeToString,
                response_deserializer=cosmos_dot_circuit_dot_v1_dot_query__pb2.AccountResponse.FromString,
                _registered_method=True)
        self.Accounts = channel.unary_unary(
                '/cosmos.circuit.v1.Query/Accounts',
                request_serializer=cosmos_dot_circuit_dot_v1_dot_query__pb2.QueryAccountsRequest.SerializeToString,
                response_deserializer=cosmos_dot_circuit_dot_v1_dot_query__pb2.AccountsResponse.FromString,
                _registered_method=True)
        self.DisabledList = channel.unary_unary(
                '/cosmos.circuit.v1.Query/DisabledList',
                request_serializer=cosmos_dot_circuit_dot_v1_dot_query__pb2.QueryDisabledListRequest.SerializeToString,
                response_deserializer=cosmos_dot_circuit_dot_v1_dot_query__pb2.DisabledListResponse.FromString,
                _registered_method=True)


class QueryServicer(object):
    """Query defines the circuit gRPC querier service.
    """

    def Account(self, request, context):
        """Account returns account permissions.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Accounts(self, request, context):
        """Account returns account permissions.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisabledList(self, request, context):
        """DisabledList returns a list of disabled message urls
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Account': grpc.unary_unary_rpc_method_handler(
                    servicer.Account,
                    request_deserializer=cosmos_dot_circuit_dot_v1_dot_query__pb2.QueryAccountRequest.FromString,
                    response_serializer=cosmos_dot_circuit_dot_v1_dot_query__pb2.AccountResponse.SerializeToString,
            ),
            'Accounts': grpc.unary_unary_rpc_method_handler(
                    servicer.Accounts,
                    request_deserializer=cosmos_dot_circuit_dot_v1_dot_query__pb2.QueryAccountsRequest.FromString,
                    response_serializer=cosmos_dot_circuit_dot_v1_dot_query__pb2.AccountsResponse.SerializeToString,
            ),
            'DisabledList': grpc.unary_unary_rpc_method_handler(
                    servicer.DisabledList,
                    request_deserializer=cosmos_dot_circuit_dot_v1_dot_query__pb2.QueryDisabledListRequest.FromString,
                    response_serializer=cosmos_dot_circuit_dot_v1_dot_query__pb2.DisabledListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cosmos.circuit.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('cosmos.circuit.v1.Query', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the circuit gRPC querier service.
    """

    @staticmethod
    def Account(request,
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
            '/cosmos.circuit.v1.Query/Account',
            cosmos_dot_circuit_dot_v1_dot_query__pb2.QueryAccountRequest.SerializeToString,
            cosmos_dot_circuit_dot_v1_dot_query__pb2.AccountResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Accounts(request,
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
            '/cosmos.circuit.v1.Query/Accounts',
            cosmos_dot_circuit_dot_v1_dot_query__pb2.QueryAccountsRequest.SerializeToString,
            cosmos_dot_circuit_dot_v1_dot_query__pb2.AccountsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DisabledList(request,
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
            '/cosmos.circuit.v1.Query/DisabledList',
            cosmos_dot_circuit_dot_v1_dot_query__pb2.QueryDisabledListRequest.SerializeToString,
            cosmos_dot_circuit_dot_v1_dot_query__pb2.DisabledListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
