function slugify(text){
  return text.toString().toLowerCase()
    .replace(/\s+/g, '-')           // Replace spaces with -
    .replace(/[^\w\-]+/g, '')       // Remove all non-word chars
    .replace(/\-\-+/g, '-')         // Replace multiple - with single -
    .replace(/^-+/, '')             // Trim - from start of text
    .replace(/-+$/, '');            // Trim - from end of text
}

$( "#search-bar" ).keyup(function() {
    var slug = slugify($( "#search-bar" ).val());
    if (slug != ''){
        $('.film').hide();
        var films = $('div.film[data-slug^=".' + slug + '"], [data-slug*="' + slug + '"]').show();
    }else{
        $('.film').show();
    }
    console.log(slug);
    console.log(films);
});

$("#search-bar").click(function() {
    $([document.documentElement, document.body]).animate({
        scrollTop: $("#search-bar").offset().top
    }, 1000);
});