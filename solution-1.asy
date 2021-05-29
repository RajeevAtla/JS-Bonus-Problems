if(!settings.multipleView) settings.batchView=false;
settings.tex="pdflatex";
settings.inlinetex=true;
deletepreamble();
defaultfilename="solution-1";
if(settings.render < 0) settings.render=4;
settings.outformat="";
settings.inlineimage=true;
settings.embed=true;
settings.toolbar=false;
viewportmargin=(2,2);

size(10cm);

pair[] coords = {(-3, -sqrt(3)), (-3, 0), (-3, sqrt(3)),
(-3/2, -3*sqrt(3)/2), (-3/2, -1*sqrt(3)/2), (-3/2, sqrt(3)/2), (-3/2, 3*sqrt(3)/2),
(0, -2*sqrt(3)), (0, -sqrt(3)), (0, 0), (0, sqrt(3)), (0, 2*sqrt(3)),
(3/2, -3*sqrt(3)/2), (3/2, -1*sqrt(3)/2), (3/2, sqrt(3)/2), (3/2, 3*sqrt(3)/2),
(3, -sqrt(3)), (3, 0), (3, sqrt(3))};




for(int n = 0; n < coords.length; ++n){
draw(shift(coords[n])*polygon(6), blue);
dot(coords[n], red);
}

pair[] coords2 = {(-9/2, -3*sqrt(3)/2), (-9/2, -sqrt(3)/2), (-9/2, sqrt(3)/2), (-9/2, 3*sqrt(3)/2),
(-3, -2*sqrt(3)), (-3, 2*sqrt(3)),
(-3/2, -5*sqrt(3)/2), (-3/2, 5*sqrt(3)/2),
(0, -3*sqrt(3)), (0, 3*sqrt(3)),
(3/2, -5*sqrt(3)/2), (3/2, 5*sqrt(3)/2),
(3, -2*sqrt(3)), (3, 2*sqrt(3)),
(9/2, -3*sqrt(3)/2), (9/2, -sqrt(3)/2), (9/2, sqrt(3)/2), (9/2, 3*sqrt(3)/2)};

for(int n = 0; n < coords2.length; ++n){
dot(coords2[n], green);
}

label("$A$", (0, 0), S);
label("$B$", (0, sqrt(3)), S);
label("$C_1$", (0, 2*sqrt(3)), S);
label("$C_2$", (-3, sqrt(3)), S);
label("$C_3$", (3, sqrt(3)), S);
label("$C_4$", (-3, -sqrt(3)), S);
label("$C_5$", (3, -sqrt(3)), S);
label("$C_6$", (0, -2*sqrt(3)), S);
label("$D_1$", (0, 3*sqrt(3)), S);
label("$D_2$", (-3/2, 5*sqrt(3)/2), S);
label("$D_2$", (3/2, 5*sqrt(3)/2), S);
label("$E$", (-3/2, sqrt(3)/2), S);
