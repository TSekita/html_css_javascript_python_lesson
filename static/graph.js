const graphDiv = document.getElementById('graph')

const trace = {
    x: [1, 2, 3, 4, 5],
    y: [10, 15, 13, 17, 22],
    type: 'scatter',
    marker: {color: 'lime', size: 8},
    line: {color: 'lime', width: 2}
 };
 
const layout = {
    width: graphDiv.offsetWidth,
    height: graphDiv.offsetHeight,
    paper_bgcolor: 'black',
    plot_bgcolor: 'black',
    xaxis: {
        showgrid: true,
        gridcolor: 'white', // 縦方向の罫線
        zerolinecolor: 'white'  // y=0 のライン
    },
    yaxis: {
        showgrid: true,
        gridcolor: 'white', // 横方向の罫線
        zerolinecolor: 'black'  // x=0 のライン
    }
 };

 Plotly.newPlot(graphDiv, [trace], layout);
