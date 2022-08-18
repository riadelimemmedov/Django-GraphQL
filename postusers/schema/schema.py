from graphene_django import DjangoObjectType
import graphene
from ..models import Post as PostModel
from ..models import Author as AuthorModel

#!Post 
class Post(DjangoObjectType):#Looks Like serializers.ModelSerializers method in Django Rest Framework
    class Meta:
        model = PostModel
        fields = ['id','title','body','author']
        
#!Author
class Author(DjangoObjectType):
    class Meta:
        model = AuthorModel
        fields = ['id','name','posts']
    
    
    def resolve_posts(self,info):
        return PostModel.objects.filter(author=self)
    
    @classmethod
    def get_node(cls,info,id):
        return Author.objects.get(id=id)

#!Query
class Query(graphene.ObjectType):
    authors = graphene.List(Author)
    posts = graphene.List(Post)
    # posts = graphene.Field(Post,name=graphene.String(required=True))

    def resolve_authors(self,info):
        return AuthorModel.objects.all()

    def resolve_posts(self,info):
        return PostModel.objects.all()  

schema = graphene.Schema(query=Query)
