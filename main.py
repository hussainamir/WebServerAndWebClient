import web_client
import web_server
import sorting_name
import frequency_finder
import threading
def start_webserver():
    web_server_thread=threading.Thread(target=web_server.start_webserver)
    web_server_thread.start()
    return web_server_thread
if __name__ == '__main__':

    user_info = input("Enter number to choose Task from 1-3, 1 for sorting name, 2 for frequency finder, 3 for web application: ")
    if user_info=="1":
        sorting_name.start_sorting_name()
    elif user_info=="2":
        frequency_finder.start_frequency_finder()
    elif user_info=="3":
        web_server_thread=start_webserver()
        web_client.start_webclient()


