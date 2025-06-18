library (data.table)
library(igraph)

nodes <- fread ("~/OneDrive - University of Eastern Finland/Projects/Minna/6_Gene_Coding_Simple.txt")
edges <- fread ("~/OneDrive - University of Eastern Finland/Projects/Minna/5_Filtered_Node_Edge_Simple_Plot.txt")


net.igraph <- graph_from_data_frame(
  d = edges, vertices = nodes, 
  directed = FALSE
)

net.igraph <- simplify(net.igraph, remove.multiple = F, remove.loops = T)


plot(net.igraph,vertex.label = nodes$Gene,
     vertex.color = adjustcolor(ifelse (nodes$Gene_Type == "Target", "red", "yellow"), alpha.f = 0.7),
     vertex.frame.color = ifelse (nodes$Gene_Type == "Target", "white", "grey"),
     vertex.size = 6,
     vertex.label.degree = pi/2, vertex.label.color = "navyblue", vertex.label.dist = 1, vertex.label.cex = 1, vertex.label.font = 4, vertex.label.family="Times",
     edge.curved = 0.5,
     layout = layout_nicely (net.igraph), main="Network of Target Genes with DEG Simple Plot", main.family = "Serif", main.font = 4)
