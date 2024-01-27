import os
from mcrcon import MCRcon

class RCON():
    def __init__(self):
        self.ip = os.environ['HOST_SERVER_IP']
        self.port = int(os.environ['RCON_PORT'])
        self.password = os.environ['RCON_PASSWORD']

    def __send_command(self, command):
        with MCRcon(self.ip, self.password, self.port) as rcon:
            response = rcon.command(command)
            return response
        
    def info(self):
        rcon = self.__send_command('info')
        return rcon

    def show_players(self):
        rcon = self.__send_command('showplayers')
        return rcon
    
    def save(self):
        rcon = self.__send_command('save')
        return rcon