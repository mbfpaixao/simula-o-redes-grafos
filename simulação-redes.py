import networkx as nx
import matplotlib.pyplot as plt
import random

# -----------------------------
# Parâmetros globais
# -----------------------------
N_NODES = 50
P_ER = 0.08          # Erdős-Rényi
M_BA = 2             # Barabási-Albert
K_WS = 6             # Watts-Strogatz
P_WS = 0.2
P_INFECT = 0.8       # probabilidade de infecção
MAX_ROUNDS = 12      # 8–12 rodadas

# -----------------------------
# Funções auxiliares
# -----------------------------
def escolher_no_inicial(G, modo="aleatorio"):
    """Escolhe nó inicial: 'aleatorio' ou 'hub'."""
    if modo == "aleatorio":
        return random.choice(list(G.nodes()))
    elif modo == "hub":
        graus = dict(G.degree())
        return max(graus, key=graus.get)
    else:
        raise ValueError("Modo deve ser 'aleatorio' ou 'hub'.")

def simular_difusao_SI(G, no_inicial, p_infect=P_INFECT, max_rounds=MAX_ROUNDS):
    """Simula difusão SI e retorna métricas."""
    infectados = {no_inicial}
    novos = {no_inicial}
    historico_infectados = [len(infectados)]
    rodada_trava = None

    for rodada in range(1, max_rounds + 1):
        novos_rodada = set()
        for i in novos:
            for vizinho in G.neighbors(i):
                if vizinho not in infectados:
                    if random.random() < p_infect:
                        novos_rodada.add(vizinho)

        if not novos_rodada:
            rodada_trava = rodada
            historico_infectados.append(len(infectados))
            break

        infectados |= novos_rodada
        novos = novos_rodada
        historico_infectados.append(len(infectados))

    if rodada_trava is None:
        rodada_trava = len(historico_infectados) - 1

    alcance_total = len(infectados)
    velocidade = None
    metade = len(G.nodes()) / 2
    for r, qtd in enumerate(historico_infectados):
        if qtd >= metade:
            velocidade = r
            break

    return {
        "no_inicial": no_inicial,
        "historico": historico_infectados,
        "alcance_total": alcance_total,
        "rodada_trava": rodada_trava,
        "velocidade_meia_rede": velocidade,
        "infectados_finais": infectados,
    }

def imprimir_resultados(nome_rede, modo_inicial, resultados):
    print(f"\n=== {nome_rede} | nó inicial: {modo_inicial} ===")
    print(f"Nó inicial: {resultados['no_inicial']}")
    print(f"Infectados por rodada: {resultados['historico']}")
    print(f"Alcance total: {resultados['alcance_total']} de {N_NODES}")
    print(f"Rodada em que travou: {resultados['rodada_trava']}")
    print(f"Rodada em que atingiu aproximadamente metade da amostra (se ocorreu): {resultados['velocidade_meia_rede']}")

# -----------------------------
# Criação das redes
# -----------------------------
G_er = nx.erdos_renyi_graph(N_NODES, P_ER)
G_ba = nx.barabasi_albert_graph(N_NODES, M_BA)
G_ws = nx.watts_strogatz_graph(N_NODES, K_WS, P_WS)

# -----------------------------
# Simulações
# -----------------------------
redes = [
    ("Erdős-Rényi", G_er),
    ("Barabási-Albert", G_ba),
    ("Watts-Strogatz", G_ws),
]

modos_iniciais = ["aleatorio", "hub"]

resultados_todos = {}

for nome, G in redes:
    resultados_todos[nome] = {}
    for modo in modos_iniciais:
        no_ini = escolher_no_inicial(G, modo=modo)
        res = simular_difusao_SI(G, no_ini)
        resultados_todos[nome][modo] = res
        imprimir_resultados(nome, modo, res)

# -----------------------------
# Visualização simples
# -----------------------------
plt.figure(figsize=(15, 5))

pos_er = nx.spring_layout(G_er, seed=42)
pos_ba = nx.spring_layout(G_ba, seed=42)
pos_ws = nx.spring_layout(G_ws, seed=42)

plt.subplot(1, 3, 1)
nx.draw(G_er, pos_er, node_size=80, node_color="skyblue", edge_color="gray")
plt.title("Erdős–Rényi")

plt.subplot(1, 3, 2)
nx.draw(G_ba, pos_ba, node_size=80, node_color="lightgreen", edge_color="gray")
plt.title("Barabási–Albert")

plt.subplot(1, 3, 3)
nx.draw(G_ws, pos_ws, node_size=80, node_color="salmon", edge_color="gray")
plt.title("Watts–Strogatz")

plt.tight_layout()
plt.show()