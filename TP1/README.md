# Título do Projeto

## Análise de um dataset - Atletas

Abrir um ficheiro csv (emd) sem o uso do módulo "csv" e retornar estatisticas ou listas de dados.


# Leitura do Arquivo

```python
    import sys

    lines = sys.stdin.readlines()
    data = [line.strip().split(',') for line in lines]
```



Este código utiliza o módulo sys da biblioteca padrão do Python para interagir com a entrada padrão escolhida para os dados.

Usou-se o método readLines(),strip() e split() para obter, separar e guardar as várias linhas do ficheiro na lista "data",aonde cada elemento representa uma linha do arquivo.

# Funcionalidades

## Lista Ordenada Alfabeticamente por Modalidade

```python
    header = data[0]
    modalidade_index = header.index('modalidade')
    sorted_data = sorted(data[1:], key=lambda x: x[modalidade_index])
    for row in [header] + sorted_data:
        print(row)
    print("\n")
```

A primeira linha do arquivo (data[0]) é extraída para a variável header. O script então encontra o índice da coluna 'modalidade' no cabeçalho e usa isso para ordenar a lista de dados (data) com base nos valores dessa coluna. Em seguida, imprime a lista ordenada, incluindo o cabeçalho.

## Percentagem de Atletas Aptos e Inaptos

```python
    header2 = data[0]
    federado_index = header2.index('federado')

    fit_count = sum(1 for row in data[1:] if row[federado_index] == 'true')
    unfit_count = sum(1 for row in data[1:] if row[federado_index] == 'false')

    total_athletes = len(data) - 1
    fit_percentage = (fit_count / total_athletes) * 100
    unfit_percentage = (unfit_count / total_athletes) * 100

    print(f"Número de Atletas: {total_athletes}")
    print(f"Atletas Aptos: {fit_count} ({fit_percentage:.2f}%)")
    print(f"Atletas Inaptos: {unfit_count} ({unfit_percentage:.2f}%)\n")
```

O script calcula a quantidade e a percentagem de atletas aptos e inaptos com base na coluna 'federado' do arquivo, criando um contador para cada vez que um atleta apresenta essa coluna como 'true' ou 'false' e adicionando cada um desses nas variaveis fit_count e unfit_count.

Para calcular a percentagem calculamos o número total de atletas fazendo o len(data)-1 (cabeçalho) e dividimos por cada uma destas variáveis. 

 Esses resultados são então impressos.

## Distribuição de Atletas por Escalão

```python
    header3 = data[0]
    idade_index = header.index('idade')

    age_groups = {
        '20-24': 0,
        '25-29': 0,
        '30-34': 0,
        '35-39': 0,
    }

    for row in data[1:]:
        age = int(row[idade_index])
        for group in age_groups:
            lower, upper = map(int, group.split('-'))
            if lower <= age <= upper:
                age_groups[group] += 1
                break

    print("Distribuição de atletas por Escalão:")
    for group, count in age_groups.items():
        print(f"{group}: {count}")
```
Apresenta a distribuição dos vários atletas de acordo com o seu Escalão, cujos níveis são representados por Intervalos de idade (5 anos).

O script itera sobre os dados, verifica a idade de cada atleta ,incrementa o contador correspondente ao grupo de idade apropriado e no fim imprime a sua distribuição por cada escalão.

Por default só existem 4 escalões visto que no csv dado as idades só variam entre 20-39 anos, mas poderão ser adicionados mais se necessário.


# Pré-Requesitos

O único pré-requisito para este projeto é ter o Python instalado.

Certifique-se de ter uma versão do Python compatível com o script. 

Para verificar se você tem o Python instalado, abra um terminal e execute o seguinte comando:

```bash
    python --version
```

# Execução do Script

```bash
    cat emd.csv | python3 Atletas.py
```

# Estrutura de Arquivos
```
    raiz_do_projeto/
    │   Atletas.py
    │   emd.csv
    │   README.md
```

