import { filtering } from "./ajax_filtering.js";
import { openCloseElement } from "./openCloseMenu.js";

document.addEventListener('DOMContentLoaded',(e)=>{
  
  let subliListContainer=document.querySelectorAll('[data-subtlistDisplayer="list-displayer"]');
  
  let sublisElement=document.querySelectorAll('[data-sublist="subtitle"]');
  let listArray=  Array.from(sublisElement);
  subliListContainer.forEach((btn,index)=>{
      btn.addEventListener('click',(e)=>{
          e.stopPropagation();
          //btn.classList.add('decor');
          console.log('added..');
          listArray[index].classList.toggle('hidden');
      });

      document.addEventListener('click',(e)=>{
          if(!btn.contains(e.target)){
              //btn.classList.remove('decor');
              listArray[index].classList.add('hidden');
          }
      })
  });
  // We will use this function to update our section base on the clicked button exp: if it's the dashboard button who is clicked our section will re,der infrmation who are related to this sectio  only

 
  let displayer= ()=> {
      document.addEventListener('click',(e)=>{
          let btns=document.querySelectorAll('[data-menu="menu-item"]');
          let tableLinks=['dashboard','edit_profile','manage_comment','post_list','statistics','add_post'];
          btns.forEach((btn,index) => {
              if(btn.contains(e.target)){
                
                  // now we will display the page using ajax... there's is function in the back-end who load the page as a html 
                  // we we'll just retrieve it here a display it...
                  ajax_callback(tableLinks[index]);
                  
                  
                  for(let i=0;i<btns.length;i++){
                    if(i==index){
                      if(! btns[index].classList.contains('decor')){
                        btns[index].classList.add('decor');
                      }
                      
                    }
                    else{
                      btns[i].classList.remove('decor');
                    }
                  }
                                 
              }
              
          });
          
      });
  };

  
  function ajax_callback(view_name=null,post_id=null,delete_post=null){
    let url_link=`http://localhost:8000/author-site/${view_name}/`;
    let xhr=new XMLHttpRequest();
    if(post_id){
      let url=url_link+post_id+'/';
      xhr.open('GET',url,true);
    }
    else{
      xhr.open('GET',url_link,true);
    }
    console.log('ajax is working well..');
    
    xhr.setRequestHeader('Content-type',"X-requested-with/XMLHttpRequest");

    xhr.onreadystatechange=function(){
      
      if (this.readyState===3){
        console.log('request is loading...');

      }
      if(delete_post){
        if (this.readyState===4 && (this.status>=200 && this.status<204)){
          console.log('post deleted');
        }
      }
      else{
        if (this.readyState===4 && (this.status>=200 && this.status<204)){
          console.log('server has respond...');
          let data=JSON.parse(this.responseText);
          let blockContainer=document.querySelector('[data-title="element_container"]');
          let my_div=document.createElement('div');
  
          
          //here that is the html code i will update every time 
          my_div.innerHTML=data.context;
          blockContainer.innerHTML='';
          blockContainer.innerHTML=my_div.innerHTML;
  
        }
      }
    
      xhr.onerror=()=>{
        console.log('some error have occur during the data fetching...');
      }

      
    }
    xhr.send();
  }
  //open submenu
  function openSubMenu(btn,subMenu){

  }

  //this function will help to return the pid of the current post
  function getPidFromHref(element){
    let post_id_value=element.href.split('/')[5];
    console.log(post_id_value);
    return post_id_value;
  }
  function eventDelegationFunc(){
    document.querySelector('[data-title="element_container"]').addEventListener('click',(event)=>{
      if(event.target.classList.contains('post_edit_view')){
          event.preventDefault();
          let element=event.target;
          let post_id_value=getPidFromHref(element);
          ajax_callback('edit_post',post_id_value);
      }
      else if(event.target.classList.contains('post_delete_view')){
         event.preventDefault();
         let value=confirm("Do you want to delete this post ?\n You will lose it forever ")
          if(value){
            let element=event.target;
            let post_id_value=getPidFromHref(element);
            ajax_callback('delete_post',post_id_value,delete_post=true);
          }
      }
      else if(event.target.classList.contains('checkbox-filter')){
        filtering(".checkbox-filter",'my_form','posts_list_table');
      }
      else if(event.target.id==='btn_open_menu_id'){
        
        let menu=document.getElementById('menu_checkbox_items');
        menu.classList.toggle('hidden');
       
      }
      else{
        
        console.log('nothing')
      }
    });
    
  }
  //callback function section
  displayer();
  eventDelegationFunc();
  
});