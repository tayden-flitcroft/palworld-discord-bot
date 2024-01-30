FROM ubuntu:20.04 as builder

ENV DEBIAN_FRONTEND=noninteractive

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y wine wine32 wine64 libwine libwine:i386 fonts-wine xvfb python3-pip

ENV WINEPREFIX=/root/.wine
ENV WINEARCH=win64

RUN pip3 install pyinstaller

COPY . /source
WORKDIR /source

RUN xvfb-run wine pyinstaller --onefile --windowed --add-data="assets/installer/mods;mods" --icon="assets/installer/icon.png" --name="Palworld_Mod_Installer" assets/installer/installer.py

FROM python:3.9-slim

WORKDIR /
COPY --from=builder /source/dist/ /app/
COPY . /

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./bot.py"]
