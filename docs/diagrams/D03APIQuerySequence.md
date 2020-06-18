# D03. Secuencia Consulta API

```mermaid
sequenceDiagram
	Title: D03. Secuencia Consulta API
    participant User as Usuario
    participant APIGateway as API Gateway
    participant AuthController as Auth Controller
    participant ChannelController as Channel Controller
    participant DjangoORM as Django ORM
    participant MySQLDB as MySQL Database
    User->>+APIGateway: HTTP Request
    APIGateway->>+AuthController: ¿Es valido el token?
    alt es válido
        AuthController-->>APIGateway: Token válido   
    else no es válido
        AuthController-->>-APIGateway: Token inválido
        APIGateway-->>User: HTTP Error Response
    end
    APIGateway->>+ChannelController: Obtén lista de canales disponibles
    ChannelController->>+DjangoORM: Consulta canales
    DjangoORM->>+MySQLDB: SQL Query
    MySQLDB-->>-DjangoORM: SQL Query Result
    DjangoORM-->>-ChannelController: Devuelve lista de objetos
    ChannelController-->>-APIGateway: Devuelve objeto en formato JSON
    APIGateway-->>-User: HTTP JSON Response
```