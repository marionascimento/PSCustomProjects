#!/bin/bash

# Verifica se o caminho do arquivo Python foi fornecido
if [ -z "$1" ]; then
    echo "Help: $0 caminho_para_o_arquivo_python"
    exit 1
fi

# Captura o caminho completo do arquivo Python
PYTHON_SCRIPT=$1

# Extrai o nome do arquivo (incluindo a extensão)
FILE_NAME=$(basename "$PYTHON_SCRIPT")

echo "Arquivo: $FILE_NAME"

# Extrai o diretório onde o script Python está localizado
SCRIPT_DIR=$(dirname "$PYTHON_SCRIPT")

# Navega até o diretório do cliente
cd "$SCRIPT_DIR"

# Atualiza pacotes do projeto
echo "O ambiente virtual não está configurado. Configurando..."
if ! poetry update; then
    echo "Erro: Falha ao configurar o ambiente virtual."
    exit 1
fi

# Executa o script Python usando o Poetry
poetry run python "$FILE_NAME"