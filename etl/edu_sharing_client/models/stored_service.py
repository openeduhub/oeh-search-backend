# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class StoredService(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'url': 'str',
        'icon': 'str',
        'logo': 'str',
        'in_language': 'str',
        'type': 'str',
        'description': 'str',
        'audience': 'list[Audience]',
        'provider': 'Provider',
        'start_date': 'str',
        'interfaces': 'list[Interface]',
        'about': 'list[str]',
        'id': 'str',
        'is_accessible_for_free': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'url': 'url',
        'icon': 'icon',
        'logo': 'logo',
        'in_language': 'inLanguage',
        'type': 'type',
        'description': 'description',
        'audience': 'audience',
        'provider': 'provider',
        'start_date': 'startDate',
        'interfaces': 'interfaces',
        'about': 'about',
        'id': 'id',
        'is_accessible_for_free': 'isAccessibleForFree'
    }

    def __init__(self, name=None, url=None, icon=None, logo=None, in_language=None, type=None, description=None, audience=None, provider=None, start_date=None, interfaces=None, about=None, id=None, is_accessible_for_free=False):  # noqa: E501
        """StoredService - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._url = None
        self._icon = None
        self._logo = None
        self._in_language = None
        self._type = None
        self._description = None
        self._audience = None
        self._provider = None
        self._start_date = None
        self._interfaces = None
        self._about = None
        self._id = None
        self._is_accessible_for_free = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        if icon is not None:
            self.icon = icon
        if logo is not None:
            self.logo = logo
        if in_language is not None:
            self.in_language = in_language
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if audience is not None:
            self.audience = audience
        if provider is not None:
            self.provider = provider
        if start_date is not None:
            self.start_date = start_date
        if interfaces is not None:
            self.interfaces = interfaces
        if about is not None:
            self.about = about
        if id is not None:
            self.id = id
        if is_accessible_for_free is not None:
            self.is_accessible_for_free = is_accessible_for_free

    @property
    def name(self):
        """Gets the name of this StoredService.  # noqa: E501


        :return: The name of this StoredService.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StoredService.


        :param name: The name of this StoredService.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this StoredService.  # noqa: E501


        :return: The url of this StoredService.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this StoredService.


        :param url: The url of this StoredService.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def icon(self):
        """Gets the icon of this StoredService.  # noqa: E501


        :return: The icon of this StoredService.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this StoredService.


        :param icon: The icon of this StoredService.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def logo(self):
        """Gets the logo of this StoredService.  # noqa: E501


        :return: The logo of this StoredService.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this StoredService.


        :param logo: The logo of this StoredService.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def in_language(self):
        """Gets the in_language of this StoredService.  # noqa: E501


        :return: The in_language of this StoredService.  # noqa: E501
        :rtype: str
        """
        return self._in_language

    @in_language.setter
    def in_language(self, in_language):
        """Sets the in_language of this StoredService.


        :param in_language: The in_language of this StoredService.  # noqa: E501
        :type: str
        """

        self._in_language = in_language

    @property
    def type(self):
        """Gets the type of this StoredService.  # noqa: E501


        :return: The type of this StoredService.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StoredService.


        :param type: The type of this StoredService.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def description(self):
        """Gets the description of this StoredService.  # noqa: E501


        :return: The description of this StoredService.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StoredService.


        :param description: The description of this StoredService.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def audience(self):
        """Gets the audience of this StoredService.  # noqa: E501


        :return: The audience of this StoredService.  # noqa: E501
        :rtype: list[Audience]
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """Sets the audience of this StoredService.


        :param audience: The audience of this StoredService.  # noqa: E501
        :type: list[Audience]
        """

        self._audience = audience

    @property
    def provider(self):
        """Gets the provider of this StoredService.  # noqa: E501


        :return: The provider of this StoredService.  # noqa: E501
        :rtype: Provider
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this StoredService.


        :param provider: The provider of this StoredService.  # noqa: E501
        :type: Provider
        """

        self._provider = provider

    @property
    def start_date(self):
        """Gets the start_date of this StoredService.  # noqa: E501


        :return: The start_date of this StoredService.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this StoredService.


        :param start_date: The start_date of this StoredService.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def interfaces(self):
        """Gets the interfaces of this StoredService.  # noqa: E501


        :return: The interfaces of this StoredService.  # noqa: E501
        :rtype: list[Interface]
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces):
        """Sets the interfaces of this StoredService.


        :param interfaces: The interfaces of this StoredService.  # noqa: E501
        :type: list[Interface]
        """

        self._interfaces = interfaces

    @property
    def about(self):
        """Gets the about of this StoredService.  # noqa: E501


        :return: The about of this StoredService.  # noqa: E501
        :rtype: list[str]
        """
        return self._about

    @about.setter
    def about(self, about):
        """Sets the about of this StoredService.


        :param about: The about of this StoredService.  # noqa: E501
        :type: list[str]
        """

        self._about = about

    @property
    def id(self):
        """Gets the id of this StoredService.  # noqa: E501


        :return: The id of this StoredService.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StoredService.


        :param id: The id of this StoredService.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_accessible_for_free(self):
        """Gets the is_accessible_for_free of this StoredService.  # noqa: E501


        :return: The is_accessible_for_free of this StoredService.  # noqa: E501
        :rtype: bool
        """
        return self._is_accessible_for_free

    @is_accessible_for_free.setter
    def is_accessible_for_free(self, is_accessible_for_free):
        """Sets the is_accessible_for_free of this StoredService.


        :param is_accessible_for_free: The is_accessible_for_free of this StoredService.  # noqa: E501
        :type: bool
        """

        self._is_accessible_for_free = is_accessible_for_free

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(StoredService, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StoredService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other