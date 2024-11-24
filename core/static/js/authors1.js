document.addEventListener('DOMContentLoaded',(e)=>{
  
  let subliListContainer=document.querySelectorAll('[data-subtlistDisplayer="list-displayer"]');
  
  let sublisElement=document.querySelectorAll('[data-sublist="subtitle"]');
  let listArray=  Array.from(sublisElement);
  subliListContainer.forEach((btn,index)=>{
      btn.addEventListener('click',(e)=>{
          e.stopPropagation();
          btn.classList.add('bg-purple-500');
          console.log('added..');
          listArray[index].classList.toggle('hidden');
      });

      document.addEventListener('click',(e)=>{
          if(!btn.contains(e.target)){
              btn.classList.remove('bg-purple-500');
              listArray[index].classList.add('hidden');
          }
      })
  });
  // We will use this function to update our section base on the clicked button exp: if it's the dashboard button who is clicked our section will re,der infrmation who are related to this sectio  only

 
  let displayer= ()=> {
      document.addEventListener('click',(e)=>{
          let btns=document.querySelectorAll('[data-menu="menu-item"]');
          let btns_array=Array.from(btns);
          btns.forEach((btn,index) => {
              if(btn.contains(e.target)&&btn.id==="btn_comment"){
                
                  // now we will display the page using ajax... there's is function in the back-end who load the page as a html 
                  // we we'll just retrieve it here a display it...
                  
                  ajax_callback('manage_comment');                  
              }
              else if(btn.contains(e.target)&&btn.id==="dashboard_btn_id"){
               
                ajax_callback('dashobard');
              }
              else if(btn.contains(e.target)&&btn.id==="btn_edit_profile"){
                
                ajax_callback('edit_profile');
              }
              else if(btn.contains(e.target)&&btn.id==="btn_add_post"){
                
                ajax_callback('add_post');
              }
              else if(btn.contains(e.target)&&btn.id==="btn_edit_post"){
                
                ajax_callback('edit_post');
              }
              
              for (let i=0;i<btns_array.length;i++){
                if(i===index){
                  btns_array[i].classList.add('bg-purple-500');
                }
                else{
                  btns_array[i].classList.remove('bg-purple-500')
                }
              }
          });
          
      });
  };

  /* function ajaxCallBackAndBtnClassDecoration('bg-purple-500'='bg-purple-500',sectionName='dashboard',btn=null){
    btn.classList.toggle('bg-purple-500');
    ajax_callback(sectionName);
  } */
  function ajax_callback(view_name){
    console.log('ajax is working well..');
    let xhr=new XMLHttpRequest();
    xhr.open('GET',`http://localhost:8000/author-site/${view_name}/`,true);
    xhr.setRequestHeader('Content-type',"X-requested-with/XMLHttpRequest");

    xhr.onreadystatechange=function(){
      
      if (this.readyState===3){
        console.log('request is loading...');

      }
      if (this.readyState===4 && (this.status>=200 && this.status<204)){
        let data=JSON.parse(this.responseText);
        let blockContainer=document.querySelector('[data-title="element_container"]');
        let my_div=document.createElement('div');

        pageLoaded=true;
        //here that is the html code i will update every time 
        my_div.innerHTML=data.context;
        blockContainer.innerHTML='';
        blockContainer.innerHTML=my_div.innerHTML;

      }
      xhr.onerror=()=>{
        console.log('some error have occur during the data fetching...');
      }

      
    }
    xhr.send();
  }
  //call function section
  displayer();
  
});