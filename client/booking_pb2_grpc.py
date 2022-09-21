# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import base_pb2 as base__pb2
import booking_pb2 as booking__pb2
import user_pb2 as user__pb2


class BookingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllBookings = channel.unary_stream(
                '/Booking/GetAllBookings',
                request_serializer=base__pb2.Empty.SerializeToString,
                response_deserializer=booking__pb2.BookingData.FromString,
                )
        self.GetBookingByUserId = channel.unary_unary(
                '/Booking/GetBookingByUserId',
                request_serializer=user__pb2.UserID.SerializeToString,
                response_deserializer=booking__pb2.BookingData.FromString,
                )


class BookingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAllBookings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBookingByUserId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAllBookings': grpc.unary_stream_rpc_method_handler(
                    servicer.GetAllBookings,
                    request_deserializer=base__pb2.Empty.FromString,
                    response_serializer=booking__pb2.BookingData.SerializeToString,
            ),
            'GetBookingByUserId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBookingByUserId,
                    request_deserializer=user__pb2.UserID.FromString,
                    response_serializer=booking__pb2.BookingData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Booking', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Booking(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAllBookings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Booking/GetAllBookings',
            base__pb2.Empty.SerializeToString,
            booking__pb2.BookingData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBookingByUserId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Booking/GetBookingByUserId',
            user__pb2.UserID.SerializeToString,
            booking__pb2.BookingData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
