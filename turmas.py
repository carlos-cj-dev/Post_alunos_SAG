import requests



# URL do endpoint da sua API
url = "https://sag-sag.rak8a3.easypanel.host/api/turmas/batch"


turmas = [
  {
    "nome": "1º ANO/INTEGRAL/2025",
    "escola_id": 50,
    "serie": "PRIMEIRO_ANO",
    "turno": "INTEGRAL"
  },
  {
    "nome": "2º ANO/INTEGRAL/2025",
    "escola_id": 50,
    "serie": "SEGUNDO_ANO",
    "turno": "INTEGRAL"
  },
  {
    "nome": "3º ANO/INTEGRAL/2025",
    "escola_id": 50,
    "serie": "TERCEIRO_ANO",
    "turno": "INTEGRAL"
  },
  {
    "nome": "4º ANO/INTEGRAL/2025",
    "escola_id": 50,
    "serie": "QUARTO_ANO",
    "turno": "INTEGRAL"
  },
  {
    "nome": "5º ANO/INTEGRAL/2025",
    "escola_id": 50,
    "serie": "QUINTO_ANO",
    "turno": "INTEGRAL"
  },
  {
    "nome": "6º ANO/INTEGRAL/2025",
    "escola_id": 50,
    "serie": "SEXTO_ANO",
    "turno": "INTEGRAL"
  },
  {
    "nome": "7º ANO/INTEGRAL/2025",
    "escola_id": 50,
    "serie": "SETIMO_ANO",
    "turno": "INTEGRAL"
  },
  {
    "nome": "8º ANO/INTEGRAL/2025",
    "escola_id": 50,
    "serie": "OITAVO_ANO",
    "turno": "INTEGRAL"
  },
  {
    "nome": "9º ANO/INTEGRAL/2025",
    "escola_id": 50,
    "serie": "NONO_ANO",
    "turno": "INTEGRAL"
  }
]

# Cabeçalhos, incluindo token se necessário
headers = {
    "Content-Type": "application/json"
}

# Enviando os dados para a API
response = requests.post(url, json=turmas, headers=headers)

# Verificando o resultado
if response.status_code in [200, 201]:
    print("Turmas cadastradas com sucesso!")
    print(response.json())  # resposta da API
else:
    print("Erro ao cadastrar turmas:")
    print(f"Status: {response.status_code}")
    print(response.text)
