# coding: utf-8

"""
    Literature Graph Service

    Fetch paper and author data from the Semantic Scholar corpus  # noqa: E501

    OpenAPI spec version: 1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from s2cholar.configuration import Configuration


class CitationBatch(object):
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
        'offset': 'int',
        'next': 'int',
        'data': 'list[object]'
    }

    attribute_map = {
        'offset': 'offset',
        'next': 'next',
        'data': 'data'
    }

    def __init__(self, offset=None, next=None, data=None, _configuration=None):  # noqa: E501
        """CitationBatch - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._offset = None
        self._next = None
        self._data = None
        self.discriminator = None

        self.offset = offset
        self.next = next
        if data is not None:
            self.data = data

    @property
    def offset(self):
        """Gets the offset of this CitationBatch.  # noqa: E501

        starting position for this batch  # noqa: E501

        :return: The offset of this CitationBatch.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this CitationBatch.

        starting position for this batch  # noqa: E501

        :param offset: The offset of this CitationBatch.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def next(self):
        """Gets the next of this CitationBatch.  # noqa: E501

        starting position of the next batch  # noqa: E501

        :return: The next of this CitationBatch.  # noqa: E501
        :rtype: int
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this CitationBatch.

        starting position of the next batch  # noqa: E501

        :param next: The next of this CitationBatch.  # noqa: E501
        :type: int
        """
        self._next = next

    @property
    def data(self):
        """Gets the data of this CitationBatch.  # noqa: E501


        :return: The data of this CitationBatch.  # noqa: E501
        :rtype: list[object]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CitationBatch.


        :param data: The data of this CitationBatch.  # noqa: E501
        :type: list[object]
        """

        self._data = data

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
        if issubclass(CitationBatch, dict):
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
        if not isinstance(other, CitationBatch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CitationBatch):
            return True

        return self.to_dict() != other.to_dict()
