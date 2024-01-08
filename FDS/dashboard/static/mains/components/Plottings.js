function getRandomColors(numColors) {
    const colorMenu = ["#F7CB44","#F9B641","#F9A242","#F68F46","#EB8055","#DE7065",
                        "#CC6A70","#B8627D","#A65C85","#90548B","#7E4E90","#6B4596",
                        "#593D9C","#403891","#253582"];
    const colors = [];
    for (let i = 0; i < numColors; i++) {
        colors.push(colorMenu[colorMenu.length-1-i]);
    }
    
    return colors;
}

const RunChart = (fetchedData) => {
    const data = fetchedData ? fetchedData[0] : null;

    if (data) {
    const rwdSvgWidth = parseInt(d3.select("#years").style("width"));
      const rwdSvgHeight = rwdSvgWidth * 2;
      const margin = rwdSvgWidth * 0.06;

    d3.select(".StageShare").remove();
    const svg = d3
        .select("#StageShareArea")
        .append("svg")
        .attr("class", "StageShare")
        .attr("width", rwdSvgWidth)
        .attr("height", rwdSvgHeight*0.6);

    const xAxisTickLable = Object.keys(data);
    const yData = Object.values(data);
    const xData = [0, 1, 2, 3];

    const xScale = d3
        .scaleLinear()
        .domain(d3.extent(xData))
        .range([margin + margin, 390 + margin]);

    const xAxis = d3
        .axisBottom(xScale)
        .tickSize(6)
        .tickPadding(0)
        .tickFormat((d) => xAxisTickLable[d]);

    const xAxisGroup = svg
        .append("g")
        .call(xAxis)
        .attr("transform", `translate(0,${rwdSvgHeight * 0.6 - margin * 3})`)
        .selectAll("text")
        .style("text-anchor", "end")
        .style("font-size", "14px")
        .style("font-weight", "700")
        .attr("dx", "-.5em")
        .attr("dy", "0em")
        .attr("transform", "rotate(-45)");

    const yScale = d3
        .scaleLinear()
        .domain([0, 100])
        .range([rwdSvgHeight * 0.6 - margin * 3, margin]);

    const yAxis = d3.axisLeft(yScale).tickSize(0);

    const yAxisGroup = svg
        .append("g")
        .call(yAxis)
        .style("font-size", "14px")
        .style("font-weight", "700")
        .attr("transform", `translate(${margin * 2},0)`);

    const lineChart = d3
        .line()
        .x((d) => xScale(d.id))
        .y((d) => yScale(d.value));

    const area = d3
        .area()
        .x((d) => xScale(d.id))
        .y1((d) => yScale(d.value))
        .y0(rwdSvgHeight * 0.6 - margin * 3);

    let defs = svg.append("svg:defs");

    defs
        .append("svg:pattern")
        .attr("id", "chartImage")
        .attr("width", rwdSvgWidth)
        .attr("height", rwdSvgHeight - margin * 12)
        .attr("patternUnits", "userSpaceOnUse")
        .append("svg:image")
        .attr("xlink:href", "../static/images/100TWD-rotate90.jpg")
        .attr("width", 360)
        .attr("height", 360 * 2.07)
        .attr("filter", "drop-shadow(2px 2px 5px black)")
        .attr("x", margin * 2+2)
        .attr("y", margin);

    svg
        .append("path")
        .data(Object.values(data))
        .attr("d", lineChart(Object.values(data).map((d, index) => ({ id: index, value: d }))))
        .attr("stroke", "red")
        .attr("stroke-width", 3)
        .attr("fill", "none")
        .attr("filter", "drop-shadow(2px -2px 5px black)");

    svg
        .append("path")
        .attr("d", area(Object.values(data).map((d, index) => ({ id: index, value: d }))))
        .attr("fill", "url(#chartImage)")
        .style("fill-opacity", 0.7);

    // Tooltip for region
    const regionTooltip = d3
        .select("body")
        .append("div")
        .attr("class", "tooltip")
        .style("opacity", 0);

    svg
    .on("mouseover", (event, d) => {
        const mouseX = event.pageX;
        const mouseY = event.pageY;
        const xValue = xScale.invert(mouseX - margin * 2);
        const yValue = yScale.invert(mouseY);

        regionTooltip.transition().duration(200).style("opacity", 0.9);
        regionTooltip
        .html(`X: ${xValue.toFixed(2)}, Y: ${yValue.toFixed(2)}`)
        .style("left", event.pageX + "px")
        .style("top", event.pageY - 28 + "px");
    })
    .on("mouseout", () => {
        regionTooltip.transition().duration(500).style("opacity", 0);
    });
    } else {
        return null;
    }
    };


const rectPlotting = (props) => {
    const rect = props.svg.append("rect").attr('id', props.id);
    
    rect
        .attr('x', props.x)
        .attr('y', props.y)
        .attr('width', props.width)
        .attr('height', props.height)
        .attr('fill', props.color)
        .attr('stroke', 'white')
        .attr('stroke-width', '2px')
        .style('opacity', 0.8)
        .style("fill-opacity", "70%")
        .style("cursor", "pointer")
        .on('mouseover', function () {
        if (d3.select(this).style("opacity") != 0) {
            rect
            .transition()
            .style("opacity", 1)
            .attr('stroke-width', '0px');
    
            props.svg.selectAll('rect')
            .filter((d, i, nodes) => d3.select(nodes[i]).attr('id') !== d3.select(this).attr('id'))
            .style('fill-opacity', "50%");
    
            props.label
            .style('visibility', 'visible')
            .style('left', props.x + props.width / 2 + 'px')
            .style('top', props.height / 2 + 'px')
            .style("background-color", "#fff")
            .style("border", `2px solid ${props.color}`)
            .style("padding", "8px")
            .style("border-radius", "5px")
            .style("box-shadow", "0 2px 4px rgba(0, 0, 0, 0.2)")
            .style("font-weight", "bold")
            .style("font-size", "14px")
            .style("color", props.color)
            .style("position", "absolute")
            .style("transform", "translate(-50%, -50%)")
            .style("opacity", 0)
            .html(props.id + ':<br>' + Math.round(props.value * 100) / 100 + '%')
            .transition()
            .duration(200)
            .style("opacity", 1);
        }
        })
        .on('mouseout', function () {
        rect
            .transition()
            .style("opacity", 0.8)
            .attr('stroke-width', '2px');
    
        props.svg.selectAll('rect')
            .filter((d, i, nodes) => d3.select(nodes[i]).attr('id') !== d3.select(this).attr('id'))
            .style('fill-opacity', "70%");
    
        props.label.style('visibility', 'hidden');
        });
    };

const RatioGraph = (props) => {
    const rwdSvgWidth = parseInt(d3.select(".container").style("width"));
    const rwdSvgHeight = rwdSvgWidth / 2.07;
    const margin = rwdSvgWidth * 0.075;
    
    d3.select('.tooltip').remove();
    d3.select('.' + props.chartName).remove();
    const svg = d3
        .select('#' + props.chartAreaId)
        .append("svg")
        .attr("class", props.chartName)
        .attr("width", rwdSvgWidth)
        .attr("height", rwdSvgHeight);

    let tooltip = d3.select(svg.node().parentNode)
        .append("div")
        .style("position", "absolute")
        .attr("class", "tooltip")
        .style('opacity', 1)
        .style('width', 'fit-content')
        .style('height', rwdSvgHeight/2)
        .style("visibility", "hidden")
        .style('color', 'black')
        .style('font-weight', 800)
        .style("border-width", "2px")
        .style("border-radius", "5px")
        .style("padding", "10px");

    if (props.data) {
        svg.append("rect")
        .style('margin-top', '20px')
        .attr('x', rwdSvgWidth * 0.025)
        .attr('y', rwdSvgHeight * 0.025)
        .attr('width', rwdSvgWidth * 0.95)
        .attr('height', rwdSvgHeight * 0.95)
        .attr('fill', 'url(#'+props.chartAreaId+'ShareImage)');

    let widths = Object.values(props.data);
    let idx = Object.keys(props.data);
    let xpositions = [];

    for (let i = 0; i < widths.length; i++) {
    if (i === 0) {
        xpositions.push(rwdSvgWidth * 0.025)
    } else {
        xpositions.push(xpositions[i - 1] + rwdSvgWidth * 0.95 * widths[i - 1] / 100)
    }
    }
    let defs = svg.append('svg:defs');
        defs.append("svg:pattern")
            .attr("id", props.chartAreaId+"ShareImage")
            .attr("width", rwdSvgWidth * 1.5)
            .attr("height", rwdSvgHeight * 1.5)
            .attr("patternUnits", "userSpaceOnUse")
            .append("svg:image")
            .attr("xlink:href", '../static/images/100TWD.jpg')
            .attr("height", rwdSvgHeight)
            .attr("width", rwdSvgWidth*0.95)
            .attr("x", xpositions[0]);

    for (let i = 0; i < widths.length; i++) {
    rectPlotting({
        svg: svg,
        label: tooltip,
        id: idx[i],
        x: xpositions[i],
        y: rwdSvgHeight * 0.025,
        value: widths[i],
        width: rwdSvgWidth * 0.95 * widths[i] / 100,
        height: rwdSvgHeight * 0.95,
        color: props.colors[i]
    });
    }
}
};

export { RatioGraph, RunChart, getRandomColors };
