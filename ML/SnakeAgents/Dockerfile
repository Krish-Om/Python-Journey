FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y\
    libsdl2-dev\
    libsdl2-image-dev\
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libfreetype6-dev \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libxtst6 \
    libxi6 \
    # Audio dependencies
    pulseaudio \
    alsa-utils \
    # Clean up to reduce image size
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

RUN pip install --no-cache-dir pygame==2.5.2

COPY *.py ./

COPY resources ./resources/

RUN useradd -m -s /bin/bash gameuser && \
chown -R gameuser:gameuser /app


USER gameuser

ENV PYTHONUNBUFFERED=1
ENV DISPLAY=:0

CMD ["python","source.py"]