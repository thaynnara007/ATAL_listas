HORA_INICIO = 1
HORA_FIM = 2

def conflito(horaInicio1, horaFim1, horaInicio2, horaFim2):

    HaConflito = True

    if (horaInicio != horaInicio2) and (horaFim1 != horaFim2):

qntdDisciplinas = int(raw_input())
atividades = []

for i in xrange(qntdDisciplinas):

    atividade = raw_input().split()

    nome = atividade[0]
    horaInicio = atividade[HORA_INICIO]
    horaFim = atividade[HORA_FIM]
    atividades.append((nome,horaInicio, horaFim))

atividades.sort()

