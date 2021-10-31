$.getJSON(getWebAppBackendUrl('send_data'),function(data){
    data = JSON.parse(data["dataset"]);
    console.log("our data", data);

    // Define D3 format to handle thousands
    const f = d3.format(",")
    
    // ---------- Updating metrics
    // Number of countries
    totalCustomers = data.length;
    d3.select("#totalCustomers").html(totalCustomers);
    
    // Total page views
    totalInteractions = d3.sum(data, d => d.pages_visited);
    d3.select("#pageViews").html(f(pageViews));
    
    // Average customer lifetime value
    averageCLV = d3.mean(data, d => d.prediction).toFixed(1);
    d3.select("#customerLV").html(averageCLV);
    
})