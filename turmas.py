import requests



# URL do endpoint da sua API
url = "https://sag-sag.rak8a3.easypanel.host/api/turmas/batch"


turmas = [
  {
    "nome": "1º ANO/TARDE/2025",
    "escola_id": 29,
    "serie": "PRIMEIRO_ANO",
    "turno": "TARDE"
  },
  {
    "nome": "2º ANO A/MANHÃ/2025",
    "escola_id": 29,
    "serie": "SEGUNDO_ANO",
    "turno": "MANHA"
  },
  {
    "nome": "2º ANO B/MANHÃ/2025",
    "escola_id": 29,
    "serie": "SEGUNDO_ANO",
    "turno": "MANHA"
  },
  {
    "nome": "3º ANO A/TARDE/2025",
    "escola_id": 29,
    "serie": "TERCEIRO_ANO",
    "turno": "TARDE"
  },
  {
    "nome": "3º ANO B/TARDE/2025",
    "escola_id": 29,
    "serie": "TERCEIRO_ANO",
    "turno": "TARDE"
  },
  {
    "nome": "4º ANO A/MANHÃ/2025",
    "escola_id": 29,
    "serie": "QUARTO_ANO",
    "turno": "MANHA"
  },
  {
    "nome": "4º ANO B/TARDE/2025",
    "escola_id": 29,
    "serie": "QUARTO_ANO",
    "turno": "TARDE"
  },
  {
    "nome": "5º ANO/MANHÃ/2025",
    "escola_id": 29,
    "serie": "QUINTO_ANO",
    "turno": "MANHA"
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
