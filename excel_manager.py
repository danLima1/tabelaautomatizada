import pandas as pd
from openpyxl import load_workbook

def add_entry(file_path, data):
    try:
        # Carregar o arquivo Excel
        book = load_workbook(file_path)
        sheet = book.active

        # Preparar os dados para adicionar
        new_row = list(data.values())

        # Adicionar os dados ao final da planilha
        sheet.append(new_row)

        # Salvar a planilha
        book.save(file_path)
        print(f"Dados adicionados com sucesso: {new_row}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def get_data(file_path):
    try:
        # Ler o arquivo Excel
        df = pd.read_excel(file_path, header=None)
        return df.values.tolist()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return []
