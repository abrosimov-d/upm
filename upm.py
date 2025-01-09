from config import Config
from pagemonitor import PageMonitor

def main():

    config = Config()
    config.read_config()

    page_monitor = PageMonitor(config)
    page_monitor.update_pages()


main()
