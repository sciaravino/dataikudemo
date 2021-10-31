$.getJSON(getWebAppBackendUrl('send_data'),function(data){
    data = JSON.parse(data["dataset"]);
    console.log("our data", data);
})