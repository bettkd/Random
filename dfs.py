# @Author = +dominic_bett
# Machine Learning
# Depth-First-Search

# create the graph in adjacency list representation
adjLists = [ [1,2,3], [5,6], [4], [2,4], [1], [], [4] ]

discovered = []
def DFS(G, start, end):
    stack = []
    stack.append(start)
    n = len(G)
    visited = []
    for i in range(0,n):
        visited.append(False)
    
    path = []
    while(len(stack)>0):
        node = stack.pop()
        if(not visited[node]):
            visited[node] = True
            path.append(node)
            if node == end:
            	return path
 
            # auxiliary stack to visit neighbors in the order they appear
            # in the adjacency list
            # alternatively: iterate through the adjacency list in reverse order
            # but this is only to get the same output as the recursive dfs
            # otherwise, this would not be necessary
            stack_aux = []
            for w in G[node]:
                if(not visited[w]):
                    stack_aux.append(w)
            while(len(stack_aux)>0):
                stack.append(stack_aux.pop())

def main(argv=None):
	print (DFS(adjLists, 1, 4))


if __name__ == '__main__':
	main()