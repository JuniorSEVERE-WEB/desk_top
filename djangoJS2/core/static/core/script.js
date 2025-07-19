function displayMessage()
{
    fetch('/get_message/')
    .then((response)=>response.json())
    .then((data)=>{
        document.querySelector('.para').innerHTML = data.message;
    })
}