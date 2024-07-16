from flask import Flask, render_template, request, redirect, url_for
from excel_manager import add_entry, get_data

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entrada_saida', methods=['GET', 'POST'])
def entrada_saida():
    if request.method == 'POST':
        data = request.form.to_dict()
        add_entry('data/entrada_saida.xlsx', data)
        return redirect(url_for('entrada_saida'))
    return render_template('entrada_saida.html')

@app.route('/controle_estoque', methods=['GET', 'POST'])
def controle_estoque():
    if request.method == 'POST':
        data = request.form.to_dict()
        add_entry('data/controle_estoque.xlsx', data)
        return redirect(url_for('controle_estoque'))
    return render_template('controle_estoque.html')

@app.route('/registro_venda', methods=['GET', 'POST'])
def registro_venda():
    if request.method == 'POST':
        data = request.form.to_dict()
        add_entry('data/registro_venda.xlsx', data)
        return redirect(url_for('registro_venda'))
    return render_template('registro_venda.html')

@app.route('/servicos', methods=['GET', 'POST'])
def servicos():
    if request.method == 'POST':
        data = request.form.to_dict()
        add_entry('data/servicos.xlsx', data)
        return redirect(url_for('servicos'))
    return render_template('servicos.html')

@app.route('/relatorios')
def relatorios():
    entrada_saida_data = get_data('data/entrada_saida.xlsx')
    controle_estoque_data = get_data('data/controle_estoque.xlsx')
    registro_venda_data = get_data('data/registro_venda.xlsx')
    servicos_data = get_data('data/servicos.xlsx')
    return render_template('relatorios.html', entrada_saida=entrada_saida_data,
                           controle_estoque=controle_estoque_data,
                           registro_venda=registro_venda_data,
                           servicos=servicos_data)

if __name__ == '__main__':
    app.run(debug=True)
