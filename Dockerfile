FROM smithmicro/web2py:debian

USER root

RUN pip uninstall uwsgi -y

RUN apt-get update && apt-get -y install \
    git \
    vim \
    wget \
    unzip \
    python3 \
    python3-pip 

RUN echo 'alias python="/usr/bin/python3.5"' >> ~/.bashrc
RUN . ~/.bashrc

COPY docker_sources/routes.py $WEB2PY_ROOT/routes.py
COPY docker_sources/requirements.txt $WEB2PY_ROOT

WORKDIR $WEB2PY_ROOT
#Install required Python pacakages, remove sample apps, set proper ownership and make accessible models whit __init__.py file
RUN pip install --upgrade pip \ 
      && pip3 install -r requirements.txt \
      && rm -rf requirements.txt \
      && rm -rf $WEB2PY_ROOT/applications/welcome $WEB2PY_ROOT/applications/examples \
      && chown -R web2py:web2py $WEB2PY_ROOT \
      && touch $WEB2PY_ROOT/applications/__init__.py 

USER web2py