import re
import json

class Path_Intersection(Exception):
    """Path is already set."""


class Wrong_Path(Exception):
    """Path does not match pattern."""


class app_parce:

    def __init__(self):
        self.data={}

    def parce(self,input):
        if self.data=={}:
            self.data=first(input)
        else:
            self.data=second(input,self.data)

        return json.dumps(self.data)


#Создание списка узлов из path
def make_path(path):
    if '/api/v' != path[:6]:
        raise Wrong_Path(f"Path {path} does not match pattern")
    try:
        path = re.sub("\/api\/v\d\/", "", path)
        path = re.sub(r"\/\{(\w+)\}", "", path)
        path = path.split('/')
    except:
        raise Wrong_Path(f"Path {path} does not match pattern")

    return path


#Поиск узла в дереве
def find_node(out,path):
    path=make_path(path)
    layer=out
    for p in path:
        if p in layer.keys():
            layer=layer[p]
        else:
            return None

    return layer


#Добавление узла в дерево
def add_node(out,path,verb):
    path=make_path(path)
    layer=out
    for i in range(len(path)-1):
        if path[i] in layer.keys():
            layer=layer[path[i]]
        else:
            layer[path[i]]=dict()
            layer=layer[path[i]]
    layer[path[-1]]=verb

    return out


#Первый запуск
def first(input):
    out={}
    for row in input:
        verb, path = row
        out=add_node(out,path,verb)

    return out


#Последующие запуски
def second(input,out):
    for row in input:
        verb, path = row
        old_verb=find_node(out,path)
        if old_verb==None:
            out=add_node(out,path,verb)
        if old_verb!=None and old_verb!=verb:
            raise Path_Intersection(f"Intersection in {path}")

    return out
