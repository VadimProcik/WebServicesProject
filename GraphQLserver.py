import graphene
import requests

# Define the schema
class Product(graphene.ObjectType):
    id = graphene.String()
    title = graphene.String()
    cost = graphene.Float()

# Mapping values to Products
class Query(graphene.ObjectType):
    product_titles = graphene.List(graphene.String)

    def resolve_product_titles(root, info):
        # Make a request to the Flask server to get product data
        response = requests.get('http://localhost:5000/getProducts')
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            products_data = response.json()
            
            # Extract titles of all products
            product_titles = [product_data['title'] for product_data in products_data]
            
            # Return the list of product titles
            return product_titles
        else:
            # If request fails, return an empty list
            return []

# Running a query to fetch product titles
schema = graphene.Schema(query=Query)
query = """
{
  productTitles
}
"""
result = schema.execute(query)
print(result.data)