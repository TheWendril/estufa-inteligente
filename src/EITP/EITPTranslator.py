from EITPbaseData import EITPOperation, EITPBaseData
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
            if line.find('operation: ') != -1:
                new_eitp_obj.header.operation = EITPOperation(int(line[12:]))

            if line.find('sender: ') != -1:
                new_eitp_obj.header.sender = int(line[9:])

            if line.find('recipient: ') != -1:
                new_eitp_obj.header.recipient = int(line[12:])

            # body converters

            if line.find('data: ') != -1:
                new_eitp_obj.body.data = float(line[7:])

            if line.find('current_time: ') != -1:
                new_eitp_obj.body.current_time = line[15:]

        return new_eitp_obj


if __name__ == '__main__':
    obj = EITPBaseData()
    obj.header.sender = 1
    obj.header.recipient = 2
    obj.header.operation = EITPOperation.GET

    obj.body.data = 2.3
    obj.body.current_time = '12:32'

    ogj = EITPTranslator.tostring(obj)
    print(ogj)
    esk = EITPTranslator.toeitpobj(ogj)
    print(esk.header.sender)
    print(esk.body.current_time)
