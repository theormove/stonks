
function getCoords(elem) {
  let box = elem.getBoundingClientRect();

  return {
    top: box.top + pageYOffset,
    left: box.left + pageXOffset
  };
}
let status=0;
let header =document.getElementById('header');
let navSection = document.getElementById('nav_section');
let drop = document.getElementById('dropdown');
let how =document.getElementById('how');
let about = document.getElementById('about');
let contacts = document.getElementById('contacts');
window.addEventListener('scroll', function() {
	if (pageYOffset>300){
		header.classList.add('header_fixed');
	}else if(status===0){
		header.classList.remove('header_fixed');
	}
});
navSection.onmouseenter = function(event) {
	if (header.classList.contains('header_fixed')==false){
		header.classList.add('header_fixed');
		status=1;
	}
};
navSection.onmouseleave = function(event) {
		status=0;
};
how.onclick = function(){
	window.scrollTo(0,671);
}
about.onclick = function(){
	window.scrollTo(0,1350);
}
contacts.onclick = function(){
	window.scrollTo(0,2366);
}