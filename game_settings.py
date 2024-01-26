import re
import os

class GameSettings:
    def __init__(self):
        self.settings = self.parse_settings(self.open_settings())

    def open_settings(self):
        doc = open('docs/PalWorldSettings.ini')
        return doc.read()
    
    def format_settings_for_discord(self):
        messages = []
        current_msg = '```\n'
        for key, value in self.settings.items():
            setting_line = f"{key}: {value}\n"
            if len(current_msg) + len(setting_line) + 4 > 2000:
                current_msg += '```'
                messages.append(current_msg)
                current_msg = '```\n' + setting_line
            else:
                current_msg += setting_line
        current_msg += '```'
        messages.append(current_msg)
        return messages

    def parse_settings(self, settings_str):
        settings_str = settings_str.replace('=', ':').replace('\n', '').replace('[/Script/Pal.PalGameWorldSettings]OptionSettings:', '').replace('(', '').replace(')', '')
        key_value_pairs = re.split(r',(?=\w+:)', settings_str)
        settings = {}

        for pair in key_value_pairs:
            if ':' in pair:
                key, value = pair.split(':', 1)
                settings[key.strip()] = value.strip().strip('"')

        return settings

    def display_settings(self):
        for key, value in self.settings.items():
            print(f"{key}: {value}")

    def update_setting(self, key, value):
        if key in self.settings:
            self.settings[key] = value
            print(f"Setting {key} updated to {value}")
        else:
            print(f"Setting {key} not found.")
