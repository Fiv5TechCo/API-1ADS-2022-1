let map;
let markers = [];

function initMap() {
  map = new google.maps.Map(document.querySelector("div.map"), {
    center: {lat: -23.2139586, lng: -45.8512006},
    zoom: 15
  });

  enableMarkers()
}

function enableMarkers() {
  $.each(points, function(key, point){
    let position = new google.maps.LatLng(point.lat, point.lng);

    let marker = new google.maps.Marker({
      position: position,
      map: map
    })

    markers.push(marker);
  })
}