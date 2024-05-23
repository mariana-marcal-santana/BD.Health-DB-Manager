import random
from datetime import datetime, timedelta

data_inicio = datetime(2023, 12, 1)
data_fim = datetime(2024, 1, 1)

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
    'Volume urinário', 'Taxa de sedimentação de eritrócitos', 'Hemoglobina', 'Contagem de leucócitos'
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
    hora = random.randint(8, 19)  
    minutos = random.choice([0, 30]) 
    while hora == 13 and minutos == 30 or hora == 19 and minutos == 30:
        hora = random.randint(8, 19)  
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

def medico_trabalha_no_dia(medico, dia_semana):
    global trabalha
    for item in trabalha:
        if item['nif'] == medico['nif'] and item['dia_da_semana'] == dia_semana:
            return True
    return False

def medicos_livres(dia_semana):
    global medicos
    global trabalha 
    medicos_livres_ = []
    for medico in medicos:
        if not medico_trabalha_no_dia(medico, dia_semana):
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

def gerar_enfermeiros(num_enfermeiros, clinicas):
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
    especialidades = ["clinica geral", "ortopedia", "cardiologia", "neurologia", "pediatria", "dermatologia", "urologia"]
    for i in range(1, 61):
        nif = str(i).zfill(9)
        nome_medico = f"Medico {i}"
        telefone = "2100000" + str(i + 20).zfill(2)
        morada = f"{random.choice(ruas_lisboa)}, 1000-{random.randint(100, 999)} Lisboa"
        especialidade = especialidades[(i - 1) // 10]  # Alterna a cada 10 médicos
        medicos.append({
            "nif": nif,
            "nome": nome_medico,
            "telefone": telefone,
            "morada": morada,
            "especialidade": especialidade
        })

def gerar_trabalha():
   
    global trabalha
    global medicos
    # Atribuindo médicos a duas clínicas em dois dias da semana
    
    for medico in medicos:
        duas_clinicas = random.sample(clinicas, 2)
        dias_semana = random.sample(range(7), 2)
        while dias_semana[0] == dias_semana[1]:
            print("Dias iguais")
            dias_semana = random.sample(range(7), 2)
        for i in range(2):
            trabalha.append({
                "nif": medico['nif'],
                "nome": duas_clinicas[i]['nome'],
                "dia_da_semana": dias_semana[i]
            })

    for dia_semana in range(7):
        for clinica in clinicas:
            for i in range(8):  
                medicos_livres_ = medicos_livres(dias_semana)
                if medicos_livres_ == []:
                    print(f"Nenhum médico disponível em {dia_semana} para a clínica {clinica['nome']}")
                    continue
                medico = random.choice(medicos_livres_)
                trabalha.append({
                    "nif": medico['nif'],
                    "nome": clinica['nome'],
                    "dia_da_semana": dia_semana
                })
                for medico in medicos_livres_:
                    medicos_livres_.remove(medico)
            
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
    
    return pacientes

id_consulta = 1
def gerar_consultas_pacientes(data_inicio, data_fim):
    global consultas
    global pacientes
    global medicos
    global clinicas
    global trabalha
    global id_consulta
    
    for paciente in pacientes :

        ssn = paciente['ssn']
        
        data_consulta_str = random_date(data_inicio, data_fim)
        dia_semana = datetime.strptime(data_consulta_str, "%Y-%m-%d").weekday()
        hora_consulta = random_time_restrict()

        clinica = random.choice(clinicas)
        nome_clinica = clinica['nome']
        medicos_clinica = get_medicos_clinica(dia_semana, clinica)
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

def gerar_consultas_medicos(data_inicio, data_fim):
    global consultas
    global medicos
    global pacientes
    global id_consulta  

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

def gerar_consultas_clinicas(data_inicio, data_fim):
    global consultas
    global clinicas
    global pacientes
    global medicos
    global id_consulta

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
            
def gerar_consultas(data_inicio, data_fim):

    gerar_consultas_pacientes(data_inicio, data_fim)
    gerar_consultas_medicos(data_inicio, data_fim)   
    gerar_consultas_clinicas(data_inicio, data_fim)
    
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

    for day in range((data_fim - data_inicio).days + 1):
        possivel_data = (data_inicio + timedelta(days=day)).date()
        possivel_hora = datetime.time(8, 0)
        for medico in medicos:
            while medico_tem_consulta_no_horario(medico, possivel_data, possivel_hora):
                possivel_hora = datetime.time(possivel_hora.hour, possivel_hora.minute + 30)
            if possivel_hora == datetime.time(13, 30):
                possivel_hora = datetime.time(14, 0)
            elif possivel_hora > datetime.time(19, 0):
                continue
            clinica =  get_clinica(medico['nif'], possivel_data.weekday())
            horarios_disponiveis.append({
                "nif": medico['nif'],
                "clinica": clinica['nome'],
                "especialidade": medico['especialidade'],
                "data": possivel_data,
                "hora": possivel_hora
            })
            possivel_hora = datetime.time(possivel_hora.hour, possivel_hora.minute + 30)
    return horarios_disponiveis

# Funções de escrita
def escrever_clinicas(clinicas):
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

def escrever_enfermeiros(enfermeiros):
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

def escrever_medicos(medicos):
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
        for entry in trabalha[:-1]:
            x = entry['dia_da_semana']
            day = None
            if x == 6:
                day = 0
            else:
                day = x + 1
            
            linha = f"('{entry['nif']}', '{entry['nome']}', {day}),\n"
            file.write(linha)
        entry = trabalha[-1]
        linha = f"('{entry['nif']}', '{entry['nome']}', {day});\n"
        file.write(linha)

def escrever_pacientes(pacientes):
    with open("populate5.sql", "w") as f:
        f.write("-- Inserir Pacientes\n")
        f.write("INSERT INTO paciente (ssn, nif, nome, telefone, morada, data_nasc) VALUES\n")
        
        values = []
        for p in pacientes:
            value = f"('{p['ssn']}', '{p['nif']}', '{p['nome']}', '{p['telefone']}', '{p['morada']}', '{p['data_nasc']}')"
            values.append(value)
        
        f.write(",\n".join(values))
        f.write(";")

def escrever_consultas(consultas):
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

def escrever_receitas(receitas):
    with open("populate7.sql", "w") as f:
        f.write("-- Inserir Receitas\n")
        f.write("INSERT INTO receita (codigo_sns, medicamento, quantidade) VALUES\n")
        
        values = []
        for receita in receitas:
            value = f"('{receita['codigo_sns']}', '{receita['medicamento']}', {receita['quantidade']})"
            values.append(value)
        
        f.write(",\n".join(values))
        f.write(";")
  
def escrever_observacoes(observacoes):
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

# Criar clinicas
gerar_clinicas(5)
escrever_clinicas(clinicas)
# Criar enfermeiros
gerar_enfermeiros(5, clinicas)
escrever_enfermeiros(enfermeiros)
# Criar médicos
gerar_medicos()
escrever_medicos(medicos)
# Atribuir trabalhos
gerar_trabalha()
escrever_trabalha()
# Criar pacientes
pacientes = gerar_pacientes(5000, 601111112)
escrever_pacientes(pacientes)
# Gerar consultas
gerar_consultas(data_inicio, data_fim)
escrever_consultas(consultas)
# Gerar receitas
gerar_receitas()
escrever_receitas(receitas)
# Gerar observações
gerar_observacoes()
escrever_observacoes(observacoes)