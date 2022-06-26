
(function scrollReveal() {
    window.sr = ScrollReveal();
    sr.reveal('.card', {
      duration   : 500,
      distance   : '20px',
      easing     : 'ease-out',
      origin     : 'bottom',
      reset      : true,
      scale      : 1,
      viewFactor : 0,
      afterReveal  : revealChildren,
    }, 150);
    
      var revealChildren = sr.reveal('.card-title, .card-text', {
      duration   : 500,
      scale      : 1,
      distance   : '20px',
      origin     : 'bottom',
      reset      : true,
      easing     : 'ease-out',
      viewFactor : 1,
    }, 75);
  })();

  (function scrollReveal() {
    window.sr = ScrollReveal();
    sr.reveal('.reveal-class', {
      duration   : 500,
      distance   : '20px',
      easing     : 'ease-out',
      origin     : 'bottom',
      reset      : true,
      scale      : 1,
      viewFactor : 0,
    }, 150);
  })();


  $(document).ready(function() {
  
    $(window).scroll(function() {
      var scroll = $(window).scrollTop();
      if (scroll >= 50) {
        $('.arrow').addClass('fade');
      } else{
        $('.arrow').removeClass('fade');
      }
    })
  });

  
  