from src.EITP.EITPBaseData import EITPType
from src.EITP.EITPMessengerBase import EITPMessengerBaseClient
import py_menu

if __main__ == '__main__':

    eitp = EITPMessengerBaseClient('', 10)
    my_id = eitp.connect(EITPType.CLIENT, 'Client')

    while True:
        eitp.socket_client.send('get_all_clients')
        client_list = list(eitp.socket_client.receive(1024))
        print(client_list)
        rotule_list = []
