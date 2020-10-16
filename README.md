# Trabalho Cloud Fiap 49BDT 
Repositório para o Trabalho da Disciplina Cloud Computing, Curso Big Data da FIAP (Turma: 49BDT-2020)


## Alunos do Grupo
* Eder Manoel (RM 337581)
* Luis Bannwart (RM 338120) 
* Kelvin Ueno (RM 339266)
* Marcos Speca (RM 337024)

## Componentes

### Aplicação Python no ElasticBeanstalk
* application.py
* http://fiaptrabalhocloud-env.eba-urmfkprc.us-east-1.elasticbeanstalk.com/

### Banco DBaaS MySQL AWS RDS
* dbmovies.cthpl6d1wkbm.us-east-1.rds.amazonaws.com:3306

### Pipeline DevOps
* Utilizado o Codecommit no CodePipeline, pois não foi possível vincular o github devido a erro de permissão de usuário.
* https://git-codecommit.us-east-1.amazonaws.com/v1/repos/fiap-cloud
* https://github.com/marcos-speca/fiap-cloud


### Object Storage
* Criado um Bucket S3 e upload do gif que aparece na aplicação 
* https://fiap-trabalho-cloud.s3.amazonaws.com/giphy.gif

## Aplicação (Funcionamento)
1. Conecta na base MySQL DBaaS
2. Gera um ID randomico entre 1 e 33 (Nro de registros da base)
3. Recupera uma frase de filme com base no ID
4. Apresenta na tela
5. Botão refresh para uma nova frase
6. Gif statico armazenado com Object Storage



