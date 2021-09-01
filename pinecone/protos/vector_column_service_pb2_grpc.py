# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pinecone.protos.vector_column_service_pb2 as vector__column__service__pb2

class VectorColumnServiceStub(object):
    """The `VectorColumnService` interface is exposed by Pinecone vector index services.
    The `Upsert` operation is for uploading the data (the vector ids and values) to be indexed.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Upsert = channel.unary_unary(
                '/pinecone_columnar.VectorColumnService/Upsert',
                request_serializer=vector__column__service__pb2.UpsertRequest.SerializeToString,
                response_deserializer=vector__column__service__pb2.UpsertResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/pinecone_columnar.VectorColumnService/Delete',
                request_serializer=vector__column__service__pb2.DeleteRequest.SerializeToString,
                response_deserializer=vector__column__service__pb2.DeleteResponse.FromString,
                )
        self.Fetch = channel.unary_unary(
                '/pinecone_columnar.VectorColumnService/Fetch',
                request_serializer=vector__column__service__pb2.FetchRequest.SerializeToString,
                response_deserializer=vector__column__service__pb2.FetchResponse.FromString,
                )
        self.Query = channel.unary_unary(
                '/pinecone_columnar.VectorColumnService/Query',
                request_serializer=vector__column__service__pb2.QueryRequest.SerializeToString,
                response_deserializer=vector__column__service__pb2.QueryResponse.FromString,
                )
        self.ListNamespaces = channel.unary_unary(
                '/pinecone_columnar.VectorColumnService/ListNamespaces',
                request_serializer=vector__column__service__pb2.ListNamespacesRequest.SerializeToString,
                response_deserializer=vector__column__service__pb2.ListNamespacesResponse.FromString,
                )
        self.Summarize = channel.unary_unary(
                '/pinecone_columnar.VectorColumnService/Summarize',
                request_serializer=vector__column__service__pb2.SummarizeRequest.SerializeToString,
                response_deserializer=vector__column__service__pb2.SummarizeResponse.FromString,
                )


class VectorColumnServiceServicer(object):
    """The `VectorColumnService` interface is exposed by Pinecone vector index services.
    The `Upsert` operation is for uploading the data (the vector ids and values) to be indexed.
    """

    def Upsert(self, request, context):
        """If a user upserts a new value for an existing vector id, it overwrites the previous value.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """The `Delete` operation deletes multiple vectors ids from a single namespace.  
        Specifying `delete_all` will delete all vectors from the default namespace.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Fetch(self, request, context):
        """The `Fetch` operation returns a vector value by id.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Query(self, request, context):
        """The `Query` operation queries the index for the nearest stored vectors to one
        or more query vectors, and returns their ids and/or values.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNamespaces(self, request, context):
        """The `ListNamespaces` operation returns the namespaces that have data in the index.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Summarize(self, request, context):
        """The `Summarize` operation returns summary statistics about the index contents.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VectorColumnServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Upsert': grpc.unary_unary_rpc_method_handler(
                    servicer.Upsert,
                    request_deserializer=vector__column__service__pb2.UpsertRequest.FromString,
                    response_serializer=vector__column__service__pb2.UpsertResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=vector__column__service__pb2.DeleteRequest.FromString,
                    response_serializer=vector__column__service__pb2.DeleteResponse.SerializeToString,
            ),
            'Fetch': grpc.unary_unary_rpc_method_handler(
                    servicer.Fetch,
                    request_deserializer=vector__column__service__pb2.FetchRequest.FromString,
                    response_serializer=vector__column__service__pb2.FetchResponse.SerializeToString,
            ),
            'Query': grpc.unary_unary_rpc_method_handler(
                    servicer.Query,
                    request_deserializer=vector__column__service__pb2.QueryRequest.FromString,
                    response_serializer=vector__column__service__pb2.QueryResponse.SerializeToString,
            ),
            'ListNamespaces': grpc.unary_unary_rpc_method_handler(
                    servicer.ListNamespaces,
                    request_deserializer=vector__column__service__pb2.ListNamespacesRequest.FromString,
                    response_serializer=vector__column__service__pb2.ListNamespacesResponse.SerializeToString,
            ),
            'Summarize': grpc.unary_unary_rpc_method_handler(
                    servicer.Summarize,
                    request_deserializer=vector__column__service__pb2.SummarizeRequest.FromString,
                    response_serializer=vector__column__service__pb2.SummarizeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pinecone_columnar.VectorColumnService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VectorColumnService(object):
    """The `VectorColumnService` interface is exposed by Pinecone vector index services.
    The `Upsert` operation is for uploading the data (the vector ids and values) to be indexed.
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
        return grpc.experimental.unary_unary(request, target, '/pinecone_columnar.VectorColumnService/Upsert',
            vector__column__service__pb2.UpsertRequest.SerializeToString,
            vector__column__service__pb2.UpsertResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/pinecone_columnar.VectorColumnService/Delete',
            vector__column__service__pb2.DeleteRequest.SerializeToString,
            vector__column__service__pb2.DeleteResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/pinecone_columnar.VectorColumnService/Fetch',
            vector__column__service__pb2.FetchRequest.SerializeToString,
            vector__column__service__pb2.FetchResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/pinecone_columnar.VectorColumnService/Query',
            vector__column__service__pb2.QueryRequest.SerializeToString,
            vector__column__service__pb2.QueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListNamespaces(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pinecone_columnar.VectorColumnService/ListNamespaces',
            vector__column__service__pb2.ListNamespacesRequest.SerializeToString,
            vector__column__service__pb2.ListNamespacesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Summarize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pinecone_columnar.VectorColumnService/Summarize',
            vector__column__service__pb2.SummarizeRequest.SerializeToString,
            vector__column__service__pb2.SummarizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
