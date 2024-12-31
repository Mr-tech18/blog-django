

export function openCloseElement(menu,btns){
    //keep in mind that the menu is the html element we want to display or not and the btn is the clikable element for displaying the menu
   
    let menuArray=Array.from(menu);

    btns.forEach((btn,index)=>{
        btn.addEventListener('click',(event)=>{
            event.stopPropagation();
            for(let i=0;i<menuArray.length;i++){
                if(i==index){
                    menuArray[i].classList.toggle('hidden');
                }
                else{
                    menuArray[i].classList.add('hidden')
                }
            }
        })
    })

    /* 
        this script above is used to close a code block whenever the user click on the any part of the document 
        1. we add an event listener to the document to "check" if there is a "click" event that occur
        2. when a "click event occur" , we loop to all of our button who have a class "show-description" 
        3. within this loor for each "btn" we check if the "click event" come from the direct child of our "btn" or "the description block with class #shown"
        4. if the "click event" was comming from a direct child of our two elemeent with classname know as ".shown-description and .description" nothing is done due to "!" operator
        5. when the click come from any other part of the document ! we add a display("hidden") to the current block of (description)
    */
    document.addEventListener('click',(event)=>{
        btns.forEach((btn,index)=>{
            if((!btn.contains(event.target))&&(!menu[index].contains(event.target))){
                menu[index].classList.add('hidden');
            }
        })
    });
  
 }