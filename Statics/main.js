const $reply = document.querySelector('#reply')
const $sendButton = document.getElementById('info-btn')
const $clearButton = document.querySelector('#clear-btn')

$sendButton.addEventListener('click', ()=>{
    $sendButton.setAttribute('disabled', 'disabled')

    // Fetching data when button is clicked
    const message = document.getElementById('data').value
    const limit = document.getElementById('searchTerm').value

    if(!message){
        $sendButton.removeAttribute('disabled')
        return alert('Please Enter an Input')
    }

    $reply.textContent = "Loading..."
    var inputData = {
        'data': message,
        'searchTerm': limit
    }

    const url = 'http://localhost:5000/data'

    var request = new Request(url, {
        method: "POST",
        body: (JSON.stringify(inputData)),
        headers: new Headers({
            'Content-Type': 'application/json'
        })
    })

    fetch(request)
    .then((response) => response.json())
    .then((data) => {
        console.log(data)
        $reply.innerHTML = "<h2>General Report : "+data.poll+"</h2>"+"<br><strong>People think that it is</strong><br><br>"+data.positive+"% Positive<br>"+data.wpositive+"% Weakly Positive<br>"+data.spositive+"% Strongly Positive<br>"+ data.negative+"% Negative<br>"+data.wnegative+"% Weakly Negative<br>"+data.snegative+"% Strongly Negative<br>"+data.neutral+"% Neutral<br>"
    })
    .catch((error) => {
        console.log(error)
    })

    $sendButton.removeAttribute('disabled')
})

$clearButton.addEventListener('click', ()=>{

    document.getElementById('data').value = ""
    document.getElementById('searchTerm').value = ""
    $reply.innerHTML = ""
})