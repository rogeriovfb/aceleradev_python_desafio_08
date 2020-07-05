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
    properties:
      id:
        type: integer
        required: true
      name:
        type: string
        required: true
      status:
        type: boolean
        required: true
      environment:
        type: string
        required: true
      version:
        type: string
        required: true
      address:
        type: string
        required: true
      user_id:
        type: integer
        required: true


  Group:
    type: object
    properties:
      id:
        type: integer
        required: true
      name:
        type: string
        required: true
 

  Event:
    type: object
    properties:
      id:
        type: integer
        required: true
      level:
        type: string
        required: true
      payload:
        type: string
        required: true
      shelve:
        type: boolean
        required: true
      date:
        type: datetime
        required: true
      agent_id:
        type: integer
        required: true

  User:
    type: object
    properties:
      id:
        type: integer
        required: true
      name:
        type: string
        required: true
      password:
        type: string
        required: true
      email:
        type: string
        required: true
      last_login:
        type: date-only
        required: true
        
    Response:
    properties:
      message:
        type: string


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
