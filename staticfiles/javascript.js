document.addEventListener("DOMContentLoaded", () => {
    const welcome = document.getElementById('logo1');
    setInterval(() => {
        welcome.src = "/static/images/logo.png";
    }, 1000);
});
document.addEventListener("DOMContentLoaded", () => {
    const welcome = document.getElementById('logo1');

    setInterval(() => {
        welcome.src = "/static/images/images/me.jpg";
    }, 2000);
});

// document.addEventListener("DOMContentLoaded", () => {
//     const img = document.getElementById("logo1");
//     const images = [
//         "/static/images/images/me.jpg",
//         "/static/images/logo.png",
//         "/static/images/back.png"
//     ];
//     let index = 0;
//     setInterval(() => {
//         index = (index + 1) % images.length; 
//         img.src = images[index]; 
//     }, 1000); 
// });
          
        //   time Selection
document.addEventListener("DOMContentLoaded",function () {
    const clock = document.getElementById('clock');
    setInterval(function () {
        let time = new Date();
        clock.innerHTML = time.toLocaleTimeString(); 
    }, 1000);
});

//                   welcome Selection

document.addEventListener("DOMContentLoaded", () => {
    const welcome = document.getElementById('welcome');
    messages=["Welcome To My Profile","मेरी प्रोफाइल पर स्वागत है","रउरा सब के स्वागत बा","माझ्या प्रोफाइलमध्ये स्वागत आहे"]
    color=["#ff7f50","#2F4F4F","#b4b4b4","#008080"]
    let index = 0; 

    setInterval(() => {
        welcome.style.background=color[index];
        welcome.innerHTML = messages[index]; 
        index = (index + 1) % messages.length; 
    }, 1500);
});

//                            midle name

document.addEventListener("DOMContentLoaded",()=>{
    const name = document.getElementById("name");
    const nam = ["","Abhay","Abhay Kumar","Abhay Kumar Maurya"];

    let index = 0; 
    setInterval(function(){
        name.innerHTML=nam[index];
        index=( index + 1) % nam.length;
    },1000)
});

// document.addEventListener("DOMContentLoaded", () => {
//     const welcome = document.getElementById('name');

//     const messages = ["Welcome", "To", "My", "Profile"," Welcome To My Profile"];

//     let index = 0; 

//     setInterval(() => {
//         welcome.innerHTML = messages[index]; 
//         index = (index + 1) % messages.length; 
//     }, 1500);
// });
