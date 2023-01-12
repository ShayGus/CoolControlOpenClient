# coding: utf-8

"""
    OpenClientCoolAutomationAPI

    Cool platform REST API  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: info@coolautomation.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cool_open_client.client.api_client import ApiClient


class DeviceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def devices_device_id_delete(self, x_access_token, device_id, **kwargs):  # noqa: E501
        """delete device  # noqa: E501

        delete device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_device_id_delete(x_access_token, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_access_token: access token (required)
        :param str device_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.devices_device_id_delete_with_http_info(x_access_token, device_id, **kwargs)  # noqa: E501
        else:
            (data) = self.devices_device_id_delete_with_http_info(x_access_token, device_id, **kwargs)  # noqa: E501
            return data

    def devices_device_id_delete_with_http_info(self, x_access_token, device_id, **kwargs):  # noqa: E501
        """delete device  # noqa: E501

        delete device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_device_id_delete_with_http_info(x_access_token, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_access_token: access token (required)
        :param str device_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_access_token', 'device_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method devices_device_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_access_token' is set
        if ('x_access_token' not in params or
                params['x_access_token'] is None):
            raise ValueError("Missing the required parameter `x_access_token` when calling `devices_device_id_delete`")  # noqa: E501
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `devices_device_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']  # noqa: E501

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

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/devices/{deviceId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Okresponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def devices_device_id_get(self, x_access_token, device_id, **kwargs):  # noqa: E501
        """get device  # noqa: E501

        get device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_device_id_get(x_access_token, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_access_token: access token (required)
        :param str device_id: (required)
        :return: DeviceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.devices_device_id_get_with_http_info(x_access_token, device_id, **kwargs)  # noqa: E501
        else:
            (data) = self.devices_device_id_get_with_http_info(x_access_token, device_id, **kwargs)  # noqa: E501
            return data

    def devices_device_id_get_with_http_info(self, x_access_token, device_id, **kwargs):  # noqa: E501
        """get device  # noqa: E501

        get device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_device_id_get_with_http_info(x_access_token, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_access_token: access token (required)
        :param str device_id: (required)
        :return: DeviceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_access_token', 'device_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method devices_device_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_access_token' is set
        if ('x_access_token' not in params or
                params['x_access_token'] is None):
            raise ValueError("Missing the required parameter `x_access_token` when calling `devices_device_id_get`")  # noqa: E501
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `devices_device_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']  # noqa: E501

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

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/devices/{deviceId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def devices_device_id_put(self, body, x_access_token, device_id, **kwargs):  # noqa: E501
        """update device  # noqa: E501

        update device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_device_id_put(body, x_access_token, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateDeviceRequestBody body: (required)
        :param str x_access_token: access token (required)
        :param str device_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.devices_device_id_put_with_http_info(body, x_access_token, device_id, **kwargs)  # noqa: E501
        else:
            (data) = self.devices_device_id_put_with_http_info(body, x_access_token, device_id, **kwargs)  # noqa: E501
            return data

    def devices_device_id_put_with_http_info(self, body, x_access_token, device_id, **kwargs):  # noqa: E501
        """update device  # noqa: E501

        update device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_device_id_put_with_http_info(body, x_access_token, device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateDeviceRequestBody body: (required)
        :param str x_access_token: access token (required)
        :param str device_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_access_token', 'device_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method devices_device_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `devices_device_id_put`")  # noqa: E501
        # verify the required parameter 'x_access_token' is set
        if ('x_access_token' not in params or
                params['x_access_token'] is None):
            raise ValueError("Missing the required parameter `x_access_token` when calling `devices_device_id_put`")  # noqa: E501
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `devices_device_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_access_token' in params:
            header_params['x-access-token'] = params['x_access_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/devices/{deviceId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Okresponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
