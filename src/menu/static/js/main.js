var currentUrl = '/cards/'; //Current URL used to generate urls to sort cards

$(document).ready(function(){
  getCards(currentUrl);
});

var body = $('body');

body.on('click', '.navLink', function(){
    let url = $(this).attr('data-url');
    getCards(url);
});

body.on('click', '.sort', function(){
    addSortButtons(currentUrl);
    let url = $(this).attr('data-url');
    getCards(url);
});

body.on('click', '.card-detail', function(){
    let url = $(this).attr('data-url');
    let return_url = currentUrl;
    getCardDetail(url, return_url);
});


function addSortButtons(url){
    $("#ascending_name").attr('data-url',url + "?ordering=name");
    $("#descending_name").attr('data-url',url +"?ordering=-name");
    $("#ascending_dishes").attr('data-url',url +"?ordering=dishes_count");
    $("#descending_dishes").attr('data-url',url +"?ordering=-dishes_count");
}

function getCards(cardsUrl){
 $.ajax({
        url: cardsUrl,
        success: function(result) {
            clearList();
            addToMenu(result);
        }
       })
}

function getCardDetail(cardUrl, return_url){
    $('#next').css('opacity',0);
    $('#prev').css('opacity',1);
    $('#prev').attr('data-url',return_url);
    $.ajax({
        url: cardUrl,
        success: function(result) {
            $('.nav-menu').empty();
            clearList();
            showDetails(result);
        }
       })
}

function showDetails(card) {
    let list = $('.menu-card-list');
    let name = "<p> Name: " + card.name + "</p>";
    let id = "<p> Number: " + card.id + "</p>";
    let description = "<p>Description: " + card.description + "</p>";
    let dishes_count = "<p>Number of Dishes: " + card.dishes_count + "</p>";
    let details = "<div class='details'>" + name + id + description + dishes_count + "</div>";
    let dishes = dishesList(card.dishes);
    list.append(details);
    list.append(dishes);
}

function dishesList(result){
        let dishes = "";
        for (i=0;i<result.length;i++) {

            let name = "<p>Name: " + result[i].name + "</p>";
            let description = "<p>Description: " + result[i].description + "</p>";
            let preparation_time = "<p>Preparation time: " + result[i].preparation_time + "</p>";
            let price = "<p>Price: " + result[i].price + "</p>";
            let vegan = "<p>Vegan: " + result[i].vegan + "</p>";
            dishes+= name + description + preparation_time + price + vegan + "</br>"
        }
        let template = "<hr><h2>Dishes:</h2><hr><div class='dishes'>"+dishes+"</div>";
        return template
}

function clearList(){
    $('.menu-card-list').empty()
}

function addToMenu(result){
    let next = result.next;
    let previous = result.previous;
    let cards = result.results;
    addButtons(next, previous);
    addCardsToList(cards);
}

function addButtons(next,previous){
    addDataUrl(next,$('#next'));
    addDataUrl(previous,$('#prev'));
}

function addDataUrl(url,element){
    $(element).removeAttr('data-url');
    if (url==null){
        $(element).css('opacity',0);
        return false
    } else {
        $(element).attr('data-url',url);
        $(element).css('opacity',1);
        return true
    }
}

function addCardsToList(cards){
    let list = $('.menu-card-list');
    for (i=0;i<cards.length;i++) {
        list.append("<li class='card-detail' data-url='/cards/"+cards[i]['id']+"'>"+cards[i]['name']+"</li>")
    }
}

