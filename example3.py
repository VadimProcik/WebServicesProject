import graphene
import requests
import json
# Define the schema
class Product(graphene.ObjectType):
        id = graphene.ID()
        title = graphene.String()
        cost = graphene.Decimal()

# Mapping values to Products
class Query(graphene.ObjectType):
        product = graphene.Field(Product)
        def resolve_product(root, info):
            data = requests.get('http://127.0.0.1:5000/getProducts')
            print(data.text)
            '''
            This is a sample fo what the API will return.
            {
            "id": "1221"
            }
            '''
            # parse the JSON
            json_content = json.loads(data.text)

            print(json_content)
            # Extract the ID from the JSON
            extractedId = json_content['id']
            print(extractedId)
            # Send back the ID in a Product
            return Product(id=extractedId)
        
schema = graphene.Schema(query=Query)
query = """
        {
        product {
        id
        title
        }
        }
"""
result = schema.execute(query)
print(result)


