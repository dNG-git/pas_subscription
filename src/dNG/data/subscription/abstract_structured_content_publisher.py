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

from dNG.runtime.not_implemented_exception import NotImplementedException

from .abstract_content_publisher import AbstractContentPublisher

class AbstractStructuredContentPublisher(AbstractContentPublisher):
    """
A content publisher accepts plain text content to be pushed to subscribers.

:author:     direct Netware Group et al.
:copyright:  direct Netware Group - All rights reserved
:package:    pas
:subpackage: subscription
:since:      v0.2.00
:license:    https://www.direct-netware.de/redirect?licenses;gpl
             GNU General Public License 2
    """

    def __init__(self):
        """
Constructor __init__(AbstractStructuredContentPublisher)

:since: v0.2.00
        """

        AbstractContentPublisher.__init__(self)

        self.supported_features['structured_content'] = True
    #

    def deliver_structured_content(self, parent_id, _id, title, content, timestamp = None, author_id = None, owner_id = None, owner_type = None):
        """
Delivers plain text but structured content to subscribers.

:param parent_id: Parent content ID
:param _id: ID of the newly created content
:param title: Content title
:param content: Plain text content
:param timestamp: UNIX publishing timestamp
:param author_id: User ID of the content author
:param owner_id: User ID of the content owner
:param owner_type: Content owner type

:since: v0.2.00
        """

        raise NotImplementedException()
    #
#
