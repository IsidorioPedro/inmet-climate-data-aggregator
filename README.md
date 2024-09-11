# inmet-climate-data-aggregator

## Project Description

This project aims to process raw meteorological data provided in CSV files and format it in a standardized way, including preserving the original metadata in the processed files. The code reads the raw CSV files, removes empty columns, formats dates and times, and concatenates multiple files into a single output CSV.

### Features

- Loads multiple CSV files from a specified directory.
- Formats the date in the `YYYY/MM/DD` style and the time in the `HHMM UTC` format.
- Removes empty columns.
- Saves the processed data into a single CSV file, including the metadata at the top.

### Directory Structure

- **data/raw**: Directory where the raw CSV files are located.
- **data/processed**: Directory where the processed CSV file will be saved.

### Execution

1. Place the CSV files in the `data/raw` directory.
2. Run the Python script to process the files.
3. The formatted file will be generated at `data/processed/formatted_data.csv` with metadata and formatted data.

---

## Descrição do Projeto

Este projeto tem como objetivo processar dados meteorológicos brutos fornecidos em arquivos CSV e formatá-los de forma padronizada, incluindo a preservação dos metadados originais nos arquivos processados. O código lê os arquivos CSV brutos, remove colunas vazias, formata datas e horas, e concatena múltiplos arquivos em um único CSV de saída.

### Funcionalidades

- Carrega múltiplos arquivos CSV de um diretório específico.
- Formata a data no estilo `YYYY/MM/DD` e a hora no formato `HHMM UTC`.
- Remove colunas vazias.
- Salva os dados processados em um único arquivo CSV, incluindo os metadados no topo.

### Estrutura de Diretórios

- **data/raw**: Diretório onde estão os arquivos CSV brutos.
- **data/processed**: Diretório onde o arquivo CSV processado será salvo.

### Execução

1. Coloque os arquivos CSV no diretório `data/raw`.
2. Execute o script Python para processar os arquivos.
3. O arquivo formatado será gerado em `data/processed/formatted_data.csv` com os metadados e dados formatados.
