def dfs(graph, start, visited=None,parent=None,exp=None,err=None):
    if visited is None:
        visited = []
    if start not in visited:
        if exp is None:
            exp =''
        exp += "("+start
        visited.append(start)
        i = 0
        for next in sorted(graph[start]):
            if next not in visited:
                if i == 0:
                    i += 1
                visited,exp,err = dfs(graph, next, visited,start,exp,err)
            elif next in visited and next!=parent:
                return visited,exp,"E3"

        exp += ")"
    return visited,exp,err



def SExpression(nodes):
    nodes = nodes.split(" ")
    nodes = [x.replace("(","").replace(")","").split(",") for x in nodes]
    graph = {}
    for node in nodes:
        if node[0] == node[1]:
            return '', 'E5'
        if node[0] in graph.keys():
            if node[1] in graph[node[0]]:
                return '',"E2"
            graph[node[0]].append(node[1])
            if len(graph[node[0]]) > 3:
                return '',"E1"
        else:
            graph[node[0]] = []
            graph[node[0]].append(node[1])

        if node[1] in graph.keys():
            if node[0] in graph[node[1]]:
                return '',"E2"
            graph[node[1]].append(node[0])
            if len(graph[node[1]]) > 3:
                return '',"E1"
        else:
            graph[node[1]] = []
            graph[node[1]].append(node[0])

    visited,exp,err = dfs(graph,sorted(graph.keys())[0])
    if len(visited) != len(graph.keys()):
        return '', "E4"
    if err is not None :
        return '',err
    else:
        return exp,''




s = raw_input()
exp,err = SExpression(s)
if exp=='':
    print err
else:
    print exp