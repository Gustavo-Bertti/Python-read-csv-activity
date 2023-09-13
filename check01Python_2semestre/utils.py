def open_path(file_path):
    try:
        with open(file_path, encoding='utf-8') as file:
            content = file.readlines()
            return content
    except FileNotFoundError:
        print("Arquivo não encontrado")