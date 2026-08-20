from graphene import Schema, String, ObjectType, Int, Field, List


class UserType(ObjectType):
    id = Int()
    name = String()
    age = Int()


class Query(ObjectType):
    user = Field(UserType, user_id=Int())
    users = List(UserType)

    users_db = [
        {"id": 1, "name": "Shyam", "age": 20},
        {"id": 2, "name": "John", "age": 25},
        {"id": 3, "name": "Doe", "age": 30},
    ]

    def resolve_user(self, info, user_id):
        matched_users = [user for user in Query.users_db if user["id"] == user_id]

        if len(matched_users) == 0:
            return None

        return matched_users[0]

    def resolve_users(self, info):
        return Query.users_db


schema = Schema(query=Query)
gql = """
query{
    user(userId: 2){
        id
        name
        age
    }
    users{
        id
        name
    }
}
"""


def main():
    result = schema.execute(gql)
    print(result.data)


if __name__ == "__main__":
    main()
