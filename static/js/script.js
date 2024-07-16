document.addEventListener('DOMContentLoaded', function() {
    // Função para enviar formulários
    function sendForm(url, data, form) {
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            alert('Registro realizado com sucesso!');
            form.reset(); // Limpa os campos do formulário
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }

    // Formulário de Entrada e Saída
    document.getElementById('entrada_saida_form').addEventListener('submit', function(event) {
        event.preventDefault();
        const data = {
            data: document.getElementById('data').value,
            tipo: document.getElementById('tipo').value,
            produto: document.getElementById('produto').value,
            quantidade: document.getElementById('quantidade').value,
            custo_unitario: document.getElementById('custo_unitario').value,
            total_custo: document.getElementById('total_custo').value
        };
        sendForm('/entrada_saida', data, this);
    });

    // Formulário de Controle de Estoque
    document.getElementById('controle_estoque_form').addEventListener('submit', function(event) {
        event.preventDefault();
        const data = {
            produto: document.getElementById('produto_estoque').value,
            quantidade: document.getElementById('quantidade_estoque').value,
            valor_venda: document.getElementById('valor_venda').value,
            custo_compra: document.getElementById('custo_compra').value
        };
        sendForm('/controle_estoque', data, this);
    });

    // Formulário de Registro de Vendas
    document.getElementById('registro_vendas_form').addEventListener('submit', function(event) {
        event.preventDefault();
        const data = {
            data: document.getElementById('data_venda').value,
            produto: document.getElementById('produto_venda').value,
            quantidade: document.getElementById('quantidade_venda').value,
            valor_unitario: document.getElementById('valor_unitario_venda').value,
            valor_total: document.getElementById('valor_total_venda').value,
            tipo_pagamento: document.getElementById('tipo_pagamento_venda').value
        };
        sendForm('/registro_vendas', data, this);
    });

    // Formulário de Serviços
    document.getElementById('servicos_form').addEventListener('submit', function(event) {
        event.preventDefault();
        const data = {
            data: document.getElementById('data_servico').value,
            servico: document.getElementById('servico').value,
            profissional: document.getElementById('profissional').value,
            valor_total: document.getElementById('valor_total_servico').value,
            comissao_estudio: document.getElementById('comissao_estudio').value,
            tipo_pagamento: document.getElementById('tipo_pagamento_servico').value,
            observacoes: document.getElementById('observacoes').value
        };
        sendForm('/servicos', data, this);
    });

    // Botão de Relatórios
    document.getElementById('gerar_relatorios').addEventListener('click', function() {
        fetch('/relatorios')
        .then(response => response.json())
        .then(data => {
            const resultDiv = document.getElementById('relatorios_result');
            resultDiv.innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});
