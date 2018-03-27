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

from dNG.data.supports_mixin import SupportsMixin
from dNG.runtime.not_implemented_exception import NotImplementedException
from dNG.runtime.type_exception import TypeException

try: from dNG.data.session.implementation import Implementation as Session
except ImportError: Session = None

class AbstractHandler(SupportsMixin):
    """
An subscription handler is responsible for managing subscriptions and handle
changes.

:author:     direct Netware Group et al.
:copyright:  direct Netware Group - All rights reserved
:package:    pas
:subpackage: subscription
:since:      v1.0.0
:license:    https://www.direct-netware.de/redirect?licenses;gpl
             GNU General Public License 2
    """

    # pylint: disable=unused-argument

    def __init__(self, _id = None):
        """
Constructor __init__(AbstractHandler)

:param _id: Subscription ID

:since: v1.0.0
        """

        SupportsMixin.__init__(self)

        self._id = None
        """
Subscription ID
        """
        self._user_id = None
        """
User ID to work with
        """

        if (_id is not None): self.id = _id
    #

    @property
    def id(self, _id):
        """
Returns the subscription ID.

:return: (int) Subscription ID
:since:  v1.0.0
        """

        return self._id
    #

    @id.setter
    def id(self, _id):
        """
Sets the subscription ID.

:param _id: Subscription ID

:since: v1.0.0
        """

        self._id = _id
    #

    @property
    def is_subscribable(self):
        """
Returns true if the handler allows if the defined user to subscribe.

:return: (bool) True if subscribable for the defined user
:since:  v1.0.0
        """

        return self.is_subscribable_for_user(self.user_id)
    #

    @property
    def is_subscribed(self):
        """
Returns true if the defined user is subscribed to the handler.

:return: (bool) True if subscribed by the defined user
:since:  v1.0.0
        """

        return self.is_subscribed_by_user(self.user_id)
    #

    @property
    def user_id(self):
        """
Returns the user ID currently used for subscription checks if any.

:return: (str) User ID; None otherwise
:since:  v1.0.0
        """

        return self._user_id
    #

    @user_id.setter
    def user_id(self, user_id):
        """
Sets the user ID used for subscription checks.

:param user_id: User ID; None otherwise

:since: v1.0.0
        """

        self._user_id = user_id
    #

    def is_subscribable_for_session_user(self, session):
        """
Returns true if the handler allows the user identified by the given session
to subscribe.

:param session: Session instance

:return: (bool) True if subscribable for the given session user
:since:  v1.0.0
        """

        return self.is_subscribable_for_user(None if (Session is None) else (Session.get_session_user_id(session)))
    #

    def is_subscribable_for_user(self, user_id):
        """
Returns true if the handler allows the given user ID to subscribe.

:param user_id: User ID

:return: (bool) True if subscribable for the given user ID
:since:  v1.0.0
        """

        raise NotImplementedException()
    #

    def is_subscribed_by_session_user(self, session):
        """
Returns true if the user identified by the given session is subscribed to
the handler.

:param session: Session instance

:return: (bool) True if subscribed by the given session user
:since:  v1.0.0
        """

        return self.is_subscribed_by_user(None if (Session is None) else (Session.get_session_user_id(session)))
    #

    def is_subscribed_by_user(self, user_id):
        """
Returns true if the given user ID is subscribed to the handler.

:param user_id: User ID

:return: (bool) True if subscribed by the given user ID
:since:  v1.0.0
        """

        raise NotImplementedException()
    #

    def set_session(self, session):
        """
Sets the session user ID to work with.

:param session: Session instance

:since: v1.0.0
        """

        if (Session is None): raise TypeException("Given session instance can not be verified")
        self.user_id = Session.get_session_user_id(session)
    #

    def subscribe(self):
        """
Subscribes the defined user.

:since: v1.0.0
        """

        return self.subscribe_user(self.user_id)
    #

    def subscribe_session_user(self, session):
        """
Subscribes the user identified by the given session.

:param session: Session instance

:since: v1.0.0
        """

        self.subscribe_user(None if (Session is None) else (Session.get_session_user_id(session)))
    #

    def subscribe_user(self, user_id):
        """
Subscribes the given user ID.

:param user_id: User ID

:since: v1.0.0
        """

        raise NotImplementedException()
    #

    def unsubscribe(self):
        """
Unsubscribes the defined user.

:since: v1.0.0
        """

        return self.unsubscribe_user(self.user_id)
    #

    def unsubscribe_session_user(self, session):
        """
Unsubscribes the user identified by the given session.

:param session: Session instance

:since: v1.0.0
        """

        self.unsubscribe_user(None if (Session is None) else (Session.get_session_user_id(session)))
    #

    def unsubscribe_user(self, user_id):
        """
Unsubscribes the given user ID.

:param user_id: User ID

:since: v1.0.0
        """

        raise NotImplementedException()
    #
#
