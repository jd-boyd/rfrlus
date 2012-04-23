var HTTP = {};

// This is a list of XMLHTTPRequest factories to try (JS p480)
HTTP._factories = [
	function() {return new XMLHttpRequest(); },
	function() {return new ActiveXObject("MSXML2.XMLHTTP.6.0"); },
	function() {return new ActiveXObject("MSXML2.XMLHTTP"); }
	//function() {return new ActiveXObject("Msxml2.XMLHTTP"); },
	//
	//function() {return new ActiveXObject("Microsoft.XMLHTTP"); },
];

//when we find a factory that works store it here
HTTP._factory = null;

//Create and return a new XMLHttpRequest object.
//
//The first time we're called, try the list of factory functions untill
//we find one that returns a non-null value and does not throw an exception.
//
HTTP.newRequest = function() {
	if (HTTP._factory !== null) { return HTTP._factory(); }

	for(var i = 0; i < HTTP._factories.length; i++) {
		try{
			var factory = HTTP._factories[i];
			var request = factory();
			if (request !== null) {
				HTTP._factory = factory;
				return request;
			}
		}
		catch(e) {
			continue;
		}
	}
	// If we get here, none of the factory candidates succeeded,
	// so throw an exception now and for all future calls.
	HTTP._factory = function() {
		throw new Error("XMLHttpRequest not supported");
	};
	HTTP._factory(); //Throw an error
};

var request = HTTP.newRequest();

function getSomething(r_str){
    request.open("GET", r_str, false);
    request.setRequestHeader("If-Modified-Since", "Sat, 1 Jan 2000 00:00:00 GMT");
    try{// try to connect to the web server and get the fill info
	request.send(null);
    } catch(e){
	alert('Error: Web Server Lost');
	return true;
    }
    // in konqueror send does not throw an error when it fails but returns null instead. I test for this here.
    if(request.responseText == null){
	alert('Error: Web Server Lost');
	return true;
    }
    else{
	var testObjects = eval('(' + request.responseText + ')');
	//alert(request.responseText);
	return testObjects;
    }
}