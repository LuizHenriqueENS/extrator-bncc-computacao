# BNCC Computação – API REST

Projeto pessoal desenvolvido em Python com o objetivo de organizar e disponibilizar as habilidades da BNCC Computação por meio de uma API REST.

O projeto surgiu da necessidade de facilitar a consulta às habilidades e aos conteúdos de Computação na Educação Básica. Para isso, desenvolvi um processo de extração e tratamento de dados diretamente do documento PDF da BNCC, convertendo as informações em uma estrutura JSON consumida pela API.

## Funcionalidades

- Extração de tabelas diretamente do documento PDF da BNCC.
- Tratamento e organização dos dados utilizando Pandas.
- Conversão das informações para o formato JSON.
- Consulta de habilidades por código.
- Pesquisa de habilidades por termos presentes nas explicações.
- Listagem das habilidades e dos eixos da Computação.

## Tecnologias utilizadas

- **Python:** desenvolvimento dos scripts e da API.
- **FastAPI:** construção dos endpoints REST.
- **Pandas:** tratamento e manipulação dos dados.
- **PyMuPDF:** extração e processamento de tabelas em PDF.
- **JSON:** estruturação e armazenamento dos dados.

## Endpoints

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/` | Verificação da API. |
| GET | `/habilidades` | Lista as habilidades. |
| GET | `/habilidades/{codigo}` | Consulta por código. |
| GET | `/habilidades/explicacao/?q=termo` | Pesquisa nas explicações. |
| GET | `/eixo` | Lista os eixos da Computação. |

## Execução

Instale as dependências:

```bash
pip install fastapi uvicorn pandas pymupdf
```

Inicie a API:

```bash
uvicorn main:app --reload
```

Documentação interativa:

`http://127.0.0.1:8000/docs`

## Possíveis melhorias futuras

- Disponibilização pública da API.
- Otimização do processamento e das consultas.
- Ampliação dos filtros de pesquisa.
- Integração com ferramentas de planejamento pedagógico.

## Sobre o projeto

Este projeto representa um experimento prático envolvendo extração de dados, automação, manipulação de informações e desenvolvimento de APIs com Python. Seu desenvolvimento também teve como motivação explorar possibilidades de aplicação da tecnologia no contexto educacional.
