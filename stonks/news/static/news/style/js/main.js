let lastscrolltop =0;
window.onscroll = function showheader() {
    let header = document.queryselector('.header_external');
    if(window.pageyoffset > 200){
    	if(window.pageyoffset-lastscrolltop>50)
    	{
	        header.classlist.add('header_fixed');
	    } else	if(lastscrolltop-window.pageyoffset>50)
	    	{
	    		header.classlist.remove('header_fixed');
	    	}
    }
    lastscrolltop = window.pageyoffset;
}
