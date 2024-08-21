Files=dir('*.png');
value = []
for i = 1:length(Files)

    filename = Files(i).name;
    img1 = imread(filename);
    
    for ii = 1:length(Files)
        filename2 = Files(ii).name;
        img2 = imread(filename2)
        clear param
        param.imageSize = [600 800]; % it works also with non-square images (use the most common aspect ratio in your set)
        param.orientationsPerScale = [8 8 8 8]; % number of orientations per scale
        param.numberBlocks = 4;
        param.fc_prefilt = 4;
        
        % Computing gist:
        gist1 = LMgist(img1, '', param);
        gist2 = LMgist(img2, '', param);
        
        % Distance between the two images:
        D = sum((gist1-gist2).^2)
        value(end + 1) = D
    end

end

B = reshape(value(:), length(Files), []).'

%% plot heatmap 
image_list = {}
for i = 1:length(Files)
    filename = Files(i).name;
    image_list{end + 1} = filename
   
end

xvalues = image_list;
yvalues = image_list;
h = heatmap(xvalues,yvalues,B);
h.Colormap = parula