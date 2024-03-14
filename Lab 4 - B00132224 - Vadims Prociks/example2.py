import graphene
# Define the schema
class Product(graphene.ObjectType):
        id = graphene.ID()
        title = graphene.String()
        cost = graphene.Decimal()

# Mapping values to Products
class Query(graphene.ObjectType):
        product = graphene.Field(Product)
        def resolve_product1(root, info):
                return Product(id=1, title="Apple", cost="2.0")
        product2 = graphene.Field(Product)
        def resolve_product2(root, info):
                return Product(id=2, title="Ham", cost="1.0")
        product3 = graphene.Field(Product)
        def resolve_product3(root, info):
                return Product(id=3, title="Juice", cost="4.2")

schema = graphene.Schema(query=Query)
query = """
    {
        product3 {
        id
        title
    }
}
"""
result = schema.execute(query)
print(result)
