def parse_float(value):
    try:
        result = float(value)
        return result
    except ValueError:
        print("Digite um número válido")
        return None

def get_file_content(file_path):
    try:
        with open(file_path, encoding='utf-8') as file:
            content = file.readlines()
            return content
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return None

def get_headers(content):
    headers = content.strip().split(",")
    return headers

def columns_to_dict(headers, content):
    data = {}
    columns = content.strip().split(",")
    for index, header_name in enumerate(headers):
        column = columns[index]
        header_name = header_name.strip('"')
        data[header_name] = column
    return data