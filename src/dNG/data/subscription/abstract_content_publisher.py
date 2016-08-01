# -*- coding: utf-8 -*-
##j## BOF

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

from dNG.data.supports_mixin import SupportsMixin
from dNG.runtime.not_implemented_exception import NotImplementedException

class AbstractContentPublisher(SupportsMixin):
#
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

	def deliver_content(self, title, content, timestamp = None, author_id = None, owner_id = None, owner_type = None):
	#
		"""
Delivers plain text content to subscribers.

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

##j## EOF