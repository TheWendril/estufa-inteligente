from src.EITP.EITPBaseData import EITPOperation, EITPBaseData
from time import struct_time


class EITPTranslator:

    @staticmethod
    def tostring(obj_instance: EITPBaseData) -> str:
        syntactic_str: str = ''

        # making the header
        syntactic_str += 'header: \n'
        syntactic_str += '\toperation: ' + str(obj_instance.header.operation.value) + '\n'
        syntactic_str += '\tsender: ' + str(obj_instance.header.sender) + '\n'
        syntactic_str += '\trecipient: ' + str(obj_instance.header.recipient) + '\n'

        # making the body
        syntactic_str += 'body: ' + '\n'
        syntactic_str += '\tdata: ' + str(obj_instance.body.data) + '\n'
        syntactic_str += '\tcurrent_time: ' + str(obj_instance.body.current_time) + '\n'

        return syntactic_str

    @staticmethod
    def toeitpobj(input_str: str) -> EITPBaseData:
        new_eitp_obj = EITPBaseData()

        for line in input_str.splitlines():

            # headers converters
            if line.find('operation: ') != -1 and line[12:] != 'None':
                new_eitp_obj.header.operation = EITPOperation(int(line[12:]))

            if line.find('sender: ') != -1 and line[9:] != 'None':
                new_eitp_obj.header.sender = int(line[9:])

            if line.find('recipient: ') != -1 and line[12:] != 'None':
                new_eitp_obj.header.recipient = int(line[12:])

            # body converters

            if line.find('data: ') != -1 and line[7:] != 'None':
                new_eitp_obj.body.data = float(line[7:])

            if line.find('current_time: ') != -1 and line[15:] != 'None':
                new_eitp_obj.body.current_time = line[15:]

        return new_eitp_obj
