#!/bin/bash

# Tela de carregamento
echo "Carregando"
for i in {1..5}
do
    sleep 1
    echo -n "."  # Imprime um ponto sem nova linha
done
echo ""  # Nova linha após a tela de carregamento

# Executa o script Python
python3 meu_script.py
