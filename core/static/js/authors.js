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
          let btns_array=Array.from(btns);
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

  /* function ajaxCallBackAndBtnClassDecoration('decor'='decor',sectionName='dashboard',btn=null){
    btn.classList.toggle('decor');
    ajax_callback(sectionName);
  } */
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

  function eventDelegationFunc(){
    document.querySelector('[data-title="element_container"]').addEventListener('click',(event)=>{
      if(event.target.classList.contains('post_edit_view')){
          event.preventDefault();
          console.log("element is:",event.target);
          let element=event.target;
          let post_id_value=element.href.split('/')[5];
          console.log(post_id_value);
          ajax_callback('edit_post',post_id_value);
      }
      else if(event.target.classList.contains('post_delete_view')){
         event.preventDefault();
         let value=confirm("Do you want to delete this post ?\n You will lose it forever ")
          console.log("element is:",event.target);
          if(value){
            let element=event.target;
            let post_id_value=element.href.split('/')[5];
            console.log(post_id_value);
            ajax_callback('delete_post',post_id_value,delete_post=true);
          }
      }
      else if(event.target.classList.contains('checkbox-filter')){
        let selected_data = {};
        document.querySelectorAll('.checkbox-filter').forEach((item, index) => {
            item.addEventListener('click', () => {
                let data_key = item.dataset.filter;

                selected_data[data_key] = Array.from(
                    document.querySelectorAll('[data-filter=' + data_key + ']:checked')
                ).map(element => element.value);
                
                

                // Convert selected_data to URL parameters
                let params = new URLSearchParams();
                Object.keys(selected_data).forEach(key => {
                    selected_data[key].forEach(value => params.append(`${key}[]`, value));
                });
                console.log(selected_data);
                let xhr = new XMLHttpRequest();
                xhr.open('GET', `${document.getElementById('my_form').getAttribute('action')}?${params.toString()}`, true);
                xhr.setRequestHeader('Content-type', 'application/json');

                xhr.onreadystatechange = function() {
                    if (this.readyState === 3) {
                        
                    }
                    if (this.readyState === 4 && (this.status >= 200 && this.status < 204)) {
                        let data = JSON.parse(this.responseText);
                        let postContainer = document.getElementById('posts_list_table');
                        postContainer.innerHTML = data.context;
                    }
                };
                xhr.onerror = function() {
                    console.log('Error...');
                };
                xhr.send(); // No data in the send method for GET request
            });
        });
      }
      else{
        
        console.log('nothing')
      }
    })
  }
  //call function section
  displayer();
  eventDelegationFunc();
  
});