"""
    Pineonce.io Public API

    Pinecone is a vector database that makes it easy to search and retrieve billions of high-dimensional vectors.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pinecone.core.client.api_client import ApiClient, Endpoint as _Endpoint
from pinecone.core.client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from pinecone.core.client.model.delete_request import DeleteRequest
from pinecone.core.client.model.describe_index_stats_request import DescribeIndexStatsRequest
from pinecone.core.client.model.describe_index_stats_response import DescribeIndexStatsResponse
from pinecone.core.client.model.fetch_response import FetchResponse
from pinecone.core.client.model.query_request import QueryRequest
from pinecone.core.client.model.query_response import QueryResponse
from pinecone.core.client.model.rpc_status import RpcStatus
from pinecone.core.client.model.update_request import UpdateRequest
from pinecone.core.client.model.upsert_request import UpsertRequest
from pinecone.core.client.model.upsert_response import UpsertResponse


class VectorOperationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __delete(
            self,
            delete_request,
            **kwargs
        ):
            """Delete  # noqa: E501

            The `Delete` operation deletes vectors, by id, from a single namespace. You can delete items by their id, from a single namespace.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete(delete_request, async_req=True)
            >>> result = thread.get()

            Args:
                delete_request (DeleteRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['delete_request'] = \
                delete_request
            return self.call_with_http_info(**kwargs)

        self.delete = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/vectors/delete',
                'operation_id': 'delete',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'delete_request',
                ],
                'required': [
                    'delete_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'delete_request':
                        (DeleteRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'delete_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__delete
        )

        def __delete1(
            self,
            **kwargs
        ):
            """Delete  # noqa: E501

            The `Delete` operation deletes vectors, by id, from a single namespace. You can delete items by their id, from a single namespace.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete1(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                ids ([str]): Vectors to delete.. [optional]
                delete_all (bool): This indicates that all vectors in the index namespace should be deleted.. [optional] if omitted the server will use the default value of False
                namespace (str): The namespace to delete vectors from, if applicable.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.delete1 = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/vectors/delete',
                'operation_id': 'delete1',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'ids',
                    'delete_all',
                    'namespace',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'ids':
                        ([str],),
                    'delete_all':
                        (bool,),
                    'namespace':
                        (str,),
                },
                'attribute_map': {
                    'ids': 'ids',
                    'delete_all': 'deleteAll',
                    'namespace': 'namespace',
                },
                'location_map': {
                    'ids': 'query',
                    'delete_all': 'query',
                    'namespace': 'query',
                },
                'collection_format_map': {
                    'ids': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete1
        )

        def __describe_index_stats(
            self,
            describe_index_stats_request,
            **kwargs
        ):
            """DescribeIndexStats  # noqa: E501

            The `DescribeIndexStats` operation returns statistics about the index's contents, including the vector count per namespace, the number of dimensions, and the index fullness. The index fullness result  may be inaccurate during pod resizing; to get the status of a pod resizing process, use [`describe_index`](https://www.pinecone.io/docs/api/operation/describe_index/).  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.describe_index_stats(describe_index_stats_request, async_req=True)
            >>> result = thread.get()

            Args:
                describe_index_stats_request (DescribeIndexStatsRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                DescribeIndexStatsResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['describe_index_stats_request'] = \
                describe_index_stats_request
            return self.call_with_http_info(**kwargs)

        self.describe_index_stats = _Endpoint(
            settings={
                'response_type': (DescribeIndexStatsResponse,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/describe_index_stats',
                'operation_id': 'describe_index_stats',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'describe_index_stats_request',
                ],
                'required': [
                    'describe_index_stats_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'describe_index_stats_request':
                        (DescribeIndexStatsRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'describe_index_stats_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__describe_index_stats
        )

        def __describe_index_stats1(
            self,
            **kwargs
        ):
            """DescribeIndexStats  # noqa: E501

            The `DescribeIndexStats` operation returns statistics about the index's contents, including the vector count per namespace, the number of dimensions, and the index fullness. The index fullness result  may be inaccurate during pod resizing; to get the status of a pod resizing process, use [`describe_index`](https://www.pinecone.io/docs/api/operation/describe_index/).  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.describe_index_stats1(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                DescribeIndexStatsResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.describe_index_stats1 = _Endpoint(
            settings={
                'response_type': (DescribeIndexStatsResponse,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/describe_index_stats',
                'operation_id': 'describe_index_stats1',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__describe_index_stats1
        )

        def __fetch(
            self,
            ids,
            **kwargs
        ):
            """Fetch  # noqa: E501

            The `Fetch` operation looks up and returns vectors, by ID, from a single namespace. The returned vectors include the vector data and/or metadata.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.fetch(ids, async_req=True)
            >>> result = thread.get()

            Args:
                ids ([str]): The vector IDs to fetch. Does not accept values containing spaces.

            Keyword Args:
                namespace (str): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                FetchResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['ids'] = \
                ids
            return self.call_with_http_info(**kwargs)

        self.fetch = _Endpoint(
            settings={
                'response_type': (FetchResponse,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/vectors/fetch',
                'operation_id': 'fetch',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ids',
                    'namespace',
                ],
                'required': [
                    'ids',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'ids':
                        ([str],),
                    'namespace':
                        (str,),
                },
                'attribute_map': {
                    'ids': 'ids',
                    'namespace': 'namespace',
                },
                'location_map': {
                    'ids': 'query',
                    'namespace': 'query',
                },
                'collection_format_map': {
                    'ids': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__fetch
        )

        def __query(
            self,
            query_request,
            **kwargs
        ):
            """Query  # noqa: E501

            The `Query` operation searches a namespace, using a query vector. It retrieves the ids of the most similar items in a namespace, along with their similarity scores.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.query(query_request, async_req=True)
            >>> result = thread.get()

            Args:
                query_request (QueryRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                QueryResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['query_request'] = \
                query_request
            return self.call_with_http_info(**kwargs)

        self.query = _Endpoint(
            settings={
                'response_type': (QueryResponse,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/query',
                'operation_id': 'query',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'query_request',
                ],
                'required': [
                    'query_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'query_request':
                        (QueryRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'query_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__query
        )

        def __update(
            self,
            update_request,
            **kwargs
        ):
            """Update  # noqa: E501

            The `Update` operation updates vector in a namespace. If a value is included, it will overwrite the previous value. If a set_metadata is included, the values of the fields specified in it will be added or overwrite the previous value.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update(update_request, async_req=True)
            >>> result = thread.get()

            Args:
                update_request (UpdateRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['update_request'] = \
                update_request
            return self.call_with_http_info(**kwargs)

        self.update = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/vectors/update',
                'operation_id': 'update',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'update_request',
                ],
                'required': [
                    'update_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'update_request':
                        (UpdateRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'update_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update
        )

        def __upsert(
            self,
            upsert_request,
            **kwargs
        ):
            """Upsert  # noqa: E501

            The `Upsert` operation writes vectors into a namespace. If a new value is upserted for an existing vector id, it will overwrite the previous value.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.upsert(upsert_request, async_req=True)
            >>> result = thread.get()

            Args:
                upsert_request (UpsertRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                UpsertResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['upsert_request'] = \
                upsert_request
            return self.call_with_http_info(**kwargs)

        self.upsert = _Endpoint(
            settings={
                'response_type': (UpsertResponse,),
                'auth': [
                    'ApiKeyAuth'
                ],
                'endpoint_path': '/vectors/upsert',
                'operation_id': 'upsert',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'upsert_request',
                ],
                'required': [
                    'upsert_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'upsert_request':
                        (UpsertRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'upsert_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__upsert
        )
