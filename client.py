from src.EITP.EITPBaseData import EITPType, EITPConnectedClient
from src.EITP.EITPMessenger import EITPMessengerClient
from simple_term_menu import TerminalMenu
import time


if __name__ == '__main__':

    eitp = EITPMessengerClient('127.0.0.1', 35000)
    my_id = eitp.connect(EITPType.CLIENT, 'Client')

    while True:
        eitp.socket_client.send('get_all_clients')
        message_received = eitp.socket_client.receive(1024)
        client_list = eval(message_received)

        # Convert to EITP TYPE and make a option list
        options = []
        for client in client_list:
            options.append(client[3])
            client[0] = EITPType(client[0])

        # making a menu
        menu = TerminalMenu(options)
        response = menu.show()

        time.sleep(2)
