function iniciarMap(){
    var coord = {lat:-33.033531 ,lng: -71.532795};
    var coord2 = {lat:-33.0208808 ,lng: -71.508829};
    var coord3 = {lat: -32.9913008 , lng: -71.5075532}
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 10,
      center: coord,
      center: coord2
    });
    var marker = new google.maps.Marker({
      position: coord,      
      map: map
      
    });
    var marker2 = new google.maps.Marker({
      position: coord2,      
      map: map
      
    });
    var marker3 = new google.maps.Marker({
      position: coord3,      
      map: map
      
    });
}