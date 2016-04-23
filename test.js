$(window).scroll(function() {
	var hT = $('#center > img').offset().top,
       hH = $('#center > img').outerHeight(),
       wH = $(window).height(),
       dH = $(document).height(),
       wS = $(this).scrollTop();
   if (wS > (hT+hH-wH)){
     $('#center > img').addClass("parallaxin");
   } else {
     $('#center > img').removeClass("parallaxin");
     $('#center > img').css({
      'transform': 'translate(0,0)'
     });
   }
  $('#hero-text').css({
    'transform': 'translate(0, '+ wS/5 +'%)'
	});
  $('.parallaxin').css({
    'transform': 'translate(0, -'+ (wS + 1000 - dH)/4 +'%)'
	});
});