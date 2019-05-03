# Docker file for the dircopy plugin app

FROM fnndsc/ubuntu-python3:latest
MAINTAINER fnndsc "dev@babymri.org"

ENV APPROOT="/usr/src/dircopy"
COPY ["dircopy", "${APPROOT}"]
COPY ["requirements.txt", "${APPROOT}"]

WORKDIR $APPROOT

RUN pip install -r requirements.txt

CMD ["dircopy.py", "--help"]
