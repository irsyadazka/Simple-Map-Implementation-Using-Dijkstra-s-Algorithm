from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from dijkstra import *
from tkinter.filedialog import askopenfilename
import networkx as nx

def chooseAndDrawGraph():
    graph = Graph()
    filename = askopenfilename(initialdir="/Users/azka/Desktop/Stima/IRK/Task7/", title="Choose a file", filetypes=[("Text files", "*.txt")])
    graph.readFile(filename)
    # fileLabel = Label(text=graph.filename, bg='#121943')
    # fileLabel.place(x = 250, y = 30)
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
    graphFrame.place(anchor="center", relx=0.5, rely=0.4)
    canvas = FigureCanvasTkAgg(container, master=graphFrame)
    canvas.draw()
    canvas.get_tk_widget().pack()

window = Tk()
window.title("Dijkstra App")
window.geometry('960x700')
window.configure(background='#121943')

Label(text='Dijkstra Algorithm to Find Shortest Path', bg='#121943', fg='light gray', font=("Courier-Bold", 20)).pack()

# graphFrame = Frame(window, bg='white')
# graphFrame.pack(side=LEFT)
container = plt.figure(figsize=(7, 3))
# canvas = FigureCanvasTkAgg(container, master=graphFrame)
# canvas.draw()
# canvas.get_tk_widget().pack()

fileLabel = Label(text="Filename", bg='#121943')
fileLabel.place(x = 250, y = 30)
Button(text='Select File', bg='#111840', font=("Courier", 12), command= lambda: chooseAndDrawGraph()).place(x = 130, y = 30)

srcNodes = StringVar()
Label(text='Source: ', bg='#121943', font=("Courier", 12)).place(x = 130, y = 60)
srcListNode = OptionMenu(window, srcNodes, "Select One...").place(x = 190, y = 60)
destNodes = StringVar()
Label(text='Destination: ', bg='#121943', font=("Courier", 12)).place(x = 320, y = 60)
destListNode = OptionMenu(window, destNodes, "Select One...").place(x = 410, y = 60)

Button(text="Solve It!", bg='#111840', font=("Courier", 12)).place(x = 130, y = 100)

window.mainloop()