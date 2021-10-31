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
    totalInteractions = d3.sum(data, d => d.campaigns);
    d3.select("#totalInteractions").html(f(totalInteractions));
    
    // Average customer lifetime value
    averageAge = d3.mean(data, d => d.Age).toFixed(1);
    d3.select("#averageAge").html(averageAge);
    
})