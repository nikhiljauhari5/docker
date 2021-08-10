FROM python

RUN pip install requests  && pip install pytest
RUN mkdir /dockerapi

COPY . /dockerapi
WORKDIR /dockerapi

CMD pytest -vs test_main.py