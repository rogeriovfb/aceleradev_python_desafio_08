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


/auth/token:
  post:
    body:
      type: Auth
    securedBy: [JWT]

/agents:
  get:
    responses:
      200:
        body: Agent

  post:
    body:
      type: Agent
    responses:
      201:
        body:
          type: Agent

  /{id}:
    put:
      body:
        type: Agent
      responses:
        200:
          body:
            type: Agent

    delete:
      responses:
        204:
          body:

  /{id}/events:
    get:
      responses:
        200:
          body:
            type: Event

    post:
      body: 
        type: Event
      responses:
        201:
          body:
            type: Event


/agents/{id}/events/{id}:
  put:
    body:
      type: Event
    responses:
      200:
        body:
          type: Event

  delete:
    responses:
      204:
        body:

/groups:
  get:
    responses:
      200:
        body:
          type: Group[]

  post:
    body:
      type: Group
    responses:
      201:
        body:
          type: Group


  /{id}:
    put:
      body:
        type: Group
      responses:
        200:
          body:
            type: Group

    delete:
      responses:
        204:
          body:

/users:
  get:
    responses:
      200:
        body:
          type: User

  post:
    body:
      type: User
    responses:
      201:
        body:
          type: User


  /{id}:
    put:
      body:
        type: User
      responses:
        200:
          body:
            type: User
    
    delete:
      responses:
        204:
          body:

'''
