from flask import Flask, request, jsonify, render_template
import pandas as pd
import os

app = Flask(__name__)

# Caminho para os arquivos Excel
DATA_DIR = 'data'
ENTRADA_SAIDA_FILE = os.path.join(DATA_DIR, 'entrada_saida.xlsx')
CONTROLE_ESTOQUE_FILE = os.path.join(DATA_DIR, 'controle_estoque.xlsx')
REGISTRO_VENDAS_FILE = os.path.join(DATA_DIR, 'registro_vendas.xlsx')
SERVICOS_FILE = os.path.join(DATA_DIR, 'servicos.xlsx')


# Função para ler dados de um arquivo Excel
def read_excel(file_path):
    if os.path.exists(file_path):
        try:
            return pd.read_excel(file_path)
        except Exception as e:
            print(f"Erro ao ler o arquivo {file_path}: {e}")
            return pd.DataFrame()
    else:
        return pd.DataFrame()


# Função para escrever dados em um arquivo Excel
def write_excel(df, file_path):
    try:
        df.to_excel(file_path, index=False)
    except Exception as e:
        print(f"Erro ao escrever o arquivo {file_path}: {e}")


# Inicializa os arquivos Excel se não existirem
def initialize_excel_files():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    files = [ENTRADA_SAIDA_FILE, CONTROLE_ESTOQUE_FILE, REGISTRO_VENDAS_FILE, SERVICOS_FILE]
    for file in files:
        if not os.path.exists(file):
            df = pd.DataFrame()
            write_excel(df, file)


initialize_excel_files()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/entrada_saida', methods=['POST'])
def entrada_saida():
    data = request.json
    df = read_excel(ENTRADA_SAIDA_FILE)
    new_row = pd.DataFrame([data])
    df = pd.concat([df, new_row], ignore_index=True)
    write_excel(df, ENTRADA_SAIDA_FILE)
    return jsonify({'status': 'success'})


@app.route('/controle_estoque', methods=['POST'])
def controle_estoque():
    data = request.json
    df = read_excel(CONTROLE_ESTOQUE_FILE)
    new_row = pd.DataFrame([data])
    df = pd.concat([df, new_row], ignore_index=True)
    write_excel(df, CONTROLE_ESTOQUE_FILE)
    return jsonify({'status': 'success'})


@app.route('/registro_vendas', methods=['POST'])
def registro_vendas():
    data = request.json
    df = read_excel(REGISTRO_VENDAS_FILE)
    new_row = pd.DataFrame([data])
    df = pd.concat([df, new_row], ignore_index=True)
    write_excel(df, REGISTRO_VENDAS_FILE)
    return jsonify({'status': 'success'})


@app.route('/servicos', methods=['POST'])
def servicos():
    data = request.json
    df = read_excel(SERVICOS_FILE)
    new_row = pd.DataFrame([data])
    df = pd.concat([df, new_row], ignore_index=True)
    write_excel(df, SERVICOS_FILE)
    return jsonify({'status': 'success'})


@app.route('/relatorios', methods=['GET'])
def relatorios():
    df_entrada_saida = read_excel(ENTRADA_SAIDA_FILE)
    df_controle_estoque = read_excel(CONTROLE_ESTOQUE_FILE)
    df_registro_vendas = read_excel(REGISTRO_VENDAS_FILE)
    df_servicos = read_excel(SERVICOS_FILE)

    relatorio = {
        'entrada_saida': df_entrada_saida.to_dict(orient='records'),
        'controle_estoque': df_controle_estoque.to_dict(orient='records'),
        'registro_vendas': df_registro_vendas.to_dict(orient='records'),
        'servicos': df_servicos.to_dict(orient='records')
    }

    return jsonify(relatorio)


if __name__ == '__main__':
    app.run(debug=True)
