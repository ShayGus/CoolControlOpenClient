# coding: utf-8

"""
    OpenClientCoolAutomationAPI

    Cool platform REST API  # noqa: E501

    OpenAPI spec version: 2.0.1
    Contact: none@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cool_open_client.client.api_client import ApiClient


class SystemControlApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def systems_system_id_controls_modes_put(self, body, origin, referer, x_access_token, system_id, **kwargs):  # noqa: E501
        """set system active operation mode for all units  # noqa: E501

        set system active operation mode for all units  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systems_system_id_controls_modes_put(body, origin, referer, x_access_token, system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SystemControlModesBody body: (required)
        :param str origin: (required)
        :param str referer: (required)
        :param str x_access_token: access token (required)
        :param str system_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systems_system_id_controls_modes_put_with_http_info(body, origin, referer, x_access_token, system_id, **kwargs)  # noqa: E501
        else:
            (data) = self.systems_system_id_controls_modes_put_with_http_info(body, origin, referer, x_access_token, system_id, **kwargs)  # noqa: E501
            return data

    def systems_system_id_controls_modes_put_with_http_info(self, body, origin, referer, x_access_token, system_id, **kwargs):  # noqa: E501
        """set system active operation mode for all units  # noqa: E501

        set system active operation mode for all units  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systems_system_id_controls_modes_put_with_http_info(body, origin, referer, x_access_token, system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SystemControlModesBody body: (required)
        :param str origin: (required)
        :param str referer: (required)
        :param str x_access_token: access token (required)
        :param str system_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'origin', 'referer', 'x_access_token', 'system_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systems_system_id_controls_modes_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `systems_system_id_controls_modes_put`")  # noqa: E501
        # verify the required parameter 'origin' is set
        if ('origin' not in params or
                params['origin'] is None):
            raise ValueError("Missing the required parameter `origin` when calling `systems_system_id_controls_modes_put`")  # noqa: E501
        # verify the required parameter 'referer' is set
        if ('referer' not in params or
                params['referer'] is None):
            raise ValueError("Missing the required parameter `referer` when calling `systems_system_id_controls_modes_put`")  # noqa: E501
        # verify the required parameter 'x_access_token' is set
        if ('x_access_token' not in params or
                params['x_access_token'] is None):
            raise ValueError("Missing the required parameter `x_access_token` when calling `systems_system_id_controls_modes_put`")  # noqa: E501
        # verify the required parameter 'system_id' is set
        if ('system_id' not in params or
                params['system_id'] is None):
            raise ValueError("Missing the required parameter `system_id` when calling `systems_system_id_controls_modes_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'system_id' in params:
            path_params['systemId'] = params['system_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'origin' in params:
            header_params['origin'] = params['origin']  # noqa: E501
        if 'referer' in params:
            header_params['referer'] = params['referer']  # noqa: E501
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
            '/systems/{systemId}/controls/modes', 'PUT',
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

    def systems_system_id_controls_switches_put(self, body, origin, referer, x_access_token, system_id, **kwargs):  # noqa: E501
        """set system active operation status for all units  # noqa: E501

        set system active operation status for all units  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systems_system_id_controls_switches_put(body, origin, referer, x_access_token, system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SystemControlSwitchesBody body: (required)
        :param str origin: (required)
        :param str referer: (required)
        :param str x_access_token: access token (required)
        :param str system_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systems_system_id_controls_switches_put_with_http_info(body, origin, referer, x_access_token, system_id, **kwargs)  # noqa: E501
        else:
            (data) = self.systems_system_id_controls_switches_put_with_http_info(body, origin, referer, x_access_token, system_id, **kwargs)  # noqa: E501
            return data

    def systems_system_id_controls_switches_put_with_http_info(self, body, origin, referer, x_access_token, system_id, **kwargs):  # noqa: E501
        """set system active operation status for all units  # noqa: E501

        set system active operation status for all units  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systems_system_id_controls_switches_put_with_http_info(body, origin, referer, x_access_token, system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SystemControlSwitchesBody body: (required)
        :param str origin: (required)
        :param str referer: (required)
        :param str x_access_token: access token (required)
        :param str system_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'origin', 'referer', 'x_access_token', 'system_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systems_system_id_controls_switches_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `systems_system_id_controls_switches_put`")  # noqa: E501
        # verify the required parameter 'origin' is set
        if ('origin' not in params or
                params['origin'] is None):
            raise ValueError("Missing the required parameter `origin` when calling `systems_system_id_controls_switches_put`")  # noqa: E501
        # verify the required parameter 'referer' is set
        if ('referer' not in params or
                params['referer'] is None):
            raise ValueError("Missing the required parameter `referer` when calling `systems_system_id_controls_switches_put`")  # noqa: E501
        # verify the required parameter 'x_access_token' is set
        if ('x_access_token' not in params or
                params['x_access_token'] is None):
            raise ValueError("Missing the required parameter `x_access_token` when calling `systems_system_id_controls_switches_put`")  # noqa: E501
        # verify the required parameter 'system_id' is set
        if ('system_id' not in params or
                params['system_id'] is None):
            raise ValueError("Missing the required parameter `system_id` when calling `systems_system_id_controls_switches_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'system_id' in params:
            path_params['systemId'] = params['system_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'origin' in params:
            header_params['origin'] = params['origin']  # noqa: E501
        if 'referer' in params:
            header_params['referer'] = params['referer']  # noqa: E501
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
            '/systems/{systemId}/controls/switches', 'PUT',
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
