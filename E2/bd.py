import random
from datetime import datetime, timedelta

data_inicio = datetime(2025, 1, 1)
data_fim = datetime(2026, 12, 31)

ruas_lisboa = [
    "Rua Augusta", "Avenida da Liberdade", "Rua do Ouro", "Rua da Prata", 
    "Rua Garrett", "Rua do Carmo", "Rua dos Fanqueiros", "Rua dos Bacalhoeiros", 
    "Rua do Alecrim", "Rua das Portas de Santo Antão", "Rua de São Bento", 
    "Rua da Madalena", "Rua do Arsenal", "Rua do Comércio", "Rua da Conceição",
    "Rua dos Douradores", "Rua dos Correeiros", "Rua da Vitória", 
    "Rua da Misericórdia", "Rua de São Nicolau", "Rua da Saudade", 
    "Rua de São Paulo", "Rua da Boavista", "Rua do Conde de Redondo", 
    "Rua das Janelas Verdes", "Rua da Escola Politécnica", "Rua do Salitre", 
    "Rua Castilho", "Rua Tomás Ribeiro", "Rua Braamcamp", "Rua Rodrigo da Fonseca", 
    "Rua Barata Salgueiro", "Rua da Imprensa Nacional", "Rua de São José", 
    "Rua do Telhal", "Rua da Horta Seca", "Rua da Madalena", "Rua do Crucifixo", 
    "Rua de Santa Justa", "Rua do Carmo", "Rua dos Sapateiros", "Rua de São Julião", 
    "Rua de Santo António da Sé", "Rua do Benformoso", "Rua da Mouraria", 
    "Rua da Palma", "Rua dos Cavaleiros", "Rua de São Lázaro", "Rua de Arroios", 
    "Rua de Sapadores", "Rua Morais Soares", "Rua dos Anjos", "Rua do Forno do Tijolo", 
    "Rua da Penha de França", "Rua Visconde de Santarém", "Rua de Dona Estefânia", 
    "Rua Pascoal de Melo", "Rua do Conde Redondo", "Rua de Santa Marta", 
    "Rua Luciano Cordeiro", "Rua Alexandre Herculano", "Rua Braancamp", 
    "Rua Barata Salgueiro", "Rua Joaquim António de Aguiar", "Rua Castilho", 
    "Rua Rodrigo da Fonseca", "Rua das Amoreiras", "Rua de Campo de Ourique", 
    "Rua Ferreira Borges", "Rua Francisco Metrass", "Rua Saraiva de Carvalho", 
    "Rua Ferreira Borges", "Rua Dom João V", "Rua de São Bento", 
    "Rua do Sol ao Rato", "Rua da Escola Politécnica", "Rua de São Marçal", 
    "Rua do Século", "Rua da Imprensa Nacional", "Rua de São Bento", 
    "Rua dos Poiais de São Bento", "Rua de São Paulo", "Rua da Boavista", 
    "Rua dos Remolares", "Rua de São Paulo", "Rua da Cintura do Porto de Lisboa", 
    "Rua Cintura do Porto de Lisboa", "Rua do Instituto Industrial", 
    "Rua Dom Luís I", "Rua de São Bento", "Rua da Imprensa Nacional", 
    "Rua Nova do Loureiro", "Rua da Rosa", "Rua Dom Pedro V", "Rua da Atalaia", 
    "Rua do Norte", "Rua do Diário de Notícias", "Rua da Bica de Duarte Belo", 
    "Rua Marechal Saldanha", "Rua de São Mamede ao Caldas", "Rua de Santa Catarina", 
    "Rua da Academia das Ciências", "Rua de São Pedro de Alcântara", 
    "Rua do Conde de Soure", "Rua de São Bento", "Rua da Escola Politécnica", 
    "Rua de São Marçal", "Rua do Século", "Rua de O Século"
]

medicamentos = [
    "Paracetamol (Tylenol)",
    "Ibuprofeno (Advil, Motrin)",
    "Amoxicilina (Amoxil)",
    "Metformina (Glifage)",
    "Omeprazol (Losec, Prilosec)",
    "Simvastatina (Zocor)",
    "Atorvastatina (Lipitor)",
    "Losartana (Cozaar)",
    "Levotiroxina (Synthroid)",
    "Hidrocortisona (Cortef)",
    "Atenolol (Tenormin)",
    "Lisinopril (Prinivil, Zestril)",
    "Furosemida (Lasix)",
    "Amlodipina (Norvasc)",
    "Clopidogrel (Plavix)",
    "Sertralina (Zoloft)",
    "Escitalopram (Lexapro)",
    "Bupropiona (Wellbutrin)",
    "Trazodona (Desyrel)",
    "Ciprofloxacino (Cipro)",
    "Azitromicina (Zithromax)",
    "Fluoxetina (Prozac)",
    "Cetirizina (Zyrtec)",
    "Loratadina (Claritin)",
    "Diazepam (Valium)",
    "Alprazolam (Xanax)",
    "Tramadol (Ultram)",
    "Prednisona (Deltasone)",
    "Warfarina (Coumadin)",
    "Ranitidina (Zantac)",
    "Esomeprazol (Nexium)",
    "Cetamina (Ketalar)",
    "Dexametasona (Decadron)",
    "Metronidazol (Flagyl)",
    "Clindamicina (Cleocin)",
    "Sulfametoxazol/Trimetoprima (Bactrim, Septra)",
    "Gabapentina (Neurontin)",
    "Lamotrigina (Lamictal)",
    "Levetiracetam (Keppra)",
    "Carbamazepina (Tegretol)",
    "Oxcarbazepina (Trileptal)",
    "Venlafaxina (Effexor)",
    "Duloxetina (Cymbalta)",
    "Aspirina (Bayer)",
    "Diclofenaco (Voltaren)",
    "Meloxicam (Mobic)",
    "Naproxeno (Aleve)",
    "Pantoprazol (Protonix)",
    "Famotidina (Pepcid)"
]

sintomas = [
    'Dor de cabeça', 'Náusea', 'Vómito', 'Febre', 'Tosse',
    'Fadiga', 'Falta de ar', 'Tontura', 'Perda de apetite', 'Dor abdominal',
    'Diarreia', 'Constipação', 'Dor no peito', 'Dor nas articulações', 'Dor muscular',
    'Arrepios', 'Suores noturnos', 'Palpitações', 'Confusão mental', 'Visão turva',
    'Zumbido nos ouvidos', 'Formigamento', 'Comichão', 'Erupção cutânea', 'Inchaço',
    'Icterícia', 'Tosse com sangue', 'Dificuldade para engolir', 'Rigidez matinal',
    'Perda de peso inexplicável', 'Incontinência urinária', 'Urgência urinária', 'Dores de garganta',
    'Rouquidão', 'Sonolência', 'Alterações de humor', 'Depressão', 'Ansiedade',
    'Insônia', 'Pesadelos', 'Paralisia', 'Espasmos musculares', 'Fraqueza',
    'Tremores', 'Sensação de desmaio', 'Desmaios', 'Dor na lombar', 'Dor de dentes',
    'Queimação ao urinar', 'Alterações no paladar'
]

medicoes = [
    'Temperatura corporal', 'Frequência cardíaca', 'Pressão arterial sistólica', 'Pressão arterial diastólica', 'Saturação de oxigênio',
    'Nível de glicose no sangue', 'Peso corporal', 'Altura', 'Índice de massa corporal', 'Taxa de respiração',
    'Nível de colesterol total', 'Nível de HDL', 'Nível de LDL', 'Nível de triglicerídeos', 'Taxa de filtração glomerular',
    'Volume urinário', 'Taxa de sedimentação de eritrócitos', 'Hemoglobina', 'Contagem de leucócitos','pressão diastólica',
]

clinicas, enfermeiros, medicos, trabalha, pacientes = [], [], [], [], []
consultas, receitas, observacoes, horarios_disponiveis = [], [], [], []

# Funções auxiliares à geração de dados
def paciente_tem_consulta_no_horario(paciente, data_consulta, hora_consulta):
    global consultas
    for consulta in consultas:
        if consulta['ssn'] == paciente['ssn'] and consulta['data'] == data_consulta and consulta['hora'] == hora_consulta:
            return True
    return False

def medico_tem_consulta_no_horario(medico, data_consulta, hora_consulta):
    global consultas
    for consulta in consultas:
        if consulta['nif'] == medico['nif'] and consulta['data'] == data_consulta and consulta['hora'] == hora_consulta:
            return True
    return False

def get_clinica(nif_medico, dia_semana):
    global trabalha
    for item in trabalha:
        if item['nif'] == nif_medico and item['dia_da_semana'] == dia_semana:
            return item['nome']

def random_date(start, end):
    # Gerar uma data aleatória dentro do intervalo especificado
    start_timestamp = start.timestamp()
    end_timestamp = end.timestamp()
    random_timestamp = random.uniform(start_timestamp, end_timestamp)
    random_date = datetime.fromtimestamp(random_timestamp)
    random_date_str = random_date.strftime("%Y-%m-%d")
    return random_date_str

def random_time_restrict():
    # Gerar uma hora aleatória entre 8:00 e 19:00, exceto entre 13:00 e 14:00
    hora = random.randint(8, 18)  
    minutos = random.choice([0, 30]) 
    while hora == 13 :
        hora = random.randint(8, 18)  
        minutos = random.choice([0, 30]) 

    hora_consulta = '{:02d}:{:02d}:00'.format(hora, minutos)
    # Verificar se a hora está dentro do intervalo permitido
    return hora_consulta
    
def get_medicos_clinica(dia_semana, clinica):
    global medicos
    medicos_clinica = []
    for item in trabalha:
        if item['nome'] == clinica['nome'] and item['dia_da_semana'] == dia_semana:
            for medico in medicos:
                if medico['nif'] == item['nif']:
                    medicos_clinica.append(medico)
    return medicos_clinica


def medicos_livres(dia_semana):
    global medicos
    global trabalha 
    medicos_livres_ = []
    for medico in medicos:
        if not any(item['nif'] == medico['nif'] and item['dia_da_semana'] == dia_semana for item in trabalha):
            medicos_livres_.append(medico)
    return medicos_livres_

# Funções de geração de dados
def gerar_clinicas(num_clinicas):
    global clinicas
    ruas_lisboa = ["Rua A", "Rua B", "Rua C", "Rua D", "Rua E", "Rua F", "Rua G", "Rua H", "Rua I", "Rua J", "Rua K", "Rua L", "Rua M", "Rua N", "Rua O"]
    localidades = ["Lisboa", "Oeiras", "Cascais", "Sintra", "Amadora"]

    for i in range(num_clinicas):
        nome_clinica = f"Clinica {localidades[i % len(localidades)]} {chr(65 + i)}"
        telefone = "21" + "".join([str(random.randint(0, 9)) for _ in range(7)])
        morada = f"{random.choice(ruas_lisboa)}, 1000-{random.randint(100, 999)} {random.choice(localidades)}"
        clinicas.append({"nome": nome_clinica, "telefone": telefone, "morada": morada})

def gerar_enfermeiros(num_enfermeiros):
    global enfermeiros
    for clinica in clinicas:
        nome_clinica = clinica['nome']
        for i in range(1, num_enfermeiros + 1):
            nome_enfermeiro = f"Enfermeiro {nome_clinica.split()[-1][0]}{i}"
            nif = ''.join([str(random.randint(0, 9)) for _ in range(9)])
            telefone = "21" + "".join([str(random.randint(0, 9)) for _ in range(7)])
            morada = f"{random.choice(ruas_lisboa)}, 1000-{random.randint(100, 999)} Lisboa"
            enfermeiros.append({"nif": nif, "nome": nome_enfermeiro, "telefone": telefone, "morada": morada, "nome_clinica": nome_clinica})

def gerar_medicos():
    global medicos
    outras_especialidades = ["ortopedia", "cardiologia", "neurologia", "pediatria", "dermatologia"]
    for i in range(1, 61):

        nif = str(i).zfill(9)
        nome_medico = f"Medico {i}"
        telefone = "2100000" + str(i + 20).zfill(2)
        morada = f"{random.choice(ruas_lisboa)}, 1000-{random.randint(100, 999)} Lisboa"

        if i <= 20: especialidade = "clinica geral"
        else: especialidade = random.choice(outras_especialidades)

        medicos.append({
            "nif": nif,
            "nome": nome_medico,
            "telefone": telefone,
            "morada": morada,
            "especialidade": especialidade
        })

def get_medicos_sem_trabalho_suficiente():
    global medicos
    global trabalha
    medicos_sem_trabalho, trabalho = [], 0

    for medico in medicos:
        for item in trabalha:
            if item['nif'] == medico['nif']:
                trabalho += 1
        if trabalho < 2:
            medicos_sem_trabalho.append([medico, trabalho])
        trabalho = 0

    return medicos_sem_trabalho

def gerar_trabalha():

    global trabalha
    global medicos
    global clinicas

    for i in range(7):
        for clinica in clinicas:
            
            medicos_livres_dia = medicos_livres(i)

            for j in range(8):

                trabalha.append({
                    "nif": medicos_livres_dia[j]['nif'],
                    "nome": clinica['nome'],
                    "dia_da_semana": i
                })

    medicos_s_trabalho = get_medicos_sem_trabalho_suficiente()

    for medico, dias in medicos_s_trabalho:

        dias = 2 - dias
        dias_trabalho = random.sample(range(7), dias)
        clinicas_possiveis = random.sample(clinicas, dias)

        while medico in get_medicos_clinica(dias_trabalho[0], clinicas_possiveis[0]) or\
            medico in get_medicos_clinica(dias_trabalho[1], clinicas_possiveis[1]) or\
            dias_trabalho[0] == dias_trabalho[1]:

            dias_trabalho = random.sample(range(7), dias)
            clinicas_possiveis = random.sample(clinicas, dias)
        
        for i in range(dias):
            trabalha.append({
                "nif": medico['nif'],
                "nome": clinicas_possiveis[i]['nome'],
                "dia_da_semana": dias_trabalho[i]
            })

def gerar_pacientes(num_pacientes, nif_inicial):
    global pacientes
    localidades = ['Alfama', 'Baixa', 'Belém', 'Chiado', 'Graça', 'Mouraria', 'Parque das Nações', 'Restelo', 'Areeiro', 'Campo de Ourique']
    
    for i in range(num_pacientes):
        contador = nif_inicial + i
        nome = f"Paciente {contador}"
        
        # Gerar código postal no formato XXXX-XXX
        codigo_postal = f"{random.randint(1000, 9999)}-{random.randint(100, 999)}"
        
        # Selecionar localidade aleatoriamente dentro de Lisboa
        localidade = random.choice(localidades)
        
        # Construir a morada
        morada = f"Rua {contador}, {codigo_postal} {localidade}"
        
        # Gerar ssn e nif
        ssn = f"{contador:011d}"
        nif = f"{contador:09d}"
        
        # Gerar telefone
        telefone = f"210{random.randint(1000000, 9999999)}"
        
        # Gerar data de nascimento
        ano = random.randint(1950, 2000)
        mes = random.randint(1, 12)
        dia = random.randint(1, 28)  # Simples para evitar problemas com meses curtos
        data_nasc = f"{ano:04d}-{mes:02d}-{dia:02d}"
        
        pacientes.append({
            "ssn": ssn,
            "nif": nif,
            "nome": nome,
            "telefone": telefone,
            "morada": morada,
            "data_nasc": data_nasc
        })
    

id_consulta = 1

def gerar_consultas_pacientes():
    global consultas
    global pacientes
    global medicos
    global clinicas
    global trabalha
    global id_consulta
    global data_inicio
    global data_fim
    
    for paciente in pacientes :

        ssn = paciente['ssn']
        
        data_consulta_str = random_date(data_inicio, data_fim)
        dia_semana = datetime.strptime(data_consulta_str, "%Y-%m-%d").weekday()
        hora_consulta = random_time_restrict()

        clinica = random.choice(clinicas)
        nome_clinica = clinica['nome']
        medicos_clinica = get_medicos_clinica(dia_semana, clinica)

        if not medicos_clinica:
            continue

        medico = random.choice(medicos_clinica)

        while medico_tem_consulta_no_horario(medico, data_consulta_str, hora_consulta):
            medico = random.choice(medicos_clinica)
            hora_consulta = random_time_restrict()

        # Criar consulta com os dados gerados
        consulta = {
            "id": id_consulta,
            "ssn": ssn, 
            "nif": medico['nif'],
            "nome_clinica": nome_clinica,
            "data": data_consulta_str,
            "hora": hora_consulta,
            "codigo_sns": None
        }
        # Adicionar consulta à lista de consultas
        id_consulta += 1
        consultas.append(consulta)

def gerar_consultas_medicos():
    global consultas
    global medicos
    global pacientes
    global id_consulta
    global data_inicio
    global data_fim  

    for day in range((data_fim - data_inicio).days + 1):
        data_consulta = (data_inicio + timedelta(days=day)).date()
        for medico in medicos:
            nome_clinica = get_clinica(medico['nif'], data_consulta.weekday())
            if nome_clinica is None:
                continue
            for i in range(2):
                hora_consulta = random_time_restrict()
                paciente = random.choice(pacientes)
                data_consulta_str = data_consulta.strftime("%Y-%m-%d")

                while paciente_tem_consulta_no_horario(paciente, data_consulta_str, hora_consulta)\
                        or medico_tem_consulta_no_horario(medico, data_consulta_str, hora_consulta):
                    hora_consulta = random_time_restrict()
                consulta = {
                    "id": id_consulta,
                    "ssn": paciente['ssn'],
                    "nif": medico['nif'],
                    "nome_clinica": nome_clinica,
                    "data": data_consulta_str,
                    "hora": hora_consulta,
                    "codigo_sns": None
                }
                id_consulta += 1
                consultas.append(consulta)

def gerar_consultas_clinicas():
    global consultas
    global clinicas
    global pacientes
    global medicos
    global id_consulta
    global data_inicio
    global data_fim

    for day in range((data_fim - data_inicio).days + 1):

        data_consulta = (data_inicio + timedelta(days=day)).date()
        data_consulta_str = data_consulta.strftime("%Y-%m-%d")

        for clinica in clinicas:
            nome_clinica = clinica['nome']
            medicos_clinica = get_medicos_clinica(data_consulta.weekday(), clinica)

            for i in range(20):
                hora_consulta = random_time_restrict()
                paciente = random.choice(pacientes)
                medico = random.choice(medicos_clinica)
                while paciente_tem_consulta_no_horario(paciente, data_consulta_str, hora_consulta) or \
                    medico_tem_consulta_no_horario(medico, data_consulta_str, hora_consulta):
                    medico = random.choice(medicos_clinica)
                    hora_consulta = random_time_restrict()
                consulta = {
                    "id": id_consulta,
                    "ssn": paciente['ssn'],
                    "nif": medico['nif'],
                    "nome_clinica": nome_clinica,
                    "data": data_consulta_str,
                    "hora": hora_consulta,
                    "codigo_sns": None
                }
                id_consulta += 1
                consultas.append(consulta)
            
def gerar_consultas():
    gerar_consultas_pacientes()
    gerar_consultas_medicos()   
    gerar_consultas_clinicas()
    
    tamanho = int (len(consultas) * 0.8)
    for i in range(tamanho):
        consulta = consultas[i]
        if consulta['codigo_sns'] is None:
            consulta['codigo_sns'] = gerar_codigo_sns()  
    
def gerar_codigo_sns():
    return ''.join([str(random.randint(0, 9)) for _ in range(12)])

def gerar_receitas():
    global consultas
    global receitas
    global medicamentos
    for consulta in consultas:
        if consulta['codigo_sns'] is not None:
            numero_medicamentos = random.randint(1, 6)
            medicamentos_escolhidos = random.sample(medicamentos, numero_medicamentos)
            for medicamento in medicamentos_escolhidos:
                quantidade = random.randint(1, 3)
                receitas.append({
                    "codigo_sns": consulta['codigo_sns'],
                    "medicamento": medicamento,
                    "quantidade": quantidade
                })

def gerar_observacoes():
    global consultas
    global sintomas
    global medicoes
    global observacoes
    for consulta in consultas:
        numero_sintomas = random.randint(1, 5)
        sintomas_escolhidos = random.sample(sintomas, numero_sintomas)
        for sintoma in sintomas_escolhidos:
            observacoes.append({
                "id": consulta['id'],
                "sintoma": sintoma,
                "valor": None
            })
        numero_metricas = random.randint(0, 3)
        metricas_escolhidas = random.sample(medicoes, numero_metricas)
        for metrica in metricas_escolhidas:
            valor = random.uniform(0, 100)
            observacoes.append({
                "id": consulta['id'],
                "medicao": metrica,
                "valor": valor
            })


def gerar_horarios_disponiveis():
    global medicos
    global clinicas
    global horarios_disponiveis
    global consultas
    
    nova_data_inicio = datetime.now().date()
    nova_data_fim = datetime.now().date() + timedelta(days=30)

    for day in range((nova_data_fim - nova_data_inicio).days + 1):
        for hora in range(8, 19):
            for minuto in [0,30]:
                if hora == 13:
                    continue
                horarios_disponiveis.append({
                    "hora": f"{hora:02d}:{minuto:02d}:00",
                    "data": (nova_data_inicio + timedelta(days=day)).strftime("%Y-%m-%d")
                })

# Funções de escrita
def escrever_clinicas():
    global clinicas
    nome_arquivo = "populate1.sql"
    with open(nome_arquivo, 'w') as file:
        file.write("-- Inserir Clínicas\n")
        file.write("INSERT INTO clinica (nome, telefone, morada) VALUES\n")
        for clinica in clinicas[:-1]:
            linha = f"('{clinica['nome']}', '{clinica['telefone']}', '{clinica['morada']}'),\n"
            file.write(linha)
        clinica = clinicas[-1]
        linha = f"('{clinica['nome']}', '{clinica['telefone']}', '{clinica['morada']}');\n"
        file.write(linha)

def escrever_enfermeiros():
    global enfermeiros
    nome_arquivo = "populate2.sql"
    with open(nome_arquivo, 'w') as file:
        file.write("-- Inserir Enfermeiros\n")
        file.write("INSERT INTO enfermeiro (nif, nome, telefone, morada, nome_clinica) VALUES\n")
        for enfermeiro in enfermeiros[:-1]:
            linha = f"('{enfermeiro['nif']}', '{enfermeiro['nome']}', '{enfermeiro['telefone']}', '{enfermeiro['morada']}', '{enfermeiro['nome_clinica']}'),\n"
            file.write(linha)
        enfermeiro = enfermeiros[-1]
        linha = f"('{enfermeiro['nif']}', '{enfermeiro['nome']}', '{enfermeiro['telefone']}', '{enfermeiro['morada']}', '{enfermeiro['nome_clinica']}');\n"
        file.write(linha)

def escrever_medicos():
    global medicos
    nome_arquivo = "populate3.sql"
    with open(nome_arquivo, 'w') as file:
        file.write("-- Inserir Médicos\n")
        file.write("INSERT INTO medico (nif, nome, telefone, morada, especialidade) VALUES\n")
        for medico in medicos[:-1]:
            linha = f"('{medico['nif']}', '{medico['nome']}', '{medico['telefone']}', '{medico['morada']}', '{medico['especialidade']}'),\n"
            file.write(linha)
        medico = medicos[-1]
        linha = f"('{medico['nif']}', '{medico['nome']}', '{medico['telefone']}', '{medico['morada']}', '{medico['especialidade']}');\n"
        file.write(linha)

def escrever_trabalha():
    global trabalha
    nome_arquivo = "populate4.sql"
    with open(nome_arquivo, 'w') as file:
        file.write("-- Inserir Trabalha\n")
        file.write("INSERT INTO trabalha (nif, nome, dia_da_semana) VALUES\n")
        for i in range(len(trabalha)):
            x = trabalha[i]['dia_da_semana']
            day = None
            if x == 6:
                day = 0
            else:
                day = x + 1
            
            if i != len(trabalha) - 1:
                linha = f"('{trabalha[i]['nif']}', '{trabalha[i]['nome']}', {day}),\n"
            else:
                linha = f"('{trabalha[i]['nif']}', '{trabalha[i]['nome']}', {day});\n"
            file.write(linha)

def escrever_pacientes():
    global pacientes
    with open("populate5.sql", "w") as f:
        f.write("-- Inserir Pacientes\n")
        f.write("INSERT INTO paciente (ssn, nif, nome, telefone, morada, data_nasc) VALUES\n")
        
        values = []
        for p in pacientes:
            value = f"('{p['ssn']}', '{p['nif']}', '{p['nome']}', '{p['telefone']}', '{p['morada']}', '{p['data_nasc']}')"
            values.append(value)
        
        f.write(",\n".join(values))
        f.write(";")

def escrever_consultas():
    global consultas
    with open("populate6.sql", "w") as f:
        f.write("-- Inserir Consultas\n")
        f.write("INSERT INTO consulta (id,ssn, nif, nome, data, hora, codigo_sns) VALUES\n")
        
        values = []
        for consulta in consultas:
            if consulta['codigo_sns'] is not None:
                value = f"('{consulta['id']}','{consulta['ssn']}', '{consulta['nif']}', '{consulta['nome_clinica']}', '{consulta['data']}', '{consulta['hora']}', '{consulta['codigo_sns']}')"
            else:
                value = f"('{consulta['id']}','{consulta['ssn']}', '{consulta['nif']}', '{consulta['nome_clinica']}', '{consulta['data']}', '{consulta['hora']}', NULL)"
            values.append(value)
        
        f.write(",\n".join(values))
        f.write(";")

def escrever_receitas():
    global receitas
    with open("populate7.sql", "w") as f:
        f.write("-- Inserir Receitas\n")
        f.write("INSERT INTO receita (codigo_sns, medicamento, quantidade) VALUES\n")
        
        values = []
        for receita in receitas:
            value = f"('{receita['codigo_sns']}', '{receita['medicamento']}', {receita['quantidade']})"
            values.append(value)
        
        f.write(",\n".join(values))
        f.write(";")
  
def escrever_observacoes():
    global observacoes
    with open("populate8.sql", "w") as f:
        f.write("-- Inserir Observações\n")
        f.write("INSERT INTO observacao (id, parametro, valor) VALUES\n")
        
        values = []
        for observacao in observacoes:
            if observacao['valor'] is not None:
                value = f"('{observacao['id']}', '{observacao['medicao']}', {observacao['valor']})"
            else:
                value = f"('{observacao['id']}', '{observacao['sintoma']}', NULL)"
            values.append(value)
        
        f.write(",\n".join(values))
        f.write(";")

def escrever_horarios():
    global horarios_disponiveis
    with open("populate9.sql", "w") as f:
        f.write("-- Inserir Horários Disponíveis\n")
        f.write("INSERT INTO horario_disponivel (data, hora) VALUES\n")
        
        values = []
        for horario in horarios_disponiveis:
            value = f"('{horario['data']}', '{horario['hora']}')"
            values.append(value)
        f.write(",\n".join(values))
        f.write(";")


# Criar clinicas
gerar_clinicas(5)
escrever_clinicas()
print(1)
# Criar enfermeiros
gerar_enfermeiros(5)
escrever_enfermeiros()
print(2)
# Criar médicos
gerar_medicos()
escrever_medicos()
print(3)
# Atribuir trabalhos
gerar_trabalha()
escrever_trabalha()
print(4)
# Criar pacientes
gerar_pacientes(5000, 601111112)
escrever_pacientes()
print(5)
# Gerar consultas
gerar_consultas()
escrever_consultas()
print(6)
# Gerar receitas
gerar_receitas()
escrever_receitas()
print(7)
# Gerar observações
gerar_observacoes()
escrever_observacoes()
print(8)
# Gerar horários disponíveis
gerar_horarios_disponiveis()
escrever_horarios()
print(9)

# Juntar os ficheiros SQL gerados
with open('populate_geral.sql', 'w') as arquivo_final:
    for nome_arquivo in ['populate1.sql', 'populate2.sql', 'populate3.sql', 'populate4.sql',\
        'populate5.sql', 'populate6.sql', 'populate7.sql', 'populate8.sql', 'populate9.sql']:
        with open(nome_arquivo, 'r') as arquivo_atual:
            arquivo_final.write(arquivo_atual.read() + '\n')