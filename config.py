class Config:
    def __init__(self):
        self.pages = []

    def read_config(self):
        try:
            with open('config.config', 'r') as f:
                config_lines = f.readlines()
                for line in config_lines:
                    line = line.strip()
                    if line:
                        self.pages.append(line)
        except FileNotFoundError:
            print("Config file not found")
        except Exception as e:
            print(f"Error reading config file: {e}")
