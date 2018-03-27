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

from dNG.data.subscription.manager import Manager
from dNG.runtime.not_implemented_exception import NotImplementedException

class AbstractSubscribableMixin(object):
    """
The "AbstractSubscribableMixin" provides an abstract interface to access a
subscription mechanism implemented on handler instances.

:author:     direct Netware Group et al.
:copyright:  direct Netware Group - All rights reserved
:package:    pas
:subpackage: subscription
:since:      v1.0.0
:license:    https://www.direct-netware.de/redirect?licenses;gpl
             GNU General Public License 2
    """

    @property
    def subscription_handler(self):
        """
Returns the subscription handler if set.

:return: (object) Subscription handler instance
:since:  v1.0.0
        """

        return Manager.load(self.subscription_handler_class_name, False)
    #

    @property
    def subscription_handler_class_name(self):
        """
Returns the subscription handler class name used for this subscribable
instance.

:return: (str) Subscription handler class name
:since:  v1.0.0
        """

        raise NotImplementedException()
    #
#
