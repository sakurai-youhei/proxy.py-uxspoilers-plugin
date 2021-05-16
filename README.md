# proxy.py-uxspoilers-plugin

A plugin for [proxy.py](https://pypi.org/project/proxy.py/) to spoil UX of web browsing

You can spoil User Experience of e.g. YouTube with a combination of [proxy.py](https://pypi.org/project/proxy.py/) plus [proxy.py-uxspoilers-plugin](https://pypi.org/project/proxy.py-uxspoilers-plugin/) and a kind of following [PAC](https://en.wikipedia.org/wiki/Proxy_auto-config)/[WPAD](https://en.wikipedia.org/wiki/Web_Proxy_Auto-Discovery_Protocol) file.

```javascript
function FindProxyForURL(url, host)
{
    if (shExpMatch(host, "*youtube*") || shExpMatch(host, "*.googlevideo.com"))
    {
        return "PROXY ip-of-your-proxy:8899";
    }
    return "DIRECT";
}
```

Run your proxy server like this:

```console
proxy --hostname=0.0.0.0 --pac-file /path/to/wpad.dat --plugin uxspoilers.FixedRustyPumpPlugin --pause-seconds 3
```

Your `/etc/dhcp/dhcpd.conf` should look like this:

```ini
option wpad code 252 = text;
host target-device {
    option wpad "http://ip-of-your-proxy:8899/wpad.dat";
    hardware ethernet 2e:8d:8d:xx:xx:xx;
}
```

Or you may configure your browser's [PAC](https://en.wikipedia.org/wiki/Proxy_auto-config) with `http://ip-of-your-proxy:8899/wpad.dat` manually.

## Installation

[![PyPI Version        ](https://img.shields.io/pypi/v/proxy.py-uxspoilers-plugin.svg)](https://pypi.org/project/proxy.py-uxspoilers-plugin/)
[![PyPI Downloads      ](https://img.shields.io/pypi/dm/proxy.py-uxspoilers-plugin.svg)](https://pypi.org/project/proxy.py-uxspoilers-plugin/)

```console
pip3 install proxy.py-uxspoilers-plugin
proxy --help --plugin uxspoilers.RandomRustyPumpPlugin
```

### Docker

[![Docker Pulls](https://img.shields.io/docker/pulls/sakuraiyouhei/proxy.py-uxspoilers-plugin)](https://hub.docker.com/r/sakuraiyouhei/proxy.py-uxspoilers-plugin/)
[![Image Size  ](https://img.shields.io/docker/image-size/sakuraiyouhei/proxy.py-uxspoilers-plugin)](https://hub.docker.com/r/sakuraiyouhei/proxy.py-uxspoilers-plugin/)

```console
docker run -it sakuraiyouhei/proxy.py-uxspoilers-plugin --help --plugin uxspoilers.RandomRustyPumpPlugin
```
