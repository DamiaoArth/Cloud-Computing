# 🛠️ API de Produtos com AWS Lambda, API Gateway e DynamoDB (Python)

Este projeto cria uma API REST com as operações `GET` e `POST` para manipular produtos armazenados no DynamoDB. A arquitetura utiliza AWS Lambda, API Gateway (HTTP API) e DynamoDB, implementado com Python.

---

## 🧱 1. Criar a Tabela no DynamoDB

**Acesse:**  
AWS Console → DynamoDB → Tabelas → Criar tabela

### Configuração:
- **Nome da tabela**: `Produtos`
- **Chave primária**:  
  - `id` (tipo `String`)

✅ Não é necessário adicionar outras colunas — o DynamoDB permite atributos dinâmicos.

**📸 Prints recomendados:**
- `Print 1` - Tela principal do DynamoDB (lista de tabelas)
- `Print 2` - Tela de criação da tabela
- `Print 3` - Configuração da chave primária

---

## ⚙️ 2. Criar a Função Lambda

**Acesse:**  
AWS Console → Lambda → Criar função

### Configuração:
- Criar do zero
- **Nome da função**: `api-produtos-lambda`
- **Tempo de execução**: Python 3.12 (ou versão disponível mais recente)
- Clique em **Criar função**

### Código:
- Substitua o conteúdo da função Lambda pelo arquivo [`lambda_function.py`](./lambda_function.py) deste repositório.

### Permissões:
- Vá em **Permissões → Função de execução → Políticas**
- Clique em **Anexar políticas**
- Adicione a política: `AmazonDynamoDBFullAccess`

**📸 Prints recomendados:**
- `Print 4` - Tela de criação da função Lambda
- `Print 5` - Editor de código com o nome do arquivo
- `Print 6` - Tela de permissões com política DynamoDB anexada

---

## 🌐 3. Criar a API Gateway (HTTP API)

**Acesse:**  
AWS Console → API Gateway → Criar API → HTTP API

### Rota:
- Caminho: `/produtos`
- Método: `ANY`
- Integração com a função Lambda criada

### Estágio:
- Nome do estágio: `prod`
- Copie o endpoint gerado após criar

Formato da URL final:
```
https://<api-id>.execute-api.sa-east-1.amazonaws.com/prod/produtos
```

**📸 Prints recomendados:**
- `Print 7` - Tela inicial da criação de API HTTP
- `Print 8` - Tela de configuração das rotas
- `Print 9` - Integração com Lambda
- `Print 10` - Estágio criado e URL final

---

## 🧪 4. Testando a API

### POST `/produtos` — Inserir Produto
```bash
curl -X POST https://<api-id>.execute-api.sa-east-1.amazonaws.com/prod/produtos \
  -H "Content-Type: application/json" \
  -d '{"nome": "Camiseta", "preco": 49.90}'
```

### GET `/produtos` — Listar Produtos
```bash
curl https://<api-id>.execute-api.sa-east-1.amazonaws.com/prod/produtos
```

**📸 Prints recomendados:**
- `Print 11` - Teste no terminal ou Postman
- `Print 12` - Log do CloudWatch com eventos recebidos

---

## 🔧 Extras

### ✅ Ativar CORS (se necessário):
- API Gateway → Rota → Configurações → Habilitar CORS → Habilitar para métodos `GET`, `POST`, `OPTIONS`

### ✅ Ver logs no CloudWatch:
- Lambda → Aba "Monitoramento" → **Ver logs no CloudWatch**
- Acompanhe erros ou chamadas feitas à função

---

## 🧩 Melhorias Futuras

- Criar rota `GET /produtos/{id}`
- Implementar `PUT` e `DELETE`
- Adicionar autenticação (JWT ou IAM)
- Documentar com Swagger / OpenAPI
- Adicionar testes com `pytest` ou `unittest`

---

## 📁 Organização de Prints

Salve os prints na pasta `prints/` e use a seguinte nomenclatura:

```markdown
![Print 1](./prints/print-1.png)
![Print 2](./prints/print-2.png)
...
```

---

## ✅ Pronto!

Sua API REST com Lambda, API Gateway e DynamoDB está funcionando e documentada. Para dúvidas ou sugestões, abra uma issue neste repositório.
