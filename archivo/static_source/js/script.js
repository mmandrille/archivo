$(document).ready()
{
  
  $('ul.faq li a').on("click", function(event)
  {
    event.preventDefault();
    $('ul.faq li').removeClass("active");
    $(this).parent().parent().addClass("active");
    
    var respuesta = $(this).parent().find('.contenedor-respuesta').html();
    
    $('.respuesta-activa').html("<h3>" + $(this).text() + "</h3><p>" + respuesta + "</p>");
  });
  
  if ($('ul.faq'))
  {
    $('ul.faq li').first().addClass("active");
    var respuesta = $('ul.faq li').first().find('.contenedor-respuesta').html();
    
    $('.respuesta-activa').html("<h3>" + $('ul.faq li').first().find("h3").text() + "</h3><p>" + respuesta + "</p>");
  }
 
  var altura = $('.nav').offset().top;
	
  var lastScrollTop = 0;
  var secciones = ["body", "faq", "archivos", "fotos", "registro"];
  var seccionIndex = 0;
  
  $('.home').on('scroll touchmove mousewheel', function(e){
  e.preventDefault();
  e.stopPropagation();
  return false;
})
  
  
  $('.paginacion a').on('click', function()
  {
    event.preventDefault();
    
    
        var headerHeight;
        if ($('nav').hasClass("sticky"))
        {
          headerHeight = 60
        }
        else headerHeight = 150;
    
    $('.paginacion a').removeClass("active");
    var target = $(this).attr('href');
    $('html, body').stop().animate({'scrollTop': $(target).offset().top - headerHeight}, 500, function () {
        //window.location.hash = target;
    });
    $(this).addClass("active");
  });
  
  $('.home').on("hashchange", function(event)
  {
    event.preventDefault();
  });
  
    $('.home').mousewheel(function(evt){
      
        var target = "";
        var headerHeight;
        if ($('nav').hasClass("sticky"))
        {
          headerHeight = 60
        }
        else headerHeight = 150;
       if (evt.deltaY > 0)
       {
        seccionIndex ++;
        if (seccionIndex >= secciones.length)
        {
          seccionIndex = secciones.length - 1;
        }
        else
        {
          target = "#"+secciones[seccionIndex];
            $('.paginacion a').removeClass("active");
            $('.paginacion a[href="'+target+'"]').addClass("active");
          $('html, body').stop().animate({'scrollTop': $(target).offset().top - headerHeight}, 700, function () {
            //window.location.hash = target;
          });
        }
       }
       else
       {
         if (evt.deltaY < 0)
         {
          seccionIndex--;
          if (seccionIndex < 0)
          {
            seccionIndex = 0;
          }
          else
          {
            target = "#"+secciones[seccionIndex];
            $('.paginacion a').removeClass("active");
            $('.paginacion a[href="'+target+'"]').addClass("active");
            $('html, body').stop().animate({'scrollTop': $(target).offset().top - headerHeight}, 700, function () {
             // window.location.hash = target;
            });
         }
       }
    }});
    
	$(window).on('scroll', function(event){
    event.preventDefault();
		if ( $(window).scrollTop() > altura ){
			$('.navbar').addClass('sticky');
		} else {
			$('.navbar').removeClass('sticky');
		}
	});
  
}