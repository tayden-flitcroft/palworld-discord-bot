FROM cdrx/pyinstaller-windows:python3 as builder

COPY . /src/
WORKDIR /src/

# Run PyInstaller to build the Windows executable
RUN pyinstaller --onefile --windowed --add-data="assets/installer/mods;mods" --icon="assets/installer/icon.png" --name="Palworld_Mod_Installer" assets/installer/installer.py

FROM python:3.9-slim

WORKDIR /

COPY --from=builder /src/dist/ /app/

COPY . /

RUN pip install --no-cache-dir -r requirements.txt

# Command to run the bot
CMD ["python", "./bot.py"]
