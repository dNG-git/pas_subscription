# -*- coding: utf-8 -*-

"""
direct PAS
Python Application Services
----------------------------------------------------------------------------
(C) direct Netware Group - All rights reserved
https://www.direct-netware.de/redirect?pas;subscription

The following license agreement remains valid unless any additions or
changes are being made by direct Netware Group in a written form.

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
more details.

You should have received a copy of the GNU General Public License along with
this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
----------------------------------------------------------------------------
https://www.direct-netware.de/redirect?licenses;gpl
----------------------------------------------------------------------------
#echo(pasSubscriptionVersion)#
#echo(__FILEPATH__)#
"""

# pylint: disable=import-error, no-name-in-module

import re

try: from urllib.parse import urlsplit
except ImportError: from urlparse import urlsplit

from dNG.runtime.named_loader import NamedLoader
from dNG.runtime.type_exception import TypeException

from .abstract_handler import AbstractHandler

class Manager(object):
    """
The subscription "Manager" class should be used to load the corresponding
subscription handler for a given subscription ID.

:author:     direct Netware Group et al.
:copyright:  direct Netware Group - All rights reserved
:package:    pas
:subpackage: subscription
:since:      v1.0.0
:license:    https://www.direct-netware.de/redirect?licenses;gpl
             GNU General Public License 2
    """

    @staticmethod
    def load(_id, required = True):
        """
Returns the corresponding subscription handler for a given subscription ID.

:param _id: Subscription ID
:param required: True if exceptions should be thrown if the handler is not
                 defined.

:return: (object) Subscription handler
:since:  v1.0.0
        """

        _return = None

        if (type(_id) is str):
            url_elements = urlsplit(_id)
            handler = NamedLoader.get_camel_case_class_name(url_elements.scheme)

            _return = NamedLoader.get_instance("dNG.data.subscription.{0}Handler".format(handler), required, _id = _id)
            if (required and (not isinstance(_return, AbstractHandler))): raise TypeException("Requested handler is not supported")
        #

        return _return
    #
#
