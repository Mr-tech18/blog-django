import { openCloseElement } from "./openCloseMenu.js";

export function closeNaveOpenMenu (btn,menu){
    

    btn.addEventListener('click',()=>{
        menu.classList.toggle('hidden');
        console.log('click...');
    });
    
}

document.addEventListener('DOMContentLoaded',()=>{
    
    console.log("test");
    
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
    
    
        let product=()=>{
        let filter=document.getElementById('dropdownSort1');
        let btn1=document.getElementById('sortDropdownButton1');
    
        btn1.addEventListener("click",()=>{
            filter.classList.toggle('hidden');
            
        },false);
        
    
    }
    
    
    
    
    function callbackMenuOpenNav(){
        let btn=document.querySelector('[data-name="menu"]');
        let menu=document.getElementById('hamburger-menu');

       closeNaveOpenMenu(btn,menu);
    }
    callbackMenuOpenNav();
    
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
    function recentPosts(){
        let btnConatinercontainer=document.querySelector('[data-pagination]');
        console.log(btnConatinercontainer);
        console.log('recent post in working...');
        const container=document.querySelector('#recent_post_container');
        console.log(container);
        if(container){
            const listArray=container.children; 
            slider(container,listArray,10,1,btnConatinercontainer);
        }
    }

    //this code use for the search functionnality
    (()=>{
        document.addEventListener('click',(e)=>{
            document.querySelectorAll('.search_box').forEach((btn,index)=>{
                if(btn.contains(e.target)){
                    let btn_search=document.getElementById('Search-tags');
                    btn_search.classList.toggle('hidden');
                    document.querySelector('.close_menu').addEventListener('click',(e)=>{
                        btn_search.classList.add('hidden');
                    });
                    console.log('it work well..');
                }
            });
            
           
        });
    })();

    popularPost();
    recentPosts();
    featureThisMonth();
    displaySubList();
    
    });