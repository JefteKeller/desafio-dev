# Gerenciador de CNABs

## Descrição do projeto

Essa aplicação possui uma interface web que aceita o envio de arquivos contendo informações no padrão CNAB, ou Centro Nacional de Automação Bancária, [arquivo CNAB para referência](https://github.com/ByCodersTec/desafio-ruby-on-rails/blob/master/CNAB.txt).

> ---
>
>  1. Faça o registro e login no sistema (necessário para acessar os outros recursos)
>  2. Através do formulário faça o envio do arquivo CNAB
>  3. O sistema irá Interpretar ("parsear") o arquivo recebido, normalizar os dados, e salvar a informação em um banco de dados relacional
>  4. O sistema irá exibir uma lista das operações importadas, e esta lista conterá um totalizador do saldo em conta
>
> ---

## Rotas disponíveis

> ---
>
> *A rota base dos recursos rodando localmente é <http://127.0.0.1:8000/api/>*
>
> ---

### *Registro de conta*

```sh
http://127.0.0.1:8000/api/accounts/register/
```

### *Logar*

```sh
http://127.0.0.1:8000/api/accounts/login/
```

### *Deslogar*

```shell
http://127.0.0.1:8000/api/accounts/logout/
```

### *Lista de Transações Registradas*

```sh
# Login necessário

http://127.0.0.1:8000/api/cnab/
```

### *Registrar Transações*

```sh
# Login necessário

http://127.0.0.1:8000/api/cnab/upload/
```

## Como utilizar a aplicação

> ---
>
> Para rodar a aplicação localmente é necessário possuir o [***Docker***](https://docs.docker.com/engine/install/) e [***Docker Compose***](https://docs.docker.com/compose/install/) instalados.
>
> ---

Faça o clone do repositório e a partir da raiz do projeto execute o comando:

```sh
docker-compose up
```

> ---
>
> ***Obs. A primeira execução pode ser demorada.***
>
> ---

### Rodar os Testes

```shell
docker-compose run --no-deps -e TEST=True web python -m manage test -v 2
```

### Verificar a cobertura dos Testes

```shell
# Coleta das estatísticas

docker-compose run --no-deps -e TEST=True web coverage run -m manage test -v 2 
```

```shell
# Retorno dos resultados

docker-compose run --no-deps -e TEST=True web coverage report
```

<br>

## Documentação do CNAB

| Descrição do campo  | Inicio | Fim | Tamanho | Comentário
| ------------- | ------------- | -----| ---- | ------
| Tipo  | 1  | 1 | 1 | Tipo da transação
| Data  | 2  | 9 | 8 | Data da ocorrência
| Valor | 10 | 19 | 10 | Valor da movimentação. Obs. O valor encontrado no arquivo será divido por cem(valor / 100.00) para normalizá-lo.
| CPF | 20 | 30 | 11 | CPF do beneficiário
| Cartão | 31 | 42 | 12 | Cartão utilizado na transação
| Hora  | 43 | 48 | 6 | Hora da ocorrência atendendo ao fuso de UTC-3
| Dono da loja | 49 | 62 | 14 | Nome do representante da loja
| Nome loja | 63 | 81 | 19 | Nome da loja

## Documentação sobre os tipos das transações

| Tipo | Descrição | Natureza | Sinal |
| ---- | -------- | --------- | ----- |
| 1 | Débito | Entrada | + |
| 2 | Boleto | Saída | - |
| 3 | Financiamento | Saída | - |
| 4 | Crédito | Entrada | + |
| 5 | Recebimento Empréstimo | Entrada | + |
| 6 | Vendas | Entrada | + |
| 7 | Recebimento TED | Entrada | + |
| 8 | Recebimento DOC | Entrada | + |
| 9 | Aluguel | Saída | - |

<br>

## Referência

Este projeto foi baseado neste desafio: <https://github.com/ByCodersTec/desafio-dev>

> ---
