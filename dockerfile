FROM python:3.9-slim
WORKDIR /
COPY assets/installer/Palworld_Mod_Installer.exe /app/
COPY . /
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./bot.py"]