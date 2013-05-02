$(function() {
    $('#alpha-asc').click(function(){
        getDoubleSort('alpha', 'asc');
        $("#alpha-desc").removeClass('checked');
        $(this).addClass('checked');
    });
    $('#alpha-desc').click(function(){
        getDoubleSort('alpha', 'desc');
        $("#alpha-asc").removeClass('checked');
        $(this).addClass('checked');
    });
    $('#size-asc').click(function(){
        getDoubleSort('size', 'asc');
        $('#size-desc').removeClass('checked');
        $(this).addClass('checked');
    });
    $('#size-desc').click(function(){
        getDoubleSort('size', 'desc');
        $('#size-asc').removeClass('checked');
        $(this).addClass('checked');
    });
});

function getDoubleSort(type, dir) {
    var a = new Array();
    a['size'] = 'alpha';
    a['alpha'] = 'size';
    if ($('#'+a[type]+'-asc').hasClass('checked')) {
        getSortedList(type, dir, a[type], 'asc');
    }
    else if ($('#'+a[type]+'-desc').hasClass('checked')) {
        getSortedList(type, dir, a[type], 'desc');
    }
    else {
        getSortedList(type, dir);
    }
}

function getDisplayedWordList() {
    $( "ul.wordlist li" ).each(function( index ) {
  console.log( index + ": " + $(this).text() );
});
}

function getSortedList(type, dir, type2, dir2) {
    var string = $("#string").html();
    var url_str = "/api?string="+string+"&"+type+"="+dir+"&"+type2+"="+dir2;
    $.ajax({
        url : url_str,
        dataType: 'json'}).done(
            function(data) {
                window.wordArray = data['word_list'];
                var wordArray = data['word_list'];
                var wordListHTML = getWordListHTML(wordArray);
                $("ul.wordlist").remove();
                $("div.wordlist").append(wordListHTML);
            });
      return false;
}

function getWordListHTML(wordArray) {
    var html = '<ul class="wordlist">';
    for (var i = 0; i < wordArray.length; i++) {
        html += "<li>"+wordArray[i]+"</li>";
    }
    html += "</ul>";
    return html;
}
