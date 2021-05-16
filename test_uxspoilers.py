'''
Created on 2021/05/15

@author: sakurai
'''
import pkg_resources
from subprocess import check_output
from sys import executable
from unittest import main
from unittest import skipIf
from unittest import TestCase

from python_wrap_cases import wrap_case


try:
    proxy_version = pkg_resources.get_distribution('proxy').version
except Exception:
    try:
        proxy_version = pkg_resources.get_distribution('construct').version
    except Exception:
        proxy_version = '0'


@wrap_case
class TestHttpProxyPluginExamples(TestCase):
    @wrap_case('uxspoilers.FixedRustyPumpPlugin', '--pause-seconds')
    @wrap_case('uxspoilers.RandomRustyPumpPlugin', '--pause-coefficient')
    def test_with_plugin_option(self, plugin, flag):
        help_ = check_output([executable, '-m', 'proxy', '--help', '--plugin',
                             plugin], text=True, errors='replace')
        self.assertIn(flag, help_)

    @wrap_case('uxspoilers.FixedRustyPumpPlugin', '--pause-seconds')
    @wrap_case('uxspoilers.RandomRustyPumpPlugin', '--pause-coefficient')
    @skipIf(proxy_version <= '2.3.1',
            'See https://github.com/abhinavsingh/proxy.py/pull/553')
    def test_with_plugins_option(self, plugin, flag):
        help_ = check_output([executable, '-m', 'proxy', '--help', '--plugins',
                             plugin], text=True, errors='replace')
        self.assertIn(flag, help_)


if __name__ == '__main__':
    main()
