# Análise de Temperatura Anual

Programa desenvolvido em Python que valida e analisa dados meteorológicos informados pelo usuário, referentes aos meses de janeiro a dezembro de um determinado ano.

🔥 Temperatura média máxima anual <br>
🌡️ Quantidade de meses escaldantes <br>
☀️ Identificação do mês mais quente do ano <br>
❄️ Identificação do mês menos quente do ano

## Como funciona

O usuário insere a temperatura máxima de cada mês, e o programa processa os dados para gerar indicadores que ajudam a entender o comportamento climático ao longo do ano.

- Número do mês (entre 1 e 12)
- Temperatura máxima mensal (entre -60°C e 50°C)

Ambos os dados passam por validação, garantindo que apenas valores válidos sejam considerados na análise.

## Validações implementadas

- Verificação de mês válido (1 a 12)
- Verificação de faixa de temperatura (-60°C a 50°C)
- Reentrada de dados em caso de valores inválidos
- Controle de duplicidade de meses  

## Regras de negócio

- Um mês é considerado escaldante quando a temperatura é superior a 33°C
- A média anual considera os 12 meses informados
- O mês mais e menos quente são definidos com base nas temperaturas máximas registradas

## Sobre o projeto

Primeiro projeto dados com Python, desenvolvido no contexto acadêmico em março de 2025, com foco na aplicação de lógica de programação.