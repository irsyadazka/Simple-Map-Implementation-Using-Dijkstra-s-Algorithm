from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from dijkstra import *
from tkinter.filedialog import askopenfilename
import networkx as nx

def graphPrep():
    global graph

    graph = Graph()
    filename = askopenfilename(title="Choose a file", filetypes=[("Text files", "*.txt")])
    graph.readFile(filename)
    fileLabel.config(text=graph.filename)
    plt.clf()
    graphDraw = nx.DiGraph()
    for node in graph.nodes:
        for edge in graph.edges[node]:
            graphDraw.add_edge(node, edge[0], weight=edge[1])

    pos = nx.circular_layout(graphDraw)
    nx.draw(graphDraw, pos, with_labels=True)
    edgeLabels = nx.get_edge_attributes(graphDraw, 'weight')
    nx.draw_networkx_edge_labels(graphDraw, pos, edge_labels=edgeLabels)

    graphFrame = Frame(window)
    graphFrame.place(anchor="center", relx=0.5, rely=0.45)
    canvas = FigureCanvasTkAgg(container, master=graphFrame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    nodeList = list(graph.nodes)
    nodeList.sort()
    srcListNode = OptionMenu(window, srcNodes, *nodeList)
    destListNode = OptionMenu(window, destNodes, *nodeList)
    srcListNode.place(x = 190, y = 75)
    destListNode.place(x = 410, y = 75)

def solvingStep():
    global graph

    graph.dijkstra(srcNodes.get(), destNodes.get())
    Label(text='Detail of Shortest path from ' + str(srcNodes.get()) + ' to ' + str(destNodes.get()) + ':', font=("Courier-Bold", 16), bg='#121943').place(x = 130, y = 480)
    if graph.distance[destNodes.get()] == float("inf"):
        pathLabel.config(text="No Path Founded")
        distanceLabel.config(text="")
        infoLabel.config(text="")
    else:
        graph.printResult(srcNodes.get(), destNodes.get())
        if len(graph.path) > 1:
            eachStep = []
            for i in range(len(graph.path)-1):
                currDistance = 0
                eachStep.append([graph.path[i], graph.path[i+1]])
                graphDraw = nx.DiGraph()
                for node in graph.nodes:
                    for edge in graph.edges[node]:
                        if [node, edge[0]] in eachStep:
                            currDistance += edge[1]
                            graphDraw.add_edge(node, edge[0], weight=edge[1], color='red')
                        else:
                            graphDraw.add_edge(node, edge[0], weight=edge[1], color='black')

                colorStep = [graphDraw[i][j]['color'] for (i, j) in graphDraw.edges()]
                pos = nx.circular_layout(graphDraw)
                nx.draw(graphDraw, pos, with_labels=True, edge_color=colorStep)
                edgeLabels = nx.get_edge_attributes(graphDraw, 'weight')
                nx.draw_networkx_edge_labels(graphDraw, pos, edge_labels=edgeLabels)
                    
                graphFrame = Frame(window)
                graphFrame.place(anchor="center", relx=0.5, rely=0.45)
                canvas = FigureCanvasTkAgg(container, master=graphFrame)
                canvas.draw()
                canvas.get_tk_widget().pack()

                pathLabel.config(text="Edge taken: " + str(graph.path[i]) + " -> " + str(graph.path[i+1]))
                distanceLabel.config(text="Distance so far: " + str(currDistance))

                time.sleep(2)
                window.update()

        pathLabel.config(text=graph.printPath())
        distanceLabel.config(text="Total Distance: " + str(graph.distance[destNodes.get()]))
        infoLabel.config(text="Time taken is " + str(graph.timeGet) + " ms with " + str(graph.iteration) + " iterations")

window = Tk()
window.title("Dijkstra App")
window.geometry('960x700')
window.configure(background='#121943')

Label(text='Shortest Path via Dijkstra Algorithm', bg='#121943', fg='light gray', font=("Courier-Bold", 25)).pack()

container = plt.figure(figsize=(7, 3))

fileLabel = Label(text="Filename", bg='#121943')
fileLabel.place(x = 250, y = 45)
Button(text='Select File', bg='#111840', font=("Courier", 12), command= lambda: graphPrep()).place(x = 130, y = 45)

srcNodes = StringVar()
Label(text='Source: ', bg='#121943', font=("Courier", 12)).place(x = 130, y = 75)
srcListNode = OptionMenu(window, srcNodes, "Select Node...")
srcListNode.place(x = 190, y = 75)
destNodes = StringVar()
Label(text='Destination: ', bg='#121943', font=("Courier", 12)).place(x = 320, y = 75)
destListNode = OptionMenu(window, destNodes, "Select Node...")
destListNode.place(x = 410, y = 75)

Button(text="Solve It!", bg='#111840', font=("Courier", 12), command= lambda:solvingStep()).place(x = 130, y = 115)

pathLabel = Label(text="", bg='#121943', font=("Courier", 14))
pathLabel.place(x = 130, y = 505)
distanceLabel = Label(text="", bg='#121943', font=("Courier", 14))
distanceLabel.place(x = 130, y = 530)
infoLabel = Label(text="", bg='#121943', font=("Courier", 14))
infoLabel.place(x = 130, y = 555)

window.mainloop()