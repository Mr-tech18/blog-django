
document.addEventListener('DOMContentLoaded',()=>{
    
    console.log("test");
    function openCloseElement(menu,btns){
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
    function slider(container,listArray,itemsPerPage,currentPage,btnConatiner){
        function renderPagination(){
        
            //let btnConatiner=document.querySelector('[data-btn-container]');
            btnConatiner.innerHTML='';
            for(let i=1;i<=Math.ceil(listArray.length/itemsPerPage);i++){
                const buttonElement=document.createElement('button');
                buttonElement.textContent=i;
                buttonElement.className='w-10 border m-1 border-purple-300 rounded p-2 hover:bg-purple-200 text-gray-400 text-xs';

                buttonElement.addEventListener('click',()=>{
                    
                    currentPage=i;
                    
                    renderData();
                });
                btnConatiner.appendChild(buttonElement);
            }
        }
    
        function renderData(){
            let start=(currentPage-1)*itemsPerPage;
            let end=start+itemsPerPage;
    
            for(let i=0;i<listArray.length;i++){
                if(i>=start && i<end){
                    
                    listArray[i].style.display='block';
                    if(currentPage!=1){
                        listArray[0].style.display='none';
                    }
                    else{
                        listArray[0].style.display='block'
                    }
                
    
                }
                else{
                    listArray[i].style.display='none';
                }
            }
        }
        renderPagination();
        renderData();
     } 
    
    /*     function slider(container, listArray, itemsPerPage, currentPage, btnConatiner) {
            function renderPagination() {
                btnConatiner.innerHTML = '';
                for (let i = 1; i <= Math.ceil(listArray.length / itemsPerPage); i++) {
                    const buttonElement = document.createElement('button');
                    buttonElement.textContent = i;
                    buttonElement.className = 'w-10 border m-1 border-purple-300 rounded p-2 hover:bg-purple-200 text-gray-400 text-xs';
        
                    buttonElement.addEventListener('click', () => {
                        currentPage = i;
                        renderData();
                    });
                    btnConatiner.appendChild(buttonElement);
                }
            }
        
            function renderData() {
                let start = (currentPage - 1) * itemsPerPage;
                let end = start + itemsPerPage;
        
                // Ensure start and end are within bounds
                start = Math.max(0, start);
                end = Math.min(listArray.length, end);
        
                for (let i = 0; i < listArray.length; i++) {  // Start loop from 0
                    if (i >= start && i < end) {
                        listArray[i].style.display = 'block';
                    } else {
                        listArray[i].style.display = 'none';
                    }
                }
            }
        
            renderPagination();
            renderData();
        }
         */
        let product=()=>{
        let filter=document.getElementById('dropdownSort1');
        let btn1=document.getElementById('sortDropdownButton1');
    
        btn1.addEventListener("click",()=>{
            filter.classList.toggle('hidden');
            
        },false);
        
    
    }
    
    
    function closeNaveOpenMenu (){
        let menu=document.querySelector('[data-name="menu"]');
        let hamMenuContainer=document.getElementById('hamburger-menu');
    
        menu.addEventListener('click',()=>{
            hamMenuContainer.classList.toggle('hidden');
        });
        
    }
    
    closeNaveOpenMenu();
    
    function openCloseFaq(){
        let btns=document.querySelectorAll('.btn-up');
        let faqResponse=document.querySelectorAll('.hidden-1-faq');
        
    
        //here we access the clicked btn using a foreach loop
        openCloseElement(faqResponse,btns);
    }
    
    function openCloseDescription(){
        let btns=document.querySelectorAll('.shown-description');
        let menu=document.querySelectorAll('.descrpiton');
        openCloseElement(menu,btns);
    }
    /* function displayComment(){
        let btn=document.getElementById('btnSubmit1');
        
        btn.addEventListener('click',(e)=>{
            let btns=document.querySelectorAll('.shown-description')[0].click();
        })
        
    } */
    openCloseDescription();
    openCloseFaq();
    //displayComment();
    
    
    function displaySubList(){
        
        let subliLists=document.querySelectorAll('.sub-list');
        let subliListContainers=document.querySelectorAll('.sublist-container');
    
        //let subliListContainerArray=Array.from(subliListContainer);
        
        subliListContainers.forEach((item,index)=>{
            item.addEventListener('mouseover',()=>{
                subliLists[index].classList.remove('hidden');
            });
            item.addEventListener('click',()=>{
                subliLists[index].classList.remove('hidden');
            });
           
        });
        subliListContainers.forEach((subliListContainer,index)=>{
            subliListContainer.addEventListener('click',()=>{
                subliLists[index].classList.toggle('hidden');
            });
        })
        document.addEventListener('mouseout',(event)=>{
            subliListContainers.forEach((subliListContainer,index)=>{
                if(!(subliListContainer.contains(event.target)&&!(subliLists[index].contains(event.target)))){
                    subliLists[index].classList.add('hidden');
                }
            });
        });
    
    
    }
    
    //pagination funcition
        
    function popularPost(){
        let btnConatinercontainer=document.querySelector('[data-btn-container]');
        const ul=document.querySelector('[data-slide-container]');
        console.log("top");
        if(ul){
            const liElements=ul.children; 
            slider(ul,liElements,2,1,btnConatinercontainer);
        }
    }
    
    function featureThisMonth(){
        let btnConatinercontainer=document.querySelector('[data-btn-container-feature]');

        const ul=document.querySelector('[data-container-1]');
        if(ul){
            const liElements=ul.children; 
            slider(ul,liElements,2,1,btnConatinercontainer);
        }
    }

    //code to close the messages framwork
    function closesMessage(){
        let messageContainer=document.querySelector('.messages');
        setTimeout(()=>{
            messageContainer.classList.add('hidden');
        },10000);
        console.log('top');
    }

    //this code use for the search functionnality
    (()=>{
        document.addEventListener('click',(e)=>{
            document.querySelectorAll('.search_box').forEach((btn,index)=>{
                if(btn.contains(e.target)){
                    let menu=document.getElementById('Search-tags');
                    menu.classList.toggle('hidden');
                    document.querySelector('.close_menu').addEventListener('click',(e)=>{
                        menu.classList.add('hidden');
                    });
                    console.log('it work well..');
                }
            });
            
           
        });
    })();
    closesMessage();
    popularPost();
    featureThisMonth();
    displaySubList();
    
    });