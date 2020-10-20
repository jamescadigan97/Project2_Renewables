var data = [{
    type: "sunburst",
     labels: [
        "Renewables","Solar", "Wind", "Water", "Biomass", "Geothermal","Industrial", "Residential", "Vertical", "Conventional",
      "Wave<br>and<br>Tidal<br>Energy","Wood<br>and<br>Wood<br>Derived<br>Fuels", "Other"
    ],
   parents: [
      "","Renewables", "Renewables", "Renewables","Renewables",
      "Renewables","Solar","Solar", "Wind", "Water","Water",
       "Biomass", "Biomass"
    ],
    values:  [755476, 107275, 300071, 273707, 58412, 16011, 72234, 35041,300071,273707,0,39851,18561],
    outsidetextfont: {size: 20, color: "#377eb8"},
    leaf: {opacity: 0.4},
    marker: {line: {width: 2}},
    branchvalues: 'total'
  }];
  
  var layout = {
    margin: {l: 0, r: 0, b: 0, t: 0},
    width: 500,
    height: 500
  };

  var data = [{
    type: "sunburst",
     labels: ["US Energy", "Non Renewable",
        "Renewables","Nuclear","Petroluem","Gases", "Coal","Solar", "Wind", "Water", "Biomass", "Geothermal","Industrial", "Residential", "Vertical", "Conventional",
      "Wave<br>and<br>Tidal<br>Energy","Wood<br>and<br>Wood<br>Derived<br>Fuels", "Other", "Binary", "Steam"
    ],
   parents: [
      "","US Energy","US Energy","Non Renewable","Non Renewable","Non Renewable","Non Renewable",
      "Renewables", "Renewables", "Renewables","Renewables",
      "Renewables","Solar","Solar", "Wind", "Water","Water",
       "Biomass", "Biomass",  "Geothermal",  "Geothermal"
    ],
    values:  [4118051, 3362575,755476, 809409,18567, 1538454,996148, 
    107275,300071, 273707, 58412, 16011, 72234, 35041,300071,273707,0,39851,18561,
    4575,11436],
    outsidetextfont: {size: 20, color: "#377eb8"},
    leaf: {opacity: 0.4},
    marker: {line: {width: 2}},
    branchvalues: 'total'
  }];
  
  var layout = {
    margin: {l: 0, r: 0, b: 0, t: 0},
    width: 500,
    height: 500,
    sunburstcolorway:[
      "black","green"
    ],
    extendsunburstcolorway: true
  };
  

  Plotly.newPlot('sunburst', data, layout);