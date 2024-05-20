
import random
import time
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


def criar_clinicas(num_clinicas):
    clinicas = []
    ruas_lisboa = ["Rua A", "Rua B", "Rua C", "Rua D", "Rua E", "Rua F", "Rua G", "Rua H", "Rua I", "Rua J", "Rua K", "Rua L", "Rua M", "Rua N", "Rua O"]
    localidades = ["Lisboa", "Oeiras", "Cascais", "Sintra", "Amadora"]

    for i in range(num_clinicas):
        nome_clinica = f"Clinica {localidades[i % len(localidades)]} {chr(65 + i)}"
        telefone = "21" + "".join([str(random.randint(0, 9)) for _ in range(7)])
        morada = f"{random.choice(ruas_lisboa)}, 1000-{random.randint(100, 999)} {random.choice(localidades)}"
        clinicas.append({"nome": nome_clinica, "telefone": telefone, "morada": morada})

    return clinicas


def escrever_clinicas_em_txt(clinicas):
    nome_arquivo = "populate.sql"
    with open(nome_arquivo, 'w') as file:
        file.write("-- Inserir Clínicas\n")
        file.write("INSERT INTO clinica (nome, telefone, morada) VALUES\n")
        for clinica in clinicas:
            linha = f"('{clinica['nome']}', '{clinica['telefone']}', '{clinica['morada']}'),\n"
            file.write(linha)
    print('\n')
    return nome_arquivo

# Gerar dados das clínicas
num_clinicas = 5
clinicas = criar_clinicas(num_clinicas)

# Escrever os dados no arquivo .txt
nome_arquivo = escrever_clinicas_em_txt(clinicas)

print(f"Os dados das clínicas foram escritos em '{nome_arquivo}'.")

def criar_enfermeiros(num_enfermeiros, clinicas):
    enfermeiros = []
    for clinica in clinicas:
        nome_clinica = clinica['nome']
        for i in range(1, num_enfermeiros + 1):
            nome_enfermeiro = f"Enfermeiro {nome_clinica.split()[-1][0]}{i}"
            nif = ''.join([str(random.randint(0, 9)) for _ in range(9)])
            telefone = "21" + "".join([str(random.randint(0, 9)) for _ in range(7)])
            morada = f"{random.choice(ruas_lisboa)}, 1000-{random.randint(100, 999)} Lisboa"
            enfermeiros.append({"nif": nif, "nome": nome_enfermeiro, "telefone": telefone, "morada": morada, "nome_clinica": nome_clinica})
    return enfermeiros

def escrever_enfermeiros_em_txt(enfermeiros):
    nome_arquivo = "populate.sql"
    with open(nome_arquivo, 'w') as file:
        file.write("-- Inserir Enfermeiros\n")
        file.write("INSERT INTO enfermeiro (nif, nome, telefone, morada, nome_clinica) VALUES\n")
        for enfermeiro in enfermeiros:
            linha = f"('{enfermeiro['nif']}', '{enfermeiro['nome']}', '{enfermeiro['telefone']}', '{enfermeiro['morada']}', '{enfermeiro['nome_clinica']}'),\n"
            file.write(linha)
    print('\n')
    return nome_arquivo

# Gerar dados dos enfermeiros
num_enfermeiros_por_clinica = 5
enfermeiros = criar_enfermeiros(num_enfermeiros_por_clinica, clinicas)

# Escrever os dados no arquivo .txt
nome_arquivo_enfermeiros = escrever_enfermeiros_em_txt(enfermeiros)

print(f"Os dados dos enfermeiros foram escritos em '{nome_arquivo_enfermeiros}'.")

def gerar_medicos():
    especialidades = ["clinica geral", "ortopedia", "cardiologia", "neurologia", "pediatria", "dermatologia", "urologia"]
    medicos = []
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
    return medicos

def escrever_medicos_em_txt(medicos):
    nome_arquivo = "populate.sql"
    with open(nome_arquivo, 'w') as file:
        file.write("-- Inserir Médicos\n")
        file.write("INSERT INTO medico (nif, nome, telefone, morada, especialidade) VALUES\n")
        for medico in medicos[:-1]:
            linha = f"('{medico['nif']}', '{medico['nome']}', '{medico['telefone']}', '{medico['morada']}', '{medico['especialidade']}'),\n"
            file.write(linha)
        medico = medicos[-1]
        linha = f"('{medico['nif']}', '{medico['nome']}', '{medico['telefone']}', '{medico['morada']}', '{medico['especialidade']}');\n"
        file.write(linha)
    print('\n')

# Uso das funções
medicos = gerar_medicos()
escrever_medicos_em_txt(medicos)
print("Os dados dos médicos foram escritos em 'medicos.txt'.")


def gerar_trabalha(medicos, clinicas):
    trabalha = []
    clinicas_nomes = [clinica['nome'] for clinica in clinicas]

    medico_clinica_dias = {medico['nif']: {} for medico in medicos}

    # Atribuir cada médico a duas clínicas aleatórias, garantindo que não estejam alocados a mais de uma clínica no mesmo dia
    for medico in medicos:
        nif = medico['nif']
        clinicas_aleatorias = random.sample(clinicas_nomes, 2)

        for clinica_nome in clinicas_aleatorias:
            for dia_semana in range(7):
                if dia_semana not in medico_clinica_dias[nif]:
                    medico_clinica_dias[nif][dia_semana] = []

                if clinica_nome not in medico_clinica_dias[nif][dia_semana]:
                    medico_clinica_dias[nif][dia_semana].append(clinica_nome)
                    trabalha.append({
                        "nif": nif,
                        "nome": clinica_nome,
                        "dia_da_semana": dia_semana
                    })

    # Garantir que cada clínica tem até 8 médicos alocados em cada dia da semana
    clinica_dias_medicos = {clinica['nome']: {dia: [] for dia in range(7)} for clinica in clinicas}

    for clinica in clinicas:
        clinica_nome = clinica['nome']
        for dia_semana in range(7):
            medicos_disponiveis = [medico['nif'] for medico in medicos if medico['nif'] not in clinica_dias_medicos[clinica_nome][dia_semana]]

            medicos_alocados = random.sample(medicos_disponiveis, min(8, len(medicos_disponiveis)))

            for nif in medicos_alocados:
                clinica_dias_medicos[clinica_nome][dia_semana].append(nif)
                trabalha.append({
                    "nif": nif,
                    "nome": clinica_nome,
                    "dia_da_semana": dia_semana
                })

    return trabalha

def escrever_trabalha_em_txt(trabalha):
    nome_arquivo = f"trabalha_{int(time.time())}.txt"
    with open(nome_arquivo, 'w') as file:
        file.write("-- Inserir Trabalha\n")
        file.write("INSERT INTO trabalha (nif, nome, dia_da_semana) VALUES\n")
        for entry in trabalha[:-1]:
            linha = f"('{entry['nif']}', '{entry['nome']}', {entry['dia_da_semana']}),\n"
            file.write(linha)
        entry = trabalha[-1]
        linha = f"('{entry['nif']}', '{entry['nome']}', {entry['dia_da_semana']});\n"
        file.write(linha)

# Uso das funções
trabalha = gerar_trabalha(medicos, clinicas)
escrever_trabalha_em_txt(trabalha)

import random

def gerar_pacientes(num_pacientes, nif_inicial):
    pacientes = []
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

def escrever_population_txt(pacientes):
    with open("population.txt", "w") as f:
        f.write("-- Inserir Pacientes\n")
        f.write("INSERT INTO paciente (ssn, nif, nome, telefone, morada, data_nasc) VALUES\n")
        
        values = []
        for p in pacientes:
            value = f"('{p['ssn']}', '{p['nif']}', '{p['nome']}', '{p['telefone']}', '{p['morada']}', '{p['data_nasc']}')"
            values.append(value)
        
        f.write(",\n".join(values))
        f.write(";")

# Definir o número de pacientes e o NIF inicial (depois do último médico)
num_pacientes = 5000
nif_inicial = 601111112  # Ajustar conforme necessário

# Gerar dados dos pacientes
pacientes = gerar_pacientes(num_pacientes, nif_inicial)

# Escrever dados no arquivo population.txt
escrever_population_txt(pacientes)


import random
from datetime import datetime, timedelta

import random
from datetime import datetime, timedelta

from datetime import datetime, timedelta
import random
consultas = []

def gerar_consultas(data_inicio, data_fim, trabalha):
    global consultas
    global pacientes
    global medicos
    global clinicas
    
    for paciente in pacientes :

        ssn = paciente['ssn']
        print(ssn)
        data_consulta = random_date(data_inicio, data_fim)
        hora_consulta = random_time_restrict()
        
        # Obter médico aleatório
        medico = random.choice(medicos)
        nome_clinica = escolhe_clinica(medico['nif'], data_consulta.weekday())
        
        # Verificar se o médico trabalha na clínica na data da consulta e se não tem outra consulta no mesmo horário
        while medico_tem_consulta_no_horario(consultas, medico, data_consulta, hora_consulta):
            hora_consulta = random_time_restrict()
           
        # Criar consulta com os dados gerados
        consulta = {
            "ssn": ssn, 
            "nif": medico['nif'],
            "nome_clinica": nome_clinica,
            "data": data_consulta,
            "hora": hora_consulta,
            "codigo_sns": None
        }

        # Adicionar consulta à lista de consultas
        consultas.append(consulta)
    
    # Gerar consultas para cada dia entre a data de início e a data de fim
    for day in range((data_fim - data_inicio).days + 1):
       
        data_consulta = data_inicio + timedelta(days=day)
       
        for clinica in clinicas:
            for i in range(20):
                
                nome_clinica = clinica['nome']
                # Gerar uma hora aleatória para a consulta
                hora_consulta = random_time_restrict()
                paciente = random.choice(pacientes)
                # Obter médico aleatório
                medico = random.choice(medicos)
                while not medico_trabalha_na_clinica_na_data(medico, data_consulta, trabalha) :
                    medico = random.choice(medicos)
                while medico_tem_consulta_no_horario(consultas, medico, data_consulta, hora_consulta):
                    hora_consulta = random_time_restrict()

        
                # Verificar se o médico trabalha na clínica na data da consulta e se não tem outra consulta no mesmo horário
                
                # Criar consulta com os dados gerados
                consulta = {
                    "ssn": paciente['ssn'],
                    "nif": medico['nif'],
                    "nome_clinica": nome_clinica,
                    "data": data_consulta,
                    "hora": hora_consulta,
                    "codigo_sns": None
                }
                
                # Adicionar consulta à lista de consultas
                consultas.append(consulta)
            
        for medico in medicos:
            for i in range(2):
                
                nome_clinica = obter_nome_clinica(medico['nif'], data_consulta.weekday())

                if nome_clinica is None:
                    continue
                hora_consulta = random_time_restrict()
                paciente = random.choice(pacientes)
                
                while medico_tem_consulta_no_horario(consultas, medico, data_consulta, hora_consulta):
                    hora_consulta = random_time_restrict()

                # Criar consulta com os dados gerados
                consulta = {
                    "ssn": paciente['ssn'],
                    "nif": medico['nif'],
                    "nome_clinica": nome_clinica,
                    "data": data_consulta,
                    "hora": hora_consulta,
                    "codigo_sns": generate_codigo_sns()
                }
                
                # Adicionar consulta à lista de consultas
                consultas.append(consulta)
       
    return consultas

def escolhe_clinica(nif_medico, dia_semana):
    for item in trabalha:
        if item['nif'] == nif_medico and item['dia_da_semana'] == dia_semana:
            return item['nome']
    return None

def random_time_restrict():
    # Gerar uma hora aleatória entre 8:00 e 18:30, exceto entre 13:00 e 14:00
    while True:
        hora = random.randint(8, 19)  
        minutos = random.choice([0, 30])  
        while hora >= 13 and hora < 14:
            hora = random.randint(8, 19)
        hora_consulta = '{:02d}:{:02d}:00'.format(hora, minutos)
        # Verificar se a hora está dentro do intervalo permitido
        return hora_consulta
    

def obter_nome_clinica(nif_medico, dia_semana):
    for item in trabalha:
        if item['nif'] == nif_medico and item['dia_da_semana'] == dia_semana:
            return item['nome']
    return None

def medico_tem_consulta_no_horario(consultas, medico, data_consulta, hora_consulta):
    for consulta in consultas:
        if consulta['nif'] == medico['nif'] and consulta['data'] == data_consulta and consulta['hora'] == hora_consulta:
            return True
    return False

def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

def medico_trabalha_na_clinica_na_data(medico, data_consulta, trabalha):
    dia_semana = data_consulta.weekday()  # 0 = segunda-feira, 6 = domingo
    nif_medico = medico['nif']
    for item in trabalha:
        if item['nif'] == nif_medico and item['dia_da_semana'] == dia_semana:
            return True

def generate_codigo_sns():
    return ''.join([str(random.randint(0, 9)) for _ in range(12)])


from datetime import datetime

# Definir datas de início e fim
data_inicio = datetime(2024, 6, 1)
data_fim = datetime(2024, 12, 31)

# Uso das funções
consultas = gerar_consultas(data_inicio, data_fim, trabalha)

# Escrever dados no arquivo consultas.sql
def escrever_consultas_em_sql(consultas):
    with open("populate.sql", "w") as f:
        f.write("-- Inserir Consultas\n")
        f.write("INSERT INTO consulta (ssn, nif, nome, data, hora, codigo_sns) VALUES\n")
        
        values = []
        for consulta in consultas:
            if consulta['codigo_sns'] is not None:
                value = f"('{consulta['ssn']}', '{consulta['nif']}', '{consulta['nome_clinica']}', '{consulta['data'].strftime('%Y-%m-%d')}', '{consulta['hora']}', '{consulta['codigo_sns']}')"
            else:
                value = f"(NULL, '{consulta['nif']}', '{consulta['nome_clinica']}', '{consulta['data'].strftime('%Y-%m-%d')}', '{consulta['hora']}', NULL)"
            values.append(value)
        
        f.write(",\n".join(values))
        f.write(";")
        
escrever_consultas_em_sql(consultas)
