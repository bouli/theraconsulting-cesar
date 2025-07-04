# Thera Consulting - Cesar Cardoso - Data Engineering


This project uses [Docker Compose](https://docs.docker.com/compose/) to manage the containers and [Prisma](https://www.prisma.io/) to manage the db.

## Usage
Initiate the DB instance with Docker Compose
```shell
docker compose up -d
```

You can access the data base using the Postgres Database using this query:
```
postgresql://postgres:postgres@localhost:6500/theraconsultingcesar
```

## Sobre o test

Como solicitado, este repositório está disponível em https://github.com/bouli/theraconsulting-cesar porém privado.
Se necessário solicite acesso sem problemas.


A aplicação está composta por 3 containers.
- db: Com um banco de dados postares;
- seed: Com a carga inicial dos dados das 2 tabelas;
- app: Com o primeiro app que busca no site "https://br.investing.com/economic-calendar/chinese-caixin-services-pmi-596” o último registro publicado e adiciona à tabela “EconomicCalendar” se ainda não existir uma vez por dia a 1 da manhã via crontab;

A ideia foi fazer scripts que pudessem se atualizar automaticamente e, se necessário, adicionar novos indicadores futuros sem muita necessidade de manutenção.

Dentro dos 3 dias disponibilizados, utilizei:
Dia 1: Investiguei os 2 diferentes tipos de páginas que precisava consultar os dados e entender um pouco mais sobre os indicadores. Descobri que, se não fosse utilizar as APIs pagas, necessitaria fazer scrapping em 2 sites. O próprio investing.com, com os links fornecidos, porém o indicador referente ao calendário econômico não parecia estar com o histórico disponível, então utilizei a página https://tradingeconomics.com/china/services-pmi .
Criei também o database inicial utilizando prisma (com o intuito de futuramente, se necessário, utilizar os migrations que são muito práticos).

Dia 2:
Para os 2 indicadores economicos, foi só o caso de fazer o download do histórico no próprio investing.com . Para o calendário econômico, utilizei inicialmente as notícias disponíveis em https://tradingeconomics.com/china/services-pmi e criei a primeira versão dos seeds passeando essas notícias criando assim 2 CSVs com os arquivos para importação nas tabelas. A ideia é que os dados sejam gerados baseados no nomes dos arquivos e nas urls.

Dia 3:
- Criei finalmente o script de push no banco com os dados de seed;
- Adicionei os containers com docker;
- Criei o primeiro script para fazer o scrapping todos os dias do indicador referente ao calendário econômico.

Tarefas pendentes:
- Criar o script de atualização diária dos 2 outros indicadores economicos (para isso usaria a tabela do site através da propriedade Highcharts.charts[0].series[0].data[0] do objetivo JS highcharts);
- Completar alguns dados faltantes dos indicadores de calendário econômico com o mesmo método citado acima;
- Criar as views no formato solicitado;
- Adicionar logging em toda a aplicação;
- Criar test para monitoramento;
- Habilitar novamente Prisma;
