def find_all_trees(graph, tree_length):
    exhausted_node = set([])
    used_node = set([])
    used_edge = set([])
    current_edge_groups = []

    def finish_all_trees(remaining_length, edge_group, edge_position):
        while edge_group < len(current_edge_groups):
            edges = current_edge_groups[edge_group]
            while edge_position < len(edges):
                edge = edges[edge_position]
                edge_position += 1
                (node1, node2) = nodes(edge)
                if node1 in exhausted_node or node2 in exhausted_node:
                    continue
                node = node1
                if node1 in used_node:
                    if node2 in used_node:
                        continue
                    else:
                        node = node2
                used_node.add(node)
                used_edge.add(edge)
                edge_groups.append(neighbors(graph, node))
                if 1 == remaining_length:
                    yield build_tree(graph, used_node, used_edge)
                else:
                    for tree in finish_all_trees(remaining_length -1
                                                , edge_group, edge_position):
                        yield tree
                edge_groups.pop()
                used_edge.delete(edge)
                used_node.delete(node)
            edge_position = 0
            edge_group += 1





def main():
    global leaves,list,vweights


    T = int(raw_input())



    for j in range(0,T):
        list = []
        leaves = []
        n = int(raw_input())
        vweights = [int(x) for x in raw_input().split()]
        AuxWeights = [int(x) for x in raw_input().split()]
        edges = []

        for i in range(0,n-1):
            edges.append(raw_input().strip())

        graph = [ [] for i in xrange(0, n)]
        edge = set()

        for temp in edges:
            temp = temp.split()
            vlist = [int(x) for x in temp]
            graph[vlist[0]-1].append(int(vlist[1]))
            graph[vlist[1]-1].append(int(vlist[0]))

        root=''
        for m in graph:
            if len(graph[m])>1:
                root = m+1
        if root=='':
            root=1
        findSubtreeWieghts(graph,root)

        for l in leaves:
            list.append(vweights[graph[l-1][0]-1]+vweights[l-1])

        count =0
        for i in list:
            count+=AuxWeights[i]
        ans = float(count)/float(len(list))
        print "%0.8f" %ans

main()