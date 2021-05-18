'''
Created on 2021/05/15

@author: sakurai
'''
from random import random
from time import sleep
from typing import Optional

from proxy.common.flag import flags
from proxy.http.parser import HttpParser
from proxy.http.proxy import HttpProxyBasePlugin


__version__ = "2021.5.18"


flags.add_argument('--pause-seconds',
                   type=float,
                   default=1.0,
                   help=('Default: 1.0.  Flag only applicable when '
                         'FixedRustyPumpPlugin is used for spoiling UX.'))
flags.add_argument('--pause-coefficient',
                   type=float,
                   default=1.0,
                   help=('Default: 1.0.  Flag only applicable when '
                         'RandomRustyPumpPlugin is used for spoiling UX.'))


class FixedRustyPumpPlugin(HttpProxyBasePlugin):
    def _pause_duration(self):
        return self.flags.pause_seconds

    def before_upstream_connection(
            self, request: HttpParser) -> Optional[HttpParser]:
        sleep(self._pause_duration())
        return request

    def handle_client_request(
            self, request: HttpParser) -> Optional[HttpParser]:
        sleep(self._pause_duration())
        return request

    def handle_upstream_chunk(self, chunk: memoryview) -> memoryview:
        sleep(self._pause_duration())
        return chunk

    def on_upstream_connection_close(self) -> None:
        pass


class RandomRustyPumpPlugin(FixedRustyPumpPlugin):
    def _pause_duration(self):
        return self.flags.pause_coefficient * random()
