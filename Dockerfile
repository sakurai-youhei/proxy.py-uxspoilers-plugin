# build stage
FROM python:3-slim AS build-env
LABEL maintainer="sakurai.youhei@gmail.com"

ADD . /src
WORKDIR /src
RUN python3 setup.py clean bdist_wheel

# container stage
#FROM abhinavsingh/proxy.py:v2.3.1
FROM python:3-slim
LABEL maintainer="sakurai.youhei@gmail.com"

COPY --from=build-env /src/dist /tmp/dist
RUN pip3 install --no-cache-dir proxy.py==2.3.1 && \
    pip3 install --no-cache-dir /tmp/dist/*.whl && \
    rm -rf /tmp/dist/
