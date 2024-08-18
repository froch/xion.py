# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ibc.applications.fee.v1 import tx_pb2 as ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the ICS29 Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterPayee = channel.unary_unary(
                '/ibc.applications.fee.v1.Msg/RegisterPayee',
                request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgRegisterPayee.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgRegisterPayeeResponse.FromString,
                _registered_method=True)
        self.RegisterCounterpartyPayee = channel.unary_unary(
                '/ibc.applications.fee.v1.Msg/RegisterCounterpartyPayee',
                request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgRegisterCounterpartyPayee.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgRegisterCounterpartyPayeeResponse.FromString,
                _registered_method=True)
        self.PayPacketFee = channel.unary_unary(
                '/ibc.applications.fee.v1.Msg/PayPacketFee',
                request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgPayPacketFee.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgPayPacketFeeResponse.FromString,
                _registered_method=True)
        self.PayPacketFeeAsync = channel.unary_unary(
                '/ibc.applications.fee.v1.Msg/PayPacketFeeAsync',
                request_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgPayPacketFeeAsync.SerializeToString,
                response_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgPayPacketFeeAsyncResponse.FromString,
                _registered_method=True)


class MsgServicer(object):
    """Msg defines the ICS29 Msg service.
    """

    def RegisterPayee(self, request, context):
        """RegisterPayee defines a rpc handler method for MsgRegisterPayee
        RegisterPayee is called by the relayer on each channelEnd and allows them to set an optional
        payee to which reverse and timeout relayer packet fees will be paid out. The payee should be registered on
        the source chain from which packets originate as this is where fee distribution takes place. This function may be
        called more than once by a relayer, in which case, the latest payee is always used.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterCounterpartyPayee(self, request, context):
        """RegisterCounterpartyPayee defines a rpc handler method for MsgRegisterCounterpartyPayee
        RegisterCounterpartyPayee is called by the relayer on each channelEnd and allows them to specify the counterparty
        payee address before relaying. This ensures they will be properly compensated for forward relaying since
        the destination chain must include the registered counterparty payee address in the acknowledgement. This function
        may be called more than once by a relayer, in which case, the latest counterparty payee address is always used.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PayPacketFee(self, request, context):
        """PayPacketFee defines a rpc handler method for MsgPayPacketFee
        PayPacketFee is an open callback that may be called by any module/user that wishes to escrow funds in order to
        incentivize the relaying of the packet at the next sequence
        NOTE: This method is intended to be used within a multi msg transaction, where the subsequent msg that follows
        initiates the lifecycle of the incentivized packet
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PayPacketFeeAsync(self, request, context):
        """PayPacketFeeAsync defines a rpc handler method for MsgPayPacketFeeAsync
        PayPacketFeeAsync is an open callback that may be called by any module/user that wishes to escrow funds in order to
        incentivize the relaying of a known packet (i.e. at a particular sequence)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterPayee': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterPayee,
                    request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgRegisterPayee.FromString,
                    response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgRegisterPayeeResponse.SerializeToString,
            ),
            'RegisterCounterpartyPayee': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterCounterpartyPayee,
                    request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgRegisterCounterpartyPayee.FromString,
                    response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgRegisterCounterpartyPayeeResponse.SerializeToString,
            ),
            'PayPacketFee': grpc.unary_unary_rpc_method_handler(
                    servicer.PayPacketFee,
                    request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgPayPacketFee.FromString,
                    response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgPayPacketFeeResponse.SerializeToString,
            ),
            'PayPacketFeeAsync': grpc.unary_unary_rpc_method_handler(
                    servicer.PayPacketFeeAsync,
                    request_deserializer=ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgPayPacketFeeAsync.FromString,
                    response_serializer=ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgPayPacketFeeAsyncResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ibc.applications.fee.v1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ibc.applications.fee.v1.Msg', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the ICS29 Msg service.
    """

    @staticmethod
    def RegisterPayee(request,
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
            '/ibc.applications.fee.v1.Msg/RegisterPayee',
            ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgRegisterPayee.SerializeToString,
            ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgRegisterPayeeResponse.FromString,
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
    def RegisterCounterpartyPayee(request,
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
            '/ibc.applications.fee.v1.Msg/RegisterCounterpartyPayee',
            ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgRegisterCounterpartyPayee.SerializeToString,
            ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgRegisterCounterpartyPayeeResponse.FromString,
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
    def PayPacketFee(request,
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
            '/ibc.applications.fee.v1.Msg/PayPacketFee',
            ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgPayPacketFee.SerializeToString,
            ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgPayPacketFeeResponse.FromString,
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
    def PayPacketFeeAsync(request,
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
            '/ibc.applications.fee.v1.Msg/PayPacketFeeAsync',
            ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgPayPacketFeeAsync.SerializeToString,
            ibc_dot_applications_dot_fee_dot_v1_dot_tx__pb2.MsgPayPacketFeeAsyncResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
