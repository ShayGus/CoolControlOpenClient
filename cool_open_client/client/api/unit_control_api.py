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


class UnitControlApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def units_unit_id_controls_fan_modes_put(self, body, x_access_token, unit_id, **kwargs):  # noqa: E501
        """set unit fan mode  # noqa: E501

        set unit fan mode  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.units_unit_id_controls_fan_modes_put(body, x_access_token, unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UnitControlFansBody body: (required)
        :param str x_access_token: access token (required)
        :param str unit_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.units_unit_id_controls_fan_modes_put_with_http_info(body, x_access_token, unit_id, **kwargs)  # noqa: E501
        else:
            (data) = self.units_unit_id_controls_fan_modes_put_with_http_info(body, x_access_token, unit_id, **kwargs)  # noqa: E501
            return data

    def units_unit_id_controls_fan_modes_put_with_http_info(self, body, x_access_token, unit_id, **kwargs):  # noqa: E501
        """set unit fan mode  # noqa: E501

        set unit fan mode  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.units_unit_id_controls_fan_modes_put_with_http_info(body, x_access_token, unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UnitControlFansBody body: (required)
        :param str x_access_token: access token (required)
        :param str unit_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_access_token', 'unit_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method units_unit_id_controls_fan_modes_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `units_unit_id_controls_fan_modes_put`")  # noqa: E501
        # verify the required parameter 'x_access_token' is set
        if ('x_access_token' not in params or
                params['x_access_token'] is None):
            raise ValueError("Missing the required parameter `x_access_token` when calling `units_unit_id_controls_fan_modes_put`")  # noqa: E501
        # verify the required parameter 'unit_id' is set
        if ('unit_id' not in params or
                params['unit_id'] is None):
            raise ValueError("Missing the required parameter `unit_id` when calling `units_unit_id_controls_fan_modes_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'unit_id' in params:
            path_params['unitId'] = params['unit_id']  # noqa: E501

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
            '/units/{unitId}/controls/fan-modes', 'PUT',
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

    def units_unit_id_controls_operation_modes_put(self, body, x_access_token, unit_id, **kwargs):  # noqa: E501
        """set unit operation mode  # noqa: E501

        set unit operation mode  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.units_unit_id_controls_operation_modes_put(body, x_access_token, unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UnitControlModesBody body: (required)
        :param str x_access_token: access token (required)
        :param str unit_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.units_unit_id_controls_operation_modes_put_with_http_info(body, x_access_token, unit_id, **kwargs)  # noqa: E501
        else:
            (data) = self.units_unit_id_controls_operation_modes_put_with_http_info(body, x_access_token, unit_id, **kwargs)  # noqa: E501
            return data

    def units_unit_id_controls_operation_modes_put_with_http_info(self, body, x_access_token, unit_id, **kwargs):  # noqa: E501
        """set unit operation mode  # noqa: E501

        set unit operation mode  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.units_unit_id_controls_operation_modes_put_with_http_info(body, x_access_token, unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UnitControlModesBody body: (required)
        :param str x_access_token: access token (required)
        :param str unit_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_access_token', 'unit_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method units_unit_id_controls_operation_modes_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `units_unit_id_controls_operation_modes_put`")  # noqa: E501
        # verify the required parameter 'x_access_token' is set
        if ('x_access_token' not in params or
                params['x_access_token'] is None):
            raise ValueError("Missing the required parameter `x_access_token` when calling `units_unit_id_controls_operation_modes_put`")  # noqa: E501
        # verify the required parameter 'unit_id' is set
        if ('unit_id' not in params or
                params['unit_id'] is None):
            raise ValueError("Missing the required parameter `unit_id` when calling `units_unit_id_controls_operation_modes_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'unit_id' in params:
            path_params['unitId'] = params['unit_id']  # noqa: E501

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
            '/units/{unitId}/controls/operation-modes', 'PUT',
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

    def units_unit_id_controls_operation_statuses_put(self, body, x_access_token, unit_id, **kwargs):  # noqa: E501
        """set unit operation status  # noqa: E501

        set unit operation status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.units_unit_id_controls_operation_statuses_put(body, x_access_token, unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UnitControlSwitchesBody body: (required)
        :param str x_access_token: access token (required)
        :param str unit_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.units_unit_id_controls_operation_statuses_put_with_http_info(body, x_access_token, unit_id, **kwargs)  # noqa: E501
        else:
            (data) = self.units_unit_id_controls_operation_statuses_put_with_http_info(body, x_access_token, unit_id, **kwargs)  # noqa: E501
            return data

    def units_unit_id_controls_operation_statuses_put_with_http_info(self, body, x_access_token, unit_id, **kwargs):  # noqa: E501
        """set unit operation status  # noqa: E501

        set unit operation status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.units_unit_id_controls_operation_statuses_put_with_http_info(body, x_access_token, unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UnitControlSwitchesBody body: (required)
        :param str x_access_token: access token (required)
        :param str unit_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_access_token', 'unit_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method units_unit_id_controls_operation_statuses_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `units_unit_id_controls_operation_statuses_put`")  # noqa: E501
        # verify the required parameter 'x_access_token' is set
        if ('x_access_token' not in params or
                params['x_access_token'] is None):
            raise ValueError("Missing the required parameter `x_access_token` when calling `units_unit_id_controls_operation_statuses_put`")  # noqa: E501
        # verify the required parameter 'unit_id' is set
        if ('unit_id' not in params or
                params['unit_id'] is None):
            raise ValueError("Missing the required parameter `unit_id` when calling `units_unit_id_controls_operation_statuses_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'unit_id' in params:
            path_params['unitId'] = params['unit_id']  # noqa: E501

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
            '/units/{unitId}/controls/operation-statuses', 'PUT',
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

    def units_unit_id_controls_setpoints_put(self, body, x_access_token, unit_id, **kwargs):  # noqa: E501
        """set unit temperature setpoint  # noqa: E501

        set unit temperature setpoint  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.units_unit_id_controls_setpoints_put(body, x_access_token, unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UnitControlSetpointsBody body: (required)
        :param str x_access_token: access token (required)
        :param str unit_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.units_unit_id_controls_setpoints_put_with_http_info(body, x_access_token, unit_id, **kwargs)  # noqa: E501
        else:
            (data) = self.units_unit_id_controls_setpoints_put_with_http_info(body, x_access_token, unit_id, **kwargs)  # noqa: E501
            return data

    def units_unit_id_controls_setpoints_put_with_http_info(self, body, x_access_token, unit_id, **kwargs):  # noqa: E501
        """set unit temperature setpoint  # noqa: E501

        set unit temperature setpoint  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.units_unit_id_controls_setpoints_put_with_http_info(body, x_access_token, unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UnitControlSetpointsBody body: (required)
        :param str x_access_token: access token (required)
        :param str unit_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_access_token', 'unit_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method units_unit_id_controls_setpoints_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `units_unit_id_controls_setpoints_put`")  # noqa: E501
        # verify the required parameter 'x_access_token' is set
        if ('x_access_token' not in params or
                params['x_access_token'] is None):
            raise ValueError("Missing the required parameter `x_access_token` when calling `units_unit_id_controls_setpoints_put`")  # noqa: E501
        # verify the required parameter 'unit_id' is set
        if ('unit_id' not in params or
                params['unit_id'] is None):
            raise ValueError("Missing the required parameter `unit_id` when calling `units_unit_id_controls_setpoints_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'unit_id' in params:
            path_params['unitId'] = params['unit_id']  # noqa: E501

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
            '/units/{unitId}/controls/setpoints', 'PUT',
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

    def units_unit_id_controls_swing_modes_put(self, body, x_access_token, unit_id, **kwargs):  # noqa: E501
        """set unit louver mode  # noqa: E501

        set unit louver mode  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.units_unit_id_controls_swing_modes_put(body, x_access_token, unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UnitControlSwingsBody body: (required)
        :param str x_access_token: access token (required)
        :param str unit_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.units_unit_id_controls_swing_modes_put_with_http_info(body, x_access_token, unit_id, **kwargs)  # noqa: E501
        else:
            (data) = self.units_unit_id_controls_swing_modes_put_with_http_info(body, x_access_token, unit_id, **kwargs)  # noqa: E501
            return data

    def units_unit_id_controls_swing_modes_put_with_http_info(self, body, x_access_token, unit_id, **kwargs):  # noqa: E501
        """set unit louver mode  # noqa: E501

        set unit louver mode  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.units_unit_id_controls_swing_modes_put_with_http_info(body, x_access_token, unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UnitControlSwingsBody body: (required)
        :param str x_access_token: access token (required)
        :param str unit_id: (required)
        :return: Okresponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_access_token', 'unit_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method units_unit_id_controls_swing_modes_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `units_unit_id_controls_swing_modes_put`")  # noqa: E501
        # verify the required parameter 'x_access_token' is set
        if ('x_access_token' not in params or
                params['x_access_token'] is None):
            raise ValueError("Missing the required parameter `x_access_token` when calling `units_unit_id_controls_swing_modes_put`")  # noqa: E501
        # verify the required parameter 'unit_id' is set
        if ('unit_id' not in params or
                params['unit_id'] is None):
            raise ValueError("Missing the required parameter `unit_id` when calling `units_unit_id_controls_swing_modes_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'unit_id' in params:
            path_params['unitId'] = params['unit_id']  # noqa: E501

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
            '/units/{unitId}/controls/swing-modes', 'PUT',
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
