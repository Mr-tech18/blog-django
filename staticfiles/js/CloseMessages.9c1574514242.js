(
    function closesMessage(){
        let messageContainer=document.querySelector('.messages');
        setTimeout(()=>{
            messageContainer.classList.add('hidden');
        },10000);
        
    }
)();