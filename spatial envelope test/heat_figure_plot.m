Files=dir('*.png');
image_list = {}
for i = 1:length(Files)
    filename = Files(i).name;
    image_list{end + 1} = filename
   
end

xvalues = image_list;
yvalues = image_list;
h = heatmap(xvalues,yvalues,B);
h.Colormap = parula

