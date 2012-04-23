//$Revision: 1.2 $
//$Date: 2008-05-15 05:07:06 $
//$Author: jdboyd $
//$Name: not supported by cvs2svn $
//$Id: name.js,v 1.2 2008-05-15 05:07:06 jdboyd Exp $


function setName()
{
  var f = document.getElementById("nameForm");
  var reqStr="nameJS?n=" + escape(f.n.value) + "&u=" + f.u.value;
  //alert(reqStr);
  var val = getSomething(reqStr);
  var p = document.getElementById("custom");

  //alert(p.childNodes.length);


  /*This now basically works, but the output formatting could be nicer.
    Also, if you get an error the first try, the second try doesn't clear
    the error message.*/
  if (val['error']==null)
      {
	  while(p.childNodes.length>1)
	      {
		  p.removeChild(p.childNodes[0]);
	      }

	  //alert(val);
	//var errF = document.getElementById('errField');
	//errF.innerHTML='';

	  var a = document.createElement('A');
	  a.href=val['result'];
	  a.appendChild(document.createTextNode(val['result']));
	  p.appendChild(a);
      }
  else
      {
	//var s = document.createElement('SPAN');
	  //alert(val['error']);
	  //s.appendChild(document.createTextNode(val['error']));
	  //p.appendChild(s);
	var errF = document.getElementById('errField');
	errF.innerHTML=val['error'];
      }
}
