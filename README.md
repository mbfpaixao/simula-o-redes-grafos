Simulação de Difusão de Informação em Redes Complexas
Este projeto implementa uma simulação simples e visual da propagação de informação em três modelos clássicos de redes complexas: Erdős–Rényi, Barabási–Albert e Watts–Strogatz.
O objetivo é observar como a estrutura da rede influencia a velocidade, o alcance e os padrões de difusão.

Objetivo do Projeto
- Entender como diferentes topologias de rede afetam a propagação de uma informação.
- Comparar o comportamento da difusão quando o nó inicial é aleatório ou um hub.
- Visualizar graficamente as redes e analisar métricas como:
- infectados por rodada
- alcance total
- velocidade de propagação
- ponto de travamento da difusão

Tecnologias Utilizadas
- Python 3
- NetworkX — geração e análise de grafos
- Matplotlib — visualização
- Random — seleção probabilística
- Ambiente virtual .venv

Instalação
Clone o repositório:
git clone https://github.com/mbfpaixao/simulacao-redes-grafos.git
cd simulacao-redes-grafos


Crie um ambiente virtual (opcional, mas recomendado):
python -m venv .venv


Ative o ambiente:
Windows:
.venv\Scripts\activate


Linux/Mac:
source .venv/bin/activate


Instale as dependências:
pip install -r requirements.txt



Como Executar
Basta rodar o arquivo principal:
python simulacao_redes.py


O terminal exibirá:
- nó inicial
- infectados por rodada
- alcance total
- rodada em que a difusão travou
- rodada em que atingiu metade da rede
E três gráficos serão exibidos mostrando as redes geradas.

Modelos de Rede Utilizados
Erdős–Rényi
Rede aleatória, conexões distribuídas de forma uniforme.
Barabási–Albert
Rede com hubs — poucos nós muito conectados.
Watts–Strogatz
Rede de pequeno mundo — alta clusterização com alguns atalhos.

Funcionamento da Simulação
A simulação usa o modelo SI (Susceptible → Infected):
- Cada nó infectado tenta infectar seus vizinhos com probabilidade 0.8.
- A simulação roda por até 12 rodadas.
- A atividade termina quando não há novos infectados.

Estrutura do Projeto
simulacao-redes-grafos/
│
├── simulacao_redes.py
├── requirements.txt
└── README.md



Autor
Marlon Brando Freitas Paixão
UFMT — Bacharelado em Ciência e Tecnologia
2026

