// setTimeout(() => console.log(data), 2500);
var rendered = 0;

const countriesLollipop = function (data, var1, var2, var3, var4) {
    console.log("hi");
    // set the dimensions and margins of the graph
    var margin = { top: 10, right: 30, bottom: 40, left: 50 },
        width = 600 - margin.left - margin.right,
        height = 600 - margin.top - margin.bottom;

    // append the svg object to the body of the page
    var svg = d3.select("#viz")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    // Add X axis
    var x = d3.scaleLinear()
        .domain([0, d3.max(data.map((d) => d[var2]))])
        // .domain([0, 35])
        .range([0, width])
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x))
        .selectAll("text")
        .attr("transform", "translate(-10,0)rotate(-45)")
        .style("text-anchor", "end");
    svg.append("text")
        .attr("transform",
            "translate(" + (width / 2) + " ," +
            (height + 40) + ")")
        .style("text-anchor", "middle")
        .text();

    // Y axis
    var y = d3.scaleLinear()
        .domain([0, d3.max(data.map((d) => d[var1]))])
        // .domain([0, 10])
        .range([height, 0])
    // .padding(1)
    svg.append("g")
        .call(d3.axisLeft(y));
    svg.append("text")
        .attr("transform",
            "translate(" + (-margin.right) + " ," +
            (height / 2) + ")" +
            "rotate(-90)")
        .style("text-anchor", "middle")
        .text();


    // // Lines
    // svg.selectAll("myline")
    // .data(data)
    // .enter()
    // .append("line")
    //     .attr("x1", function(d) { return x(d["Happiness.Score"]); })
    //     .attr("x2", x(0))
    //     .attr("y1", function(d) { return y(d.Country); })
    //     .attr("y2", function(d) { return y(d.Country); })
    //     .attr("stroke", "grey")

    // Circles
    svg.selectAll("mycircle")
    .data(data)
    .enter()
    .append("circle")
        .transition()
        .attr("cx", function (d) { return x(d[var2]); })
        .attr("cy", function (d) { return y(d[var1]); })
        .attr("r", "4")
        .style("fill", "#b17db5")
        .attr("stroke", "black")
}

// const perCapita = function(){
//     return Promise.all(
//         data.happinessTerrorism.map((row, i) => {
//             return fetch(`https://data.opendatasoft.com/api/records/1.0/search/?dataset=world-population%40kapsarc&facet=year&facet=country_name&refine.year=2017&refine.country_name=${row['Country']}`)
//             .then(response => {
//                 return response.json();
//             }).then(jsonData => {
//                 console.log(jsonData);
//                 if (jsonData["records"].length != 0){
//                     row["terrorIncidents"] = (row["terrorIncidents"] / jsonData["records"][0]["fields"]["value"]);
//                 } else {
//                     delete row;
//                 };
//             });
//         })
//     );
// };

const redraw = function(data, var1, var2, var3, var4) {
    console.log("hello:", var1, ",", var2);
    // set the dimensions and margins of the graph
    var margin = { top: 10, right: 30, bottom: 40, left: 50 },
        width = 600 - margin.left - margin.right,
        height = 600 - margin.top - margin.bottom;

    // append the svg object to the body of the page
    var svg = d3.select("#viz")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    // Parse the Data

    // Add X axis
    var x = d3.scaleLinear()
        .domain([0, d3.max(data.map((d) => d[var2]))])
        // .domain([0, 5])
        .range([0, width])
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x))
        .selectAll("text")
        .attr("transform", "translate(-10,0)rotate(-45)")
        .style("text-anchor", "end");
    svg.append("text")
        .attr("transform",
            "translate(" + (width / 2) + " ," +
            (height + 40) + ")")
        .style("text-anchor", "middle")
        .text( var4 );

    // Y axis
    var y = d3.scaleLinear()
        .domain([0, d3.max(data.map((d) => d[var1]))])
        // .domain([0, 10])
        .range([height, 0])
    // .padding(1)
    svg.append("g")
        .call(d3.axisLeft(y));
    svg.append("text")
        .attr("transform",
            "translate(" + (-margin.right) + " ," +
            (height / 2) + ")" +
            "rotate(-90)")
        .style("text-anchor", "middle")
        .text(var3);


    // // Lines
    // svg.selectAll("myline")
    // .data(data)
    // .enter()
    // .append("line")
    //     .attr("x1", function(d) { return x(d["Happiness.Score"]); })
    //     .attr("x2", x(0))
    //     .attr("y1", function(d) { return y(d.Country); })
    //     .attr("y2", function(d) { return y(d.Country); })
    //     .attr("stroke", "grey")

    // Circles
    svg.selectAll("mycircle")
        .data(data)
        .enter()
        .append("circle")
        .transition()
        .duration(500)
        .attr("cx", function (d) { return x(d[var2]); })
        .attr("cy", function (d) { return y(d[var1]); })
        .attr("r", "4")
        .style("fill", "#b17db5")
        .attr("stroke", "black")
}

const render = function () {

  const viz1 = String(document.getElementById("vizSelector1").value);
  const name1 = String(document.getElementById("vizSelector1").title);
  const viz2 = String(document.getElementById("vizSelector2").value);
  const name2 = String(document.getElementById("vizSelector2").title);
  if (rendered === 0){
      countriesLollipop(data.happiness, viz1, viz2, name1, name2);
      rendered = 1;
  } else {
      d3.select("svg").remove();
      redraw(data.happiness, viz1, viz2, name1, name2);
  }
}
