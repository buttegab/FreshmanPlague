#!/usr/bin/env python
"""
Modified Barabasi-Albert Network Generation, for disease spread simulation.
Complexity Science F2016, Olin College
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

class Student(object):
	""" 
	Base student; used as node in network. 
	"""

	def __init__(self, immune_strength=1, tolerance=5):
		self.immune_strength = immune_strength
		self.tolerance = tolerance #these do nothing right now.


def create_student_ba_graph(size=90, new_edges_per_node=3):
	""" 
	Creates a graph of [size] Student nodes, using weighted connections.
	Eventually, efficiency might be a concern here. Should be fine
	for n=90, though.
	TODO: vary the edges new nodes introduce.
	TODO: roommates, relationships, etc - "colored" edges.
	"""
	G = nx.Graph()
	if size <= 0:
		return G
	first_student = Student()
	G.add_node(first_student)
	students_list = []
	students_list.append([first_student,0])
	for i in range(size):
		new_student = Student()
		G.add_node(new_student)

		all_students = range(len(students_list))
		probs_base = [float(k[1]+1) for k in students_list]
		probs = probs_base/np.sum(probs_base)
		number_of_friends = min(len(students_list), new_edges_per_node)
		new_friends = np.random.choice(all_students, size=number_of_friends, replace=False, p=probs)
		for friend in new_friends:
			students_list[friend][1] += 1
			G.add_edge(new_student, students_list[friend][0])
		students_list.append([new_student, nx.degree(G, new_student)])
	return G



if __name__=="__main__":
	test_graph = create_student_ba_graph()
	nx.draw(test_graph)
	plt.show()



