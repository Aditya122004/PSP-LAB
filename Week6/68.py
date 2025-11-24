graph={'A':['B','C'],'B':['A','C','D'],'C':['A','B','D'],'D':['B','C']}
for vertex in graph:
    graph[vertex]=set(graph[vertex])
vertices=list(graph.keys())
print("Similarity between vertex pairs")
for i in range(len(vertices)):
    for j in range(i+1,len(vertices)):
        v1=vertices[i]
        v2=vertices[j]
        inter=graph[v1]&graph[v2]
        union=graph[v1]|graph[v2]
        if len(union)==0:
            similarity=0
        else:
            similarity=len(inter)/len(union)
        print(f"Similarity ({v1},{v2})={similarity:.2f}")
    
