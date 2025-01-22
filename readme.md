Este projeto é uma implementação de análise e visualização de grafos utilizando o algoritmo Fruchterman-Reingold e outras ferramentas.

## Estrutura do Projeto

- **`runner.py`**: Arquivo principal para execução do pipeline de análise e visualização de grafos.
- **`fruchterman_reingold.py`**: Implementação do algoritmo Fruchterman-Reingold para disposição de grafos.
- **`networkx.py`**: Wrapper personalizado baseado na API do NetworkX para processar e executar o algoritmo Fruchterman-Reingold.
- **`testing.py`**: Contém utilitários para calcular cruzamentos de arestas no grafo.
- **`.gitignore`**: Arquivo para excluir arquivos desnecessários do repositório.
- **`test.ipynb`**: Notebook para testes e experimentações.

## Dependências

As seguintes bibliotecas são necessárias para executar o projeto:

- **`numpy`**: Para cálculos numéricos.
- **`networkx`**: Para manipulação de grafos.
- **`matplotlib`**: Para visualização de grafos.

### Instalação

1. Clone este repositório:
   git clone https://github.com/seu-usuario/seu-repositorio.git
   
2. Acesse o diretório do projeto:
   cd seu-repositorio
   
3. Crie e ative um ambiente virtual:
   python -m venv env
   source env/bin/activate  # No Windows: env\Scripts\activate
   
4. Instale as dependências:
   pip install numpy networkx matplotlib
   

## Uso

Para executar a análise de grafos, utilize o arquivo `runner.py` como ponto de entrada. Exemplo de uso:


from runner import run_and_plot_graph_analysis

# Defina as arestas do grafo
edges = [(1, 2), (2, 3), (3, 1), (3, 4)]
run_and_plot_graph_analysis(edges)

Este script gerará uma visualização do grafo com informações sobre o tempo de execução do algoritmo e o número de cruzamentos de arestas.