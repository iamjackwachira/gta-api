import graphene
import vehicles.schema


class Query(vehicles.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
