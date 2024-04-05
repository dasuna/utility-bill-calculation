# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class IntentStatisticsList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, assistant_sid, intent_sid):
        """
        Initialize the IntentStatisticsList

        :param Version version: Version that contains the resource
        :param assistant_sid: The unique ID of the parent Assistant.
        :param intent_sid: The unique ID of the Intent associated with this Field.

        :returns: twilio.rest.preview.understand.assistant.intent.intent_statistics.IntentStatisticsList
        :rtype: twilio.rest.preview.understand.assistant.intent.intent_statistics.IntentStatisticsList
        """
        super(IntentStatisticsList, self).__init__(version)

        # Path Solution
        self._solution = {'assistant_sid': assistant_sid, 'intent_sid': intent_sid, }

    def get(self):
        """
        Constructs a IntentStatisticsContext

        :returns: twilio.rest.preview.understand.assistant.intent.intent_statistics.IntentStatisticsContext
        :rtype: twilio.rest.preview.understand.assistant.intent.intent_statistics.IntentStatisticsContext
        """
        return IntentStatisticsContext(
            self._version,
            assistant_sid=self._solution['assistant_sid'],
            intent_sid=self._solution['intent_sid'],
        )

    def __call__(self):
        """
        Constructs a IntentStatisticsContext

        :returns: twilio.rest.preview.understand.assistant.intent.intent_statistics.IntentStatisticsContext
        :rtype: twilio.rest.preview.understand.assistant.intent.intent_statistics.IntentStatisticsContext
        """
        return IntentStatisticsContext(
            self._version,
            assistant_sid=self._solution['assistant_sid'],
            intent_sid=self._solution['intent_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Understand.IntentStatisticsList>'


class IntentStatisticsPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the IntentStatisticsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param assistant_sid: The unique ID of the parent Assistant.
        :param intent_sid: The unique ID of the Intent associated with this Field.

        :returns: twilio.rest.preview.understand.assistant.intent.intent_statistics.IntentStatisticsPage
        :rtype: twilio.rest.preview.understand.assistant.intent.intent_statistics.IntentStatisticsPage
        """
        super(IntentStatisticsPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of IntentStatisticsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.understand.assistant.intent.intent_statistics.IntentStatisticsInstance
        :rtype: twilio.rest.preview.understand.assistant.intent.intent_statistics.IntentStatisticsInstance
        """
        return IntentStatisticsInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            intent_sid=self._solution['intent_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Understand.IntentStatisticsPage>'


class IntentStatisticsContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, assistant_sid, intent_sid):
        """
        Initialize the IntentStatisticsContext

        :param Version version: Version that contains the resource
        :param assistant_sid: The assistant_sid
        :param intent_sid: The intent_sid

        :returns: twilio.rest.preview.understand.assistant.intent.intent_statistics.IntentStatisticsContext
        :rtype: twilio.rest.preview.understand.assistant.intent.intent_statistics.IntentStatisticsContext
        """
        super(IntentStatisticsContext, self).__init__(version)

        # Path Solution
        self._solution = {'assistant_sid': assistant_sid, 'intent_sid': intent_sid, }
        self._uri = '/Assistants/{assistant_sid}/Intents/{intent_sid}/Statistics'.format(**self._solution)

    def fetch(self):
        """
        Fetch a IntentStatisticsInstance

        :returns: Fetched IntentStatisticsInstance
        :rtype: twilio.rest.preview.understand.assistant.intent.intent_statistics.IntentStatisticsInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return IntentStatisticsInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            intent_sid=self._solution['intent_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Understand.IntentStatisticsContext {}>'.format(context)


class IntentStatisticsInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, assistant_sid, intent_sid):
        """
        Initialize the IntentStatisticsInstance

        :returns: twilio.rest.preview.understand.assistant.intent.intent_statistics.IntentStatisticsInstance
        :rtype: twilio.rest.preview.understand.assistant.intent.intent_statistics.IntentStatisticsInstance
        """
        super(IntentStatisticsInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'assistant_sid': payload['assistant_sid'],
            'intent_sid': payload['intent_sid'],
            'samples_count': deserialize.integer(payload['samples_count']),
            'fields_count': deserialize.integer(payload['fields_count']),
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'assistant_sid': assistant_sid, 'intent_sid': intent_sid, }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: IntentStatisticsContext for this IntentStatisticsInstance
        :rtype: twilio.rest.preview.understand.assistant.intent.intent_statistics.IntentStatisticsContext
        """
        if self._context is None:
            self._context = IntentStatisticsContext(
                self._version,
                assistant_sid=self._solution['assistant_sid'],
                intent_sid=self._solution['intent_sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The unique ID of the Account that created this Field.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def assistant_sid(self):
        """
        :returns: The unique ID of the parent Assistant.
        :rtype: unicode
        """
        return self._properties['assistant_sid']

    @property
    def intent_sid(self):
        """
        :returns: The unique ID of the Intent associated with this Field.
        :rtype: unicode
        """
        return self._properties['intent_sid']

    @property
    def samples_count(self):
        """
        :returns: The total number of Samples associated with this Intent.
        :rtype: unicode
        """
        return self._properties['samples_count']

    @property
    def fields_count(self):
        """
        :returns: The total number of Fields associated with this Intent.
        :rtype: unicode
        """
        return self._properties['fields_count']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a IntentStatisticsInstance

        :returns: Fetched IntentStatisticsInstance
        :rtype: twilio.rest.preview.understand.assistant.intent.intent_statistics.IntentStatisticsInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Understand.IntentStatisticsInstance {}>'.format(context)
