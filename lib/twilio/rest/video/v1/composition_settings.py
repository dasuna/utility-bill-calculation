# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class CompositionSettingsList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the CompositionSettingsList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.video.v1.composition_settings.CompositionSettingsList
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsList
        """
        super(CompositionSettingsList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self):
        """
        Constructs a CompositionSettingsContext

        :returns: twilio.rest.video.v1.composition_settings.CompositionSettingsContext
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsContext
        """
        return CompositionSettingsContext(self._version, )

    def __call__(self):
        """
        Constructs a CompositionSettingsContext

        :returns: twilio.rest.video.v1.composition_settings.CompositionSettingsContext
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsContext
        """
        return CompositionSettingsContext(self._version, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.CompositionSettingsList>'


class CompositionSettingsPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the CompositionSettingsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.video.v1.composition_settings.CompositionSettingsPage
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsPage
        """
        super(CompositionSettingsPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CompositionSettingsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.video.v1.composition_settings.CompositionSettingsInstance
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsInstance
        """
        return CompositionSettingsInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.CompositionSettingsPage>'


class CompositionSettingsContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the CompositionSettingsContext

        :param Version version: Version that contains the resource

        :returns: twilio.rest.video.v1.composition_settings.CompositionSettingsContext
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsContext
        """
        super(CompositionSettingsContext, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/CompositionSettings/Default'.format(**self._solution)

    def fetch(self):
        """
        Fetch a CompositionSettingsInstance

        :returns: Fetched CompositionSettingsInstance
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return CompositionSettingsInstance(self._version, payload, )

    def create(self, friendly_name, aws_credentials_sid=values.unset,
               encryption_key_sid=values.unset, aws_s3_url=values.unset,
               aws_storage_enabled=values.unset, encryption_enabled=values.unset):
        """
        Create a new CompositionSettingsInstance

        :param unicode friendly_name: Friendly name of the configuration to be shown in the console
        :param unicode aws_credentials_sid: SID of the Stored Credential resource CRxx
        :param unicode encryption_key_sid: SID of the Public Key resource CRxx
        :param unicode aws_s3_url: Identity of the external location where the compositions should be stored. We only support DNS-compliant URLs like http://<my-bucket>.s3-<aws-region>.amazonaws.com/compositions, where compositions is the path where you want compositions to be stored.
        :param bool aws_storage_enabled: true|false When set to true, all Compositions will be written to the AwsS3Url specified above. When set to false, all Compositions will be stored in Twilio's cloud.
        :param bool encryption_enabled: true|false When set to true, all Compositions will be stored encrypted.

        :returns: Newly created CompositionSettingsInstance
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'AwsCredentialsSid': aws_credentials_sid,
            'EncryptionKeySid': encryption_key_sid,
            'AwsS3Url': aws_s3_url,
            'AwsStorageEnabled': aws_storage_enabled,
            'EncryptionEnabled': encryption_enabled,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return CompositionSettingsInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.CompositionSettingsContext {}>'.format(context)


class CompositionSettingsInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload):
        """
        Initialize the CompositionSettingsInstance

        :returns: twilio.rest.video.v1.composition_settings.CompositionSettingsInstance
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsInstance
        """
        super(CompositionSettingsInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'friendly_name': payload['friendly_name'],
            'aws_credentials_sid': payload['aws_credentials_sid'],
            'aws_s3_url': payload['aws_s3_url'],
            'aws_storage_enabled': payload['aws_storage_enabled'],
            'encryption_key_sid': payload['encryption_key_sid'],
            'encryption_enabled': payload['encryption_enabled'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {}

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: CompositionSettingsContext for this CompositionSettingsInstance
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsContext
        """
        if self._context is None:
            self._context = CompositionSettingsContext(self._version, )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The Twilio Account SID associated with this item
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """
        :returns: Friendly name of the configuration to be shown in the console
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def aws_credentials_sid(self):
        """
        :returns: SID of the Stored Credential resource CRxx
        :rtype: unicode
        """
        return self._properties['aws_credentials_sid']

    @property
    def aws_s3_url(self):
        """
        :returns: URL of the S3 bucket where the compositions should be stored. We only support DNS-compliant URLs like http://<my-bucket>.s3-<aws-region>.amazonaws.com/compositions, where compositions is the path where you want compositions to be stored.
        :rtype: unicode
        """
        return self._properties['aws_s3_url']

    @property
    def aws_storage_enabled(self):
        """
        :returns: true|false When set to true, all Compositions will be written to the AwsS3Url specified above. When set to false, all Compositions will be stored in Twilio's cloud.
        :rtype: bool
        """
        return self._properties['aws_storage_enabled']

    @property
    def encryption_key_sid(self):
        """
        :returns: SID of the Public Key resource CRxx
        :rtype: unicode
        """
        return self._properties['encryption_key_sid']

    @property
    def encryption_enabled(self):
        """
        :returns: true|false When set to true, all Compositions will be stored encrypted.
        :rtype: bool
        """
        return self._properties['encryption_enabled']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a CompositionSettingsInstance

        :returns: Fetched CompositionSettingsInstance
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsInstance
        """
        return self._proxy.fetch()

    def create(self, friendly_name, aws_credentials_sid=values.unset,
               encryption_key_sid=values.unset, aws_s3_url=values.unset,
               aws_storage_enabled=values.unset, encryption_enabled=values.unset):
        """
        Create a new CompositionSettingsInstance

        :param unicode friendly_name: Friendly name of the configuration to be shown in the console
        :param unicode aws_credentials_sid: SID of the Stored Credential resource CRxx
        :param unicode encryption_key_sid: SID of the Public Key resource CRxx
        :param unicode aws_s3_url: Identity of the external location where the compositions should be stored. We only support DNS-compliant URLs like http://<my-bucket>.s3-<aws-region>.amazonaws.com/compositions, where compositions is the path where you want compositions to be stored.
        :param bool aws_storage_enabled: true|false When set to true, all Compositions will be written to the AwsS3Url specified above. When set to false, all Compositions will be stored in Twilio's cloud.
        :param bool encryption_enabled: true|false When set to true, all Compositions will be stored encrypted.

        :returns: Newly created CompositionSettingsInstance
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsInstance
        """
        return self._proxy.create(
            friendly_name,
            aws_credentials_sid=aws_credentials_sid,
            encryption_key_sid=encryption_key_sid,
            aws_s3_url=aws_s3_url,
            aws_storage_enabled=aws_storage_enabled,
            encryption_enabled=encryption_enabled,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.CompositionSettingsInstance {}>'.format(context)