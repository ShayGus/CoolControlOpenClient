# coding: utf-8

"""
    OpenClientCoolAutomationAPI

    Cool platform REST API  # noqa: E501

    OpenAPI spec version: 1.0.2
    Contact: info@coolautomation.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cool_open_client.client.api_client import ApiClient


class SystemUnitsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def systems_system_id_units_get(self, x_access_token, system_id, **kwargs):  # noqa: E501
        """get system units  # noqa: E501

        get system units  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systems_system_id_units_get(x_access_token, system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_access_token: access token (required)
        :param str system_id: (required)
        :return: UnitsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systems_system_id_units_get_with_http_info(x_access_token, system_id, **kwargs)  # noqa: E501
        else:
            (data) = self.systems_system_id_units_get_with_http_info(x_access_token, system_id, **kwargs)  # noqa: E501
            return data

    def systems_system_id_units_get_with_http_info(self, x_access_token, system_id, **kwargs):  # noqa: E501
        """get system units  # noqa: E501

        get system units  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systems_system_id_units_get_with_http_info(x_access_token, system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_access_token: access token (required)
        :param str system_id: (required)
        :return: UnitsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_access_token', 'system_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systems_system_id_units_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_access_token' is set
        if ('x_access_token' not in params or
                params['x_access_token'] is None):
            raise ValueError("Missing the required parameter `x_access_token` when calling `systems_system_id_units_get`")  # noqa: E501
        # verify the required parameter 'system_id' is set
        if ('system_id' not in params or
                params['system_id'] is None):
            raise ValueError("Missing the required parameter `system_id` when calling `systems_system_id_units_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'system_id' in params:
            path_params['systemId'] = params['system_id']  # noqa: E501

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
            '/systems/{systemId}/units', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UnitsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def systems_system_id_units_unit_id_delete(self, x_access_token, system_id, unit_id, **kwargs):  # noqa: E501
        """remove unit from system  # noqa: E501

        remove unit from system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systems_system_id_units_unit_id_delete(x_access_token, system_id, unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_access_token: access token (required)
        :param str system_id: (required)
        :param str unit_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systems_system_id_units_unit_id_delete_with_http_info(x_access_token, system_id, unit_id, **kwargs)  # noqa: E501
        else:
            (data) = self.systems_system_id_units_unit_id_delete_with_http_info(x_access_token, system_id, unit_id, **kwargs)  # noqa: E501
            return data

    def systems_system_id_units_unit_id_delete_with_http_info(self, x_access_token, system_id, unit_id, **kwargs):  # noqa: E501
        """remove unit from system  # noqa: E501

        remove unit from system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systems_system_id_units_unit_id_delete_with_http_info(x_access_token, system_id, unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_access_token: access token (required)
        :param str system_id: (required)
        :param str unit_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_access_token', 'system_id', 'unit_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systems_system_id_units_unit_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_access_token' is set
        if ('x_access_token' not in params or
                params['x_access_token'] is None):
            raise ValueError("Missing the required parameter `x_access_token` when calling `systems_system_id_units_unit_id_delete`")  # noqa: E501
        # verify the required parameter 'system_id' is set
        if ('system_id' not in params or
                params['system_id'] is None):
            raise ValueError("Missing the required parameter `system_id` when calling `systems_system_id_units_unit_id_delete`")  # noqa: E501
        # verify the required parameter 'unit_id' is set
        if ('unit_id' not in params or
                params['unit_id'] is None):
            raise ValueError("Missing the required parameter `unit_id` when calling `systems_system_id_units_unit_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'system_id' in params:
            path_params['systemId'] = params['system_id']  # noqa: E501
        if 'unit_id' in params:
            path_params['unitId'] = params['unit_id']  # noqa: E501

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
            '/systems/{systemId}/units/{unitId}', 'DELETE',
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

    def systems_system_id_units_unit_id_post(self, x_access_token, system_id, unit_id, **kwargs):  # noqa: E501
        """add unit to system  # noqa: E501

        add unit to system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systems_system_id_units_unit_id_post(x_access_token, system_id, unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_access_token: access token (required)
        :param str system_id: (required)
        :param str unit_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.systems_system_id_units_unit_id_post_with_http_info(x_access_token, system_id, unit_id, **kwargs)  # noqa: E501
        else:
            (data) = self.systems_system_id_units_unit_id_post_with_http_info(x_access_token, system_id, unit_id, **kwargs)  # noqa: E501
            return data

    def systems_system_id_units_unit_id_post_with_http_info(self, x_access_token, system_id, unit_id, **kwargs):  # noqa: E501
        """add unit to system  # noqa: E501

        add unit to system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.systems_system_id_units_unit_id_post_with_http_info(x_access_token, system_id, unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_access_token: access token (required)
        :param str system_id: (required)
        :param str unit_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_access_token', 'system_id', 'unit_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method systems_system_id_units_unit_id_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_access_token' is set
        if ('x_access_token' not in params or
                params['x_access_token'] is None):
            raise ValueError("Missing the required parameter `x_access_token` when calling `systems_system_id_units_unit_id_post`")  # noqa: E501
        # verify the required parameter 'system_id' is set
        if ('system_id' not in params or
                params['system_id'] is None):
            raise ValueError("Missing the required parameter `system_id` when calling `systems_system_id_units_unit_id_post`")  # noqa: E501
        # verify the required parameter 'unit_id' is set
        if ('unit_id' not in params or
                params['unit_id'] is None):
            raise ValueError("Missing the required parameter `unit_id` when calling `systems_system_id_units_unit_id_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'system_id' in params:
            path_params['systemId'] = params['system_id']  # noqa: E501
        if 'unit_id' in params:
            path_params['unitId'] = params['unit_id']  # noqa: E501

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
            '/systems/{systemId}/units/{unitId}', 'POST',
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
