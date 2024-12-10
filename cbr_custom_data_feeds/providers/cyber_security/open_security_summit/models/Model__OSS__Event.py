from typing                                                                                             import Dict
from cbr_custom_data_feeds.providers.cyber_security.open_security_summit.models.Model__OSS__Participant import Model__OSS__Participant
from cbr_custom_data_feeds.providers.cyber_security.open_security_summit.models.Model__OSS__Session     import Model__OSS__Session
from osbot_utils.base_classes.Type_Safe                                                                 import Type_Safe


class Model__OSS__Event(Type_Safe):
    month      : str
    year       : int
    organizers : Dict[str,Model__OSS__Participant]
    sessions   : Dict[str, Model__OSS__Session   ]
