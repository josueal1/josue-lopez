function onClick(e) {
  console.log("I was clicked");
  var nameOnCard = $("#cc_info").val();
  console.log(nameOnCard);
}


function setup() {
  $("#ok_button").click(onClick); //$().on("click")
}


$(document).ready(setup);
