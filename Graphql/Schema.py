import graphene
from data import users

class User(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()

class Query(graphene.ObjectType):
    all_users = graphene.List(User)
    user = graphene.Field(User, id=graphene.ID(required=True))

    def resolve_all_users(root, info):
        return users

    def resolve_user(root, info, id):
        return next((u for u in users if u["id"] == id), None)

schema = graphene.Schema(query=Query)