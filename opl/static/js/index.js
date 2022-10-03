
let anchorSel = 'a[href^="#"]';

let anchorList = document.querySelectorAll(anchorSel);

anchorList.forEach(link => {
    link.onclick = function(e){
        e.preventDefault();
        console.log(this.hash)
        let anchorDestination = document.querySelector(this.hash);
        anchorDestination.scrollIntoView(
            {
                behaviour : 'smooth',
                block: 'center'
            })
    }
});


