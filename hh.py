#######################
# LEONIDAS PASTRAS    #
# p20155              #
# 5/4/2022            #
# ex. 1/6             #
#######################

from queue import Empty
from xml.etree.ElementTree import tostring
import networkx as nx
import matplotlib.pyplot as plt
import random

seqList = [[5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3] , [6, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1]] #works with any amount of lists!

def ParallelSort(listA, listB): #reverse sorts both lists based on listA
    i = 0
    for j in range(len(listA)):
        i += 1
        loops = len(listA) - i
        for i in range(loops):
            if listA[i] < listA[i + 1]:
                temp = listA[i]
                listA[i] = listA[i + 1]
                listA[i + 1] = temp
                temp = listB[i]
                listB[i] = listB[i + 1]
                listB[i + 1] = temp

def HavelHakimiGraph(mainSeq):
    if nx.is_graphical(mainSeq):    #Checks if the given sequence is graphical
        G = nx.Graph()
        seqLen = len(mainSeq)   #Caclculates the length of the given sequence
        assistSeq = mainSeq.copy()  #Creates a copy of the given sequence to act as the list of edge connections left
        nodes = []  #Creates the empty list nodes
        for i in range(seqLen): nodes += ["v" + str(i + 1)] #Depending on the length of the given sequence, fills the "nodes" list 
        G.add_nodes_from(nodes)
        E = []
        while assistSeq[0] != 0: #loops while there are still connections to be made
            while True:     #Picks a random edge from "assistSeq" that is not zero
                randomEdge = random.randint(1, seqLen) - 1
                if assistSeq[randomEdge] > 0: 
                    connNeeded = assistSeq[randomEdge]
                    break                                       #stuff...
            connLeft = connNeeded
            i = 0
            while connLeft > 0:
                if i != randomEdge: #Makes sure to not connect with itself
                    E.append([nodes[i], nodes[randomEdge]])
                    assistSeq[i] -= 1
                    connLeft -= 1
                i += 1
            assistSeq[randomEdge] = 0
            ParallelSort(assistSeq, nodes)
        print("---------------------new graph------------------------") #fancy stuff...
        for conn in E:
            print("Connecting ", str(conn[1]), " with ", str(conn[0]) + "...")
        G.add_edges_from(E)
        print(E)
        nx.draw_circular(G,with_labels=True)
        plt.savefig("hhGraph.eps")
        plt.show() 

for seq in seqList:
    HavelHakimiGraph(seq)

