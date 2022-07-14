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


class SiteSystemsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def sites_site_id_systems_get(self, x_access_token, site_id, **kwargs):  # noqa: E501
        """get site systems  # noqa: E501

        get site systems  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sites_site_id_systems_get(x_access_token, site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_access_token: access token (required)
        :param str site_id: (required)
        :return: SystemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sites_site_id_systems_get_with_http_info(x_access_token, site_id, **kwargs)  # noqa: E501
        else:
            (data) = self.sites_site_id_systems_get_with_http_info(x_access_token, site_id, **kwargs)  # noqa: E501
            return data

    def sites_site_id_systems_get_with_http_info(self, x_access_token, site_id, **kwargs):  # noqa: E501
        """get site systems  # noqa: E501

        get site systems  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sites_site_id_systems_get_with_http_info(x_access_token, site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_access_token: access token (required)
        :param str site_id: (required)
        :return: SystemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_access_token', 'site_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sites_site_id_systems_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_access_token' is set
        if ('x_access_token' not in params or
                params['x_access_token'] is None):
            raise ValueError("Missing the required parameter `x_access_token` when calling `sites_site_id_systems_get`")  # noqa: E501
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `sites_site_id_systems_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']  # noqa: E501

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
            '/sites/{siteId}/systems', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SystemsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sites_site_id_systems_post(self, body, x_access_token, site_id, **kwargs):  # noqa: E501
        """create site system  # noqa: E501

        create site system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sites_site_id_systems_post(body, x_access_token, site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateSystemRequestBody body: (required)
        :param str x_access_token: access token (required)
        :param str site_id: (required)
        :return: OkresponseWithId
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sites_site_id_systems_post_with_http_info(body, x_access_token, site_id, **kwargs)  # noqa: E501
        else:
            (data) = self.sites_site_id_systems_post_with_http_info(body, x_access_token, site_id, **kwargs)  # noqa: E501
            return data

    def sites_site_id_systems_post_with_http_info(self, body, x_access_token, site_id, **kwargs):  # noqa: E501
        """create site system  # noqa: E501

        create site system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sites_site_id_systems_post_with_http_info(body, x_access_token, site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateSystemRequestBody body: (required)
        :param str x_access_token: access token (required)
        :param str site_id: (required)
        :return: OkresponseWithId
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_access_token', 'site_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sites_site_id_systems_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `sites_site_id_systems_post`")  # noqa: E501
        # verify the required parameter 'x_access_token' is set
        if ('x_access_token' not in params or
                params['x_access_token'] is None):
            raise ValueError("Missing the required parameter `x_access_token` when calling `sites_site_id_systems_post`")  # noqa: E501
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `sites_site_id_systems_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']  # noqa: E501

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
            '/sites/{siteId}/systems', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OkresponseWithId',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
