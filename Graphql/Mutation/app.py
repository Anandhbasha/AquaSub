from flask import Flask, request, jsonify
import graphene 

users = [
    {"id": "1", "name": "Kumar", "email": "kumar@example.com"},
    {"id": "2", "name": "Anand", "email": "anand@example.com"}
]

#  User Type
class User(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()

#  Queries (Read)
class Query(graphene.ObjectType):
    all_users = graphene.List(User)
    user = graphene.Field(User, id=graphene.ID(required=True))

    def resolve_all_users(root, info):
        return users

    def resolve_user(root, info, id):
        return next((u for u in users if u["id"] == id), None)

#  Create
class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(lambda: User)

    def mutate(root, info, name, email):
        new_id = str(len(users) + 1)
        user = {"id": new_id, "name": name, "email": email}
        users.append(user)
        return CreateUser(user=user)

# Update
class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        email = graphene.String()

    user = graphene.Field(lambda: User)

    def mutate(root, info, id, name=None, email=None):
        user = next((u for u in users if u["id"] == id), None)
        if user:
            if name: user["name"] = name
            if email: user["email"] = email
        return UpdateUser(user=user)

#  Delete
class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    def mutate(root, info, id):
        global users
        before = len(users)
        users = [u for u in users if u["id"] != id]
        return DeleteUser(ok=len(users) < before)

#  Mutation Register
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

#  Schema
schema = graphene.Schema(query=Query, mutation=Mutation)

#  Flask Setup
app = Flask(__name__)

@app.route("/graphql", methods=["POST"])
def graphql():
    data = request.get_json()
    result = schema.execute(
        data.get("query"),
        variable_values=data.get("variables")
    )
    return jsonify(result.to_dict())

if __name__ == "__main__":
    app.run(debug=True)