from src.EITP.EITPBaseData import EITPType, EITPConnectedClient
from src.EITP.EITPMessenger import EITPMessengerClient
import time


if __name__ == '__main__':

    eitp = EITPMessengerClient('127.0.0.1', 35000)
    my_id = eitp.connect(EITPType.CLIENT, 'Client')

    while True:
        eitp.socket_client.send('get_all_clients')
        message_received = eitp.socket_client.receive(1024)
        client_list = eval(message_received)

        # Convert to EITP TYPE and make a option list
        for client in client_list:
            client[0] = EITPType(client[0])

        # show menu and wait a option
        print('ROTULE     ID   TYPE')
        for client in client_list:
            if client[0] != EITPType.CLIENT:
                print(str(client[3]) + ' ' + str(client[2]) + ' ' + str(client[0].name))

        option = list(input('>> ').split(' '))

        if option[0] == 'GET':
            data = eitp.get(my_id, int(option[1]))
            print(data)

        elif option[0] == 'ENABLE':
            eitp.enable(my_id, int(option[1]))

        elif option[0] == 'DISABLE':
            eitp.disable(my_id, int(option[1]))

        elif option[0] == 'DISCONNECT':
            eitp.disconnect(my_id)
            exit(0)

