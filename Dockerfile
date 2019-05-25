from python:alpine

LABEL maintainer="bananaprotocol@protonmail.com"

WORKDIR /usr/share/app

RUN python3 -m pip install -U discord.py 

COPY bot.py ./

ENV TOKEN=
ENV TARGET_ID=
ENV TARGET_ROLE=
ENV EMOTE=

CMD ["python", "bot.py"]

