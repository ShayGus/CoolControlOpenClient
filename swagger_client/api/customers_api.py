# coding: utf-8

"""
    v1 rest

    Cool platform REST API  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: info@coolautomation.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class CustomersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def customers_get(self, x_access_token, **kwargs):  # noqa: E501
        """get my customers  # noqa: E501

        Get all the customers caller has permissions to see  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.customers_get(x_access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_access_token: access token (required)
        :return: CustomersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.customers_get_with_http_info(x_access_token, **kwargs)  # noqa: E501
        else:
            (data) = self.customers_get_with_http_info(x_access_token, **kwargs)  # noqa: E501
            return data

    def customers_get_with_http_info(self, x_access_token, **kwargs):  # noqa: E501
        """get my customers  # noqa: E501

        Get all the customers caller has permissions to see  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.customers_get_with_http_info(x_access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_access_token: access token (required)
        :return: CustomersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method customers_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_access_token' is set
        if self.api_client.client_side_validation and ('x_access_token' not in params or
                                                       params['x_access_token'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `x_access_token` when calling `customers_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_access_token' in params:
            header_params['x-access-token'] = params['x_access_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/customers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomersResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
