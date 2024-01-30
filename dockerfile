FROM python:3.9-slim
WORKDIR /
COPY . /
RUN pip install --no-cache-dir -r requirements.txt
RUN pyinstaller --onefile --windowed --add-data="./assets/installer/mods:mods" --icon="./assets/installer/icon.png" --name="Palworld Mod Installer" ./assets/installer/installer.py
CMD ["python", "./bot.py"]
