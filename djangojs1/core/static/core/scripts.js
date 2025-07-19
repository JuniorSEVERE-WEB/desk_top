function loadMessage()
{
    fetch('/get_message/')
    .then((response)=>response.json())
    .then(data=>{
        document.querySelector('#result').innerHTML = data.message;
    })
}