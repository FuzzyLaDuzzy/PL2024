
# Titulo do Projeto

## Markdown to HTML

Converter um ficheiro Markdown do STDIN para HTML.

# Funcionalidades

## Inicialização de Variáveis

html_text: String que armazenará o conteúdo HTML resultante.

markdown_lines: Lista de linhas lidas a partir da entrada padrão.

is_ordered_list e is_unordered_list: Flags para verificar se a lista atual é ordenada ou não ordenada.

```python
html_text = ""
markdown_lines = sys.stdin.readlines()
is_ordered_list = False
is_unordered_list = False
```

## Loop Principal para Processamento de Linhas Markdown

Itera sobre cada linha do Markdown.

```python
for line in markdown_lines:
    line = line.rstrip()  # Remove espaços em branco no final da linha
```

## Conversão de Cabeçalhos

Verifica se a linha começa com um ou mais # e substitui pela tag HTML <h1>, <h2>, etc.

```python
for i in range(3, 0, -1):
    if line.startswith('#' * i):
        line = line.replace('#' * i, f'<h{i}>', 1) + f'</h{i}>'
```

## Conversão de Texto em Negrito e Itálico

Substitui ** por <b> e </b>.

Substitui * por <i> e </i>.

```python
if '**' in line:
    line = line.replace('**', '<b>', 1)
    line = line.replace('**', '</b>', 1)

if '*' in line:
    line = line.replace('*', '<i>', 1)
    line = line.replace('*', '</i>', 1)
```

## Conversão de Listas Ordenadas

Verifica se a linha começa com um padrão de lista ordenada (número seguido de ponto).

Adiciona tags HTML <ol>, <li> conforme necessário.

```python
if re.match(r'\d+\.', line):
    line = '<li>' + line[line.find(' ')+1:] + '</li>'
    if not is_ordered_list:
        line = '<ol>\n' + line
        is_ordered_list = True
else:
    if is_ordered_list:
        line = '</ol>\n' + line
        is_ordered_list = False
```

## Conversão de Listas Não Ordenadas

Verifica se a linha começa com - .

Adiciona tags HTML <ul>, <li> conforme necessário.


```python
if line.startswith('- '):
    line = '<li>' + line[2:] + '</li>'
    if not is_unordered_list:
        line = '<ul>\n' + line
        is_unordered_list = True
else:
    if is_unordered_list:
        line = '</ul>\n' + line
        is_unordered_list = False
```

## Conversão de Código

Substitui o caractere de crase ` por <code>.

```python
if '`' in line:
    line = line.replace('`', '<code>', 1)
    line = line.replace('`', '</code>', 1)
```

## Conversão de Regras Horizontais

Substitui uma linha contendo apenas --- por <hr>.

```python
if line.strip() == '---':
    line = '<hr>'
```


## Conversão de Links

Extrai o texto do link e a URL e substitui por uma tag HTML de link.

```python
start_link = line.find('[')
end_link = line.find(']')
start_url = line.find('(')
end_url = line.find(')')
if start_link != -1 and end_link != -1 and start_url != -1 and end_url != -1:
    link_text = line[start_link+1:end_link]
    url = line[start_url+1:end_url]
    line = line.replace(f'[{link_text}]({url})', f'<a href="{url}">{link_text}</a>')
```

## Conversão de Imagens

Extrai o texto alternativo e a URL da imagem e substitui por uma tag HTML de imagem.

```python
start_alt_text = line.find('![')
end_alt_text = line.find(']')
start_img_url = line.find('(')
end_img_url = line.find(')')
if start_alt_text != -1 and end_alt_text != -1 and start_img_url != -1 and end_img_url != -1:
    alt_text = line[start_alt_text+2:end_alt_text]
    img_url = line[start_img_url+1:end_img_url]
    line = line.replace(f'![{alt_text}]({img_url})', f'<img src="{img_url}" alt="{alt_text}"/>')
```

# Pré-Requesitos

O único pré-requisito para este projeto é ter o Python instalado.

Certifique-se de ter uma versão do Python compatível com o script. 

Para verificar se você tem o Python instalado, abra um terminal e execute o seguinte comando:

```bash
    python --version
```

# Execução do Script

```bash
    cat test.md | python3 Markdown_to_Html.py
```

# Estrutura de Arquivos
```
    raiz_do_projeto/
    │   Markdown_to_Html.py
    │   test.md
    │   README.md
```
