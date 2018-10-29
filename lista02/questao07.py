HORA_INICIO = 1
HORA_FIM = 2

def conflito(horaInicio, horaFim):

    global horasOcupadas

    haConflito = False

    for hora in xrange(horaInicio, horaFim):

        haConflito = haConflito or horasOcupadas[hora]

        if haConflito: break

    return haConflito

def marcaHorario(horaInicio, horaFim):

    global horasOcupadas

    for hora in xrange(horaInicio, horaFim):
        horasOcupadas[hora] = True

def encontraAtividades():

    global atividades
    global atividadesPegas
    global horasOcupadas

    for atividade in atividades:

        if not conflito(atividade[HORA_INICIO], atividade[HORA_FIM]):
            
            atividadesPegas.append(atividade)
            marcaHorario(atividade[HORA_INICIO], atividade[HORA_FIM])
          

qntdDisciplinas = int(raw_input())
atividades = []
atividadesPegas = []
horasOcupadas = [False for i in xrange(25)]

for i in xrange(qntdDisciplinas):

    atividade = raw_input().split()

    nome = atividade[0]
    horaInicio = int(atividade[HORA_INICIO])
    horaFim = int(atividade[HORA_FIM])
    intervalo = horaFim - horaInicio
    atividades.append((intervalo,horaInicio, horaFim, nome))

atividades.sort()
encontraAtividades()

print "--------------------ATIVIDADES SEM CONFLITOS-------------------------------------------"
for atividade in atividadesPegas:

    print '%s: %d - %d' %(atividade[3], atividade[HORA_INICIO], atividade[HORA_FIM])

