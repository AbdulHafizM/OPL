const toggleBtn = document.querySelector('.toggle_icon').firstChild;
const navLinks = document.querySelectorAll('.nav-link');

toggleBtn.addEventListener('click', ()=>{
    navLinks.forEach((i)=>{
        if(i.classList.toggle('active')){
            i.style.display = 'block'
        }else{
            i.style.display = 'none'
        }
    })
})