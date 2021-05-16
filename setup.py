from os.path import abspath
from os.path import dirname
from os.path import join
from re import MULTILINE
from re import search
from textwrap import dedent

from setuptools import setup


here = abspath(dirname(__file__))

with open(join(here, "uxspoilers.py"), encoding="utf-8") as fp:
    version = search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                     fp.read(), MULTILINE).group(1)

with open(join(here, "README.md"), encoding="utf-8") as fp:
    long_description = fp.read()

setup(name="proxy.py-uxspoilers-plugin",
      version=version,
      py_modules=['uxspoilers'],
      python_requires=">=3",
      install_requires=["proxy.py>=2.3.0"],
      author="Youhei Sakurai",
      author_email="sakurai.youhei@gmail.com",
      maintainer="Youhei Sakurai",
      maintainer_email="sakurai.youhei@gmail.com",
      url="https://github.com/sakurai-youhei/proxy.py-uxspoilers-plugin",
      license="MIT",
      description=long_description.splitlines()[1],
      long_description=long_description,
      long_description_content_type="text/markdown",
      platforms="any",
      classifiers=dedent("""\
        Intended Audience :: Developers
        License :: OSI Approved :: MIT License
        Operating System :: OS Independent
        Programming Language :: Python
        Programming Language :: Python :: 3
      """).splitlines())
