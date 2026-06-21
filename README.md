# Ombala SDK Python

SDK Python para a [API Ombala](https://api.useombala.ao) — envio de SMS em Angola.

## Instalação

```bash
pip install ombala
```

## Uso

```python
from ombala import Ombala

client = Ombala("Token a9eb6ea6-5777-4848-a9ed-8cbffc74a503")

# Enviar SMS
client.messages.send(
    message="Olá, tudo bem?",
    from_="MINHALOJA",
    to="921939411",
)

# Listar mensagens
client.messages.list(page=1)

# Ver saldo
client.credits.balance()
```

## API

### Mensagens

| Método | Descrição |
|---|---|
| `messages.send(message, from_, to, schedule?)` | Enviar SMS |
| `messages.list(page?)` | Listar mensagens |
| `messages.get(message_id, id?)` | Obter mensagem por ID |
| `messages.delete(message_id)` | Apagar registo de envio |
| `messages.list_recipients(page?)` | Listar destinatários |
| `messages.list_by_date_range(start, end, page?)` | Listar mensagens por intervalo de datas |
| `messages.list_by_recipient(phone_number?, page?)` | Listar mensagens de um número |

### Remetentes

| Método | Descrição |
|---|---|
| `senders.create(name)` | Criar remetente |
| `senders.list()` | Listar remetentes |
| `senders.list_approved()` | Listar remetentes aprovados |
| `senders.list_pending()` | Listar remetentes pendentes |
| `senders.delete(sender_id)` | Apagar remetente |

### Créditos

| Método | Descrição |
|---|---|
| `credits.balance()` | Mostrar saldo |
| `credits.recharges()` | Histórico de carregamentos |
