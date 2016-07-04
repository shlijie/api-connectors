# coding: utf-8

"""
    BitMEX API

    REST API for the BitMEX.com trading platform.<br><br><a href=\"/app/restAPI\">REST Documentation</a><br><a href=\"/app/wsAPI\">Websocket Documentation</a>

    OpenAPI spec version: 1.2.0
    Contact: support@bitmex.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class OrderBookL2(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, symbol=None, id=None, side=None, size=None, price=None):
        """
        OrderBookL2 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'symbol': 'str',
            'id': 'float',
            'side': 'str',
            'size': 'float',
            'price': 'float'
        }

        self.attribute_map = {
            'symbol': 'symbol',
            'id': 'id',
            'side': 'side',
            'size': 'size',
            'price': 'price'
        }

        self._symbol = symbol
        self._id = id
        self._side = side
        self._size = size
        self._price = price

    @property
    def symbol(self):
        """
        Gets the symbol of this OrderBookL2.


        :return: The symbol of this OrderBookL2.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """
        Sets the symbol of this OrderBookL2.


        :param symbol: The symbol of this OrderBookL2.
        :type: str
        """

        self._symbol = symbol

    @property
    def id(self):
        """
        Gets the id of this OrderBookL2.


        :return: The id of this OrderBookL2.
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OrderBookL2.


        :param id: The id of this OrderBookL2.
        :type: float
        """

        self._id = id

    @property
    def side(self):
        """
        Gets the side of this OrderBookL2.


        :return: The side of this OrderBookL2.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """
        Sets the side of this OrderBookL2.


        :param side: The side of this OrderBookL2.
        :type: str
        """

        self._side = side

    @property
    def size(self):
        """
        Gets the size of this OrderBookL2.


        :return: The size of this OrderBookL2.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this OrderBookL2.


        :param size: The size of this OrderBookL2.
        :type: float
        """

        self._size = size

    @property
    def price(self):
        """
        Gets the price of this OrderBookL2.


        :return: The price of this OrderBookL2.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this OrderBookL2.


        :param price: The price of this OrderBookL2.
        :type: float
        """

        self._price = price

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
