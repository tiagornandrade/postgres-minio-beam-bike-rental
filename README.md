# Postgres MinIO Beam - Bike Rental

## Descrição do Projeto

Este projeto, denominado Postgres MinIO Beam - Bike Rental, é uma solução para processamento de dados relacionados ao aluguel de bicicletas. Ele utiliza o Apache Beam para criar pipelines de processamento de dados que movem e transformam dados entre o PostgreSQL (Postgres), o sistema de armazenamento MinIO e diferentes camadas de dados, como landing, raw, trusted e refined.

## Estrutura do Projeto

O projeto está organizado nas seguintes pastas e arquivos:

### Pastas:

1. **minio_lake-data**: Esta pasta armazena os dados brutos e processados do MinIO.

2. **utils/minio**: Contém utilitários relacionados ao MinIO, incluindo scripts para transferir dados entre diferentes camadas.

3. **utils/postgres**: Aqui estão os utilitários específicos para interação com o PostgreSQL.

### Arquivos:

1. **utils.postgres.generate.py**: Um script Python responsável por gerar dados simulados para o PostgreSQL.

2. **utils.minio.landing_to_raw.py**: Um utilitário para transferir dados da camada landing para a camada raw no MinIO.

3. **utils.minio.raw_to_trusted.py**: Utilitário que move dados da camada raw para a camada trusted no MinIO após aplicar transformações.

4. **pipeline_beam/landing_to_raw.py**: Um pipeline Apache Beam para processar dados da camada landing para a camada raw.

5. **pipeline_beam/raw_to_trusted.py**: Outro pipeline Apache Beam para transformar dados da camada raw para a camada trusted.

## Configuração e Execução

Antes de executar qualquer script ou pipeline, certifique-se de configurar corretamente as credenciais do MinIO e PostgreSQL no arquivo de configuração apropriado.

### Executando o Pipeline Apache Beam

Para executar os pipelines Apache Beam, utilize os seguintes comandos:

```bash
python pipeline_beam/landing_to_raw.py
python pipeline_beam/raw_to_trusted.py
```

### Utilizando os Scripts de Utilitários

Os scripts de utilitários podem ser executados da seguinte forma:

```bash
python utils.postgres.generate.py
python utils.minio.landing_to_raw.py
python utils.minio.raw_to_trusted.py
```

Lembre-se de ajustar as configurações de acordo com o seu ambiente.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para criar pull requests, reportar problemas ou sugerir melhorias.
