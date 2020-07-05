doc = '''
#%RAML 1.0
title: API

securitySchemes:
  JWT:
    type: x-{other}
    describedBy:
      headers:
        Authorization:
          description: X-AuthToken
          type: string
          required: true
      responses:
        401:
          description: Authentication problem

types:
  Auth:
    type: object
    discriminator: token
    properties:
      token: string
      
  Agent:
    type: object
    discriminator: agent
    properties:
      agent_id:
        type: integer
        required: true
        example: 1
      name:
        type: string
        required: true
        example: "name example"
      status:
        type: boolean
        required: true
        example: true
      environment:
        type: string
        required: true
        example: "environment example"
      version:
        type: string
        required: true
        example: "version example"
      address:
        type: string
        required: true
        example: "address example"
      user_id:
        type: integer
        required: true
        example: 1
    example:
      agent_id: 1
      user_id: 1
      name: "name example"
      status: true
      environment: "environment example"
      version: "version example"
      address: "address example"

  Group:
    type: object
    discriminator: group
    properties:
      id:
        type: integer
        required: true
        example: 1
      name:
        type: string
        required: true
        example: "name example"
    example:
      group_id: 1
      name: "group example"
 
  Event:
    type: object
    discriminator: event
    properties:
      id:
        type: integer
        required: true
        example: 1
      level:
        type: string
        required: true
        example: 1
      payload:
        type: string
        required: true
        example: "payload example"
      shelve:
        type: boolean
        required: true
        example: true
      date:
        type: datetime
        required: true
        example: "2020-07-05T00:00:00Z"
      agent_id:
        type: integer
        required: true
        example: 1
        
    example:
      event_id: 1
      agent_id: 1
      level: "level example"
      data: "payload example"
      shelve: true

  User:
    type: object
    discriminator: user
    properties:
      id:
        type: integer
        required: true
        example: 1
      name:
        type: string
        required: true
        example: "name example"
      password:
        type: string
        required: true
        example: "password example"
      email:
        type: string
        required: true
        example: "name@example.com"
      last_login:
        type: date-only
        required: true
        example: "2020-07-05"
        
    Response:
    properties:
      message:
        type: string
        example: "message example"

/auth/token:
    post:
      description: Return JWT
      body:
        application/json:
          type: Auth
          username: string
          password: string
      responses: 
        201:
          body: 
            application/json:
              description: Token gerado
        400:
          body: 
            application/json:
              description: Token expirado
      securedBy: [JWT]
      
/agents:
  get:
    responses: 
      200:
        body:
          type: Response
      401:
        body:
          type: Response
      404:
        body:
          type: Response
    securedBy: [JWT]
  post:
    body: 
      application/json:
    responses: 
      201:
        body:
          type: Response
      401:
        body:
          type: Response
    securedBy: [JWT]

  /{id}:
    get:
      responses: 
        200:
          body:
            type: Response
        401:
          body:
            type: Response
        404:
          body:
            type: Response
      securedBy: [JWT]
    put:
      responses:
        200:
          body:
            type: Response
        401:
          body:
            type: Response
        404:
          body:
            type: Response
      securedBy: [JWT]
    delete:
      responses:
        200:
          body:
            type: Response
        401:
          body:
            type: Response
        404:
          body:
            type: Response
      securedBy: [JWT]
      
  /{id}/events:
    get:
      responses:
        200:
          body:
            type: Event[]
        401:
          body:
            type: Response
        404:
          body:
            type: Response
      securedBy: [JWT]
      
    post:
      body: 
        application/json:
        201:
          body:
            type: Response
        401:
          body:
            type: Response
        404:
          body:
            type: Response
      securedBy: [JWT]
      
    put:
      description: Update Event
      body:
        type: Event
        200:
          body:
            type: Response
        401:
          body:
            type: Response
        404:
          body:
            type: Response
      responses:
        200:
          body:
            type: Event
        400:
          body:
            type: Response
      securedBy: [JWT]
      
    delete:
      description: Delete Event
      body: 
        application/json:
        200:
          body:
            type: Response
        401:
          body:
            type: Response
        404:
          body:
            type: Response
      responses:
        200:
          body:
            type: Response
        401:
          body:
            type: Response
        404:
          body:
            type: Response
      securedBy: [JWT]

/groups:
  get:
    responses:
      200:
        body:
          type: Group[]
      401:
        body:
          type: Response
    securedBy: [JWT]
    
  post:
    body:
      application/json:
    responses:
      201:
        body:
          type: Group
      401:
        body:
          type: Response
    securedBy: [JWT]
  /{id}:
    get:
      responses:
        200:
          body:
            type: Group[]
        401:
          body:
            type: Response
        404:
          body:
            type: Response
      securedBy: [JWT]
    put:
      body:
        type: Group
      responses:
        200:
          body:
            type: Group
        401:
          body:
            type: Response
      securedBy: [JWT]
    delete:
      responses:
        204:
          body:
            type: Response
        400:
          body:
            type: Response
      securedBy: [JWT]
/users:
  get:
    responses:
      200:
        body:
          type: User[]
    securedBy: [JWT]
  post:
    body:
      application/json:
        properties:
    responses:
      201:
        body:
          type: User
      401:
        body:
          type: Response
      404:
        body:
          type: Response
    securedBy: [JWT]
  /{id}:
    get:
      responses:
        200:
          body:
            type: User[]
        401:
          body:
            type: Response
        404:
          body:
            type: Response
      securedBy: [JWT]
    put:
      body:
        type: User
      responses:
        200:
          body:
            type: User
        401:
          body:
            type: Response
        404:
          body:
            type: Response
      securedBy: [JWT]
    delete:
      responses:
        200:
          body:
            type: Response
        401:
          body:
            type: Response
        404:
          body:
            type: Response
      securedBy: [JWT]
'''
