from flask_restful import Resource
from util.serial_processor import send_and_receive_data
import util.commands as commands

class CheckCopyright(Resource):
    def get(self):
    	serial_return = send_and_receive_data(commands.COPYRIGHT)
        return {'serial_status': serial_return[0], 'serial_response': serial_return[1]}