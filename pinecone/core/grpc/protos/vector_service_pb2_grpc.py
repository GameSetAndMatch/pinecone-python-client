#
# Copyright (c) 2020-2021 Pinecone Systems Inc. All right reserved.
#

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pinecone.core.grpc.protos.vector_service_pb2 as vector__service__pb2

class VectorServiceStub(object):
    """The `VectorService` interface is exposed by Pinecone's vector index services.
    This service could also be called a `gRPC` service or a `REST`-like api.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Upsert = channel.unary_unary(
                '/VectorService/Upsert',
                request_serializer=vector__service__pb2.UpsertRequest.SerializeToString,
                response_deserializer=vector__service__pb2.UpsertResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/VectorService/Delete',
                request_serializer=vector__service__pb2.DeleteRequest.SerializeToString,
                response_deserializer=vector__service__pb2.DeleteResponse.FromString,
                )
        self.Fetch = channel.unary_unary(
                '/VectorService/Fetch',
                request_serializer=vector__service__pb2.FetchRequest.SerializeToString,
                response_deserializer=vector__service__pb2.FetchResponse.FromString,
                )
        self.Query = channel.unary_unary(
                '/VectorService/Query',
                request_serializer=vector__service__pb2.QueryRequest.SerializeToString,
                response_deserializer=vector__service__pb2.QueryResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/VectorService/Update',
                request_serializer=vector__service__pb2.UpdateRequest.SerializeToString,
                response_deserializer=vector__service__pb2.UpdateResponse.FromString,
                )
        self.DescribeIndexStats = channel.unary_unary(
                '/VectorService/DescribeIndexStats',
                request_serializer=vector__service__pb2.DescribeIndexStatsRequest.SerializeToString,
                response_deserializer=vector__service__pb2.DescribeIndexStatsResponse.FromString,
                )


class VectorServiceServicer(object):
    """The `VectorService` interface is exposed by Pinecone's vector index services.
    This service could also be called a `gRPC` service or a `REST`-like api.
    """

    def Upsert(self, request, context):
        """Upsert

        The `Upsert` operation writes vectors into a namespace.
        If a new value is upserted for an existing vector id, it will overwrite the previous value.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete

        The `Delete` operation deletes vectors, by id, from a single namespace.
        You can delete items by their id, from a single namespace.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Fetch(self, request, context):
        """Fetch

        The `Fetch` operation looks up and returns vectors, by id, from a single namespace.
        The returned vectors include the vector data and/or metadata.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Query(self, request, context):
        """Query

        The `Query` operation searches a namespace, using a query vector.
        It retrieves the ids of the most similar items in a namespace, along with their similarity scores.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Update

        The `Update` operation updates vector in a namespace.
        If a value is included, it will overwrite the previous value.
        If a set_metadata is included, the values of the fields specified in it will be added or overwrite the previous value.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeIndexStats(self, request, context):
        """DescribeIndexStats

        The `DescribeIndexStats` operation returns statistics about the index's contents.
        For example: The vector count per namespace and the number of dimensions.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VectorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Upsert': grpc.unary_unary_rpc_method_handler(
                    servicer.Upsert,
                    request_deserializer=vector__service__pb2.UpsertRequest.FromString,
                    response_serializer=vector__service__pb2.UpsertResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=vector__service__pb2.DeleteRequest.FromString,
                    response_serializer=vector__service__pb2.DeleteResponse.SerializeToString,
            ),
            'Fetch': grpc.unary_unary_rpc_method_handler(
                    servicer.Fetch,
                    request_deserializer=vector__service__pb2.FetchRequest.FromString,
                    response_serializer=vector__service__pb2.FetchResponse.SerializeToString,
            ),
            'Query': grpc.unary_unary_rpc_method_handler(
                    servicer.Query,
                    request_deserializer=vector__service__pb2.QueryRequest.FromString,
                    response_serializer=vector__service__pb2.QueryResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=vector__service__pb2.UpdateRequest.FromString,
                    response_serializer=vector__service__pb2.UpdateResponse.SerializeToString,
            ),
            'DescribeIndexStats': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeIndexStats,
                    request_deserializer=vector__service__pb2.DescribeIndexStatsRequest.FromString,
                    response_serializer=vector__service__pb2.DescribeIndexStatsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'VectorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VectorService(object):
    """The `VectorService` interface is exposed by Pinecone's vector index services.
    This service could also be called a `gRPC` service or a `REST`-like api.
    """

    @staticmethod
    def Upsert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/VectorService/Upsert',
            vector__service__pb2.UpsertRequest.SerializeToString,
            vector__service__pb2.UpsertResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/VectorService/Delete',
            vector__service__pb2.DeleteRequest.SerializeToString,
            vector__service__pb2.DeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Fetch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/VectorService/Fetch',
            vector__service__pb2.FetchRequest.SerializeToString,
            vector__service__pb2.FetchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Query(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/VectorService/Query',
            vector__service__pb2.QueryRequest.SerializeToString,
            vector__service__pb2.QueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/VectorService/Update',
            vector__service__pb2.UpdateRequest.SerializeToString,
            vector__service__pb2.UpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeIndexStats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/VectorService/DescribeIndexStats',
            vector__service__pb2.DescribeIndexStatsRequest.SerializeToString,
            vector__service__pb2.DescribeIndexStatsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
