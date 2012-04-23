if (typeof jQuery == 'undefined' || typeof $ == 'undefined') {
    var jQ = document.createElement('script');
    jQ.type = 'text/javascript';
    jQ.onload=loadJqm;
    jQ.src = 'http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js';
    document.body.appendChild(jQ);
    } else {
    if(typeof console != 'undefined') 
    {
	console.log('jQuery already loaded');
    }
    loadJqm();
    }

    function loadJqm() {
	try{
	$("body").append("<link rel='stylesheet' type='text/css' href='http://referurl.net/style_dialog.css' />");
	} catch (e) {
	    alert("Something went wrong with jQuery.\nFalling back to plain web page");
	    //  console.log("Something went wrong with jQuery.\nFalling back to plain web page");
	    location.href='http://referurl.net/add?r='+encodeURIComponent(location.href);
	    //    return;
	}
	var jqm=document.createElement('script');
	jqm.type="text/javascript";
	jqm.src="http://referurl.net/jquery.simplemodal.1.4.min.js";
	jqm.onload=runthis;
	document.body.appendChild(jqm);
    }

    function runthis() {
	$.modal('<iframe src ="http://referurl.net/altAdd?r=' + encodeURIComponent(location.href) + '" width=550px height=400px scrolling="no"><p>Your browser does not support iframes.</p></iframe>');
    }
