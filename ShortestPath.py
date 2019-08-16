import sys
import math
from enum import Enum

class Vertex:
	def __init__(self,value=None,p=None,m=None,f=None,color=None,edges=None):
		self.value=value
		self.p=p
		self.m=m
		self.f=f
		self.edges=edges
		self.color=color
		
	
class Edge:
	def __init__(self,s=None,d=None,weight=None):
		self.s=s
		self.d=d
		self.weight=weight
		
class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255	
        
  
def MakeGraph():
	a=Vertex(value='a')
	b=Vertex(value='b')
	c=Vertex(value='c')
	d=Vertex(value='d')
	e=Vertex(value='e')
	f=Vertex(value='f')
	g=Vertex(value='g')
	h=Vertex(value='h')
	i=Vertex(value='i')
	
	e1=Edge(s=a,d=b,weight=15)
	e2=Edge(s=a,d=c,weight=13)
	e3=Edge(s=a,d=d,weight=5)
	e4=Edge(s=b,d=h,weight=12)
	e5=Edge(s=c,d=b,weight=2)
	e6=Edge(s=c,d=f,weight=6)
	e7=Edge(s=c,d=d,weight=18)
	e8=Edge(s=d,d=e,weight=4)
	e9=Edge(s=d,d=i,weight=99)
	e10=Edge(s=f,d=b,weight=8)
	e11=Edge(s=f,d=h,weight=17)
	e12=Edge(s=e,d=c,weight=3)
	e13=Edge(s=e,d=f,weight=1)
	e14=Edge(s=e,d=g,weight=9)
	e15=Edge(s=e,d=i,weight=14)
	e16=Edge(s=g,d=f,weight=16)
	e17=Edge(s=g,d=h,weight=7)
	e18=Edge(s=g,d=i,weight=10)
	e19=Edge(s=i,d=h,weight=11)
	
	a.edges=[e1,e2,e3]
	b.edges=[e4,e1,e5,e10]
	c.edges=[e5,e6,e7,e2,e12]
	d.edges=[e8,e9,e3,e7]
	e.edges=[e12,e13,e14,e15,e8]
	f.edges=[e10,e11,e6,e13,e16]
	g.edges=[e16,e17,e18,e14]
	h.edges=[e4,e11,e17]
	i.edges=[e19,e9,e15,e18]
	
	graph=[]
	graph=[a,b,c,d,e,f,g,h,i]
	
	return graph
	

def initialize(graph,s):
	for i in graph:
		i.m=float("inf")
		i.p=None
	s.m=0

def relax(u,v,w):
	if v.m>u.m+w:
		v.m=u.m+w
		v.p=u
	
def Dijkstra(G,s):
	initialize(G,s)
	S=[]
	Q=[]
	for i in range(0,len(G),1):
		Q.append(G[i])
	while len(Q)!=0:
		ind=extract_min(Q)
		u=Q.pop(ind)
		S.append(u)
		for i in u.edges:
			if (i.d.value!=u.value):
				relax(u,i.d,i.weight)

def extract_min(l):
	low=float("inf")
	indeks=0
	for i in range(0,len(l),1):
		if (l[i].m<low):
			low=l[i].m
			indeks=i
	return indeks
	

def ShortestPath(G):
	Dijkstra(G,G[0])
	print(G[7].m)
	
def PrintPath(G,s,v):
	if v==s:
		print(s.value)
	elif v.p==None:
		print("No path")
	else:
		PrintPath(G,s,v.p)
		print(v.value)
	
def BFS(G,s):
	for i in G:
		i.color=VertexColor.WHITE
		i.m=float("inf")
		i.p=None
	s.color=VertexColor.GRAY
	s.m=0
	s.p=None
	Q=[]
	Q.append(s)
	while len(Q)!=0:
		u=Q.pop()
		print(u.value)
		for i in u.edges:
			if(i.d.value!=u.value):
				if(i.d.color==VertexColor.WHITE):
					i.d.color=VertexColor.GRAY
					i.d.m=u.m+1
					i.d.p=u
					Q.append(i.d)
		u.color=VertexColor.BLACK
	
	

def main():
	graph=MakeGraph()
	ShortestPath(graph)
	#BFS(graph,graph[0])
	#print(graph[7].m)
	PrintPath(graph,graph[0],graph[7])
	
if __name__=="__main__":
	main()
		
	
	
	
	
	
