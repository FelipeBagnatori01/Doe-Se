function addListenerScroll() {
    document.getElementById('scrollable-content').addEventListener('scroll', event => {
        const {scrollHeight, scrollTop, clientHeight} = event.target;
    
        if (Math.abs(scrollHeight - clientHeight - scrollTop) < 1) {
            loadPost();
        }
    });
}

function drawPost(owner, handle, text, likes, comments){
    // Get the element
    var elem = document.querySelector('#template-post');

    // Create a copy of it
    var clone = elem.cloneNode(true);

    // Update the post
    clone.id = 'drawnPost';
    clone.querySelector('.name').innerText = owner;
    clone.querySelector('.at').innerText = handle;
    clone.querySelector('.description-text').innerText = text;
    clone.querySelector('.fa-heart').innerText = likes;
    clone.querySelector('.fa-comment').innerText = comments;

    // Inject it into the DOM
    document.getElementById("scrollable-content").appendChild(clone);
}

var text
var image
var user

const sendSearchData = (post) => {
    $.ajax({
        type: 'Post',
        url: 'search/',
        data: {
            'text': text,
            'image': image,
            'user': user
        },
        success: (res) => {
            console.log(res)
        },
        error: (err) => {
            console.log(err)
        }
    })
}

function loadPost(){
    var pos;
    sendSearchData(pos);
    console.log(pos);
    drawPost("pessoa", "@pes", text, "12345", "985");
}  