

document.addEventListener("DOMContentLoaded", () => {
    const img = document.getElementById("logo1");
    const images = [
        "/static/images/me.jpg",
        // "/static/images/logo.png",
        // "/static/images/me2.jpg",
        "/static/images/me3.jpg",
        // "/static/images/me4.jpg",
        // "/static/images/me5.jpg",
    ];
    let index = 0;
    setInterval(() => {
        index = (index + 1) % images.length; 
        img.src = images[index]; 
    }, 3000);
});         
        //   time Selection
document.addEventListener("DOMContentLoaded",function () {
    const clock = document.getElementById('clock');
    setInterval(function () {
        let time = new Date();
        clock.innerHTML = time.toLocaleDateString(); 
    }, 1000);
});

//                   welcome Selection

document.addEventListener("DOMContentLoaded", () => {
    const welcome = document.getElementById('welcome');
    messages=["Welcome To My Profile","मेरी प्रोफाइल पर स्वागत है","माझ्या प्रोफाइलमध्ये स्वागत आहे"]
    color=["#154c79","#004d4b","#008080"]
    let index = 0; 

    setInterval(() => {
        welcome.style.background=color[index];
        welcome.innerHTML = messages[index]; 
        index = (index + 1) % messages.length; 
    }, 1500);
});
//                            midle name

// document.addEventListener("DOMContentLoaded",()=>{
//     const name = document.getElementById("name");
//     const nam = ["Abhay","Abhay Kumar","Abhay Kumar Maurya"];
//     color=["#ff7f50","#2F4F4F","#b4b4b4","#008080"]

//     let index = 0; 
//     setInterval(function(){
//         name.innerHTML=nam[index];
//         name.style.color=color[index]
//         index=( index + 1) % nam.length;
//     },1000)
// });


// footer
// last update
document.addEventListener("DOMContentLoaded", function() {
    let text = document.lastModified; 
    document.getElementById("lastUpdated").innerHTML = text;
});


                // comment section


document.querySelector('form').addEventListener('submit', function(event) {
    let isValid = true;

    // Check if all fields are filled
    document.querySelectorAll('input, textarea').forEach(function(input) {
        if (!input.value) {
            isValid = false;
            input.style.borderColor = 'red';
        } else {
            input.style.borderColor = '#ccc';
        }
    });

    if (!isValid) {
        event.preventDefault();
        alert('Please fill out all fields.');
    }
});