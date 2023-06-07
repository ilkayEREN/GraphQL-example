from flask import Flask, jsonify, request
import graphene

# User class
class User(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    age = graphene.Int()

# Root class for GraphQL query
class Query(graphene.ObjectType):
    allUsers = graphene.List(User)

    def resolve_allUsers(self, info):
        # Here, you can fetch all users from the database
        # As an example, we are returning hardcoded users
        users_data = [
            {
                'id': 1,
                'name': 'ilkay eren',
                'age': 21
            },
            {
                'id': 2,
                'name': 'your name here',
                'age': 35
            }
        ]
        return [User(**user_data) for user_data in users_data]

# Flask application
app = Flask(__name__)

# GraphQL schema
schema = graphene.Schema(query=Query)

# GraphQL endpoint
@app.route('/graphql', methods=['POST'])
def graphql():
    data = request.get_json()
    query = data['query']
    result = schema.execute(query)
    
    # Converting the data and errors properties of the result
    response_data = {'data': result.data}
    if result.errors:
        response_data['errors'] = [str(error) for error in result.errors]
    
    return jsonify(response_data)

# Running the server
if __name__ == '__main__':
    app.run()
