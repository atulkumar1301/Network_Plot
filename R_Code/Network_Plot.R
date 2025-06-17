library (data.table)
library(igraph)

nodes <- fread ("~/OneDrive - University of Eastern Finland/Projects/Minna/6_Gene_Coding.txt")
edges <- fread ("~/OneDrive - University of Eastern Finland/Projects/Minna/5_Filtered_Node_Edge.txt")


net.igraph <- graph_from_data_frame(
  d = edges, vertices = nodes, 
  directed = FALSE
)

net.igraph <- simplify(net.igraph, remove.multiple = F, remove.loops = T)


plot(net.igraph,vertex.label = ifelse (nodes$Gene_Type == "Target", nodes$Gene, NA),
     vertex.color = adjustcolor(ifelse (nodes$Gene_Type == "Target", "red", "yellow"), alpha.f = 0.7),
     vertex.frame.color = ifelse (nodes$Gene_Type == "Target", "white", "grey"),
     vertex.size = ifelse (nodes$Gene_Type == "Target", 80, 40),
     vertex.label.degree = pi/2, vertex.label.color = "navyblue", vertex.label.dist = 1, vertex.label.cex = 0.4, vertex.label.font = 4, vertex.label.family="Times",
     edge.curved = 0.5,
     rescale = FALSE, ylim=c(-44,14),xlim=c(-22,18), asp = 0,
     layout = layout_with_kk (net.igraph), main="Network of Target Genes with DEG", main.family = "Serif", main.font = 4)



